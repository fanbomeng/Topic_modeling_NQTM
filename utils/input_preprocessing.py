import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
total_words = set(nltk.corpus.words.words())




class NQTM_utility():
    # preprocessing, remove stop_words, none english words, inputs are list to string
    def processing(self,SC):
        New_collection=[]
        for sentence in SC:
            tmp=[]
            sentence=sentence.lower()
            word_tokens = word_tokenize(sentence)
            for W in word_tokens:
                if (W in stop_words) or (W not in total_words) or ( not W.isalpha()):
                    continue
                tmp.append(W)
            New_collection.append(' '.join(tmp))
        return New_collection
