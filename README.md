# CyrTranslit
Bi-directional transliteration of Cyrillic script text into Roman alphabet text and vice versa.

By default, transliterates for the Serbian language. A language flag can be set in order to transliterate Macedonian, Montenegrin, and Russian.

## What is transliteration?
Transliteration is the conversion of a text from one script to another. For instance, a Roman alphabet transliteration of the Serbian phrase "Република Косово" is "Republika Kosovo".

## Usage
### Installation
CyrTransit is [hosted in the Python Package Index (PyPI)](https://pypi.python.org/pypi/cyrtranslit) so it can be installed using pip:
```
python -m pip install cyrtranslit		# latest version
python -m pip install cyrtranslit==0.4	# specific version
python -m pip install cyrtranslit>=0.4	# minimum version
```

### List supported languages
```python
>>> import cyrtranslit
>>> cyrtranslit.supported()
['me', 'sr', 'mk', 'ru']
```
### From Cyrillic script text to Roman alphabet text. 
#### Serbian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin('Мој ховеркрафт је пун јегуља')
'Moj hoverkraft je pun jegulja'
```
#### Macedonian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin('Моето летачко возило е полно со јагули', 'mk')
'Moeto letačko vozilo e polno so jaguli'
```
#### Montenegrin
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Република Косово", "me")
"Republika Kosovo"
```
#### Russian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin('Моё судно на воздушной подушке полно угрей', 'ru')
'Moyo sudno na vozdushnoj podushke polno ugrej'
```
### From Roman alphabet text to Cyrillic script text
#### Serbian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic('Moj hoverkraft je pun jegulja')
'Мој ховеркрафт је пун јегуља'
```
#### Macedonian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic('Moeto letačko vozilo e polno so jaguli', 'mk')
'Моето летачко возило е полно со јагули'
```
#### Montenegrin
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic("Republika Kosovo", "me")
"Република Косово"
```
#### Russian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic('Moyo sudno na vozdushnoj podushke polno ugrej', 'ru')
'Моё судно на воздушной подушке полно угрей'
```

### Contributing support for a new Cyrillic script
Follow these steps in order to add suport for a new Cyrillic script:

1. Create a new transliteration dictionary in the **[mapping.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping.py)** file and reference to it in the _**[TRANSLIT\_DICT](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping.py#L138-L155)**_ dictionary.
2. Watch out for cases where two consecutive Roman alphabet letters are meant to transliterate into a single Cyrillic script letter. These cases need to be explicitely checked for [inside the **to_cyrillic()** function in **\_\_init\_\_.py**](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/__init__.py#L95-L118).
3. Add test cases inside of **[tests.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/tests.py)**.

Consider contributing support for the following Cyrillic scripts:
- Bulgarian
- Ukrainian
