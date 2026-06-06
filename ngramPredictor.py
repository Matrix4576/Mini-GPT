from tokenizer import encode, decode, DATA
from predictor import *
sample = (53, 62, 57, 45)
def ngram(sample):
    blocksize = len(sample)
    model_count = generateModel_Count(blocksize)
    model = model_count[0]
    count = model_count[1]
    try:
        possibleCHR = getPossibleChrSet(sample, model, count)
        topPossibility = topPredictions(possibleCHR)
        letterChosen = topPossibility[0]
        print(letterChosen)
    except KeyError:
        sample = sample[len(sample):]