# -*- coding: utf-8 -*-

def to_latin(string_to_transliterate, from_lang_code='sr'):

    # First check if we support the cyrillic alphabet we want to transliterate to latin.
    if from_lang_code.lower() not in translit_dict:
        # If we don't support it, then just return the original string.
        return string_to_transliterate

    # If we do support it, check if the implementation is not missing before proceeding.
    elif translit_dict[from_lang_code.lower()] == None:
        return string_to_transliterate

    # Everything checks out, proceed with transliteration.
    else:

        # Get the character per character transliteration dictionary
        transliteration_dict = translit_dict[from_lang_code.lower()]

        # Initiatilize the output latin string variable
        latinized_str = ''

        # Transliterate by traversing the inputted string character by character.
        string_to_transliterate = string_to_transliterate.decode('utf-8')
        length_of_string_to_transliterate = len(string_to_transliterate)
        index = 0

        for c in string_to_transliterate:

            # If character is in dictionary, it means it's a cyrillic so let's transliterate that character.
            if c in transliteration_dict:
                # Transliterate current character.
                latinized_str = latinized_str + transliteration_dict[c]

            # If character is not in character transliteration dictionary, 
            # it is most likely a number or a special character so just keep it.   
            else:    
                latinized_str = latinized_str + c

        # Return the transliterated string.
        return latinized_str.encode('utf-8')


def to_cyrillic(string_to_transliterate, to_lang_code='sr'):
    # First check if we support the cyrillic alphabet we want to transliterate to latin.
    if to_lang_code.lower() not in translit_dict:
        # If we don't support it, then just return the original string.
        return string_to_transliterate

    # If we do support it, check if the implementation is not missing before proceeding.
    elif translit_dict[to_lang_code.lower()] == None:
        return string_to_transliterate

    else:
        # Get the character per character transliteration dictionary
        transliteration_dict = translit_dict[to_lang_code.lower()]

        # The dictionary is to transliterate from cyrillic to latin but
        # we want to transliterate from latin to cyrillic so let's swap keys and values.
        swapped_translit_dict = {y:x for x,y in transliteration_dict.iteritems()}
        
        # Initiatilize the output cyrillic string variable
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
            # Watch out for Dž and and dž. Don't want to interpret Dž/dž as D/d and j. ž ==> \xc5\xbe
            c_plus_1 = None
            if index != length_of_string_to_transliterate - 1:
                c_plus_1 = string_to_transliterate[index+1]

            if  ((c == u'L' or c == u'l') and c_plus_1 == u'j') or \
                ((c == u'N' or c == u'n') and c_plus_1 == u'j') or \
                ((c == u'D' or c == u'd') and c_plus_1 == u'ž'):

                index += 1
                c = c + c_plus_1

            # If character is in dictionary, it means it's a cyrillic so let's transliterate that character.
            if c in swapped_translit_dict:
                # Transliterate current character.
                cyrillic_str = cyrillic_str + swapped_translit_dict[c]

            # If character is not in character transliteration dictionary, 
            # it is most likely a number or a special character so just keep it.   
            else:    
                cyrillic_str = cyrillic_str + c

            index += 1

        return cyrillic_str.encode('utf-8')

sr_to_lat_dict = {
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
    u'Њ': u'Nj',u'њ':u'nj',
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
    u'Ш': u'Š', u'ш': u'š'
}

translit_dict = {
    'sr': sr_to_lat_dict, # Serbia
    'bs': None, # Bosnia and Herzegovina
    'me': None, # Montenegro
    'mk': None # Macedonia
}
    