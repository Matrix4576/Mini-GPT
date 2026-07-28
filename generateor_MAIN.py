from tokenizer import *
from ngramPredictor import *
from predictor import *

PROMPT = input("Enter prompt >> ")
encodedPrompt = encode(PROMPT)
print(encodedPrompt)