# unicode_lipsum

Tests files encoded with UTF-8, UTF-16LE and UTF-32LE.

By convention, all UTF-8 files end with `.utf8.txt` while all UTF-16LE files end with `.utf16.txt` and
all UTF-32LE end with `.utf32.txt`.

A small number of files are encoded using Latin 1 (ISO-8859-1): esperanto.latin1.txt, french.latin1.txt, german.latin1.txt, portuguese.latin1.txt
in the wikipedia_mars directory. They are not exactly equivalent to the Unicode files: e.g., it is not possible to reproduce the equivalent UTF-8 files from the Latin 1 files.

The wikipedia_mars files are derived from the Mars wikipedia article in different languages.
Wikipedia is licensed under a Creative Commons license.
 The `html2text` Python program is used to convert them to text, by stripping HTML codes.

The lipsum file come from the package [https://github.com/rusticstuff/simdutf8](simdutf8)
by Hans Kratz (licensed under both MIT and Apache).


These files are provided for research purposes.
