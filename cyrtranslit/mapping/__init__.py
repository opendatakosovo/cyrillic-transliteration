# -*- coding: utf-8 -*-
"""
Cyrillic transliteration mapping package.

This package contains transliteration mappings for various Cyrillic and Greek scripts.
Each language has its own module with specific transliteration dictionaries.

Supported languages:
- bg: Bulgarian
- by: Belarusian
- el: Greek
- me: Montenegrin
- mk: Macedonian
- mn: Mongolian
- rs: Serbian (ISO 3166-1 country code alias)
- ru: Russian
- sr: Serbian
- tj: Tajik
- ua: Ukrainian
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

# Bundle up all the dictionaries in a lookup dictionary
TRANSLIT_DICT = {
    'sr': {  # Serbian (ISO 639-1 language code)
        'tolatin': SR_CYR_TO_LAT_DICT,
        'tocyrillic': SR_LAT_TO_CYR_DICT
    },
    'rs': {  # Serbian (ISO 3166-1 country code alias)
        'tolatin': SR_CYR_TO_LAT_DICT,
        'tocyrillic': SR_LAT_TO_CYR_DICT
    },
    'me': {  # Montenegro
        'tolatin': ME_CYR_TO_LAT_DICT,
        'tocyrillic': ME_LAT_TO_CYR_DICT
    },
    'mk': {  # Macedonia
        'tolatin': MK_CYR_TO_LAT_DICT,
        'tocyrillic': MK_LAT_TO_CYR_DICT,
        'tolatin_accented': MK_CYR_TO_LAT_ACCENTED_DICT,
        'tocyrillic_accented': MK_LAT_TO_CYR_ACCENTED_DICT
    },
    'ru': {  # Russian
        'tolatin': RU_CYR_TO_LAT_DICT,
        'tocyrillic': RU_LAT_TO_CYR_DICT
    },
    'tj': {  # Tajik
        'tolatin': TJ_CYR_TO_LAT_DICT,
        'tocyrillic': TJ_LAT_TO_CYR_DICT
    },
    'bg': {  # Bulgarian
        'tolatin': BG_CYR_TO_LAT_DICT,
        'tocyrillic': BG_LAT_TO_CYR_DICT,
        'tolatin_accented': BG_CYR_TO_LAT_ACCENTED_DICT,
        'tocyrillic_accented': BG_LAT_TO_CYR_ACCENTED_DICT
    },
    'ua': {  # Ukrainian
        'tolatin': UA_CYR_TO_LAT_DICT,
        'tocyrillic': UA_LAT_TO_CYR_DICT
    },
    'by': {  # Belarusian
        'tolatin': BY_CYR_TO_LAT_DICT,
        'tocyrillic': BY_LAT_TO_CYR_DICT
    },
    'mn': {  # Mongolian
        'tolatin': MN_CYR_TO_LAT_DICT,
        'tocyrillic': MN_LAT_TO_CYR_DICT
    },
    'el': {  # Greek (ISO 639-1 language code)
        'tolatin': EL_GRE_TO_LAT_DICT,
        'tocyrillic': EL_LAT_TO_GRE_DICT
    }
}

# Export the main dictionary for backward compatibility
__all__ = ['TRANSLIT_DICT']
