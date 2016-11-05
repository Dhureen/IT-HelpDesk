import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import punkt
import re
import operator
import random

datafile = open("dataset.pickle", "rb")
dataset = pickle.load(datafile)
datafile.close()

allWords = []


def preprocess(sentence):
    words = nltk.word_tokenize(sentence)
    #print words[0][0]
    stpwords = set(stopwords.words('english'))
    stopremoved = [w.lower() for w in words if w.lower() not in stpwords]
    numremoved = [w for w in stopremoved if not any(c.isdigit() for c in w)]
    return numremoved

def find_features(sentence):
    sent_features = {}
    for w in word_features:
        sent_features[w] = (w in sentence)
        
    return sent_features

    
for w in dataset:
    allWords += preprocess(w[0])
    
dist = nltk.FreqDist(allWords)
word_features = list(dist.keys())[:50]

featuresets = [(find_features(w[0]), w[1]) for w in dataset]
random.shuffle(featuresets)

training_set = featuresets[:len(featuresets)/2]
testing_set = featuresets[len(featuresets)/2:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

class_f = open('naivebayes.pickle','wb')
pickle.dump(classifier,class_f)
class_f.close()
#for e, f in dist.iteritems():
 #   print str(e) + " : " + str(f)
#for e in values:
 #       print str(e)

#sorted_x = sorted(dist.iteritems(), key=operator.itemgetter(1))
#print sorted_x

