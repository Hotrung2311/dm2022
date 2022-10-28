import json
import math

input_k = 3

data = []
with open('archive/yelp_academic_dataset_tip.json') as f:
    i = 0
    for line in f:
        if i < 100:
            data.append(len(json.loads(line)['text']))
            i += 1

centroid = []


def init_centroid(k, arr):
    ret = []
    for i in range(k - 2):
        ret.append((max(arr) - min(arr)) / (k - 1) * (i + 1))
    ret.append(min(arr))
    ret.append(max(arr))
    ret.sort()
    centroid.append(ret)
    return ret


