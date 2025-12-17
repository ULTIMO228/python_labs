import pytest
from src.lab03.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "text, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
        ("Simple Text", "simple text"),
    ],
)
def test_normalize(text, expected):
    assert normalize(text, True, True) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("!!! ... ,,,", []),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        ([], {}),
        (["word"], {"word": 1}),
        (["a", "a", "a"], {"a": 3}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({"banana": 1, "apple": 1}, 2, [("apple", 1), ("banana", 1)]),
        ({}, 5, []),
        ({"a": 10}, 0, []),
        ({"a": 5}, 10, [("a", 5)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected
