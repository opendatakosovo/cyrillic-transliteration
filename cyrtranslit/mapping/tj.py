# -*- coding: utf-8 -*-
"""
Tajik (tj) transliteration mappings.

ISO 639-1 language code: tj

Transliteration follows ISO 9 (1995).
https://en.wikipedia.org/wiki/Tajik_alphabet#Cyrillic
"""

import copy
from .ru import RU_CYR_TO_LAT_DICT

# Transliterate from Tajik cyrillic to latin
TJ_CYR_TO_LAT_DICT = copy.deepcopy(RU_CYR_TO_LAT_DICT)
# Change Mapping according to ISO 9 (1995)
TJ_CYR_TO_LAT_DICT[u"Э"] = u"È"
TJ_CYR_TO_LAT_DICT[u"э"] = u"è"
TJ_CYR_TO_LAT_DICT[u"ъ"] = u"’"
TJ_CYR_TO_LAT_DICT[u"Х"] = u"H"
TJ_CYR_TO_LAT_DICT[u"х"] = u"h"
TJ_CYR_TO_LAT_DICT[u"Ч"] = u"Č"
TJ_CYR_TO_LAT_DICT[u"ч"] = u"č"
TJ_CYR_TO_LAT_DICT[u"Ж"] = u"Ž"
TJ_CYR_TO_LAT_DICT[u"ж"] = u"ž"
TJ_CYR_TO_LAT_DICT[u"Ё"] = u"Ë"
TJ_CYR_TO_LAT_DICT[u"ё"] = u"ë"
TJ_CYR_TO_LAT_DICT[u"Ш"] = u"Š"
TJ_CYR_TO_LAT_DICT[u"ш"] = u"š"
TJ_CYR_TO_LAT_DICT[u"Ю"] = u"Û"
TJ_CYR_TO_LAT_DICT[u"ю"] = u"û"
TJ_CYR_TO_LAT_DICT[u"Я"] = u"Â"
TJ_CYR_TO_LAT_DICT[u"я"] = u"â"
# delete letters not used
del TJ_CYR_TO_LAT_DICT[u"Ц"]
del TJ_CYR_TO_LAT_DICT[u"ц"]
del TJ_CYR_TO_LAT_DICT[u"Щ"]
del TJ_CYR_TO_LAT_DICT[u"щ"]
del TJ_CYR_TO_LAT_DICT[u"Ы"]
del TJ_CYR_TO_LAT_DICT[u"ы"]

# update the dict for the additional letters in the tajik cyrillic alphabet ( Ғ, Ӣ, Қ, Ӯ, Ҳ, Ҷ )
# see https://en.wikipedia.org/wiki/Tajik_alphabet#Cyrillic
TJ_CYR_TO_LAT_DICT.update({
    u"Ғ": u"Ǧ", u"ғ": u"ǧ",
    u"Ӣ": u"Ī", u"ӣ": u"ī",
    u"Қ": u"Q", u"қ": u"q",
    u"Ӯ": u"Ū", u"ӯ": u"ū",
    u"Ҳ": u"Ḩ", u"ҳ": u"ḩ",
    u"Ҷ": u"Ç", u"ҷ": u"ç"
})

# transliterate from latin tajik to cyrillic
TJ_LAT_TO_CYR_DICT = {y: x for x, y in iter(TJ_CYR_TO_LAT_DICT.items())}
