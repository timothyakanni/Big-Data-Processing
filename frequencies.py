# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:52:47 2017

@author: Feranmi
"""
from nltk.text import TextCollection
import math

# Here documents is the list of all text documents
documents = []
count = 1
with open("wikitexts.txt") as infile:
    for line in infile:            
        for res in line.split("\n"):   
            if len(res) != 0:
                documents.append(res)            
#                with open('d'+ str(count) + '.txt', 'w') as output:
#                    output.write(res)
#            
#                count += 1

# This is the combination of all texts documents           
allDocuments = TextCollection(documents)      
#print(len(allDocuments))

# This will contains words with length greater than or equal to 4
# and consist of unique words
word_len = []      
for doc in documents:   
    for word in doc.split():
        if len(word) >= 4 and word not in word_len:
            word_len.append(word)
            
# here the list is sorted
word_len = sorted(word_len)

# This function is for tf(w, D) that is the numbers of times the term w 
# occur in all Documents
def tf_func(word, DocsList, allDocs):      
    #for word in wordLen:
    word_count_overall = 0    
    for d in DocsList:                        
        word_count_per_doc = d.count(word)                     
        word_count_overall += word_count_per_doc     
               
    tf = word_count_overall / len(allDocs)
    return tf
          
# This is for idf(w, D) that is the inverse document frequence.Here df(w, D)
# is very useful and df(w, D) is the number of documents in the collection of
# Documents that contain at least one occurence of term w
# df(w, D)
def idf_func(word, DocsList):
    
    n = len(DocsList)
    count = 0
    for doc in DocsList:                   
        # This is used for df
        word_count = doc.count(word)
        if word_count > 0:
            count += 1
                    
    df = count/n                   
    idf = math.log(n/(1+df))  
    
    return idf
    
# This is tf(w, di) which is the number of times term w occur in one document di
# and this is calculated for each document and used in combination with
# idf_funct to get tf_idf(w, di)
def tf_docfunc(word, doc):     
   
   word_count_per_doc = doc.count(word)                    
   tf_doc = word_count_per_doc / len(doc)
                
   tf_ = tf_doc
   return tf_ 
    
# Writing part
# tf(w, D) for plotting graph
tf_wD_list = []
with open('frequencies.txt', 'w') as output:
    for word in word_len:
        output.write(word)
        output.write(' ')
        second = tf_func(word, documents, allDocuments)
        tf_wD_list.append(second)
        output.write(str(second))
        output.write(' ')
        param0 = idf_func(word, documents)
        for doc in documents:
            param1 = tf_docfunc(word, doc)
            tf_idf = param0 * param1
            output.write(str(tf_idf))
            output.write(' ')
        output.write('\n')
        
# Plotting section
tf_wD_list.sort(reverse = True)
import matplotlib.pyplot as plt
plt.plot(tf_wD_list)

plt.savefig("frequencies.png")
plt.show()


 

        


            







