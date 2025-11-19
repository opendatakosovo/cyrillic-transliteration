[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7734906.svg)](https://doi.org/10.5281/zenodo.7734906)

## What is CyrTranslit?
A Python package for bi-directional transliteration of Cyrillic script to Latin script and vice versa.

By default, transliterates for the Serbian language. A language flag can be set in order to transliterate to and from Belarusian, Bulgarian, Greek, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian.

**Note:** Greek is also supported. While Greek uses its own alphabet and is not Cyrillic, it has been included due to user demand and shared transliteration needs.

**Note:** Development of v1.2.0 is ongoing. Not yet released.

## What is transliteration?
Transliteration is the conversion of a text from one script to another. For instance, a Latin alphabet transliteration of the Serbian phrase _"Мој ховеркрафт је пун јегуља"_ is _"Moj hoverkraft je pun jegulja"_.

## Citation
A citation would be much appreciated if you use CyrTranslit in a research publication:

[Georges Labrèche. (2023). CyrTranslit (v1.1.1). Zenodo. https://doi.org/10.5281/zenodo.7734906](https://doi.org/10.5281/zenodo.7734906)

BibTex entry:
```bibtex
@software{georges_labreche_2023_7734906,
  author       = {Georges Labrèche},
  title        = {CyrTranslit},
  month        = mar,
  year         = 2023,
  note         = {{A Python package for bi-directional 
                   transliteration of Cyrillic script to Latin script
                   and vice versa. Supports transliteration for
                   Bulgarian, Montenegrin, Macedonian, Mongolian,
                   Russian, Serbian, Tajik, and Ukrainian.}},
  publisher    = {Zenodo},
  version      = {v1.1.1},
  doi          = {10.5281/zenodo.7734906},
  url          = {https://doi.org/10.5281/zenodo.7734906}
}
```

## Supporting research
CyrTranslit is actively used as a reliable tool to advance research! Here's an incomplete list of publications for research projects that have relied on CyrTranslit:
- Ljajić, Adela & Prodanović, Nikola & Medvecki, Darija & Bašaragin, Bojana & Mitrović, Jelena. (2022). "[Topic Modeling Technique on Covid19 Tweets in Serbian](https://www.researchgate.net/publication/364302202_Topic_Modeling_Technique_on_Covid19_Tweets_in_Serbian)," in 12th International Conference on Information Society and Technology (ICIST), Kopaonik, Serbia.
- Mussylmanbay, Meiirgali. (2022). "[Addresses Standardization and Geocoding using Natural Language Processing](https://nur.nu.edu.kz/handle/123456789/6705)," Nazarbayev University, Kazakhstan.
- Jokic, Danka & Stanković, Ranka & Krstev, Cvetana & Šandrih Todorović, Branislava. (2021). "[A Twitter Corpus and Lexicon for Abusive Speech Detection in Serbian](https://drops.dagstuhl.de/opus/volltexte/2021/14549/)," in 3rd Conference on Language, Data and Knowledge (LDK 2021). 10.4230/OASIcs.LDK.2021.13. 
- Lakew, Surafel Melaku (2020). "[Thesis Multilingual Neural Machine Translation for Low Resource Languages](https://surafelml.github.io/phd-thesis/)," University of Trento, Italy.
- Filo, Denis. (2020). "[Neuronový strojový překlad pro jazykové páry s malým množstvím trénovacích dat: Low-Resource Neural Machine Translation](https://www.fit.vut.cz/study/thesis/23087/.en)," Brno University of Technology, Brno, Czechia.
- Batanović, Vuk & Nikolic, Bosko. (2019). "[Using Language Technologies to Automate the UNDP Rapid Integrated Assessment Mechanism in Serbian](https://www.researchgate.net/publication/339615659_Using_Language_Technologies_to_Automate_the_UNDP_Rapid_Integrated_Assessment_Mechanism_in_Serbian)," in International Conference on Language Technologies for All: Enabling Linguistic Diversity and Multilingualism Worldwide (LT4All), Paris, France.
- Brown, J. M. M. & Schmidt, Andreas & Wierzba, Marta (Eds.). (2019). "[Of trees and birds: A Festschrift for Gisbert Fanselow](https://publishup.uni-potsdam.de/opus4-ubp/frontdoor/deliver/index/docId/42654/file/of_trees_and_birds.pdf)," Universitätsverlag Potsdam, Potsdam.
- Lakew, Surafel Melaku & Erofeeva, Aliia & Federico, Marcello. (2018). "[Neural Machine Translation into Language Varieties](https://aclanthology.org/W18-6316/)," in 3rd Conference on Machine Translation: Research Papers, Brussels, Belgium.
- Ljajić, Adela & Marovac, Ulfeta. (2018). "[Improving sentiment analysis for twitter data by handling negation rules in the Serbian language](http://www.doiserbia.nb.rs/Article.aspx?ID=1820-02141800013L)," Computer Science and Information Systems. 16. 13-13. 10.2298/CSIS180122013L. 
- Жабран, И., Кикоть, А., Гафияк, А., Бородина, Е., & Алёшин, С. (2017). "[Developing Q-Orca site backend using various Python programming language libraries](https://www.moderntechno.de/index.php/meit/article/view/meit07-03-021)," Modern Engineering and Innovative Technologies, 3(07-03), 48–53.

## How do I install this?
CyrTranslit is [hosted in the Python Package Index (PyPI)](https://pypi.python.org/pypi/cyrtranslit) so it can be installed using pip:
```
python3 -m pip install cyrtranslit         # latest version
python3 -m pip install cyrtranslit==1.2.0  # specific version
python3 -m pip install cyrtranslit>=1.2.0  # minimum version
```

## What languages are supported?
CyrTranslit currently supports bi-directional transliteration of Belarusian, Bulgarian, Greek, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian.

Language codes are based on ISO 639-1 standards. For Serbian, both `sr` (ISO 639-1 language code) and `rs` (ISO 3166-1 country code) are accepted:
```python
>>> import cyrtranslit
>>> cyrtranslit.supported()
['bg', 'by', 'el', 'me', 'mk', 'mn', 'rs', 'ru', 'sr', 'tj', 'ua']
```
## How do I use this? 
CyrTranslit can be used both programatically and via command line interface.

### Programmatically
#### Belarusian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Прывітанне, свет!", "by")
"Pryvitanne, svet!"
>>> cyrtranslit.to_cyrillic("Pryvitanne, svet!", "by")
"Прывітанне, свет!"
```

#### Bulgarian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Съединението прави силата!", "bg")
"Săedinenieto pravi silata!"
>>> cyrtranslit.to_cyrillic("Săedinenieto pravi silata!", "bg")
"Съединението прави силата!"
```

#### Greek
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Το χόβερκραφτ μου είναι γεμάτο χέλια", "el")
"To choverkraft moy einai gemato chelia"
>>> cyrtranslit.to_cyrillic("To choverkraft moy einai gemato chelia", "el")
"Το χόβερκραφτ μου είναι γεμάτο χέλια"
```

#### Montenegrin
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Република", "me")
"Republika"
>>> cyrtranslit.to_cyrillic("Republika", "me")
"Република"
```

#### Macedonian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Моето летачко возило е полно со јагули", "mk")
"Moeto letačko vozilo e polno so jaguli"
>>> cyrtranslit.to_cyrillic("Moeto letačko vozilo e polno so jaguli", "mk")
"Моето летачко возило е полно со јагули"
```

#### Mongolian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө", "mn")
"Amragaa Sünjidmaagaa geseer irlee dee khö-khö-khö"
>>> cyrtranslit.to_cyrillic("Amragaa Sünjidmaagaa geseer irlee dee khö-khö-khö", "mn")
"Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө"
```

#### Russian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Моё судно на воздушной подушке полно угрей", "ru")
"Moyo sudno na vozdushnoj podushke polno ugrej"
>>> cyrtranslit.to_cyrillic("Moyo sudno na vozdushnoj podushke polno ugrej", "ru")
"Моё судно на воздушной подушке полно угрей"
```

#### Serbian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Мој ховеркрафт је пун јегуља")
"Moj hoverkraft je pun jegulja"
>>> cyrtranslit.to_cyrillic("Moj hoverkraft je pun jegulja")
"Мој ховеркрафт је пун јегуља"
```

#### Tajik
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Ман мактуб навишта истодам", "tj")
"Man maktub navišta istodam"
>>> cyrtranslit.to_cyrillic("Man maktub navišta istodam", "tj")
"Ман мактуб навишта истодам"
```

#### Ukrainian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Під лежачий камінь вода не тече", "ua")
"Pid ležačyj kamin' voda ne teče"
>>> cyrtranslit.to_cyrillic("Pid ležačyj kamin' voda ne teče", "ua")
"Під лежачий камінь вода не тече"
```

## Command Line Interface
Sample command line call to transliterate a Russian text file:
```bash
$ cyrtranslit -l RU -i tests/ru.txt -o tests/output.txt
```

Use the -c argument to accomplish the reverse, that is to input latin characters and output cyrillic.

Use the -h argument for help.

You can also omit the input and output files and use standard input/output
```bash
$ echo 'Мој ховеркрафт је пун јегуља' | cyrtranslit -l sr
Moj hoverkraft je pun jegulja
$ echo 'Moj hoverkraft je pun jegulja' | cyrtranslit -l sr
Мој ховеркрафт је пун јегуља
```

### File Encodings
By default, input files are expected to be UTF-8. For files with different encodings, use the `-e/--encoding` parameter:

```bash
$ cyrtranslit -l BG -i file.txt -e windows-1251
```

If no encoding is specified and encoding fails with the default UTF-8, then CyrTranslit automatically tries the following common Cyrillic encodings: windows-1251, iso-8859-5, koi8-r, and cp866.

Try CyrTranslit by running it directly on the Python command line interface, e.g.:
```python
>>> import sys
>>> import cyrtranslit.cyrtranslit
>>> sys.argv.extend(['-l', 'UA'])
>>> sys.argv.extend(['-i', 'tests/ua.txt'])
>>> sys.argv.extend(['-o', 'tests/output.txt'])
>>> cyrtranslit.cyrtranslit.main()
>>> exit()
```


## How can I contribute?
Include support for other Cyrillic script alphabets. Follow these steps in order to do so:

1. Create a new transliteration dictionary in the **[mapping.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping.py)** file and reference to it in the _**[TRANSLIT\_DICT](https://github.com/opendatakosovo/cyrillic-transliteration/blob/ab88bb466d12b9a9ad8d3eb6dc86d0bab871175d/cyrtranslit/mapping.py#L326-L360)**_ dictionary.
2. Watch out for cases where two consecutive Latin alphabet letters are meant to transliterate into a single Cyrillic script letter. These cases need to be explicitly checked for [inside the **to_cyrillic()** function in **\_\_init\_\_.py**](https://github.com/opendatakosovo/cyrillic-transliteration/blob/ab88bb466d12b9a9ad8d3eb6dc86d0bab871175d/cyrtranslit/__init__.py#L62-L191).
3. Add test cases inside of **[tests.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/tests.py)**.
4. Add test CLI input files in the **[tests](https://github.com/opendatakosovo/cyrillic-transliteration/tree/master/tests)** directory.
5. Update the documentation in the **[README.md](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/README.md)**.
6. List yourself as one of the contributors.

Before tagging a release version and deploying to [PyPI](https://pypi.org/):
1. Update the `version` and `download_url` properties in [setup.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/setup.py).
2. [Reserve a Zenodo DOI](https://cassgvp.github.io/github-for-collaborative-documentation/docs/tut/6-Zenodo-integration.html) for the release and update this readme's Zenodo badge and [citation instructions](https://github.com/opendatakosovo/cyrillic-transliteration#citation).

A big thank you to everyone who contributed:
- Bulgarian 🇧🇬: [@Syndamia](https://github.com/Syndamia) and [@Sparkycz](https://github.com/Sparkycz).
- Russian 🇷🇺: [@ratijas](https://github.com/ratijas) and [@rominf](https://github.com/rominf).
- Tajik 🇹🇯: [@diejani](https://github.com/diejani).
- Ukrainian 🇺🇦: [@AnonymousVoice1](https://github.com/AnonymousVoice1).
- Mongolian 🇲🇳: [@Serbipunk](https://github.com/Serbipunk).
- Command Line Interface (CLI): [@ZJaume](https://github.com/ZJaume).