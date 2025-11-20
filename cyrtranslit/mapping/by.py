# -*- coding: utf-8 -*-
"""
Belarusian (by) transliteration mappings.

ISO 639-1 language code: by

Transliteration follows ISO 9:1995 and BGN/PCGN romanization standards.
https://en.wikipedia.org/wiki/Belarusian_alphabet
https://en.wikipedia.org/wiki/Romanization_of_Belarusian
"""

import copy
from .ru import RU_CYR_TO_LAT_DICT

# Transliterate from Belarusian (based on ISO 9:1995 and BGN/PCGN)
BY_CYR_TO_LAT_DICT = copy.deepcopy(RU_CYR_TO_LAT_DICT)
# Change mapping to match Belarusian scientific transliteration
BY_CYR_TO_LAT_DICT[u"Г"] = u"H"
BY_CYR_TO_LAT_DICT[u"г"] = u"h"
BY_CYR_TO_LAT_DICT[u"Ё"] = u"Ë"
BY_CYR_TO_LAT_DICT[u"ё"] = u"ë"
BY_CYR_TO_LAT_DICT[u"Ж"] = u"Ž"
BY_CYR_TO_LAT_DICT[u"ж"] = u"ž"
BY_CYR_TO_LAT_DICT[u"Х"] = u"X"
BY_CYR_TO_LAT_DICT[u"х"] = u"x"
BY_CYR_TO_LAT_DICT[u"Ц"] = u"C"
BY_CYR_TO_LAT_DICT[u"ц"] = u"c"
BY_CYR_TO_LAT_DICT[u"Ч"] = u"Č"
BY_CYR_TO_LAT_DICT[u"ч"] = u"č"
BY_CYR_TO_LAT_DICT[u"Ш"] = u"Š"
BY_CYR_TO_LAT_DICT[u"ш"] = u"š"
BY_CYR_TO_LAT_DICT[u"Ы"] = u"Y"
BY_CYR_TO_LAT_DICT[u"ы"] = u"y"
BY_CYR_TO_LAT_DICT[u"Ь"] = u"'"
BY_CYR_TO_LAT_DICT[u"ь"] = u"'"
BY_CYR_TO_LAT_DICT[u"Э"] = u"Ė"
BY_CYR_TO_LAT_DICT[u"э"] = u"ė"
BY_CYR_TO_LAT_DICT[u"Ю"] = u"Ju"
BY_CYR_TO_LAT_DICT[u"ю"] = u"ju"
BY_CYR_TO_LAT_DICT[u"Я"] = u"Ja"
BY_CYR_TO_LAT_DICT[u"я"] = u"ja"
# Delete letters not used in Belarusian
del BY_CYR_TO_LAT_DICT[u"Щ"]
del BY_CYR_TO_LAT_DICT[u"щ"]
del BY_CYR_TO_LAT_DICT[u"Ъ"]
del BY_CYR_TO_LAT_DICT[u"ъ"]
# Update for Belarusian-specific letters
BY_CYR_TO_LAT_DICT.update({
    u"І": u"I", u"і": u"i",
    u"Ў": u"Ŭ", u"ў": u"ŭ"
})

# Latin to Cyrillic
BY_LAT_TO_CYR_DICT = {y: x for x, y in iter(BY_CYR_TO_LAT_DICT.items())}
BY_LAT_TO_CYR_DICT.update({
    u"JU": u"Ю", u"Ju": u"Ю", u"ju": u"ю",
    u"JA": u"Я", u"Ja": u"Я", u"ja": u"я",
    u"''": u"Ьь"  # Two apostrophes for Ьь
})
# Single apostrophe defaults to lowercase ь
BY_LAT_TO_CYR_DICT[u"'"] = u"ь"
