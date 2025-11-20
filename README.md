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


## Advancing research

CyrTranslit is actively used as a reliable tool to advance research! Here's an incomplete list of publications for research projects that have relied on CyrTranslit:

### Text Normalization, Unicode Perturbations & Robustness

- Cooper, Portia, Blanco, Eduardo, and Surdeanu, Mihai. (2025). "[The Lies Characters Tell: Utilizing Large Language Models to Normalize Adversarial Unicode Perturbations](https://aclanthology.org/2025.findings-acl.969.pdf)," *Findings of the Association for Computational Linguistics: ACL 2025*.

- Cooper, Portia, Surdeanu, Mihai, and Blanco, Eduardo. (2023). "[Hiding in Plain Sight: Tweets with Hate Speech Masked by Homoglyphs](https://aclanthology.org/2023.findings-emnlp.192.pdf)," *Findings of the Association for Computational Linguistics: EMNLP 2023*.


### Low-Resource NLP & Machine Translation

- Cvetanović, Aleksa and Tadić, Predrag. (2024). "[Synthetic Dataset Creation and Fine-Tuning of Transformer Models for Question Answering in Serbian](https://arxiv.org/pdf/2404.08617)," arXiv:2404.08617.

- Lakew, Surafel Melaku. (2020). "[Multilingual Neural Machine Translation for Low Resource Languages](https://surafelml.github.io/phd-thesis/)," PhD Thesis, University of Trento.

- Filo, Denis. (2020). "[Neuronový strojový překlad pro jazykové páry s malým množstvím trénovacích dat: Low-Resource Neural Machine Translation](https://www.fit.vut.cz/study/thesis/23087/.en)," Master's Thesis, Brno University of Technology.

- Lakew, Surafel Melaku, Erofeeva, Aliia, and Federico, Marcello. (2018). "[Neural Machine Translation into Language Varieties](https://aclanthology.org/W18-6316/)," *Proceedings of the Third Conference on Machine Translation (WMT 2018)*.


### Serbian Language NLP (Topic Modeling, Sentiment, Lexicons, QA, Abuse Detection)

- Medvecki, Darija, Bašaragin, Bojana, Ljajić, Adela, and Milošević, Nikola. (2024). "[Multilingual transformer and BERTopic for short text topic modeling: The case of Serbian](https://doi.org/10.1007/978-3-031-50755-7_16)," *Lecture Notes in Networks and Systems* 872:159-169, Springer.

- Bogdanović, Miloš, Kocić, Jelena, and Stoimenov, Leonid. (2024). "[SRBerta—A Transformer Language Model for Serbian Cyrillic Legal Texts](https://doi.org/10.3390/info15020074)," *Information* 15(2):74.

- Košprdić, Miloš, Prodanović, Nikola, Ljajić, Adela, Bašaragin, Bojana, and Milošević, Nikola. (2024). "[From Zero to Hero: Harnessing Transformers for Biomedical Named Entity Recognition in Zero- and Few-shot Contexts](https://doi.org/10.1016/j.artmed.2024.102970)," *Artificial Intelligence in Medicine* 157:102970.

- Ljajić, Adela, Prodanović, Nikola, Medvecki, Darija, Bašaragin, Bojana, and Mitrović, Jelena. (2022). "[Uncovering the Reasons Behind COVID-19 Vaccine Hesitancy in Serbia: Sentiment-Based Topic Modeling](https://doi.org/10.2196/42261)," *Journal of Medical Internet Research* 24(11):e42261.

- Ljajić, Adela, Prodanović, Nikola, Medvecki, Darija, Bašaragin, Bojana, and Mitrović, Jelena. (2022). "[Topic Modeling Technique on Covid19 Tweets in Serbian](https://www.researchgate.net/publication/364302202_Topic_Modeling_Technique_on_Covid19_Tweets_in_Serbian)," *Proceedings of the 12th International Conference on Information Society and Technology (ICIST 2022)*.

- Jokic, Danka, Stanković, Ranka, Krstev, Cvetana, and Šandrih Todorović, Branislava. (2021). "[A Twitter Corpus and Lexicon for Abusive Speech Detection in Serbian](https://drops.dagstuhl.de/opus/volltexte/2021/14549/)," *Proceedings of the 3rd Conference on Language, Data and Knowledge (LDK 2021)*.

- Batanović, Vuk and Nikolic, Bosko. (2019). "[Using Language Technologies to Automate the UNDP Rapid Integrated Assessment Mechanism in Serbian](https://www.researchgate.net/publication/339615659_Using_Language_Technologies_to_Automate_the_UNDP_Rapid_Integrated_Assessment_Mechanism_in_Serbian)," *Proceedings of the Conference on Language Technologies for All (LT4All)*.

- Ljajić, Adela and Marovac, Ulfeta. (2018). "[Improving sentiment analysis for twitter data by handling negation rules in the Serbian language](http://www.doiserbia.nb.rs/Article.aspx?ID=1820-02141800013L)," *Computer Science and Information Systems* 16(1):13-33.


### NLP Applications for Society, Government, and Political Analysis

- Paula, Katrin and Scholz, Nele. (2025). "[Where do regimes rally their supporters? The geographical distribution of pro-government mobilization in Russia from February to April 2022](https://www.sciencedirect.com/science/article/pii/S096262982500068X)," *Political Geography* 116:103277.


