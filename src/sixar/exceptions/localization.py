class LocalizationError(Exception):
    pass


class TranslationFileNotFoundError(LocalizationError):
    pass


class InvalidTranslationFileError(LocalizationError):
    pass
