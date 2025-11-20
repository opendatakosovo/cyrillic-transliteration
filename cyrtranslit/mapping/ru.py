# -*- coding: utf-8 -*-
"""
Russian (ru) transliteration mappings.

ISO 639-1 language code: ru

Transliteration follows GOST 7.79-2000 System B.
"""

# This dictionary is to transliterate from Russian Cyrillic to Latin (GOST_7.79-2000 System B).
RU_CYR_TO_LAT_DICT = {
    u"А": u"A", u"а": u"a",
    u"Б": u"B", u"б": u"b",
    u"В": u"V", u"в": u"v",
    u"Г": u"G", u"г": u"g",
    u"Д": u"D", u"д": u"d",
    u"Е": u"E", u"е": u"e",
    u"Ё": u"YO", u"ё": u"yo",
    u"Ж": u"ZH", u"ж": u"zh",
    u"З": u"Z", u"з": u"z",
    u"И": u"I", u"и": u"i",
    u"Й": u"J", u"й": u"j",
    u"К": u"K", u"к": u"k",
    u"Л": u"L", u"л": u"l",
    u"М": u"M", u"м": u"m",
    u"Н": u"N", u"н": u"n",
    u"О": u"O", u"о": u"o",
    u"П": u"P", u"п": u"p",
    u"Р": u"R", u"р": u"r",
    u"С": u"S", u"с": u"s",
    u"Т": u"T", u"т": u"t",
    u"У": u"U", u"у": u"u",
    u"Ф": u"F", u"ф": u"f",
    u"Х": u"H", u"х": u"h",
    u"Ц": u"CZ", u"ц": u"cz",
    u"Ч": u"CH", u"ч": u"ch",
    u"Ш": u"SH", u"ш": u"sh",
    u"Щ": u"SHH", u"щ": u"shh",
    u"Ъ": u"''", u"ъ": u"''",
    u"Ы": u"Y'", u"ы": u"y'",
    u"Ь": u"'", u"ь": u"'",
    u"Э": u"E'", u"э": u"e'",
    u"Ю": u"Yu", u"ю": u"yu",
    u"Я": u"Ya", u"я": u"ya",
}

# This dictionary is to transliterate from Russian Latin to Cyrillic.
RU_LAT_TO_CYR_DICT = {y: x for x, y in RU_CYR_TO_LAT_DICT.items()}
RU_LAT_TO_CYR_DICT.update({
    u"''": u"ъ",
    u"'": u"ь",
    u"C": u"К", u"c": u"к",
    u"CK": u"К", u"Ck": u"К", u"ck": u"к",
    u"JA": u"ЖА", u"Ja": u"Жа", u"ja": u"жа",
    u"JE": u"ЖЕ", u"Je": u"Же", u"je": u"же",
    u"JI": u"ЖИ", u"Ji": u"Жи", u"ji": u"жи",
    u"JO": u"ЖО", u"Jo": u"Жо", u"jo": u"жо",
    u"JU": u"ЖУ", u"Ju": u"Жу", u"ju": u"жу",
    u"PH": u"Ф", u"Ph": u"Ф", u"ph": u"ф",
    u"TH": u"З", u"Th": u"З", u"th": u"з",
    u"W": u"В", u"w": u"в", u"Q": u"К", u"q": u"к",
    u"WH": u"В", u"Wh": u"В", u"wh": u"в",
    u"Y": u"И", u"y": u"и",
    u"YA": u"Я", u"Ya": u"Я", u"ya": u"я",
    u"YE": u"Е", u"Ye": u"Е", u"ye": u"е",
    u"YI": u"И", u"Yi": u"И", u"yi": u"и",
    u"YO": u"Ё", u"Yo": u"Ё", u"yo": u"ё",
    u"YU": u"Ю", u"Yu": u"Ю", u"yu": u"ю",
    u"Y'": u"ы", u"y'": u"ы",
    u"iy": u"ый", u"ij": u"ый",  # dobriy => добрый
})
