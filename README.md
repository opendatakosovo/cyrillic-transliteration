[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4643047.svg)](https://doi.org/10.5281/zenodo.4643047)

## What is CyrTranslit?
A Python package for bi-directional transliteration of Cyrillic script to Latin script and vice versa.

By default, transliterates for the Serbian language. A language flag can be set in order to transliterate to and from Bulgarian, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian.

## What is transliteration?
Transliteration is the conversion of a text from one script to another. For instance, a Latin alphabet transliteration of the Serbian phrase "Мој ховеркрафт је пун јегуља" is "Moj hoverkraft je pun jegulja".

## How do I install this?
CyrTranslit is [hosted in the Python Package Index (PyPI)](https://pypi.python.org/pypi/cyrtranslit) so it can be installed using pip:
```
python -m pip install cyrtranslit       # latest version
python -m pip install cyrtranslit==1.0  # specific version
python -m pip install cyrtranslit>=1.0  # minimum version
```

## What languages are supported?
CyrTranslit currently supports bi-directional transliteration of Bulgarian, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian:
```python
>>> import cyrtranslit
>>> cyrtranslit.supported()
['bg', 'me', 'mk', 'mn', 'ru', 'sr', 'tj', 'ua']
```
## How do I use this? 

### Bulgarian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Съединението прави силата!", "bg")
"Săedinenieto pravi silata!"
>>> cyrtranslit.to_cyrillic("Săedinenieto pravi silata!", "bg")
"Съединението прави силата!"
```

### Montenegrin
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Република", "me")
"Republika"
>>> cyrtranslit.to_cyrillic("Republika", "me")
"Република"
```

### Macedonian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Моето летачко возило е полно со јагули", "mk")
"Moeto letačko vozilo e polno so jaguli"
>>> cyrtranslit.to_cyrillic("Moeto letačko vozilo e polno so jaguli", "mk")
"Моето летачко возило е полно со јагули"
```
### Mongolian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө", "mn")
"Amragaa Sünjidmaagaa geseer irlee dee khö-khö-khö"
>>> cyrtranslit.to_cyrillic("Amragaa Sünjidmaagaa geseer irlee dee khö-khö-khö", "mn")
"Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө"
```

### Russian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Моё судно на воздушной подушке полно угрей", "ru")
"Moyo sudno na vozdushnoj podushke polno ugrej"
>>> cyrtranslit.to_cyrillic("Moyo sudno na vozdushnoj podushke polno ugrej", "ru")
"Моё судно на воздушной подушке полно угрей"
```

### Serbian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Мој ховеркрафт је пун јегуља")
"Moj hoverkraft je pun jegulja"
>>> cyrtranslit.to_cyrillic("Moj hoverkraft je pun jegulja")
"Мој ховеркрафт је пун јегуља"
```

### Tajik
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Ман мактуб навишта истодам", "tj")
"Man maktub navišta istodam"
>>> cyrtranslit.to_cyrillic("Man maktub navišta istodam", "tj")
"Ман мактуб навишта истодам"
```

### Ukrainian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Під лежачий камінь вода не тече", "ua")
"Pid ležačyj kamin' voda ne teče"
>>> cyrtranslit.to_cyrillic("Pid ležačyj kamin' voda ne teče", "ua")
"Під лежачий камінь вода не тече"
```

## How can I contribute?
You can include support for other Cyrillic script alphabets. Follow these steps in order to do so:

1. Create a new transliteration dictionary in the **[mapping.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping.py)** file and reference to it in the _**[TRANSLIT\_DICT](https://github.com/opendatakosovo/cyrillic-transliteration/blob/4eabac0526f7cfb0fa39d6b9481ee3b5189dafe2/cyrtranslit/mapping.py#L261-L290)**_ dictionary.
2. Watch out for cases where two consecutive Latin alphabet letters are meant to transliterate into a single Cyrillic script letter. These cases need to be explicitely checked for [inside the **to_cyrillic()** function in **\_\_init\_\_.py**](https://github.com/opendatakosovo/cyrillic-transliteration/blob/4eabac0526f7cfb0fa39d6b9481ee3b5189dafe2/cyrtranslit/__init__.py#L62-L156).
3. Add test cases inside of **[tests.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/tests.py)**.
4. Update the documentation in the **[README.md](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/README.md)** and in the **[doc directory](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/doc)**. 

A big thank you to everyone who contributed:
- [@Syndamia](https://github.com/Syndamia) / Bulgarian 🇧🇬 
- [@ratijas](https://github.com/ratijas) / Russian 🇷🇺 
- [@diejani](https://github.com/diejani) / Tajik 🇹🇯 
- [@AnonymousVoice1](https://github.com/AnonymousVoice1) / Ukrainian 🇺🇦 
- [@Serbipunk](https://github.com/Serbipunk) / Mongolian 🇲🇳

## Citation
A citation would be much appreciated if you use CyrTranslit in a research publication:

[Georges Labrèche. (2021, March 29). CyrTranslit (Version v1.0). Zenodo. http://doi.org/10.5281/zenodo.4643047](https://doi.org/10.5281/zenodo.4643047)

BibTex entry:
```
@software{georges_labreche_2021_4643047,
  author       = {Georges Labrèche},
  title        = {CyrTranslit},
  month        = mar,
  year         = 2021,
  note         = {{A Python package for bi-directional 
                   transliteration of Cyrillic script to Latin script
                   and vice versa. Supports Bulgarian, Montenegrin,
                   Macedonian, Mongolian, Russian, Serbian, Tajik, and
                   Ukrainian.}},
  publisher    = {Zenodo},
  version      = {v1.0},
  doi          = {10.5281/zenodo.4643047},
  url          = {https://doi.org/10.5281/zenodo.4643047}
}
```
