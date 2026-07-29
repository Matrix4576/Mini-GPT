from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UKW = "<UKW>"

@lru_cache(maxsize=None)
def _load_corpus():
    with open(BASE_DIR / "sample-texts" / "mergedB1.txt", "r", encoding="utf-8") as f:
        text1 = f.read()
    with open(BASE_DIR / "sample-texts" / "mergedB2.txt", "r", encoding="utf-8") as f:
        text2 = f.read()
    return text1 + "\n" + text2

@lru_cache(maxsize=None)
def _build_vocab():
    corpus = _load_corpus()
    chars = sorted(set(corpus))
    if UKW not in chars:
        chars.append(UKW)
    stoi = {ch: i for i, ch in enumerate(chars)}
    itos = {i: ch for i, ch in enumerate(chars)}
    return stoi, itos

@lru_cache(maxsize=None)
def get_data():
    return tuple(encode(_load_corpus()))

def encode(text):
    stoi, _ = _build_vocab()
    return [stoi.get(ch, stoi[UKW]) for ch in text]

def decode(tokens):
    _, itos = _build_vocab()
    return "".join(itos.get(token, UKW) for token in tokens)
