# -*- coding: utf-8 -*-
"""
Bulgarian (bg) transliteration mappings.

ISO 639-1 language code: bg

Supports accented I with grave for stress marking and homograph disambiguation.
Following ISO 9:1995.
"""

import copy
from .ru import RU_CYR_TO_LAT_DICT

# Transliterate from Bulgarian Cyrillic to Latin
BG_CYR_TO_LAT_DICT = copy.deepcopy(RU_CYR_TO_LAT_DICT)

# There are a couple of letters that don't exist in Bulgarian:
del BG_CYR_TO_LAT_DICT[u"Ё"]
del BG_CYR_TO_LAT_DICT[u"ё"]
del BG_CYR_TO_LAT_DICT[u"Ы"]
del BG_CYR_TO_LAT_DICT[u"ы"]
del BG_CYR_TO_LAT_DICT[u"Э"]
del BG_CYR_TO_LAT_DICT[u"э"]

# Some letters that are pronounced differently
BG_CYR_TO_LAT_DICT[u"Й"] = u"Y"
BG_CYR_TO_LAT_DICT[u"й"] = u"y"
BG_CYR_TO_LAT_DICT[u"Х"] = u"H"
BG_CYR_TO_LAT_DICT[u"х"] = u"h"
BG_CYR_TO_LAT_DICT[u"Ц"] = u"TS"
BG_CYR_TO_LAT_DICT[u"ц"] = u"ts"
BG_CYR_TO_LAT_DICT[u"Щ"] = u"SHT"
BG_CYR_TO_LAT_DICT[u"щ"] = u"sht"
BG_CYR_TO_LAT_DICT[u"Ю"] = u"YU"
BG_CYR_TO_LAT_DICT[u"ю"] = u"yu"
BG_CYR_TO_LAT_DICT[u"Я"] = u"YA"
BG_CYR_TO_LAT_DICT[u"я"] = u"ya"

# The following letters use the pre-2012 "Andreichin" system for lettering,
# because in the newest "Ivanov" system "a" and "y" translate to two Bulgarian
# letters and choosing to which one depends on the word and text context
# https://en.wikipedia.org/wiki/Romanization_of_Bulgarian
BG_CYR_TO_LAT_DICT[u"Ъ"] = u"Ă"
BG_CYR_TO_LAT_DICT[u"ъ"] = u"ă"
BG_CYR_TO_LAT_DICT[u"Ь"] = u"J"
BG_CYR_TO_LAT_DICT[u"ь"] = u"j"

# Transliterate from Latin Bulgarian to Cyrillic.
# Build this BEFORE adding accented Cyrillic characters to avoid reverse mapping conflicts
BG_LAT_TO_CYR_DICT = {y: x for x, y in iter(BG_CYR_TO_LAT_DICT.items())}

# Accented vowels with grave accent (used for stress marking and homograph disambiguation)
# Following ISO 9:1995
# Source: https://en.wikipedia.org/wiki/I_with_grave_(Cyrillic)
# Used to distinguish: ѝ (her) vs и (and)
#
# By default (preserve_accents=False), accented Cyrillic maps to unaccented Latin
BG_CYR_TO_LAT_DICT[u"Ѝ"] = u"I"  # Cyrillic I with grave → I (U+040D)
BG_CYR_TO_LAT_DICT[u"ѝ"] = u"i"  # Cyrillic i with grave → i (U+045D)

# Accented map: When preserve_accents=True, these override the standard mappings
BG_CYR_TO_LAT_ACCENTED_DICT = {
    u"Ѝ": u"Ì",  # Cyrillic I with grave → Ì
    u"ѝ": u"ì",  # Cyrillic i with grave → ì
}

BG_LAT_TO_CYR_DICT.update({
    u"ZH": u"Ж", u"Zh": u"Ж", u"zh": u"ж",
    u"TS": u"Ц", u"Ts": u"Ц", u"ts": u"ц",
    u"CH": u"Ч", u"Ch": u"Ч", u"ch": u"ч",
    u"SH": u"Ш", u"Sh": u"Ш", u"sh": u"ш",
    u"SHT": u"Щ", u"Sht": u"Щ", u"sht": u"щ",
    u"YU": u"Ю", u"Yu": u"Ю", u"yu": u"ю",
    u"YA": u"Я", u"Ya": u"Я", u"ya": u"я",
    # Accented Latin to unaccented Cyrillic (preserve_accents=False)
    u"Ì": u"И", u"ì": u"и",  # Latin I with grave → Cyrillic I
})

# Accented map for Latin→Cyrillic: When preserve_accents=True, these override
BG_LAT_TO_CYR_ACCENTED_DICT = {
    u"Ì": u"Ѝ", u"ì": u"ѝ",  # Latin I with grave → Cyrillic Ѝ
}
