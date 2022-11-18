import cyrtranslit
from cyrtranslit.mapping import TRANSLIT_DICT
from argparse import ArgumentParser, FileType
import os
import sys

def __is_valid_language_code(parse, arg):
    ''' Validates inputted two-letter language code.
    :param parse: The argument parser. Used to display error message.
    :param arg: The language code argument.
    '''
    if arg.lower() not in TRANSLIT_DICT:
        parser.error("The language code %s is not supported. Support language codes are: %s." % (arg, ", ".join(TRANSLIT_DICT.keys()).upper()))
    else:
        return arg

def main():
    # Setup argument parser
    parser = ArgumentParser(description="Transiliterate text in a given file.")

    # Input file.
    # Not required.
    parser.add_argument("-i", dest="input_file", required=False,
                        help="input file",
                        type=FileType('rt'),
                        default=sys.stdin)

    # Output file.
    # Not required. If not specified, transliteration will appear as console output.
    parser.add_argument("-o", dest="output_file", required=False,
                        help="ouput file",
                        type=FileType('w'),
                        default=sys.stdout)

    # Language code for cyrillic text in inputted file.
    # Required.
    parser.add_argument("-l", dest="language_code", required=True,
                        help="two-letter ISO 639-1 language code of cyrillic text",
                        type=lambda x: __is_valid_language_code(parser, x))

    # Flag for reverse transliteration, i.e. from latin/roman alphabet to cyrillic.
    parser.add_argument("-c", dest="to_cyrillic", action='store_true',
                        help="Parse latin characters to cyrillic (reverse of transliteration)")

    # Parse arguments
    args = parser.parse_args()

    # Fetch arguments.
    lang_code = args.language_code
    file_output = args.output_file
    file_input = args.input_file
    to_cyrillic = args.to_cyrillic

    # Transliterate and write directly to output line by line
    for line in file_input:
        if to_cyrillic is True:
            file_output.write(cyrtranslit.to_cyrillic(line, lang_code=lang_code))
        else:
            file_output.write(cyrtranslit.to_latin(line, lang_code=lang_code))

    # Close output stream.
    file_output.close()

if __name__ == "__main__":
    main()
