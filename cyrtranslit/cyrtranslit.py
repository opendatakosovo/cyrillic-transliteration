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
                        default=None)

    # Output file.
    # Not required. If not specified, transliteration will appear as console output.
    parser.add_argument("-o", dest="output_file", required=False,
                        help="ouput file",
                        default=None)

    # Language code for cyrillic text in inputted file.
    # Required.
    parser.add_argument("-l", dest="language_code", required=True,
                        help="two-letter ISO 639-1 language code of cyrillic text",
                        type=lambda x: __is_valid_language_code(parser, x))

    # Flag for reverse transliteration, i.e. from latin/roman alphabet to cyrillic.
    parser.add_argument("-c", dest="to_cyrillic", action='store_true',
                        help="Parse latin characters to cyrillic (reverse of transliteration)")

    # Flag to preserve accent marks in transliteration
    parser.add_argument("-p", "--preserve-accents", dest="preserve_accents", action='store_true',
                        help="Preserve accent marks (e.g., Macedonian/Bulgarian Ѐ→È, ѝ→ì instead of Ѐ→E, ѝ→i)")

    # Input file encoding.
    # Not required. Defaults to utf-8 with fallback to common Cyrillic encodings.
    parser.add_argument("-e", "--encoding", dest="encoding", required=False,
                        help="input file encoding (default: utf-8 with automatic fallback to windows-1251, iso-8859-5, koi8-r, cp866)",
                        default="utf-8")

    # Parse arguments
    args = parser.parse_args()

    # Fetch arguments.
    lang_code = args.language_code
    to_cyrillic = args.to_cyrillic
    preserve_accents = args.preserve_accents
    encoding = args.encoding

    # Open input file with proper encoding handling
    if args.input_file:
        # Try specified encoding first
        file_input = None
        tried_encodings = [encoding]

        # Helper function to test if an encoding works
        def try_encoding(filepath, enc):
            try:
                f = open(filepath, 'r', encoding=enc)
                # Try to read the file to actually test the encoding
                f.read()
                # If successful, reopen from the beginning
                f.close()
                return open(filepath, 'r', encoding=enc)
            except (UnicodeDecodeError, LookupError):
                if f:
                    f.close()
                return None

        file_input = try_encoding(args.input_file, encoding)

        if file_input is None:
            # If specified encoding fails, try common Cyrillic encodings as fallback
            fallback_encodings = ['windows-1251', 'iso-8859-5', 'koi8-r', 'cp866']

            for fallback_enc in fallback_encodings:
                if fallback_enc == encoding:
                    continue  # Already tried this one
                tried_encodings.append(fallback_enc)
                file_input = try_encoding(args.input_file, fallback_enc)
                if file_input is not None:
                    print(f"Warning: Failed to decode with {encoding}, using {fallback_enc} instead.", file=sys.stderr)
                    break

            if file_input is None:
                print(f"Error: Unable to decode file with any of the attempted encodings: {', '.join(tried_encodings)}", file=sys.stderr)
                print(f"Try specifying the correct encoding with -e/--encoding parameter.", file=sys.stderr)
                print(f"Common Cyrillic encodings: windows-1251, iso-8859-5, koi8-r, cp866", file=sys.stderr)
                sys.exit(1)
    else:
        file_input = sys.stdin

    # Open output file
    if args.output_file:
        file_output = open(args.output_file, 'w', encoding='utf-8')
    else:
        file_output = sys.stdout

    # Transliterate and write directly to output line by line
    try:
        for line in file_input:
            if to_cyrillic is True:
                file_output.write(cyrtranslit.to_cyrillic(line, lang_code=lang_code, preserve_accents=preserve_accents))
            else:
                file_output.write(cyrtranslit.to_latin(line, lang_code=lang_code, preserve_accents=preserve_accents))
    finally:
        # Close streams if they're not stdin/stdout
        if args.input_file and file_input:
            file_input.close()
        if args.output_file and file_output:
            file_output.close()

if __name__ == "__main__":
    main()
