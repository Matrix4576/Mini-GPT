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


def add_one_smoothing(countYX, sample_context, countMap, V):
    denominator = countMap.get(sample_context, 0) + V
    return {char: (count + 1) / denominator for char, count in countYX.items()}


def getPossibleChrSet(sample_context, model, countMap, smoothing_fn=add_one_smoothing):
    V = len(get_data())  # Vocabulary size / Smoothening Const
    possibleChrSet = model.get(sample_context)
    if possibleChrSet is None:
        return {}
    countYX = {}
    for token in possibleChrSet:
        char = decode([token])
        countYX[char] = countYX.get(char, 0) + 1
    return smoothing_fn(countYX, sample_context, countMap, V)

def topPredictions(probabilityMap, lt):
    sorted_probs = sorted(
        probabilityMap.items(),
        key=lambda x: x[1],
        reverse=True
    )
    return sorted_probs[:lt]