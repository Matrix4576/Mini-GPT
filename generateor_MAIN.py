from functools import lru_cache
from tokenizer import encode, decode
from predictor import generateModel_Count, getPossibleChrSet, topPredictions


models = {}

def getModel(blocksize):
    if blocksize not in models:
        models[blocksize] = generateModel_Count(blocksize)
    return models[blocksize]

@lru_cache(maxsize=100000)
def getNextLetter(sentence):
    if not sentence:
        return ""
    model, count = getModel(len(sentence))
    possibleCHR = getPossibleChrSet(sentence, model, count)
    if possibleCHR:
        topPossibility = topPredictions(possibleCHR, lt=1)
        if topPossibility:
            return topPossibility[0][0]
    if len(sentence) <= 1:
        return ""
    return getNextLetter(sentence[1:])

def generate(sentence, limit=20):
    sentence = list(sentence)
    for i in range(limit):
        nLetter = getNextLetter(tuple(sentence))
        if not nLetter:
            break
        sentence.extend(encode(nLetter))
        if nLetter in ".!?":
            break
    return decode(sentence)


def main():
    prompt = input("Enter prompt >> ")
    encodedPrompt = tuple(encode(prompt))
    print(generate(encodedPrompt))


if __name__ == "__main__":
    main()