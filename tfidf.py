from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import os

stemmer = SnowballStemmer("english")


def makeFreq(somefile):
    
    f = open(somefile,"r",encoding="utf-8")
    content = f.read()
    f.close()
    
    wordList = []
    
    content = word_tokenize(content)
    for word in content:
        if(word.isalnum() is True):
            wordList.append(stemmer.stem(word))

    wordSet = set(wordList)
    
    wordDict = dict.fromkeys(wordSet,0)

    for word in wordList:
        wordDict[word]+=1
    
    return wordDict


import glob

ulaz1 = input()
ulaz2 = input()


files = glob.glob(ulaz1+'**/*.txt',recursive = True)

# lista 82 dok
fl = []

putanja = ulaz2
tfFreqDict = makeFreq(putanja)
fl.insert(0,tfFreqDict)

for file in files:
    fl.append(makeFreq(file))


# tf and idf algs (but slightly modified) from this site https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76

def computeTF(wordDict):
    tfDict = {}
    bagOfWordsCount = sum(tfFreqDict.values())
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict


def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = {}#dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] = idfDict.get(word,0)+1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict


def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

idfs = computeIDF(fl)

tfidf = computeTFIDF(tfFreqDict,idfs)


br = 0
line1=""
for k,v in sorted(tfidf.items(),key = lambda x:(-x[1],x[0])):
    #print(k,v)
    br+=1
    line1+=k
    if(br==10):
        break
    line1+=", "

#task 2
# treba mi tfidf, moram da podelim fajl na recenice i da racunam recenice po tfidfu

def sentenceRelevanceScore(sentence): #skor za jednu recenicu
    words = []
    score=0
    for word in word_tokenize(sentence):
        if(word.isalnum() is True):
            words.append(stemmer.stem(word))
    br=1
    # za svaku recenicu pravi novi dict gde se rec slika u tfidf values
    # sortiraj recnik
    # nadjes top 10 reci
    # saberes te reci po values
    tempDict = {}
    
    for word in words:
        if word in tfidf:
            tempDict[word] = tfidf[word] #tempDict je recnik reci iz words sa tfidf value
    
    for k,v in sorted(tempDict.items(),key = lambda x: -x[1]):
        
        for word in words:
            if(k==word):
                score+=v
                br+=1
        if(br==10):
            break
    return score
            
            
    #for k,v in tfidf.items():
        #br+=1
        #for word in words:
            #if(k==word):
                #score+=v
        #if(br==10):
            #break
    #return score 

def documentRelevanceScore(document): #ispisuje 5 recenica prima content
    sentences = sent_tokenize(document)
    
    index = 0
    sentenceDict = {}
    for sentence in sentences:
        sentenceDict[sentence]=[sentenceRelevanceScore(sentence),index]
        index+=1
    
        
    sentenceDictSortedByScore = dict(sorted(sentenceDict.items(),key=lambda x: -x[1][0]))
    
    sentenceDictSortedByIndex = {}
    
    i=0
    
    for k,v in sentenceDictSortedByScore.items():
        i+=1
        sentenceDictSortedByIndex[k]=v
        if(i==5):
            break
        
    templine = ""
    br1 = 0
    for k,v in sorted(sentenceDictSortedByIndex.items(),key=lambda x: x[1][1]):
        br1+=1
        templine+=k
        if(br1==5):
            break
        templine+=" "

    return templine

g = open(putanja,"r",encoding="utf-8")
doc = g.read()
g.close()

line2 = documentRelevanceScore(doc)

import sys
sys.stdout.reconfigure(encoding='utf-8')

print(line1)
print(line2)
