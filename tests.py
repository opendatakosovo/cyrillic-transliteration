# -*- coding: utf-8 -*-
import unittest
import cyrtranslit

# Test inputs and output strings
serbian_alphabet_cyrillic = 'АаБбВвГгДдЂђЕеЖжЗзИиЈјКкЛлЉљМмНнЊњОоПпРрСсТтЋћУуФфХхЦцЧчЏџШш'
serbian_alphabet_latin = 'AaBbVvGgDdĐđEeŽžZzIiJjKkLlLjljMmNnNjnjOoPpRrSsTtĆćUuFfHhCcČčDždžŠš'

montenegrin_alphabet_cyrillic = 'АаБбВвГгДдЂђЕеЖжЗзЗ́з́ИиЈјКкЛлЉљМмНнЊњОоПпРрСсТтЋћУуФфХхЦцЧчЏџШшС́с́'
montenegrin_alphabet_latin = 'AaBbVvGgDdĐđEeŽžZzŹźIiJjKkLlLjljMmNnNjnjOoPpRrSsTtĆćUuFfHhCcČčDždžŠšŚś'

macedonian_alphabet_cyrillic = 'АаБбВвГгДдЃѓЕеЖжЗзЅѕИиЈјКкЛлЉљМмНнЊњОоПпРрСсТтЌќУуФфХхЦцЧчЏџШш'
macedonian_alphabet_latin = 'AaBbVvGgDdǴǵEeŽžZzDzdzIiJjKkLlLjljMmNnNjnjOoPpRrSsTtḰḱUuFfHhCcČčDždžŠš'

russian_alphabet_cyrillic = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыьЭэЮюЯя'
russian_alphabet_latin = 'AaBbVvGgDdEeYOyoZHzhZzIiJjKkLlMmNnOoPpRrSsTtUuFfHhCZczCHchSHshSHHshh\'\'\'\'Y\'y\'\'E\'e\'YuyuYaya'

tajik_alphabet_cyrillic = 'АаБбВвГгҒғДдЕеЁёЖжЗзИиӢӣЙйКкЛлМмНнОоПпРрСсТтУуӮӯФфХхҲҳЧчҶҷШшъЭэЮюЯя'
tajik_alphabet_latin = 'AaBbVvGgǦǧDdEeËëŽžZzIiĪīJjKkLlMmNnOoPpRrSsTtUuŪūFfHhḨḩČčÇçŠš’ÈèÛûÂâ'

bulgarian_alphabet_cyrillic = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЬьЮюЯя'
bulgarian_alphabet_latin = 'AaBbVvGgDdEeZHzhZzIiYyKkLlMmNnOoPpRrSsTtUuFfHhTStsCHchSHshSHTshtĂăJjYUyuYAya'

# not testing Ь for the apostrophe, sticking with just ь. Both will transliterate to '.
ukrainian_alphabet_cyrillic = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЮюЯяь'
ukrainian_alphabet_latin = 'AaBbVvHhGgDdEeJejeŽžZzYyIiJijiJjKkLlMmNnOoPpRrSsTtUuFfXxCcČčŠšŠčščJujuJaja\''

belarusian_alphabet_cyrillic = 'АаБбВвГгДдЕеЁёЖжЗзІіЙйКкЛлМмНнОоПпРрСсТтУуЎўФфХхЦцЧчШшЫыЬьЭэЮюЯя'
belarusian_alphabet_latin = 'AaBbVvHhDdEeËëŽžZzIiJjKkLlMmNnOoPpRrSsTtUuŬŭFfXxCcČčŠšYy\'\'ĖėJujuJaja'

greek_alphabet = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω'
greek_alphabet_latin = 'AaVvGgDdEeZzHhThthIiKkLlMmNnXxOoPpRrSssTtYyFfChchPspsWw'

