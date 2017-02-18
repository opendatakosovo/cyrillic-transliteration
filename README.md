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
>>> ['me', 'sr', 'mk', 'ru']
```
### From Cyrillic script text to Roman alphabet text. 
#### Serbian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Република Косово")
>>> "Republika Kosovo"
```
#### Macedonian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Република Косово", "mk")
>>> "Republika Kosovo"
```
#### Montenegrin
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Република Косово", "me")
>>> "Republika Kosovo"
```
#### Russian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("Республика Косово", "ru")
>>> "Recpublika Kosovo"
```
### From Roman alphabet text to Cyrillic script text
#### Serbian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic("Republika Kosovo")
>>> "Република Косово"
```
#### Macedonian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic("Republika Kosovo", "mk")
>>> "Република Косово"
```
#### Montenegrin
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic("Republika Kosovo", "me")
>>> "Република Косово"
```
#### Russian
```python
>>> import cyrtranslit
>>> cyrtranslit.to_cyrillic("Respublika Kosovo", "ru")
>>> "Республика Косово"
```

### Contribute a new Cyrillic alphabet
Simply create a new transliteration dictionary in the **[mapping.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping.py)** file and reference to it in the _**[TRANSLIT\_DICT](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/cyrtranslit/mapping.py#L138-L155)**_ dictionary.

When adding a new language, don't forget to also add test cases for it inside of **[tests.py](https://github.com/opendatakosovo/cyrillic-transliteration/blob/master/tests.py)**.

Consider contributing support for the following Cyrillic alphabets:
- Bulgarian
- Ukrainian
