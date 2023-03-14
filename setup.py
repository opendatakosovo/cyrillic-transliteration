# -*- coding: utf-8 -*-
from setuptools import setup

# use this to read the contents of the README.md file
from pathlib import Path

setup(
  name='cyrtranslit',
  packages=['cyrtranslit'],
  version='1.1.1',
  description='Bi-directional Cyrillic transliteration. Transliterate Cyrillic script to Latin script and vice versa. Supports transliteration for Bulgarian, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian.',
  long_description=(Path(__file__).parent / "README.md").read_text(),
  long_description_content_type='text/markdown',
  author='Georges Labrèche, Open Data Kosovo',
  author_email='georges@tanagraspace.com',
  url='https://github.com/opendatakosovo/cyrillic-transliteration',
  download_url='https://github.com/opendatakosovo/cyrillic-transliteration/archive/v1.1.1.tar.gz',
  license='MIT',
  keywords=['cyrillic', 'latin', 'transliteration', 'transliterate', 'cyrtranslit', 'bulgarian', 'montenegrin', 'macedonian', 'mongolian', 'russian', 'serbian', 'tajik', 'ukrainian'],
  classifiers=['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.1',
               'Programming Language :: Python :: 3.2',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Programming Language :: Python :: 3.8',
               'Programming Language :: Python :: 3.9',
               'Programming Language :: Python :: 3.10'],
  entry_points={
      "console_scripts": [
          "cyrtranslit=cyrtranslit.cyrtranslit:main",
      ]
  }
)