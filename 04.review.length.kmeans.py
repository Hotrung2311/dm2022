import json
import math

data = []
with open('archive/yelp_academic_dataset_tip.json') as f:
    i = 0
    for line in f:
        if i < 100:
            data.append(len(json.loads(line)['text']))
            i += 1

input_k = 3

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


print(init_centroid(input_k, data))


def min_distance(p, arr):
    ret = 0
    tmp = []
    for a in arr:
        tmp.append(math.sqrt(pow(a - p, 2)))
    ret = tmp.index(min(tmp))
    return ret


cluster = [[] for i in range(input_k)]
for rd in data:
    for i in range(input_k):
        if min_distance(rd, centroid[-1]) == i:
            cluster[i].append(rd)
print(cluster)
