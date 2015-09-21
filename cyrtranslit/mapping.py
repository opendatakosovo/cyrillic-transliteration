# -*- coding: utf-8 -*-
import copy
# Build the dictionaries to transliterate Serbian cyrillic to latin and vice versa.

# This dictionary is to transliterate from cyrillic to latin.
SR_CYR_TO_LAT_DICT = {
    u'А': u'A', u'а': u'a',
    u'Б': u'B', u'б': u'b',
    u'В': u'V', u'в': u'v',
    u'Г': u'G', u'г': u'g',
    u'Д': u'D', u'д': u'd',
    u'Ђ': u'Đ', u'ђ': u'đ',
    u'Е': u'E', u'е': u'e',
    u'Ж': u'Ž', u'ж': u'ž',
    u'З': u'Z', u'з': u'z',
    u'И': u'I', u'и': u'i',
    u'Ј': u'J', u'ј': u'j',
    u'К': u'K', u'к': u'k',
    u'Л': u'L', u'л': u'l',
    u'Љ': u'Lj',u'љ': u'lj',
    u'М': u'M', u'м': u'm',
    u'Н': u'N', u'н': u'n',
    u'Њ': u'Nj',u'њ': u'nj',
    u'О': u'O', u'о': u'o',
    u'П': u'P', u'п': u'p',
    u'Р': u'R', u'р': u'r',
    u'С': u'S', u'с': u's',
    u'Т': u'T', u'т': u't',
    u'Ћ': u'Ć', u'ћ': u'ć',
    u'У': u'U', u'у': u'u',
    u'Ф': u'F', u'ф': u'f',
    u'Х': u'H', u'х': u'h',
    u'Ц': u'C', u'ц': u'c',
    u'Ч': u'Č', u'ч': u'č',
    u'Џ': u'Dž',u'џ': u'dž',
    u'Ш': u'Š', u'ш': u'š',
}

# This dictionary is to transliterate from Serbian latin to cyrillic.
# Let's build it by simply swapping keys and values of previous dictionary.
SR_LAT_TO_CYR_DICT = {y:x for x,y in SR_CYR_TO_LAT_DICT.iteritems()}

# Build the dictionaries to transliterate Montenegrin cyrillic to latin and vice versa.

# Montenegrin Latin is based on Serbo-Croatian Latin, with the addition of the two letters Ś and Ź, to replace the digraphs SJ and ZJ.
# These parallel the two letters of the Montenegrin Cyrillic alphabet not found in Serbian, С́ and З́.
# These, respectively, could also be represented in the original alphabets as šj and žj, and шj and жj.
# Source: https://en.wikipedia.org/wiki/Montenegrin_alphabet#Latin_alphabet
# Also see: http://news.bbc.co.uk/2/hi/8520466.stm
ME_CYR_TO_LAT_DICT = copy.deepcopy(SR_CYR_TO_LAT_DICT)
ME_CYR_TO_LAT_DICT.update({
    u'С́': u'Ś', u'с́': u'ś', # Montenegrin
    u'З́': u'Ź', u'з́': u'ź' # Montenegrin
})

# This dictionary is to transliterate from Montenegrin latin to cyrillic.
ME_LAT_TO_CYR_DICT = {y:x for x,y in ME_CYR_TO_LAT_DICT.iteritems()}

# Build the dictionaries to transliterate Macedonian cyrillic to latin and vice versa.
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

# This dictionary is to transliterate from Macedonian latin to cyrillic.
MK_LAT_TO_CYR_DICT = {y:x for x,y in MK_CYR_TO_LAT_DICT.iteritems()}


# Bundle up all the dictionaries in a lookup dictionary
TRANSLIT_DICT = {
    'sr': { # Serbia
        'tolatin': SR_CYR_TO_LAT_DICT,
        'tocyrillic': SR_LAT_TO_CYR_DICT
    },
    'me': { # Montenegro
        'tolatin': ME_CYR_TO_LAT_DICT,
        'tocyrillic': ME_LAT_TO_CYR_DICT
    },
    'mk': { # Macedonia
        'tolatin': MK_CYR_TO_LAT_DICT,
        'tocyrillic': MK_LAT_TO_CYR_DICT
    }
}