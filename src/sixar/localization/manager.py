import json
import pathlib

from sixar.exceptions.localization import (
    InvalidTranslationFileError,
    TranslationFileNotFoundError,
)


class LocalizationManager:
    def __init__(self, language):
        language_list = ["fa", "en"]
        if language not in language_list:
            raise ValueError("Invalid language")
        path = pathlib.Path(__file__).parent
        path_language = path / "translations" / f"{language}.json"
        try:
            with open(path_language, "r", encoding="utf-8") as file:
                self.messages = json.load(file)
        except FileNotFoundError as exp:
            raise TranslationFileNotFoundError("Translation file not found") from exp
        except json.JSONDecodeError as exp:
            raise InvalidTranslationFileError(
                "Translation file contains invalid JSON"
            ) from exp
        self.language = language

    def get_message(self, key):
        return self.messages[key]
