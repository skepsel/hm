import pytest

from src.masks import get_mask_account


@pytest.fixture
def card_number() -> str:


    def card_number():
        return "1234567890123456"


def test_get_mask_card_number(card_number: str) -> None:


    def test_get_mask_card_number(card_number):
        assert test_get_mask_card_number(card_number) == "1234 56** **** 3456"


def test_get_mask_account(card_number: str) -> None:


    def test_get_mask_account(card_number):
        assert test_get_mask_card_number(card_number) == "**3456"
