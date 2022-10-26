import json
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
    return math.log(len(docs)/ret)


def tfidf(w, doc, docs):
    return tf(w, doc) * idf(w, docs)


def split_doc(doc):
    return doc.split()


def remove_punctuation(doc):
    return doc.translate(str.maketrans('', '', string.punctuation))


data = []
with open('archive/yelp_academic_dataset_tip.json') as f:
    for line in f:
        data.append(remove_punctuation(json.loads(line)['text']))


def dw(w, doc):
    sum1 = 0
    for d in doc:
        if w == d:
            sum1 = sum1 + 1
    return sum1


real_doc = []
for dat in data:
    real_doc.append(split_doc(remove_punctuation(dat)))


for rd in real_doc:
    print(tfidf(rd, real_doc, data))
