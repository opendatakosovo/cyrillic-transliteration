# -*- coding: utf-8 -*-
"""
Mongolian (mn) transliteration mappings.

ISO 639-1 language code: mn

This version of Mongolian Latin <-> Cyrillic is based on MNS 5217:2012
as far as I know this is the latest standard. Inform me @ https://github.com/Serbipunk

References:
https://gogo.mn/r/101115
https://en.wikipedia.org/wiki/Mongolian_Cyrillic_alphabet
"""

# This list contains alternating Cyrillic and Latin mappings
# Format: [Cyrillic_upper, Latin_upper, Cyrillic_lower, Latin_lower, ...]
MN_CYR_LAT_LIST = [
    u"А", u"A", u"а", u"a",
    u"Э", u"E", u"э", u"e",
    u"И", u"I", u"и", u"i",  # i
    u"О", u"O", u"о", u"o",
    u"У", u"U", u"у", u"u",
    u"Ө", u"Ö", u"ө", u"ö",
    u"Ү", u"Ü", u"ү", u"ü",
    u"Н", u"N", u"н", u"n",
    u"М", u"M", u"м", u"m",
    u"Л", u"L", u"л", u"l",
    u"В", u"V", u"в", u"v",
    u"П", u"P", u"п", u"p",
    u"Ф", u"F", u"ф", u"f",
    u"К", u"K", u"к", u"k",
    u"Х", u"Kh", u"х", u"kh",        # lat 1
    u"Х", u"KH", u"х", u"kH",        # lat 1
    u"Г", u"G", u"г", u"g",
    u"С", u"S", u"с", u"s",
    u"Ш", u"Sh", u"ш", u"sh",  # sh  # lat2
    u"Ш", u"SH", u"ш", u"sH",  # sh  # lat2
    u"Т", u"T", u"т", u"t",
    u"Д", u"D", u"д", u"d",
    u"Ц", u"Ts", u"ц", u"ts",        # lat3
    u"Ц", u"TS", u"ц", u"tS",        # lat3
    u"Ч", u"Ch", u"ч", u"ch",        # lat4
    u"Ч", u"CH", u"ч", u"cH",        # lat4
    u"З", u"Z", u"з", u"z",
    u"Ж", u"J", u"ж", u"j",
    u"Й", u"I", u"й", u"i",  # i * 2
    u"Р", u"R", u"р", u"r",
    u"Б", u"B", u"б", u"b",
    u"Е", u"Ye", u"е", u"ye",             # lat 5
    u"Е", u"YE", u"е", u"yE",             # lat 5
    u"Ё", u"Yo", u"ё", u"yo",             # lat 6
    u"Ё", u"YO", u"ё", u"yO",             # lat 6
    u"Ъ", u"I", u"ъ", u"i",  # i * 3
    u"Ы", u"Y", u"ы", u"y",
    u"Ь", u"I", u"ь", u"i",  # i * 4
    u"Ю", u"Yu", u"ю", u"yu",             # lat 8
    u"Ю", u"YU", u"ю", u"yU",             # lat 8
    u"Я", u"Ya", u"я", u"ya",             # lat 9
    u"Я", u"YA", u"я", u"yA",             # lat 9
]
# Building the dictionary with the filter to skip pairs with 2-character Latin letters where the second character is uppercase
MN_CYR_TO_LAT_DICT = {
    c: l for c, l in zip(MN_CYR_LAT_LIST[::2], MN_CYR_LAT_LIST[1::2])
    if not (len(l) == 2 and l[1].isupper())
}

# Handle Щ (shcha): This letter is part of Mongolian Cyrillic (inherited from Russian)
# but is rarely used in practice. It's pronounced the same as Ш (/ʃ/), so both
# transliterate to "Sh/sh" in Latin. When going Latin → Cyrillic, "Sh" defaults to Ш.
MN_CYR_TO_LAT_DICT['Щ'] = 'Sh'
MN_CYR_TO_LAT_DICT['щ'] = 'sh'

MN_LAT_TO_CYR_DICT = dict([(l, c) for c, l in zip(MN_CYR_LAT_LIST[-2::-2], MN_CYR_LAT_LIST[-1::-2])])
