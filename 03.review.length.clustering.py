import json

data = []
with open('archive/yelp_academic_dataset_tip.json') as f:
    i = 0
    for line in f:
        if i < 100:
            data.append(json.loads(line)['text'])
            i += 1

print(data)


def cluster(p):
    ret = []
    for d in data:
        if p != d:
            if len(p) == len(d):
                ret.append(d)
                data.remove(d)
    return ret


result = []
for d in data:
    result.append(cluster(d))

print(result)