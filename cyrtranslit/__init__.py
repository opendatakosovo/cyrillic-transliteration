# -*- coding: utf-8 -*-
from mapping import TRANSLIT_DICT

def to_latin(string_to_transliterate, lang_code='sr'):
    ''' Transliterate serbian cyrillic string of characters to latin string of characters.
    :param string_to_transliterate: The cyrillic string to transliterate into latin characters.
    :param lang_code: Indicates the cyrillic language code we are translating from. Defaults to Serbian (sr).
    :return: A string of latin characters transliterated from the given cyrillic string.
    '''

    # First check if we support the cyrillic alphabet we want to transliterate to latin.
    if lang_code.lower() not in TRANSLIT_DICT:
        # If we don't support it, then just return the original string.
        return string_to_transliterate

    # If we do support it, check if the implementation is not missing before proceeding.
    elif TRANSLIT_DICT[lang_code.lower()]['tolatin'] == None:
        return string_to_transliterate

    # Everything checks out, proceed with transliteration.
    else:

        # Get the character per character transliteration dictionary
        transliteration_dict = TRANSLIT_DICT[lang_code.lower()]['tolatin']

        # Initialize the output latin string variable
        latinized_str = ''

        # Transliterate by traversing the inputted string character by character.
        string_to_transliterate = string_to_transliterate.decode('utf-8')

        for c in string_to_transliterate:

            # If character is in dictionary, it means it's a cyrillic so let's transliterate that character.
            if c in transliteration_dict:
                # Transliterate current character.
                latinized_str += transliteration_dict[c]

            # If character is not in character transliteration dictionary,
            # it is most likely a number or a special character so just keep it.
            else:
                latinized_str += c

        # Return the transliterated string.
        return latinized_str.encode('utf-8')


def to_cyrillic(string_to_transliterate, lang_code='sr'):
    ''' Transliterate serbian latin string of characters to cyrillic string of characters.
    :param string_to_transliterate: The latin string to transliterate into cyrillic characters.
    :param lang_code: Indicates the cyrillic language code we are translating to. Defaults to Serbian (sr).
    :return: A string of cyrillic characters transliterated from the given latin string.
    '''

    # First check if we support the cyrillic alphabet we want to transliterate to latin.
    if lang_code.lower() not in TRANSLIT_DICT:
        # If we don't support it, then just return the original string.
        return string_to_transliterate

    # If we do support it, check if the implementation is not missing before proceeding.
    elif TRANSLIT_DICT[lang_code.lower()]['tocyrillic'] == None:
        return string_to_transliterate

    else:
        # Get the character per character transliteration dictionary
        transliteration_dict = TRANSLIT_DICT[lang_code.lower()]['tocyrillic']

        # Initialize the output cyrillic string variable
        cyrillic_str = ''

        string_to_transliterate = string_to_transliterate.decode('utf-8')

        # Transliterate by traversing the inputted string character by character.
        length_of_string_to_transliterate = len(string_to_transliterate)
        index = 0

        while index < length_of_string_to_transliterate:
            # Grab a character from the string at the current index
            c = string_to_transliterate[index]

            # Watch out for Lj and lj. Don't want to interpret Lj/lj as L/l and j.
            # Watch out for Nj and nj. Don't want to interpret Nj/nj as N/n and j.
            # Watch out for Dž and and dž. Don't want to interpret Dž/dž as D/d and j.
            c_plus_1 = None
            if index != length_of_string_to_transliterate - 1:
                c_plus_1 = string_to_transliterate[index+1]

            if ((c == u'L' or c == u'l') and c_plus_1 == u'j') or \
                ((c == u'N' or c == u'n') and c_plus_1 == u'j') or \
                ((c == u'D' or c == u'd') and c_plus_1 == u'ž')or \
                (lang_code == 'mk' and (c == u'D' or c == u'd') and c_plus_1 == u'z'):

                index += 1
                c += c_plus_1

            # If character is in dictionary, it means it's a cyrillic so let's transliterate that character.
            if c in transliteration_dict:
                # Transliterate current character.
                cyrillic_str += transliteration_dict[c]

            # If character is not in character transliteration dictionary,
            # it is most likely a number or a special character so just keep it.
            else:
                cyrillic_str += c

            index += 1

        return cyrillic_str.encode('utf-8')

def supported():
    ''' Returns list of supported languages
    :return:
    '''
    return TRANSLIT_DICT.keys()