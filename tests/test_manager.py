import pytest

from sixar.localization import manager


def test_manager_fa():
    lang = manager.LocalizationManager("fa")
    assert lang.language == "fa"


def test_manager_en():
    lang = manager.LocalizationManager("en")
    assert lang.language == "en"


def test_manager_valueerror():
    with pytest.raises(ValueError):
        manager.LocalizationManager(123)


def test_manager_keyerror():
    lan = manager.LocalizationManager("fa")
    with pytest.raises(KeyError):
        lan.get_message("persian")


def test_translation_file_not_found(tmp_path, monkeypatch):
    monkeypatch.setattr(manager, "__file__", str(tmp_path / "manager.py"))
    with pytest.raises(manager.TranslationFileNotFoundError):
        manager.LocalizationManager("fa")


def test_invalid_json(tmp_path, monkeypatch):
    monkeypatch.setattr(manager, "__file__", str(tmp_path / "manager.py"))
    file_path = tmp_path / "translations" / "fa.json"
    Invalid_json = "بان شما با موفقیت انتخاب شد."
    path = file_path.parent
    path.mkdir()
    file_path.write_text(Invalid_json, encoding="utf-8")
    with pytest.raises(manager.InvalidTranslationFileError):
        manager.LocalizationManager("fa")
