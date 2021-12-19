import json 
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from pathlib import Path
import glob
import os


doc_index = 0
word_index = 0
temp_forward = []
sentences = []
content = []
articals = []
pure_articals = []
tokened = []
without_stops = []
without_punctuation = []
without_repetition_space = []
without_repetition = []
temp_forward = []
forward_index = {}
inverted_index = {}
document_id = {}
condition = 0
lexicon = {}
files = Path(r"E:\DSA PROJECT\nela-elections-2020\newsdata")
all_files_paths = [f for f in files.glob('*.json')]
snow_stemmer = SnowballStemmer(language='english')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

for path in all_files_paths:
    file = open(path, "r")
    obj = json.load(file)
    for i in obj:
        sentences.append(i) 
        for i in sentences:
            content.append(i['content'])
            document_id[i['id']] = doc_index
        for i in content:
            tokened = nltk.word_tokenize(i)
            for j in tokened:
                articals.append(j)
        for i in articals:
            strencode = str(i).encode("ascii", "ignore")
            strencode = strencode.decode()
            pure_articals.append(strencode)
        for i in range(len(pure_articals)):
            pure_articals[i] = snow_stemmer.stem(pure_articals[i])
        #print(pure_articals)
        without_stops.clear()
        for i in pure_articals:
            if i.lower() not in stop_words:
                without_stops.append(i)
        #print(without_stops)
        #print(len(pure_articals))
        for i in without_stops:
            if (i.isalnum()):
                without_punctuation.append(i)
        without_repetition = list(dict.fromkeys(without_punctuation))
        for i in without_repetition:
            if i not in lexicon:
                lexicon[i] = word_index
                word_index += 1
        #print(without_repetition)
        for i in without_repetition:
            temp = lexicon[i]
            temp_forward.append(temp)
        #print(temp_forward)
        forward_index[doc_index] = temp_forward
        doc_index += 1
        temp_forward = []
        without_repetition = []
        without_punctuation = []
        sentences = []
        content = []
        articals = []
        pure_articals = []

forString = json.dumps(forward_index)
forward_file = open(r"forward_index.json", "w")
forward_file.write(forString)
forward_file.close()   

lexiString = json.dumps(lexicon)
lexiFile = open("lexicon.json", "w")
lexiFile.write(lexiString)
lexiFile.close()

docString = json.dumps(document_id)
docFile = open("doc_id.json", "w")
docFile.write(docString)
docFile.close()


# for i in lexicon:
#     for j in forward_index:
#         for k in range(len(forward_index[j])):
#             if (lexicon[i] == forward_index[j][k]):
#                 temp_inverted.append(j)
#     inverted_index[in_index] = temp_inverted
#     in_index += 1
#     temp_inverted = []














 
        






















#     file = open(path, "r",)
#     obj = json.load(file)
#     for i in obj:
#         sentences.append(i)



























# p = "E:\DSA PROJECT\nela-elections-2020\newsdata\369news.json"
# file = open(r"p", "r")
# obj = json.load(file)

# filtered_list = []
# new_words = []
# final_list = []

# for i in obj:


# temp = nltk.word_tokenize(temp)
	
# print("Orignal:               ", temp)

# for word in temp:
#     if word.lower() not in stop_words:
#         filtered_list.append(word)

# for i in range(len(filtered_list)):
#     if(filtered_list[i].isalnum()):
#         new_words.append(filtered_list[i])

# print("Without StopWords:     ", filtered_list)
# print("Without Punctuations : ", new_words)


# for word in new_words:
#     for check in new_words:
#         if (word.lower() == check.lower()):
#             condition = condition + 1
#     if (condition == 1):
#         final_list.append(word)
#     if (condition != 1):
#         final_list.append(word)
#         for check_in in range(len(new_words)):
#             if (new_words[check_in].lower() == word.lower()):
#                 new_words[check_in] = " "
#     condition = 0

# final_list_final = []

# for i in final_list:
#     if (i.lower() != " "):
#         final_list_final.append(i)



# print("Removed Repetition:    ", final_list_final)

# for i in range(len(final_list)):
#     final_list[i] = snow_stemmer.stem(final_list[i])

# print("Stemmed:               ", final_list)
# key = 0













