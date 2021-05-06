import os
import sys

import nltk.data

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) == 2:
    print(sys.argv[1])
    with open(sys.argv[1], "r", encoding="utf-8") as inf:
        text = ' '.join(inf.readlines())
else:
    print("Usage: python sentence-tokenize.py filename")
    sys.exit()

tokenizer = nltk.data.load(
    os.path.join(SCRIPT_DIR, '../models/sentence-tokenizer-v1.pickle'))
print('\n\n'.join([' '.join(x.split()) for x in tokenizer.tokenize(text)]))
