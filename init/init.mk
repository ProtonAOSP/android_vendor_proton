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

# Custom init scripts
PRODUCT_COPY_FILES += \
    vendor/proton/init/init.proton.sh:$(TARGET_COPY_OUT_SYSTEM)/bin/init.proton.sh \
    vendor/proton/init/proton.rc:$(TARGET_COPY_OUT_SYSTEM)/etc/init/proton.rc \

# SEpolicy to allow init actions
PRODUCT_PRIVATE_SEPOLICY_DIRS += vendor/proton/init/sepolicy
