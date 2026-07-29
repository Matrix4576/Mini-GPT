from tokenizer import encode, decode
from predictor import *
from wordfreq import iter_wordlist
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def isPrefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def isWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

trie = Trie()
for word in iter_wordlist("en"):
    trie.insert(word.lower())

def ngram(sample: tuple, os: str):
    blocksize = len(sample)
    model_count = generateModel_Count(blocksize)
    model = model_count[0]
    count = model_count[1]
    try:
        possibleCHR = getPossibleChrSet(sample, model, count)
        topPossibility = topPredictions(possibleCHR, lt=5)
        letterChosen = topPossibility # gives a list of tuples ("letter", probability)
        retList = []
        for letters in letterChosen:
            os += letters[0]
            if (trie.isPrefix(os) == True):
                retList.append(letters)
                os = os[:-1]
            else:
                os = os[:-1]
        return retList
    except KeyError:
        n_sample = sample[-len(sample) + 1:]
        return ngram(n_sample, os)