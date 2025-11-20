# -*- coding: utf-8 -*-
"""
Greek (el) transliteration mappings.

ISO 639-1 language code: el

Transliteration follows ELOT 743 / ISO 843.
https://en.wikipedia.org/wiki/Greek_alphabet
https://en.wikipedia.org/wiki/Romanization_of_Greek
"""

# Transliterate from Greek to Latin (ELOT 743 / ISO 843)
EL_GRE_TO_LAT_DICT = {
    u"Α": u"A", u"α": u"a", u"Ά": u"A", u"ά": u"a",  # alpha (with/without tonos)
    u"Β": u"V", u"β": u"v",
    u"Γ": u"G", u"γ": u"g",
    u"Δ": u"D", u"δ": u"d",
    u"Ε": u"E", u"ε": u"e", u"Έ": u"E", u"έ": u"e",  # epsilon (with/without tonos)
    u"Ζ": u"Z", u"ζ": u"z",
    u"Η": u"H", u"η": u"h", u"Ή": u"H", u"ή": u"h",  # eta (with/without tonos)
    u"Θ": u"Th", u"θ": u"th",
    u"Ι": u"I", u"ι": u"i", u"Ί": u"I", u"ί": u"i", u"Ϊ": u"I", u"ϊ": u"i",  # iota (with tonos/dialytika)
    u"Κ": u"K", u"κ": u"k",
    u"Λ": u"L", u"λ": u"l",
    u"Μ": u"M", u"μ": u"m",
    u"Ν": u"N", u"ν": u"n",
    u"Ξ": u"X", u"ξ": u"x",
    u"Ο": u"O", u"ο": u"o", u"Ό": u"O", u"ό": u"o",  # omicron (with/without tonos)
    u"Π": u"P", u"π": u"p",
    u"Ρ": u"R", u"ρ": u"r",
    u"Σ": u"S", u"σ": u"s", u"ς": u"s",  # sigma (ς is final sigma)
    u"Τ": u"T", u"τ": u"t",
    u"Υ": u"Y", u"υ": u"y", u"Ύ": u"Y", u"ύ": u"y", u"Ϋ": u"Y", u"ϋ": u"y",  # upsilon (with tonos/dialytika)
    u"Φ": u"F", u"φ": u"f",
    u"Χ": u"Ch", u"χ": u"ch",
    u"Ψ": u"Ps", u"ψ": u"ps",
    u"Ω": u"W", u"ω": u"w", u"Ώ": u"W", u"ώ": u"w",  # omega (with/without tonos)
}

# This dictionary is to transliterate from Latin to Greek
# Build the reverse mapping, but only include unaccented letters
# (accented vowels transliterate to same Latin as unaccented, so we default to unaccented)
EL_LAT_TO_GRE_DICT = {
    u"A": u"Α", u"a": u"α",
    u"V": u"Β", u"v": u"β",
    u"G": u"Γ", u"g": u"γ",
    u"D": u"Δ", u"d": u"δ",
    u"E": u"Ε", u"e": u"ε",
    u"Z": u"Ζ", u"z": u"ζ",
    u"H": u"Η", u"h": u"η",
    u"I": u"Ι", u"i": u"ι",
    u"K": u"Κ", u"k": u"κ",
    u"L": u"Λ", u"l": u"λ",
    u"M": u"Μ", u"m": u"μ",
    u"N": u"Ν", u"n": u"ν",
    u"X": u"Ξ", u"x": u"ξ",
    u"O": u"Ο", u"o": u"ο",
    u"P": u"Π", u"p": u"π",
    u"R": u"Ρ", u"r": u"ρ",
    u"S": u"Σ", u"s": u"σ",
    u"T": u"Τ", u"t": u"τ",
    u"Y": u"Υ", u"y": u"υ",
    u"F": u"Φ", u"f": u"φ",
    u"W": u"Ω", u"w": u"ω",
}
EL_LAT_TO_GRE_DICT.update({
    u"TH": u"Θ", u"Th": u"Θ", u"th": u"θ",
    u"CH": u"Χ", u"Ch": u"Χ", u"ch": u"χ",
    u"PS": u"Ψ", u"Ps": u"Ψ", u"ps": u"ψ",
})