mongolian_alphabet_cyrillic = 'АаЭэИиОоУуӨөҮүНнМмЛлВвПпФфКкХхГгСсШшТтДдЦцЧчЗзЖжРрБбЕеЁёЫыЮюЯя'  # exclude (Й Ъ Ь)<->I  Щ<->Sh
mongolian_alphabet_latin = 'AaEeIiOoUuÖöÜüNnMmLlVvPpFfKkKhkhGgSsShshTtDdTstsChchZzJjRrBbYeyeYoyoYyYuyuYaya'

special_chars = '‘’‚“”„†‡‰‹›♠♣♥♦‾←↑→↓™!"#$%&\'()*+,-./ :;<=>?@[\\]^_`{|}~…–—¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×'

diacritic_chars = 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

numerical_chars = '1234567890'

alphabet_chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

mix_characters_some_cyrillic = '!ЉFљñМ мНÈÆнЊњО)*+,оП>пР?р'
mix_characters_all_latin = '!LjFljñM mNÈÆnNjnjO)*+,oP>pR?r'

mix_characters_some_cyrillic_no_alpha = '\'Ћ<=>?ћУуФфХхЦцЧчЏ%4џШ12ш♥'
mix_characters_all_latin_no_alpha = '\'Ć<=>?ćUuFfHhCcČčDž%4džŠ12š♥'


class TestSerbianTransliterationFromCyrillicToLatin(unittest.TestCase):

    def test_alphabet_transliteration(self):
        ''' Transliteration of entire Serbian cyrillic alphabet to latin.
        '''
        transliterated_serbian_alphabet = cyrtranslit.to_latin(serbian_alphabet_cyrillic)

        self.assertEqual(transliterated_serbian_alphabet, serbian_alphabet_latin)


    def test_special_characters(self):
        ''' Special characters should remain the same.
        '''
        transliterated_special_chars = cyrtranslit.to_latin(special_chars)

        self.assertEqual(transliterated_special_chars, special_chars)


    def test_special_diacritic_characters(self):
        ''' Diacritic characters should remain the same.
        '''
        transliterated_diacritic_chars = cyrtranslit.to_latin(diacritic_chars)

        self.assertEqual(transliterated_diacritic_chars, diacritic_chars)


    def test_numerical_characters(self):
        ''' Numerical characters should remain the same.
        '''
        transliterated_numerical_chars = cyrtranslit.to_latin(numerical_chars)

        self.assertEqual(transliterated_numerical_chars, numerical_chars)


    def test_latin_alphabet_characters(self):
        ''' Alphabet characters should remain the same.
        '''
        transliterated_alphabet_chars = cyrtranslit.to_latin(alphabet_chars)

        self.assertEqual(transliterated_alphabet_chars, alphabet_chars)


    def test_mix_characters(self):
        ''' Serbian cyrillic characters should be transliterated but non serbian cyrillic ones shouldn't.
        '''

        transliterated_mix = cyrtranslit.to_latin(mix_characters_some_cyrillic)

        self.assertEqual(transliterated_mix, mix_characters_all_latin)


class TestSerbianTransliterationFromLatinToCyrillic(unittest.TestCase):

    def test_alphabet_transliteration(self):
        ''' Transliteration of entire Serbian cyrillic alphabet to latin.
        '''
        transliterated_serbian_alphabet = cyrtranslit.to_cyrillic(serbian_alphabet_latin)

        self.assertEqual(transliterated_serbian_alphabet, serbian_alphabet_cyrillic)


    def test_special_characters(self):
        ''' Special characters should remain the same.
        '''
        transliterated_special_chars = cyrtranslit.to_cyrillic(special_chars)

        self.assertEqual(transliterated_special_chars, special_chars)


    def test_special_diacritic_characters(self):
        ''' Diacritic characters should remain the same.
        '''
        transliterated_diacritic_chars = cyrtranslit.to_cyrillic(diacritic_chars)

        self.assertEqual(transliterated_diacritic_chars, diacritic_chars)


    def test_numerical_characters(self):
        ''' Numerical characters should remain the same.
        '''
        transliterated_numerical_chars = cyrtranslit.to_cyrillic(numerical_chars)

        self.assertEqual(transliterated_numerical_chars, numerical_chars)

    def test_mix_characters(self):
        ''' Serbian cyrillic characters should be transliterated but non serbian cyrillic ones shouldn't.
        '''
        transliterated_mix = cyrtranslit.to_cyrillic(mix_characters_all_latin_no_alpha)

        self.assertEqual(transliterated_mix, mix_characters_some_cyrillic_no_alpha)


