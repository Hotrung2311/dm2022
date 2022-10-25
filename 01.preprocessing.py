import json
import math
import string


def split_doc(doc):
    x = doc.split()
    print(x)


def remove_punctuation(doc):
    return doc.translate(str.maketrans('', '', string.punctuation))


data = []
with open('archive/yelp_academic_dataset_tip.json') as f:
    for line in f:
        data.append(remove_punctuation(json.loads(line)['text']))


def idf(dw, d):
    df = dw / d
    return math.log(1 / df)


def tf(w, doc):
    result = 0
    for d in doc:
        if w == d:
            result = result + 1
    return result / len(doc)