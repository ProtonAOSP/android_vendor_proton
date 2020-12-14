#!/usr/bin/env python3

import sys
import os
import shutil

DEST_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/colors"

# User-visible name, (Light, Dark)
COLORS = {
    "Pixel Blue": ("#0075E2", "#82B4F4"),

    # 200 and 500 from GM2 colors in AOSP SystemUI
    "Google Blue": ("#4285F4", "#AECBFA"),
    "Google Red": ("#B71C1C", "#F6AEA9"),
    "Google Yellow": ("#FBBC04", "#FDE293"),
    "Google Green": ("#34A853", "#41AF6A"),
    "Google Gray": ("#9AA0A6", "#E8EAED"),

    # iOS system colors from Apple Human Interface Guidelines
    "Apple Blue": ((0, 122, 255), (10, 132, 255)),
    "Apple Green": ((52, 199, 89), (48, 209, 88)),
    "Apple Indigo": ((88, 86, 214), (94, 92, 230)),
    "Apple Orange": ((255, 149, 0), (255, 159, 10)),
    "Apple Pink": ((255, 45, 85), (255, 55, 95)),
    "Apple Purple": ((175, 82, 222), (191, 90, 242)),
    "Apple Red": ((255, 59, 48), (255, 69, 58)),
    "Apple Teal": ((90, 200, 250), (100, 210, 255)),
    "Apple Yellow": ((255, 204, 0), (255, 214, 10)),
}

# Android.mk
ANDROID_MK_TEMPLATE = """#
# Copyright (C) 2020 The Proton AOSP Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

LOCAL_RRO_THEME := AccentColor%APKNAME%

LOCAL_PRODUCT_MODULE := true

LOCAL_RESOURCE_DIR := $(LOCAL_PATH)/res

LOCAL_PACKAGE_NAME := AccentColor%APKNAME%Overlay
LOCAL_SDK_VERSION := current

include $(BUILD_RRO_PACKAGE)
"""

# AndroidManifest.xml
ANDROID_MANIFEST_TEMPLATE = """<!--
    Copyright (C) 2020 The Proton AOSP Project

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
-->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="org.protonaosp.theme.color.%PKGNAME%">

    <overlay android:targetPackage="android"
        android:category="android.theme.customization.accent_color"
        android:priority="1" />

    <application
        android:label="%USERNAME%"
        android:hasCode="false" />

</manifest>
"""

# colors_device_defaults.xml
COLORS_XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<!--
    Copyright (C) 2020 The Proton AOSP Project

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
-->
<resources>
    <color name="accent_device_default_light">%LIGHTCOLOR%</color>
    <color name="accent_device_default_dark">%DARKCOLOR%</color>
</resources>
"""

def raw_color_to_hex(raw):
    if isinstance(raw, str) and raw.startswith("#"):
        return raw.lower()
    elif isinstance(raw, tuple):
        r, g, b = raw
        return "#" + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)
    else:
        raise ValueError(raw)

def main():
    for user_name, (light_raw, dark_raw) in COLORS.items():
        pkg_apk_name = user_name.replace(" ", "")
        pkg_name = user_name.lower().replace(" ", "_")
        apk_name = f"AccentColor{pkg_apk_name}Overlay"
        pkg_dir = f"{DEST_DIR}/{apk_name}"

        print(apk_name)
        shutil.rmtree(pkg_dir, ignore_errors=True)

        light = raw_color_to_hex(light_raw)
        dark = raw_color_to_hex(dark_raw)

        xml_dir = f"{pkg_dir}/res/values"
        os.makedirs(xml_dir, exist_ok=True)
        with open(f"{xml_dir}/colors_device_defaults.xml", "w+") as f:
            f.write(COLORS_XML_TEMPLATE.replace("%LIGHTCOLOR%", light).replace("%DARKCOLOR%", dark))

        with open(f"{pkg_dir}/Android.mk", "w+") as f:
            f.write(ANDROID_MK_TEMPLATE.replace("%APKNAME%", pkg_apk_name))

        with open(f"{pkg_dir}/AndroidManifest.xml", "w+") as f:
            f.write(ANDROID_MANIFEST_TEMPLATE.replace("%PKGNAME%", pkg_name).replace("%USERNAME%", user_name))

if __name__ == '__main__':
    main()
