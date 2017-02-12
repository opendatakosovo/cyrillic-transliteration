# CyrTranslit
Bi-directional Cyrillic transliterator for Python. Transliterate Cyrillic text to Latin and vice versa.

By default, transliterates for the Serbian language but a language flag can be set in order to transliterate Macedonian and Montenegrin.

## What is transliteration?
Transliteration is the conversion of a text from one script to another. For instance, a Latin transliteration of the Serbian phrase "Република Косово", usually translated as "Republika Kosovo", is "Republika Kosovo".

## Usage
### Installation
CyrTransit is [hosted in the Python Package Index (PyPi)](https://pypi.python.org/pypi/cyrtranslit) so it can be installed using pip:
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
### From Cyrillic to Latin
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
### From Latin to Cyrillic
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
Simply create a new transliteration dictionary in the **mapper.py** file and reference to it in the _**TRANSLIT\_DICT**_ dictionary.

Consider contributing support for the following Cyrillic alphabets:
- Bulgarian
- Ukrainian