class TestSerbianCountryCodeAlias(unittest.TestCase):
    ''' Test that 'rs' (ISO 3166-1 country code) works as alias for 'sr' (ISO 639-1 language code).
        Addresses issue #46.
    '''

    def test_rs_to_latin(self):
        ''' Test transliteration using 'rs' country code to latin.
        '''
        transliterated = cyrtranslit.to_latin("Мој ховеркрафт је пун јегуља", lang_code='rs')
        self.assertEqual(transliterated, "Moj hoverkraft je pun jegulja")

    def test_rs_to_cyrillic(self):
        ''' Test transliteration using 'rs' country code to cyrillic.
        '''
        transliterated = cyrtranslit.to_cyrillic("Moj hoverkraft je pun jegulja", lang_code='rs')
        self.assertEqual(transliterated, "Мој ховеркрафт је пун јегуља")

    def test_rs_alphabet_to_latin(self):
        ''' Test full alphabet transliteration with 'rs' code.
        '''
        transliterated = cyrtranslit.to_latin(serbian_alphabet_cyrillic, lang_code='rs')
        self.assertEqual(transliterated, serbian_alphabet_latin)


class TestMontenegrinTransliteration(unittest.TestCase):
    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliteration of entire cyrillic alphabet to latin.
        '''
        transliterated_alphabet = cyrtranslit.to_latin(montenegrin_alphabet_cyrillic, lang_code='me')

        # transliterated_alphabet =  u's\u0301' 's\xcc\x81'
        self.assertEqual(transliterated_alphabet, montenegrin_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliteration of entire latin alphabet to cyrillic.
        '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(montenegrin_alphabet_latin, lang_code='me')

        self.assertEqual(transliterated_alphabet, montenegrin_alphabet_cyrillic)


class TestMacedonianTransliteration(unittest.TestCase):
    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliteration of entire cyrillic alphabet to latin.
        '''
        transliterated_alphabet = cyrtranslit.to_latin(macedonian_alphabet_cyrillic, lang_code='mk')

        # transliterated_alphabet =  u's\u0301' 's\xcc\x81'
        self.assertEqual(transliterated_alphabet, macedonian_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliteration of entire latin alphabet to cyrillic.
        '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(macedonian_alphabet_latin, lang_code='mk')

        self.assertEqual(transliterated_alphabet, macedonian_alphabet_cyrillic)


class TestRussianTransliteration(unittest.TestCase):
    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliteration of entire cyrillic alphabet to latin.
        '''
        transliterated_alphabet = cyrtranslit.to_latin(russian_alphabet_cyrillic, lang_code='ru')

        self.assertEqual(transliterated_alphabet, russian_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliteration of entire latin alphabet to cyrillic.
        '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(russian_alphabet_latin, lang_code='ru')

        self.assertEqual(transliterated_alphabet, russian_alphabet_cyrillic.replace('Ъ', 'ъ').replace('Ь', 'ь').replace('Ы', 'ы'))

    def test_h_transliteration(self):
        ''' Cyrillic Х should transliterate to H, not X.
        '''
        self.assertEqual(cyrtranslit.to_latin('Х', lang_code='ru'), 'H')
        self.assertEqual(cyrtranslit.to_latin('х', lang_code='ru'), 'h')
        self.assertEqual(cyrtranslit.to_cyrillic('H', lang_code='ru'), 'Х')
        self.assertEqual(cyrtranslit.to_cyrillic('h', lang_code='ru'), 'х')

    def test_ya_capitalization(self):
        ''' Capital Я should transliterate to Ya, not YA.
        '''
        self.assertEqual(cyrtranslit.to_latin('Я', lang_code='ru'), 'Ya')
        self.assertEqual(cyrtranslit.to_latin('я', lang_code='ru'), 'ya')
        self.assertEqual(cyrtranslit.to_latin('Янковский', lang_code='ru'), 'Yankovskij')
        self.assertEqual(cyrtranslit.to_latin('яблоко', lang_code='ru'), 'yabloko')
        self.assertEqual(cyrtranslit.to_cyrillic('Ya', lang_code='ru'), 'Я')
        self.assertEqual(cyrtranslit.to_cyrillic('ya', lang_code='ru'), 'я')

class TestTajikTransliteration(unittest.TestCase):
    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliterate the entire cyrillic alphabet to latin '''
        transliterated_alphabet = cyrtranslit.to_latin(tajik_alphabet_cyrillic, lang_code='tj')

        self.assertEqual(transliterated_alphabet, tajik_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliterate the entire latin alphabet to cyrillic '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(tajik_alphabet_latin, lang_code='tj')

        self.assertEqual(transliterated_alphabet, tajik_alphabet_cyrillic)
 
class TestUkrainianTransliteration(unittest.TestCase):
    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliterate the entire cyrillic alphabet to latin '''
        transliterated_alphabet = cyrtranslit.to_latin(ukrainian_alphabet_cyrillic, lang_code='ua')

        self.assertEqual(transliterated_alphabet, ukrainian_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliterate the entire latin alphabet to cyrillic '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(ukrainian_alphabet_latin, lang_code='ua')

        self.assertEqual(transliterated_alphabet, ukrainian_alphabet_cyrillic)


    def test_special_diacritic_characters(self):
        ''' Diacritic characters should remain the same.
        '''
        transliterated_diacritic_chars = cyrtranslit.to_latin(diacritic_chars, lang_code='tj')

        self.assertEqual(transliterated_diacritic_chars, diacritic_chars)


    def test_numerical_characters(self):
        ''' Numerical characters should remain the same.
        '''
        transliterated_numerical_chars = cyrtranslit.to_latin(numerical_chars, lang_code='tj')

        self.assertEqual(transliterated_numerical_chars, numerical_chars)


class TestBelarusianTransliteration(unittest.TestCase):
    ''' Test Belarusian transliteration. Addresses issue #47.
    '''

    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliterate the entire Belarusian cyrillic alphabet to latin.
        '''
        transliterated_alphabet = cyrtranslit.to_latin(belarusian_alphabet_cyrillic, lang_code='by')

        self.assertEqual(transliterated_alphabet, belarusian_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliterate the entire Belarusian latin alphabet to cyrillic.
        '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(belarusian_alphabet_latin, lang_code='by')

        self.assertEqual(transliterated_alphabet, belarusian_alphabet_cyrillic)

    def test_phrase_transliteration_to_latin(self):
        ''' Test common Belarusian phrase transliteration.
        '''
        # "Hello, World!" in Belarusian
        cyrillic_text = "Прывітанне, свет!"
        expected_latin = "Pryvitanne, svet!"

        transliterated = cyrtranslit.to_latin(cyrillic_text, lang_code='by')
        self.assertEqual(transliterated, expected_latin)

    def test_short_u_transliteration(self):
        ''' Test Belarusian unique letter Ў (short U).
        '''
        # Ў is unique to Belarusian
        self.assertEqual(cyrtranslit.to_latin("Ў", lang_code='by'), "Ŭ")
        self.assertEqual(cyrtranslit.to_latin("ў", lang_code='by'), "ŭ")
        self.assertEqual(cyrtranslit.to_cyrillic("Ŭ", lang_code='by'), "Ў")
        self.assertEqual(cyrtranslit.to_cyrillic("ŭ", lang_code='by'), "ў")


class TestGreekTransliteration(unittest.TestCase):
    ''' Test Greek transliteration. Addresses issue #40.
    '''

    def test_alphabet_transliteration_to_latin(self):
        ''' Transliterate the entire Greek alphabet to latin.
        '''
        transliterated_alphabet = cyrtranslit.to_latin(greek_alphabet, lang_code='el')

        self.assertEqual(transliterated_alphabet, greek_alphabet_latin)

    def test_alphabet_transliteration_to_greek(self):
        ''' Transliterate the entire latin alphabet to Greek.
            Note: Final sigma (ς) converts to regular sigma (σ) when going Latin→Greek
            since we can't determine word endings from Latin text.
        '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(greek_alphabet_latin, lang_code='el')

        # Replace final sigma with regular sigma for comparison
        expected_greek = greek_alphabet.replace('ς', 'σ')
        self.assertEqual(transliterated_alphabet, expected_greek)

    def test_theta_transliteration(self):
        ''' Test Greek Theta (Θθ) transliterates to Th/th.
        '''
        self.assertEqual(cyrtranslit.to_latin('Θ', lang_code='el'), 'Th')
        self.assertEqual(cyrtranslit.to_latin('θ', lang_code='el'), 'th')
        self.assertEqual(cyrtranslit.to_cyrillic('Th', lang_code='el'), 'Θ')
        self.assertEqual(cyrtranslit.to_cyrillic('th', lang_code='el'), 'θ')

    def test_chi_transliteration(self):
        ''' Test Greek Chi (Χχ) transliterates to Ch/ch.
        '''
        self.assertEqual(cyrtranslit.to_latin('Χ', lang_code='el'), 'Ch')
        self.assertEqual(cyrtranslit.to_latin('χ', lang_code='el'), 'ch')
        self.assertEqual(cyrtranslit.to_cyrillic('Ch', lang_code='el'), 'Χ')
        self.assertEqual(cyrtranslit.to_cyrillic('ch', lang_code='el'), 'χ')

    def test_psi_transliteration(self):
        ''' Test Greek Psi (Ψψ) transliterates to Ps/ps.
        '''
        self.assertEqual(cyrtranslit.to_latin('Ψ', lang_code='el'), 'Ps')
        self.assertEqual(cyrtranslit.to_latin('ψ', lang_code='el'), 'ps')
        self.assertEqual(cyrtranslit.to_cyrillic('Ps', lang_code='el'), 'Ψ')
        self.assertEqual(cyrtranslit.to_cyrillic('ps', lang_code='el'), 'ψ')

    def test_final_sigma(self):
        ''' Test Greek final sigma (ς) transliterates same as regular sigma.
        '''
        self.assertEqual(cyrtranslit.to_latin('ς', lang_code='el'), 's')
        self.assertEqual(cyrtranslit.to_latin('Σ', lang_code='el'), 'S')
        self.assertEqual(cyrtranslit.to_latin('σ', lang_code='el'), 's')

    def test_phrase_transliteration(self):
        ''' Test common Greek phrase transliteration.
        '''
        # "Hello" in Greek (Γειά σου)
        greek_text = "Γειά σου"
        expected_latin = "Geia soy"

        transliterated = cyrtranslit.to_latin(greek_text, lang_code='el')
        self.assertEqual(transliterated, expected_latin)


class TestBulgarianTransliteration(unittest.TestCase):
    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliteration of entire cyrillic alphabet to latin.
        '''
        transliterated_alphabet = cyrtranslit.to_latin(bulgarian_alphabet_cyrillic, lang_code='bg')

        self.assertEqual(transliterated_alphabet, bulgarian_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliteration of entire latin alphabet to cyrillic.
        '''
        transliterated_alphabet = cyrtranslit.to_cyrillic(bulgarian_alphabet_latin, lang_code='bg')

        self.assertEqual(transliterated_alphabet, bulgarian_alphabet_cyrillic)

    def test_sh_at_the_end_of_string(self):
        ''' Check if "sh" at the of the string doesn't cause any exception.'''
        transliterated_alphabet = cyrtranslit.to_cyrillic("AaBbsh", lang_code='bg')

        self.assertEqual(transliterated_alphabet, "АаБбш")


class TestMongolianTransliterationFromCyrillicToLatin(unittest.TestCase):

    def test_alphabet_transliteration_cyrillic_to_latin(self):
        ''' Transliteration of entire Mongolian cyrillic alphabet to latin.
        '''
        transliterated_mongolian_alphabet = cyrtranslit.to_latin(mongolian_alphabet_cyrillic, 'mn')

        self.assertEqual(transliterated_mongolian_alphabet, mongolian_alphabet_latin)

    def test_alphabet_transliteration_latin_to_cyrillic(self):
        ''' Transliteration of entire latin alphabet to cyrillic.
        '''
        transliterated_mongolian_alphabet = cyrtranslit.to_cyrillic(mongolian_alphabet_latin, 'mn')

        self.assertEqual(transliterated_mongolian_alphabet, mongolian_alphabet_cyrillic)

    def test_mixed_casing_transliteration_latin_to_cyrillic(self):
        ''' Transliteration from latin with mixed casing, e.g. Sh SH sh sH.
        '''
        input_latin = 'KhKHkhkHShSHshsHTsTStstSChCHchcHYeYEyeyEYoYOyoyOYaYAyayA'
        expected_output_cyrillic = 'ХХххШШшшЦЦццЧЧччЕЕееЁЁёёЯЯяя'

        actual_output_cyrillic = cyrtranslit.to_cyrillic(input_latin, 'mn')

        self.assertEqual(actual_output_cyrillic, expected_output_cyrillic)

    def test_transliteration_cyrillic_to_sh(self):
        ''' Transliteration from Ш/Щ and ш/щ should be Sh and sh.
            Both Ш and Щ are pronounced the same (/ʃ/) in Mongolian.
        '''
        input_cyrillic = 'ШшЩщ'
        expected_output_latin = 'ShshShsh'

        actual_output_latin = cyrtranslit.to_latin(input_cyrillic, 'mn')

        self.assertEqual(actual_output_latin, expected_output_latin)

    def test_transliteration_sh_to_cyrillic_defaults_to_sha(self):
        ''' Transliteration from Latin Sh/sh should default to Ш (not Щ).
            Ш is more commonly used in Mongolian than Щ (which appears mainly in loanwords).
        '''
        input_latin = 'ShSHshsH'
        expected_output_cyrillic = 'ШШшш'  # All variants should produce Ш (with proper casing)

        actual_output_cyrillic = cyrtranslit.to_cyrillic(input_latin, 'mn')

        self.assertEqual(actual_output_cyrillic, expected_output_cyrillic)


class TestFileEncoding(unittest.TestCase):
    ''' Test transliteration from files with different encodings.
    '''

    def test_windows1251_encoded_file(self):
        ''' Test that we can read and transliterate a windows-1251 encoded file.
            This addresses issue #49 where files with non-UTF-8 Cyrillic encodings
            would fail with UnicodeDecodeError.
        '''
        import subprocess
        import sys

        # Run the CLI tool on a windows-1251 encoded file (auto-detection)
        result = subprocess.run(
            [sys.executable, '-m', 'cyrtranslit.cyrtranslit', '-l', 'bg', '-i', 'tests/bg_windows1251.txt'],
            capture_output=True,
            text=True
        )

        # Should not fail with UnicodeDecodeError
        self.assertEqual(result.returncode, 0, f"Command failed with: {result.stderr}")

        # Should produce Latin output
        self.assertIn('Zdravey', result.stdout)

        # Should show a warning that it fell back to windows-1251
        self.assertIn('windows-1251', result.stderr)

    def test_explicit_encoding_parameter(self):
        ''' Test that we can explicitly specify the encoding with -e parameter.
        '''
        import subprocess
        import sys

        # Run the CLI tool with explicit encoding parameter
        result = subprocess.run(
            [sys.executable, '-m', 'cyrtranslit.cyrtranslit', '-l', 'bg', '-i', 'tests/bg_windows1251.txt', '-e', 'windows-1251'],
            capture_output=True,
            text=True
        )

        # Should not fail
        self.assertEqual(result.returncode, 0, f"Command failed with: {result.stderr}")

        # Should produce Latin output
        self.assertIn('Zdravey', result.stdout)

        # Should NOT show a warning when correct encoding is specified
        self.assertNotIn('Warning', result.stderr)


if __name__ == '__main__':
    # Run all tests.
    unittest.main()
