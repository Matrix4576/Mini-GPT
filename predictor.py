from tokenizer import decode, DATA
def generateModel_Count(blockSize):
    model = {}
    countMap = {}
    for i in range(len(DATA) - blockSize):
        x = DATA[i: i + blockSize]
        y = DATA[i + blockSize]
        context = tuple(x)
        if context not in countMap:
            countMap[context] = 0
            countMap[context] += 1
        else:
            countMap[context] += 1
        if context not in model:
            model[context] = []
            model[context].append(y)
        else:
            model[context].append(y)
    return model, countMap
def getPossibleChrSet(sample_context, model, countMap):
    V = 50
    possibleChrSet = model[sample_context]
    countYX = {}
    for letters in possibleChrSet:
        if decode([letters]) not in countYX:
            countYX[decode([letters])] = 0
            countYX[decode([letters])] += 1
        else:
            countYX[decode([letters])] += 1
    probabilityMap = {}
    for letters, counts in countYX.items():
        probabilityMap[letters] = (counts + 1)/(countMap[sample_context] + V)
    return probabilityMap
def topPredictions(probabilityMap):
    sorted_probs = sorted(
        probabilityMap.items(),
        key=lambda x: x[1],
        reverse=True
    )
    return sorted_probs[:3]