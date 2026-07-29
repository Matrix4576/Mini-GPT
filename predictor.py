from collections import defaultdict
from tokenizer import decode, get_data
def generateModel_Count(blockSize):
    data = get_data()
    model = defaultdict(list)
    countMap = defaultdict(int)
    for i in range(len(data) - blockSize):
        context = tuple(data[i: i + blockSize])
        y = data[i + blockSize]
        countMap[context] += 1
        model[context].append(y)
    return dict(model), dict(countMap)
def getPossibleChrSet(sample_context, model, countMap):
    V = 50
    possibleChrSet = model[sample_context]
    countYX = {}
    for letters in possibleChrSet:
        char = decode([letters])
        countYX[char] = countYX.get(char, 0) + 1
    return {
        letters: (counts + 1) / (countMap[sample_context] + V)
        for letters, counts in countYX.items()
    }
def topPredictions(probabilityMap, lt):
    sorted_probs = sorted(
        probabilityMap.items(),
        key=lambda x: x[1],
        reverse=True
    )
    return sorted_probs[:lt]