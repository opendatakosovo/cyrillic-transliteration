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
russian_alphabet_latin = 'AaBbVvGgDdEeYOyoZHzhZzIiJjKkLlMmNnOoPpRrSsTtUuFfXxCZczCHchSHshSHHshh\'\'\'\'Y\'y\'\'E\'e\'YUyuYAya'

tajik_alphabet_cyrillic = 'АаБбВвГгҒғДдЕеЁёЖжЗзИиӢӣЙйКкЛлМмНнОоПпРрСсТтУуӮӯФфХхҲҳЧчҶҷШшъЭэЮюЯя'
tajik_alphabet_latin = 'AaBbVvGgǦǧDdEeËëŽžZzIiĪīJjKkLlMmNnOoPpRrSsTtUuŪūFfHhḨḩČčÇçŠš’ÈèÛûÂâ'

bulgarian_alphabet_cyrillic = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЬьЮюЯя'
bulgarian_alphabet_latin = 'AaBbVvGgDdEeZHzhZzIiYyKkLlMmNnOoPpRrSsTtUuFfHhTStsCHchSHshSHTshtĂăJjYUyuYAya'

ukrainian_alphabet_cyrillic = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЮюЯяь' # not testing Ь for the apostrophe, sticking with just ь. Both will transliterate to '.
ukrainian_alphabet_latin = 'AaBbVvHhGgDdEeJejeŽžZzYyIiÏïJjKkLlMmNnOoPpRrSsTtUuFfXxCcČčŠšŠčščJujuJaja\''

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


if __name__ == '__main__':
    # Run all tests.
    unittest.main()
