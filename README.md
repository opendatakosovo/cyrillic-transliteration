# serbian-transliterator
Transliterate Serbian text from cyrillic to latin and vise-versa.

## What is transliteration?
Transliteration is the conversion of a text from one script to another. For instance, a Latin transliteration of the Serbian phrase "Република Косово", usually translated as "Republika Kosovo", is "Republika Kosovo".

## Usage
### From cyrillic to latin
```python
>>> import srtranslitr
>>> srtranslitr.to_latin("Република Косово")
>>> "Republika Kosovo"
```
### From latin to cyrillic
```python
>>> import srtranslitr
>>> srtranslitr.to_cyrillic("Republika Kosovo")
>>> "Република Косово"
```
## Future features
- Bosnian transliteration.
- Macedonian transliteration.
- Montenegrin transliteration.



