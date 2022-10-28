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
    tmp = []
    for a in arr:
        tmp.append(math.sqrt(pow(a - p, 2)))
    ret = tmp.index(min(tmp))
    return ret


def update_centroid(arr):
    ret = []
    for j in arr:
        ret.append(sum(j)/len(j))
    return ret


cluster = [[] for ii in range(input_k)]
temp = [[] for ii in range(input_k)]
flag = 0
while flag == 0:
    for rd in data:
        for i in range(input_k):
            if min_distance(rd, centroid[-1]) == i:
                cluster[i].append(rd)
    print(cluster)
    if temp != cluster:
        temp = cluster
    else:
        flag = 1

print(update_centroid(cluster))
