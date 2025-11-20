# -*- coding: utf-8 -*-
"""
Macedonian (mk) transliteration mappings.

ISO 639-1 language code: mk

Supports accented vowels with grave accent used for homograph disambiguation:
- Ѐ/ѐ (U+0400/U+0450) - IE with grave
- Ѝ/ѝ (U+040D/U+045D) - I with grave

Following ISO 9:1968/1995, adopted by Macedonian Academy of Arts and Sciences (1970).
"""

import copy
from .sr import SR_CYR_TO_LAT_DICT

# Build the dictionaries to transliterate Macedonian Cyrillic to Latin and vice versa.
MK_CYR_TO_LAT_DICT = copy.deepcopy(SR_CYR_TO_LAT_DICT)

# Differences with Serbian:
# 1) Between Ze (З з) and I (И и) is the letter Dze (Ѕ ѕ), which looks like the Latin letter S and represents /d͡z/.
MK_CYR_TO_LAT_DICT[u'Ѕ'] = u'Dz'
MK_CYR_TO_LAT_DICT[u'ѕ'] = u'dz'

# 2) Dje (Ђ ђ) is replaced by Gje (Ѓ ѓ), which represents /ɟ/ (voiced palatal stop).
# In some dialects, it represents /d͡ʑ/ instead, like Dje
# It is written ⟨Ǵ ǵ⟩ in the corresponding Macedonian Latin alphabet.
del MK_CYR_TO_LAT_DICT[u'Ђ']
del MK_CYR_TO_LAT_DICT[u'ђ']
MK_CYR_TO_LAT_DICT[u'Ѓ'] = u'Ǵ'
MK_CYR_TO_LAT_DICT[u'ѓ'] = u'ǵ'

# 3) Tshe (Ћ ћ) is replaced by Kje (Ќ ќ), which represents /c/ (voiceless palatal stop).
# In some dialects, it represents /t͡ɕ/ instead, like Tshe.
# It is written ⟨Ḱ ḱ⟩ in the corresponding Macedonian Latin alphabet.
del MK_CYR_TO_LAT_DICT[u'Ћ']
del MK_CYR_TO_LAT_DICT[u'ћ']
MK_CYR_TO_LAT_DICT[u'Ќ'] = u'Ḱ'
MK_CYR_TO_LAT_DICT[u'ќ'] = u'ḱ'

# This dictionary is to transliterate from Macedonian Latin to Cyrillic.
# Build this BEFORE adding accented Cyrillic characters to avoid reverse mapping conflicts
MK_LAT_TO_CYR_DICT = {y: x for x, y in iter(MK_CYR_TO_LAT_DICT.items())}

# 4) Accented vowels with grave accent (used to disambiguate homographs in Macedonian)
# Following ISO 9:1968/1995, adopted by Macedonian Academy of Arts and Sciences in 1970
# Source: https://en.wikipedia.org/wiki/I_with_grave_(Cyrillic)
# These are used to distinguish homographs:
# - ѝ (her) vs и (and)
# - нѐ (us) vs не (no)
# - сѐ (everything) vs се (short reflexive pronoun)
#
# By default (preserve_accents=False), accented Cyrillic maps to unaccented Latin
MK_CYR_TO_LAT_DICT[u'Ѐ'] = u'E'  # Cyrillic E with grave → E (U+0400)
MK_CYR_TO_LAT_DICT[u'ѐ'] = u'e'  # Cyrillic e with grave → e (U+0450)
MK_CYR_TO_LAT_DICT[u'Ѝ'] = u'I'  # Cyrillic I with grave → I (U+040D)
MK_CYR_TO_LAT_DICT[u'ѝ'] = u'i'  # Cyrillic i with grave → i (U+045D)

# Accented map: When preserve_accents=True, these override the standard mappings
MK_CYR_TO_LAT_ACCENTED_DICT = {
    u'Ѐ': u'È',  # Cyrillic E with grave → È
    u'ѐ': u'è',  # Cyrillic e with grave → è
    u'Ѝ': u'Ì',  # Cyrillic I with grave → Ì
    u'ѝ': u'ì',  # Cyrillic i with grave → ì
}

# Add mappings for accented Latin to unaccented Cyrillic (preserve_accents=False)
MK_LAT_TO_CYR_DICT.update({
    u'È': u'Е', u'è': u'е',  # Latin E with grave → Cyrillic E
    u'Ì': u'И', u'ì': u'и',  # Latin I with grave → Cyrillic I
})

# Accented map for Latin→Cyrillic: When preserve_accents=True, these override
MK_LAT_TO_CYR_ACCENTED_DICT = {
    u'È': u'Ѐ', u'è': u'ѐ',  # Latin E with grave → Cyrillic Ѐ
    u'Ì': u'Ѝ', u'ì': u'ѝ',  # Latin I with grave → Cyrillic Ѝ
}
