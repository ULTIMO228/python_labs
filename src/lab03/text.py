import re

def normalize(text: str, casefold: bool, yo2e: bool):
    text = ' '.join(text.split())
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё","е").replace('Ё', 'Е')
    return text

def tokenize(text: str):
    text=text.replace(',', ' ').replace('.',' ')
    return re.sub(r'[^a-zA-Zа-яА-Я0-9-\s]', '', text).split()

def count_freq(tokens: list[str]):
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def top_n(freq: dict[str, int], n: int):
    s = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return s[:n]

if __name__ == "__main__":
    print(normalize("ПрИвЕт\nМИр\t", True,False))
    print(normalize("ёжик, Ёлка", False,True))
    print(normalize("Hello\r\nWorld", False,False))
    print(normalize("  двойные   пробелы  ", False,False))
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))
    print(count_freq(["a","b","a","c","b","a"]))
    print(top_n(count_freq(["a","b","a","c","b","a"]),2))
    print((count_freq(["bb","aa","bb","aa","cc"])))
    print(top_n(count_freq(["bb","aa","bb","aa","cc"]),2))