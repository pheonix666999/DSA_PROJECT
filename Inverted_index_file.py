import json
from pathlib import Path 


inverted_index = {}
file = open(r"E:\DSA PROJECT\forward_index.json", "r")
obj = json.load(file)
print(len(obj))

temp_inverted = []
in_index = 0

for i in obj:
    for j in obj[i]:
        if j in inverted_index:
            inverted_index[j].append(i)
        else:
            temp_inverted = []
            temp_inverted.append(i)
            inverted_index[j] = temp_inverted




invertedString = json.dumps(inverted_index)
invertedFile = open("E:\DSA PROJECT\inverted_index.json", "w")
invertedFile.write(invertedString)
invertedFile.close()
