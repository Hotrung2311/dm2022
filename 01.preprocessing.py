import json
import math
import string

import math
import string


def tf(w, doc):
    ret = 0
    for d in doc:
        if w == d:
            ret += 1
    return ret / len(doc)


def idf(w, docs):
    ret = 0
    for doc in docs:
        for d in doc:
            if w == d:
                ret += 1
                break
    return math.log(len(docs) / ret)


def tfidf(w, doc, docs):
    return tf(w, doc) * idf(w, docs)


def split_doc(doc):
    return doc.split()


def remove_punctuation(doc):
    return doc.translate(str.maketrans('', '', string.punctuation))


data = []
with open('archive/yelp_academic_dataset_tip.json') as f:
    i = 0
    for line in f:
        if i < 5:
            data.append(split_doc(remove_punctuation(json.loads(line)['text'])))
            i += 1

d_data = data[0]
result = tfidf("Avengers", d_data, data)
print(result)