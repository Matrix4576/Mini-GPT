from tokenizer import encode, decode, DATA
from predictor import *
sample = (53, 62, 57, 45)
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

def ngram(sample):
    blocksize = len(sample)
    model_count = generateModel_Count(blocksize)
    model = model_count[0]
    count = model_count[1]
    try:
        possibleCHR = getPossibleChrSet(sample, model, count)
        topPossibility = topPredictions(possibleCHR)
        letterChosen = topPossibility[:4]
        print(letterChosen)
    except Exception as e:
        sample = sample[-len(sample) + 1:]
        print(decode(sample))
        ngram(sample)
print(decode(sample))
ngram(sample)