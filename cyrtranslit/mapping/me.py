# -*- coding: utf-8 -*-
"""
Montenegrin (me) transliteration mappings.

ISO 3166-1 country code: me

Montenegrin Latin is based on Serbo-Croatian Latin, with the addition of the two letters Ś and Ź,
to replace the digraphs SJ and ZJ. These parallel the two letters of the Montenegrin Cyrillic
alphabet not found in Serbian, С́ and З́. These, respectively, could also be represented in the
original alphabets as šj and žj, and шj and жj.

Source: https://en.wikipedia.org/wiki/Montenegrin_alphabet#Latin_alphabet
Also see: http://news.bbc.co.uk/2/hi/8520466.stm
"""

import copy
from .sr import SR_CYR_TO_LAT_DICT

ME_CYR_TO_LAT_DICT = copy.deepcopy(SR_CYR_TO_LAT_DICT)
ME_CYR_TO_LAT_DICT.update({
    u'С́': u'Ś', u'с́': u'ś',  # Montenegrin
    u'З́': u'Ź', u'з́': u'ź'  # Montenegrin
})

# This dictionary is to transliterate from Montenegrin Latin to Cyrillic.
ME_LAT_TO_CYR_DICT = {y: x for x, y in iter(ME_CYR_TO_LAT_DICT.items())}
