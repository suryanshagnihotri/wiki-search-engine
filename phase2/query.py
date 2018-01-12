# suryansh agnihotri
import math
import operator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
from nltk import PorterStemmer
from nltk.corpus import wordnet as wn
import time

from Stemmer import Stemmer

stemmer =Stemmer("english")
words = stopwords.words('english')
stopwords_dict = {}
for i in words:
    stopwords_dict[i] = 1

index_file_path="./Index/Split/"
main_index_file="./Index/Split/main"
main_title_file="./Title/Split/main"
title_file_path="./Title/Split/"
map_fields = { "T":0 , "B":1 , "I":2 , "C":3 , "E":4 , "R":5,}
reverse_fields = { "0":"T" , "1":"X" , "2":"i" , "3":"C" , "4":"E" , "5":"R"}
map = { "t":"T" , "b":"B" , "i":"I" , "c":"C" , "e":"E" , "r":"R"}
map_weight = { "0":300.0 , "1":300.0 , "2":100.0 , "3":75.0 , "4":50.0 , "5":60.0}
docid_title={}
N=17600000

def find_posting_list(query_word):
    f=open(main_index_file,"r");
    # list of lines in main index file
    lines=f.readlines()
    second_level_file=""
    for item in lines:
        item=item[:-1]
        item_list=item.split(" ")
        word=item_list[0]
        if word>query_word:
            break;
        second_level_file=item_list[1]
    if second_level_file=="":
        return ""
    else:
        third_level_file=""
        second_level_file=index_file_path+"0"+second_level_file
        with open(second_level_file) as second_level_file_ptr:
            for line in second_level_file_ptr:
                line=line[:-1]
                word_list=line.split(" ")
                if word_list[0]>query_word:
                    break
                third_level_file=word_list[1]
        if third_level_file=="":
            return ""
        else:
            third_level_file=  index_file_path+third_level_file
            with open(third_level_file,"r") as third_level_file_ptr:
                ok=0
                posting_list=""
                for line in third_level_file_ptr:
                    line=line[:-1]
                    word_list=line.split(" ")
                    if word_list[0]==query_word:
                        ok=1
                        posting_list=word_list[1]
                    elif word_list[0]>query_word:
                        break
            if ok==0:
                return ""
            else:
                return posting_list




def find_title(docid):
    docid=int(docid)
    f=open(main_title_file,"r");
    lines=f.readlines()
    second_level_file=""
    for item in lines:
        item=item[:-1]
        item_list=item.split(" ")
        word_id=int(item_list[0])
        if word_id>docid:
            break;
        second_level_file=item_list[1]
    if second_level_file=="":
        return ""
    else:
        third_level_file=""
        second_level_file=title_file_path+"0"+second_level_file
        with open(second_level_file) as second_level_file_ptr:
            for line in second_level_file_ptr:
                line=line[:-1]
                word_list=line.split(" ")
                word_id=int(word_list[0])
                if word_id>docid:
                    break
                third_level_file=word_list[1]
        if third_level_file=="":
            return ""
        else:
            third_level_file=  title_file_path+third_level_file
            with open(third_level_file,"r") as third_level_file_ptr:
                ok=0
                title=""
                for line in third_level_file_ptr:
                    line=line[:-1]
                    word_list=line.split(" ")
                    word_id=int(word_list[0])
                    if word_id==docid:
                        ok=1
                        title=' '.join(word_list[1:])
                    elif word_id>docid:
                        break
            if ok==0:
                return ""
            else:
                return title
def get_docid(x):
    res=""
    for c in x:
        if c>='A' and c<='Z':
            break
        res+=c
    return res

def get_frequency(x,c):
    ind=-1
    for i in range(len(x)):
        if x[i]==c:
            ind=i
            break
    # print "ind ",ind
    if ind==-1:
        return 0
    else:
        i=ind+1
        res="0"
        while i<len(x):
            if x[i]>='A' and x[i]<='Z':
                break
            res+=(x[i])
            i+=1
    return int(res)


def RankDocuments(query_words):
    ranked_docs = {}
    seen_docid={}
    first_word=1
    for i in range(len(query_words)):
        postlist = find_posting_list(query_words[i])
        if(postlist != ""):
            postlist = postlist.split("|")
            term_freq=len(postlist)
            postlist[-1] = postlist[-1][:-1]
            # optimisation possible here
            for x in postlist:
                doc_id = get_docid(x)
                if first_word:
                    seen_docid[doc_id]=1
                else:
                    if doc_id not in seen_docid:
                        continue
                weight=0
                freq=get_frequency(x,'T')
                tf=freq
                for field in categories[i]:
                    if field in map:
                        freq = get_frequency(x,map[field])
                    if field in map:
                        tf+=freq*map_weight[str(map_fields[map[field]])]
                weight+=tf*(math.log(N/(term_freq*1.0)))
                try:
                    ranked_docs[doc_id] += weight
                except:
                    ranked_docs[doc_id] = weight
        first_word=0
    try:
        return ranked_docs
    except:
        return -1

# handle all types of query including field queries
def process_query(q):
    temp = q.split(" ")
    # print temp
    words = []
    categories = []
    for w in temp:
        t = w.split(":")
        if(len(t) == 1):
            word = t[0].lower()
            try:
                stopwords_dict[word]
            except:
                s=stemmer.stemWord(word)
                # s = PorterStemmer().stem_word(word)
                words.append(s)
                categories.append("NA")
        else:
            word = t[1]
            cat = t[0]
            try:
                stopwords_dict[word]
            except:
                s=stemmer.stemWord(word)
                words.append(s)
                categories.append(cat)
    return [words,categories]

while True:
    print "Enter query"
    query = raw_input()
    tt=time.time()
    processed_query=process_query(query)
    query_words=processed_query[0]
    categories=processed_query[1]
    r=RankDocuments(query_words)
    if r!=-1:
        sorted_r = sorted(r.items(), key=operator.itemgetter(1),reverse = True)
        if(len(sorted_r) == 0):
            print "No documents found"
        else:
            count = 0
            for i in range(len(sorted_r)):
                count += 1
                if(count > 10):
                    break
                docid = sorted_r[i][0]
                title=find_title(docid)
                if title=="":
                    count-=1
                if title!="":
                    print docid,title
    else:
        print "No documents found"
    ttt=time.time()
    print ttt-tt