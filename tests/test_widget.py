from src.widget import get_date


def test_mask_account_card(data: str, result: str) -> None:
    assert mask_account_card(data) == result


def test_get_date(date_input: str) -> None:
    assert get_date(date_input) == "03.07.2019"


def test_get_date(get_dates: str) -> None:
    assert get_date(get_dates) == "03.07.2019"


def test_get_date_2(date_input: str) -> None:
    assert get_date(date_input) == "05.11.2015"
