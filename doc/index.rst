.. CyrTranslit documentation master file, created by
   sphinx-quickstart on Sat Feb 18 05:20:15 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CyrTranslit 1.0
===============
:Source Code: https://github.com/opendatakosovo/cyrillic-transliteration
:PyPI: https://pypi.python.org/pypi/cyrtranslit
:License: MIT
:Author: Georges Labrèche, Open Data Kosovo
:Version: 1.0

====================
What is CyrTranslit?
====================
A Python package for bi-directional transliteration of Cyrillic script to Latin script and vice versa.

By default, transliterates for the Serbian language. A language flag can be set in order to transliterate to and from Bulgarian, Montenegrin, Macedonian, Russian, Serbian, Tajik, and Ukrainian.

========================
What is transliteration?
========================

Transliteration is the conversion of a text from one script to another. For instance, a Latin alphabet transliteration of the Serbian phrase "Мој ховеркрафт је пун јегуља" is "Moj hoverkraft je pun jegulja".

======================
How do I install this?
======================
CyrTranslit is hosted in the Python Package Index (PyPI_) so it can be installed in the Terminal using pip:

Latest version:
    ``$ python -m pip install cyrtranslit``

Specific version: 
    ``$ python -m pip install cyrtranslit==1.0``

Minimum version:
    ``$ python -m pip install cyrtranslit>=1.0``


=============================
What languages are supported?
=============================
CyrTranslit currently supports bi-directional transliteration of Bulgarian, Montenegrin, Macedonian, Russian, Serbian, Tajik, and Ukrainian:

>>> import cyrtranslit
>>> cyrtranslit.supported()
['bg', 'me', 'mk', 'ru', 'sr', 'tj', 'ua']

==================
How do I use this?
==================
*********
Bulgarian
*********
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Съединението прави силата!", "bg")
"Săedinenieto pravi silata!"
>>> cyrtranslit.to_cyrillic("Săedinenieto pravi silata!", "bg")
"Съединението прави силата!"

***********
Montenegrin
***********
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Република", "me")
"Republika Kosovo"
>>> cyrtranslit.to_cyrillic("Republika", "me")
"Република Косово"

**********
Macedonian
**********
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Моето летачко возило е полно со јагули", "mk")
"Moeto letačko vozilo e polno so jaguli"
>>> cyrtranslit.to_cyrillic("Moeto letačko vozilo e polno so jaguli", "mk")
"Моето летачко возило е полно со јагули"

*******
Russian
*******
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Моё судно на воздушной подушке полно угрей", "ru")
"Moyo sudno na vozdushnoj podushke polno ugrej"
>>> cyrtranslit.to_cyrillic("Moyo sudno na vozdushnoj podushke polno ugrej", "ru")
"Моё судно на воздушной подушке полно угрей"

*******
Serbian
*******
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Мој ховеркрафт је пун јегуља")
"Moj hoverkraft je pun jegulja"
>>> cyrtranslit.to_cyrillic("Moj hoverkraft je pun jegulja")
"Мој ховеркрафт је пун јегуља"

*****
Tajik
*****
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Ман мактуб навишта истодам", "tj")
"Man maktub navišta istodam"
>>> cyrtranslit.to_cyrillic("Man maktub navišta istodam", "tj")
"Ман мактуб навишта истодам"

*********
Ukrainian
*********
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Під лежачий камінь вода не тече", "ua")
"Pid ležačyj kamin' voda ne teče"
>>> cyrtranslit.to_cyrillic("Pid ležačyj kamin' voda ne teče", "ua")
"Під лежачий камінь вода не тече"

*********
Mongolian
*********
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө", "mn")
"Amragaa Sünjidmaagaa geseer irlee dee khö-khö-khö"
>>> cyrtranslit.to_cyrillic("Amragaa Sünjidmaagaa geseer irlee dee khö-khö-khö", "mn")
"Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө"

=====================
How can I contribute?
=====================

You can include support for other Cyrillic script alphabets. Follow these steps in order to do so:

1. Create a new transliteration dictionary in the mapping.py_ file and reference to it in the TRANSLIT\_DICT dictionary_.
2. Watch out for cases where two consecutive Roman alphabet letters are meant to transliterate into a single Cyrillic script letter. These cases need to be explicitely checked for inside the to\_cyrillic() function_ in \_\_init\_\_.py.
3. Add test cases inside of tests.py_.
4. Update the documentation in the README.md_ and in the doc directory_. 


.. _PyPI: https://pypi.python.org/pypi/cyrtranslit
.. _mapping.py: https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping.py
.. _dictionary: https://github.com/opendatakosovo/cyrillic-transliteration/blob/4eabac0526f7cfb0fa39d6b9481ee3b5189dafe2/cyrtranslit/mapping.py#L261-L290
.. _function: https://github.com/opendatakosovo/cyrillic-transliteration/blob/4eabac0526f7cfb0fa39d6b9481ee3b5189dafe2/cyrtranslit/__init__.py#L62-L156
.. _tests.py: https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/tests.py
.. _README.md: https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/README.md
.. _directory: https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/doc