### Engineering, Software Systems, and Backend Development

- Alyoshin, S.P., Borodina, E.A., Hafiiak, A.M., Zhabran, I.B., and Kikot, A.S. (2019). "[Developing Q-Orca site backend using various Python programming language libraries](https://reposit.nupp.edu.ua/bitstream/PoltNTU/5811/1/ME%26IT_Part%203_P%2048_March%202019_Aleshin_Borodina_Hafiiak_Zhabran_Kikot%20%28pdf.io%29.pdf)," *Modern Engineering and Innovative Technologies* 3(7-3):48-53.

- Жабран, И., Кикоть, А., Гафияк, А., Бородина, Е., and Алёшин, С. (2017). "[Developing Q-Orca site backend using various Python programming language libraries](https://www.moderntechno.de/index.php/meit/article/view/meit07-03-021)," *Modern Engineering and Innovative Technologies* 3(07-03):48-53.


### Proceedings, Collections, and Meta-Documents

- Anonymous. (2021). "[Complete Volume: Proceedings of the 3rd Conference on Language, Data and Knowledge (LDK 2021)](http://dagstuhl.sunsite.rwth-aachen.de/volltexte/2021/14535/pdf/oasics-vol093-ldk2021-complete.pdf)," *OASIcs* Vol. 93.

- Brown, J. M. M., Schmidt, Andreas, and Wierzba, Marta (Eds.). (2019). "[Of trees and birds: A Festschrift for Gisbert Fanselow](https://publishup.uni-potsdam.de/opus4-ubp/frontdoor/deliver/index/docId/42654/file/of_trees_and_birds.pdf)," Universitätsverlag Potsdam.


### Addresses, Geocoding, and NLP

- Mussylmanbay, Meiirgali. (2022). "[Addresses Standardization and Geocoding using Natural Language Processing](https://nur.nu.edu.kz/handle/123456789/6705)," Master's Thesis, Nazarbayev University.


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

### Accented Characters (Macedonian & Bulgarian)

CyrTranslit supports Cyrillic characters with grave accents used in Macedonian and Bulgarian for homograph disambiguation and stress marking. By default, accents are stripped during transliteration for cleaner output. Use the `preserve_accents` parameter to preserve them.

#### Supported Accented Characters

**Macedonian:**
- **Ѐ/ѐ** (U+0400/U+0450) - Cyrillic IE with grave
  - **Purpose:** Distinguishes homographs (e.g., нѐ "us" vs не "no", сѐ "everything" vs се "reflexive pronoun")
  - **Standard:** ISO 9:1968/1995, adopted by Macedonian Academy of Arts and Sciences (1970)

- **Ѝ/ѝ** (U+040D/U+045D) - Cyrillic I with grave
  - **Purpose:** Distinguishes homographs (e.g., ѝ "her" vs и "and")
  - **Standard:** ISO 9:1968/1995

**Bulgarian:**
- **Ѝ/ѝ** (U+040D/U+045D) - Cyrillic I with grave
  - **Purpose:** Stress marking and homograph disambiguation (e.g., ѝ "her" vs и "and")
  - **Standard:** ISO 9:1995

**Sources:**
- ISO 9:1995 - Information and documentation — Transliteration of Cyrillic characters into Latin characters
- [Wikipedia: I with grave (Cyrillic)](https://en.wikipedia.org/wiki/I_with_grave_(Cyrillic))
- [Wikipedia: Ye with grave](https://en.wikipedia.org/wiki/Ye_with_grave)

#### Usage Examples

**Default behavior (accents stripped):**

```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("ѝ је", "mk")
"i je"
>>> cyrtranslit.to_latin("нѐ сме", "mk")
"ne sme"
>>> cyrtranslit.to_cyrillic("i je", "mk")
"и је"
```

**With accents preserved:**

```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("ѝ је", "mk", preserve_accents=True)
"ì je"
>>> cyrtranslit.to_latin("нѐ сме", "mk", preserve_accents=True)
"nè sme"
>>> cyrtranslit.to_cyrillic("ì je", "mk", preserve_accents=True)
"ѝ је"
>>> cyrtranslit.to_cyrillic("nè sme", "mk", preserve_accents=True)
"нѐ сме"
```

**Command-line usage:**

```bash
# Default (accents stripped)
$ echo "ѝ је" | cyrtranslit -l mk
i je

# Preserve accents
$ echo "ѝ је" | cyrtranslit -l mk --preserve-accents
ì je
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

1. Create a new transliteration mapping file in the **[mapping/](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping/)** directory (using the language code as the filename, e.g., `xx.py`) and reference to it in the _**[TRANSLIT\_DICT](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping/__init__.py)**_ dictionary in **mapping/\_\_init\_\_.py**. If the language uses accented characters (like Macedonian and Bulgarian), create separate accented dictionaries (e.g., `XX_CYR_TO_LAT_ACCENTED_DICT`) following the pattern in **[mk.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping/mk.py)** or **[bg.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping/bg.py)**.
2. Watch out for cases where two consecutive Latin alphabet letters are meant to transliterate into a single Cyrillic script letter. These cases need to be explicitly checked for inside the **to_cyrillic()** function in **[\_\_init\_\_.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/__init__.py)**.
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