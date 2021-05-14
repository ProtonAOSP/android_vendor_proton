#!/usr/bin/env python3

import math
import collections

sRGB = collections.namedtuple("sRGB", ["r", "g", "b"])
RGB = collections.namedtuple("RGB", ["r", "g", "b"])
Oklab = collections.namedtuple("Oklab", ["L", "a", "b"])
Oklch = collections.namedtuple("Oklch", ["L", "C", "h"])

def srgb_to_linear(srgb):
    def oetf(x):
        if x >= 0.0031308:
            return 1.055 * (x ** (1.0 / 2.4)) - 0.055
        else:
            return 12.92 * x

    return RGB(oetf(srgb.r), oetf(srgb.g), oetf(srgb.b))

def linear_to_srgb(rgb):
    def eotf(x):
        if x >= 0.04045:
            return ((x + 0.055) / (1 + 0.055)) ** 2.4
        else:
            return x / 12.92

    return sRGB(eotf(rgb.r), eotf(rgb.g), eotf(rgb.b))

def rgb_to_oklab(rgb):
    l = 0.4122214708 * rgb.r + 0.5363325363 * rgb.g + 0.0514459929 * rgb.b
    m = 0.2119034982 * rgb.r + 0.6806995451 * rgb.g + 0.1073969566 * rgb.b
    s = 0.0883024619 * rgb.r + 0.2817188376 * rgb.g + 0.6299787005 * rgb.b

    l_ = l ** (1/3)
    m_ = m ** (1/3)
    s_ = s ** (1/3)

    return Oklab(
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )

def oklab_to_rgb(oklab):
    l_ = oklab.L + 0.3963377774 * oklab.a + 0.2158037573 * oklab.b
    m_ = oklab.L - 0.1055613458 * oklab.a - 0.0638541728 * oklab.b
    s_ = oklab.L - 0.0894841775 * oklab.a - 1.2914855480 * oklab.b

    l = l_ * l_ * l_
    m = m_ * m_ * m_
    s = s_ * s_ * s_

    return RGB(
        +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )

def oklab_to_oklch(oklab):
    return Oklch(
        L = oklab.L,
        C = math.sqrt(oklab.a ** 2 + oklab.b ** 2),
        h = math.degrees(math.atan2(oklab.b, oklab.a)),
    )

def oklch_to_oklab(oklch):
    h_rad = math.radians(oklch.h)

    return Oklab(
        L = oklch.L,
        a = oklch.C * math.cos(h_rad),
        b = oklch.C * math.sin(h_rad),
    )

def main():
    while True:
        orig_hex = input("Tinted RGB hex: ").replace("#", "")

        orig_srgb = sRGB(int(orig_hex[:2], 16) / 255, int(orig_hex[2:4], 16) / 255, int(orig_hex[4:], 16) / 255)
        orig_rgb = srgb_to_linear(orig_srgb)
        orig_oklab = rgb_to_oklab(orig_rgb)
        orig_oklch = oklab_to_oklch(orig_oklab)

        new_oklch = Oklch(orig_oklab.L, 0, 0)
        new_oklab = oklch_to_oklab(new_oklch)
        new_rgb = oklab_to_rgb(new_oklab)
        new_srgb = linear_to_srgb(new_rgb)

        new_hex = hex(int(round(new_srgb.r * 255)))[2:] + hex(int(round(new_srgb.g * 255)))[2:] + hex(int(round(new_srgb.b * 255)))[2:]
        print(f"    => {new_hex}")

        print("\n")

if __name__ == "__main__":
    main()
