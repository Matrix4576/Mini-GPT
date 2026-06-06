with open("sample-texts//mergedB1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("sample-texts//mergedB2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()
corpus = text1 + "\n" + text2
chars = sorted(set(corpus))
UKW = "<UKW>"
if UKW not in chars: 
    chars.append(UKW)
vocab_size = len(chars)
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

def encode(text):
    tokens = []
    for ch in text:
        if ch in stoi:
            tokens.append(stoi[ch])
        else:
            tokens.append(stoi[UKW])
    return tokens

def decode(tokens):
    s = ""
    for token in tokens:
        if token in itos:
            s += itos[token]
        else:
            s += UKW
    return s

DATA = encode(corpus)