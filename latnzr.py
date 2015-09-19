# -*- coding: utf-8 -*-
sr_cyrl_rs_to_lat_cyrl_dict = {
    'А': 'A', 'а': 'a',
    'Б': 'B', 'б': 'b',
    'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g', 
    'Д': 'D', 'д': 'd', 
    'Ђ': 'Đ', 'ђ': 'đ', 
    'Е': 'E', 'е': 'e', 
    'Ж': 'Ž', 'ж': 'ž', 
    'З': 'Z', 'з': 'z', 
    'И': 'I', 'и': 'i', 
    'Ј': 'J', 'ј': 'j', 
    'К': 'K', 'к': 'k', 
    'Л': 'L', 'л': 'l', 
    'Љ': 'Lj','љ': 'lj', 
    'М': 'M', 'м': 'm',
    'Н': 'N', 'н': 'n',
    'Њ': 'Nj', 'њ': 'nj',
    'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p',
    'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't',
    'Ћ': 'Ć', 'ћ': 'ć',
    'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f',
    'Х': 'H', 'х': 'h',
    'Ц': 'C', 'ц': 'c',
    'Ч': 'Č', 'ч': 'č',
    'Џ': 'Dž', 'џ': 'dž',
    'Ш': 'Š', 'ш': 'š'

}

to_lat_dict = {
    'sr-cyrl-rs': sr_cyrl_rs_to_lat_cyrl_dict, # Cyrillic Serbia
    'sr-cyrl-ba': None, # Cyrillic Bosnia and Herzegovina
    'sr-cyrl-me': None # Cyrillic Montenegro
}

def to_latin(from_lang_code, string_to_transliterate):

    # First check if we support the cyrillic alphabet we want to transliterate to latin.
    if from_lang_code.lower() not in to_lat_dict:
        # If we don't support it, then just return the original string.
        return string_to_transliterate

    # If we do support it, check if the implementation is not missing before proceeding.
    elif to_lat_dict[from_lang_code.lower()] == None:
        return string_to_transliterate

    # Everything checks out, proceed with transliteration.
    else:

        # Get the character per character transliteration dictionary
        transliteration_dict = to_lat_dict[from_lang_code.lower()]

        # Initiatilize the output latin string variable
        latinized_str = ''

        # Transliterate by traversing the inputted string character by character.
        length_of_string_to_transliterate = len(string_to_transliterate)
        index = 0

        while index < length_of_string_to_transliterate:

            # Grab a character from the string at the current index
            c = string_to_transliterate[index]

            # If the character is '\xd0' or '\xd1', it means that it's only the first half of an encoded cyrillic character,
            # grab the second half.
            if c == '\xd0' or c == '\xd1':
                index = index + 1
                c = c + string_to_transliterate[index]

            # If character is in dictionary, it means it's a cyrillic so let's transliterate that character.
            if c in transliteration_dict:
                # Transliterate current character.
                latinized_str = latinized_str + transliteration_dict[c]

            # If character is not in character transliteration dictionary, 
            # it is most likely a number or a special character so just keep it.   
            else:    
                latinized_str = latinized_str + c

            index = index + 1


        # Return the transliterated string.
        return latinized_str
    