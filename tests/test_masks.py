import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number() -> None:
    """
    Тестирование mask_card_number. Проверка, что номер карты правильно маскируется
    """

    assert get_mask_card_number("1234567891011121") == "1234 56** **** 1121"
    assert get_mask_card_number("12345") == "Некорректный номер карты"


@pytest.fixture
def masks_card() -> str:
    return "3646473263542725"


def test_masks_card(masks_card: str) -> None:
    assert get_mask_card_number(masks_card) == "3646 47 ** 2725"


def test_masks_account() -> None:
    assert get_mask_account("85749856745845201234") == "**1234"


def test_mask_account_number() -> None:
    """
    Тестирование mask_account_number. Проверка, что номер счета правильно маскируется.
    """

    assert get_mask_account("76666108430178874305") == "**4305"

    assert get_mask_account("234") == "Некорректный номер счета"


("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 ** 6361")