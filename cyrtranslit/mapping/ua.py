# -*- coding: utf-8 -*-
"""
Ukrainian (ua) transliteration mappings.

ISO 639-1 language code: ua

Transliteration follows Scientific Ukrainian transliteration system.
"""

import copy
from .ru import RU_CYR_TO_LAT_DICT

# Transliterate from Ukrainian
UA_CYR_TO_LAT_DICT = copy.deepcopy(RU_CYR_TO_LAT_DICT)
# Change mapping to match with Scientific Ukrainian
UA_CYR_TO_LAT_DICT[u"Г"] = u"H"
UA_CYR_TO_LAT_DICT[u"г"] = u"h"
UA_CYR_TO_LAT_DICT[u"Ж"] = u"Ž"
UA_CYR_TO_LAT_DICT[u"ж"] = u"ž"
UA_CYR_TO_LAT_DICT[u"И"] = u"Y"
UA_CYR_TO_LAT_DICT[u"и"] = u"y"
UA_CYR_TO_LAT_DICT[u"Х"] = u"X"
UA_CYR_TO_LAT_DICT[u"х"] = u"x"
UA_CYR_TO_LAT_DICT[u"Ц"] = u"C"
UA_CYR_TO_LAT_DICT[u"ц"] = u"c"
UA_CYR_TO_LAT_DICT[u"Ч"] = u"Č"
UA_CYR_TO_LAT_DICT[u"ч"] = u"č"
UA_CYR_TO_LAT_DICT[u"Ш"] = u"Š"
UA_CYR_TO_LAT_DICT[u"ш"] = u"š"
UA_CYR_TO_LAT_DICT[u"Щ"] = u"Šč"
UA_CYR_TO_LAT_DICT[u"щ"] = u"šč"
UA_CYR_TO_LAT_DICT[u"Ю"] = u"Ju"
UA_CYR_TO_LAT_DICT[u"ю"] = u"ju"
UA_CYR_TO_LAT_DICT[u"Я"] = u"Ja"
UA_CYR_TO_LAT_DICT[u"я"] = u"ja"
# Delete unused letters
del UA_CYR_TO_LAT_DICT[u"Ё"]
del UA_CYR_TO_LAT_DICT[u"ё"]
del UA_CYR_TO_LAT_DICT[u"Ъ"]
del UA_CYR_TO_LAT_DICT[u"ъ"]
del UA_CYR_TO_LAT_DICT[u"Ы"]
del UA_CYR_TO_LAT_DICT[u"ы"]
del UA_CYR_TO_LAT_DICT[u"Э"]
del UA_CYR_TO_LAT_DICT[u"э"]

# Update for Ukrainian letters
UA_CYR_TO_LAT_DICT.update({
    u"Ґ": u"G", u"ґ": u"g",
    u"Є": u"Je", u"є": u"je",
    u"І": u"I", u"і": u"i",
    u"Ї": u"Ji", u"ї": u"ji"
})

# Latin to Cyrillic
UA_LAT_TO_CYR_DICT = {y: x for x, y in iter(UA_CYR_TO_LAT_DICT.items())}
UA_LAT_TO_CYR_DICT.update({
    u"JE": u"Є", u"jE": u"є",
    u"JI": u"Ї", u"jI": u"ї"
})
