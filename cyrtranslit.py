import cyrtranslit
from cyrtranslit.mapping import TRANSLIT_DICT
from argparse import ArgumentParser
import os.path


def __is_valid_input_file(parser, arg):
    ''' Validates inputted file to transiletrate.
    :param parse: The argument parser. Used to display error message.
    :param arg: The file path argument.
    '''

    if not os.path.exists(arg):
        parser.error("The file %s does not exist." % arg)
    else:
        return open(arg, 'r')

def __is_valid_language_code(parse, arg):
    ''' Validates inputted two-letter language code.
    :param parse: The argument parser. Used to display error message.
    :param arg: The language code argument.
    '''
    if arg.lower() not in TRANSLIT_DICT:
        parser.error("The language code %s is not supported. Support language codes are: %s." % (arg, ", ".join(TRANSLIT_DICT.keys()).upper()))
    else:
        return arg

def __open_output_file(arg):
    return open(arg, 'w')

# Setup argument parser
parser = ArgumentParser(description="Transiliterate text in a given file.")

# Input file.
# Required.
parser.add_argument("-i", dest="input_file", required=True,
                    help="input file",
                    type=lambda x: __is_valid_input_file(parser, x))

# Output file.
# Not required. If not specified, transliteration will appear as console output.
parser.add_argument("-o", dest="output_file", required=False,
                    help="ouput file",
                    type=lambda x: __open_output_file(x))

# Language code for cyrillic text in inputted file.
# Required.
parser.add_argument("-l", dest="language_code", required=True,
                    help="two-letter ISO 639-1 language code of cyrillic text",
                    type=lambda x: __is_valid_language_code(parser, x))

parser.add_argument("-c", dest="to_cyrillic", action='store_true',
                    help="Parse latin characters to cyrillic (reverse of transliteration)")

# Parse arguments
args = parser.parse_args()

# Fetch arguments.
text_input = args.input_file.read()
lang_code = args.language_code
file_output = args.output_file
to_cyrillic = args.to_cyrillic

# Transliterate.
if to_cyrillic is True:
    text_output = cyrtranslit.to_cyrillic(text_input, lang_code=lang_code)
else:
    text_output = cyrtranslit.to_latin(text_input, lang_code=lang_code)

# Write output.
if file_output is None:
    print(text_output)
else:
    file_output.write(text_output)
    # Close output stream.
    file_output.close()

# Close input stream.
args.input_file.close()
