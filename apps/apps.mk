# Copyright (C) 2020 The Proton AOSP Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

$(call inherit-product, vendor/proton/themes/themes.mk)

LOCAL_PATH := vendor/proton/apps

# LineageOS apps
PRODUCT_PACKAGES += \
    ExactCalculator \
    Jelly \

# SystemUI plugins
PRODUCT_PACKAGES += \
    QuickAccessWallet \

# Config
PRODUCT_PACKAGES += \
    SimpleDeviceConfig \

# Wallpapers
PRODUCT_PACKAGES += \
    ProtonWallpaperStub \

# Repainter integration
PRODUCT_PACKAGES += \
    RepainterServicePriv \

# Permissions for Google product apps
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/default-permissions-product.xml:$(TARGET_COPY_OUT_PRODUCT)/etc/default-permissions/default-permissions-product.xml \

# Google apps and services
ifeq ($(WITH_GMS),true)

$(call inherit-product, vendor/gapps/common/common-vendor.mk)

# SetupWizard
PRODUCT_PRODUCT_PROPERTIES += \
    ro.setupwizard.rotation_locked=true \
    setupwizard.theme=glif_v3_light \

# Google Assistant
PRODUCT_PRODUCT_PROPERTIES += \
    ro.opa.eligible_device=true \

# Client ID
PRODUCT_PRODUCT_PROPERTIES += \
    ro.com.google.clientidbase=android-google \

# Overlays
PRODUCT_PACKAGE_OVERLAYS += $(LOCAL_PATH)/gms_overlay

endif
