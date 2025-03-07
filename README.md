# Tanqeeh

![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)

**Tanqeeh** is a Python library designed to preprocess and clean Arabic text efficiently. It provides a comprehensive set of functions to normalize, remove unwanted characters, fix spacing issues, and enhance text quality for NLP applications.

## Features 🚀
- **Tatweel Removal**: Removes Arabic elongation (ـ).
- **Normalization**: Converts Persian/Urdu characters to Arabic equivalents.
- **Diacritic Correction**: Cleans excessive or incorrect diacritics.
- **Punctuation & Numbers Handling**: Removes unwanted symbols and numerals.
- **Emoji & URL Removal**: Deletes emojis and links from text.
- **Stopword Removal**: Supports filtering out common Arabic stopwords.
- **Repeated Characters & Words**: Cleans excessive repetitions.
- **Final Ya Normalization**: Converts `ى` to `ي`.
- **Latin Character Filtering**: Removes English words from Arabic text.

## Installation 📦
```bash
pip install arabic-text-cleaner
```

## Usage 📝
```python
from arabic_text_cleaner import ArabicTextCleaner

cleaner = ArabicTextCleaner()
text = "مرررررحبااااا 🌟🌟 هذاااا نص تجريبي !!!! يحتوي على ١٢٣ وأرقام ورموز @#*&"
cleaned_text = cleaner.full_clean(text)
print(cleaned_text)
```

## API Methods ⚙️
| Method | Description |
|--------|-------------|
| `remove_tatweel(text)` | Removes Arabic elongation (ـ) |
| `normalize_persian_urdu(text)` | Normalizes Persian/Urdu characters to Arabic |
| `clean_arabic_text(text)` | Removes non-Arabic letters and special symbols |
| `remove_isolated_letters(text)` | Removes single Arabic letters |
| `remove_extra_spaces(text)` | Cleans extra spaces and trims text |
| `remove_numbers(text)` | Deletes Arabic and Latin numerals |
| `remove_punctuation(text)` | Removes common punctuation marks |
| `unify_alef(text)` | Normalizes different forms of Alef to `ا` |
| `remove_stopwords(text)` | Removes predefined Arabic stopwords |
| `remove_repeated_chars(text)` | Removes excessive character repetition |
| `remove_emojis(text)` | Deletes emojis from text |
| `remove_latin_chars(text)` | Removes English characters from text |
| `unify_final_ya(text)` | Converts `ى` to `ي` |
| `remove_repeated_words(text)` | Deletes consecutive repeated words |
| `remove_short_words(text, min_length=2)` | Filters out short words |
| `replace_numbers_with_words(text)` | Converts digits to Arabic words |
| `remove_foreign_words(text)` | Removes foreign words |
| `remove_urls(text)` | Removes URLs from text |
| `full_clean(text)` | Applies all cleaning functions in sequence |

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing 🤝
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## Contact 📬
For inquiries or support, reach out via [GitHub Issues](https://github.com/your-repo/issues).
