# -*- coding: utf-8 -*-
"""
Cyrillic transliteration mapping package.

This package contains transliteration mappings for various Cyrillic and Greek scripts.
Each language has its own module with specific transliteration dictionaries.

Supported languages:
- be: Belarusian
- bg: Bulgarian
- cnr: Montenegrin
- el: Greek
- mk: Macedonian
- mn: Mongolian
- ru: Russian
- sr: Serbian
- tg: Tajik
- uk: Ukrainian
"""

# Import all language-specific mappings
from .sr import SR_CYR_TO_LAT_DICT, SR_LAT_TO_CYR_DICT
from .me import ME_CYR_TO_LAT_DICT, ME_LAT_TO_CYR_DICT
from .mk import (
    MK_CYR_TO_LAT_DICT,
    MK_LAT_TO_CYR_DICT,
    MK_CYR_TO_LAT_ACCENTED_DICT,
    MK_LAT_TO_CYR_ACCENTED_DICT
)
from .ru import RU_CYR_TO_LAT_DICT, RU_LAT_TO_CYR_DICT
from .tj import TJ_CYR_TO_LAT_DICT, TJ_LAT_TO_CYR_DICT
from .bg import (
    BG_CYR_TO_LAT_DICT,
    BG_LAT_TO_CYR_DICT,
    BG_CYR_TO_LAT_ACCENTED_DICT,
    BG_LAT_TO_CYR_ACCENTED_DICT
)
from .ua import UA_CYR_TO_LAT_DICT, UA_LAT_TO_CYR_DICT
from .by import BY_CYR_TO_LAT_DICT, BY_LAT_TO_CYR_DICT
from .mn import MN_CYR_TO_LAT_DICT, MN_LAT_TO_CYR_DICT
from .el import EL_GRE_TO_LAT_DICT, EL_LAT_TO_GRE_DICT

# Canonical public language codes. Use ISO 639-1 where available and ISO 639-3
# where no ISO 639-1 code exists.
CANONICAL_LANG_CODES = [
    'be',
    'bg',
    'cnr',
    'el',
    'mk',
    'mn',
    'ru',
    'sr',
    'tg',
    'uk'
]

# Accepted non-canonical codes. This preserves the historical API while also
# accepting ISO 639 alpha-3 codes used by language-processing libraries.
LANG_CODE_ALIASES = {
    'bel': 'be',
    'by': 'be',
    'bul': 'bg',
    'ell': 'el',
    'me': 'cnr',
    'mkd': 'mk',
    'mon': 'mn',
    'rs': 'sr',
    'rus': 'ru',
    'srp': 'sr',
    'tgk': 'tg',
    'tj': 'tg',
    'ua': 'uk',
    'ukr': 'uk',
}

# Bundle up all canonical dictionaries in a lookup dictionary.
TRANSLIT_DICT = {
    'be': {  # Belarusian
        'tolatin': BY_CYR_TO_LAT_DICT,
        'tocyrillic': BY_LAT_TO_CYR_DICT
    },
    'bg': {  # Bulgarian
        'tolatin': BG_CYR_TO_LAT_DICT,
        'tocyrillic': BG_LAT_TO_CYR_DICT,
        'tolatin_accented': BG_CYR_TO_LAT_ACCENTED_DICT,
        'tocyrillic_accented': BG_LAT_TO_CYR_ACCENTED_DICT
    },
    'cnr': {  # Montenegrin
        'tolatin': ME_CYR_TO_LAT_DICT,
        'tocyrillic': ME_LAT_TO_CYR_DICT
    },
    'el': {  # Greek (ISO 639-1 language code)
        'tolatin': EL_GRE_TO_LAT_DICT,
        'tocyrillic': EL_LAT_TO_GRE_DICT
    },
    'mk': {  # Macedonian
        'tolatin': MK_CYR_TO_LAT_DICT,
        'tocyrillic': MK_LAT_TO_CYR_DICT,
        'tolatin_accented': MK_CYR_TO_LAT_ACCENTED_DICT,
        'tocyrillic_accented': MK_LAT_TO_CYR_ACCENTED_DICT
    },
    'mn': {  # Mongolian
        'tolatin': MN_CYR_TO_LAT_DICT,
        'tocyrillic': MN_LAT_TO_CYR_DICT
    },
    'ru': {  # Russian
        'tolatin': RU_CYR_TO_LAT_DICT,
        'tocyrillic': RU_LAT_TO_CYR_DICT
    },
    'sr': {  # Serbian (ISO 639-1 language code)
        'tolatin': SR_CYR_TO_LAT_DICT,
        'tocyrillic': SR_LAT_TO_CYR_DICT
    },
    'tg': {  # Tajik
        'tolatin': TJ_CYR_TO_LAT_DICT,
        'tocyrillic': TJ_LAT_TO_CYR_DICT
    },
    'uk': {  # Ukrainian
        'tolatin': UA_CYR_TO_LAT_DICT,
        'tocyrillic': UA_LAT_TO_CYR_DICT
    }
}

for alias, canonical_lang_code in LANG_CODE_ALIASES.items():
    TRANSLIT_DICT[alias] = TRANSLIT_DICT[canonical_lang_code]


def normalize_lang_code(lang_code):
    ''' Return the canonical language code for a supported code or alias.
    :param lang_code: Language code to normalize.
    :return: Canonical language code if an alias is known; otherwise lowercased input.
    '''
    normalized_lang_code = lang_code.lower()
    return LANG_CODE_ALIASES.get(normalized_lang_code, normalized_lang_code)


# Export the main dictionary for backward compatibility
__all__ = [
    'CANONICAL_LANG_CODES',
    'LANG_CODE_ALIASES',
    'TRANSLIT_DICT',
    'normalize_lang_code'
]
