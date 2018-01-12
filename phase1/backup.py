import xml.sax
import sys
import re
from nltk.corpus import stopwords
from nltk import PorterStemmer
import gc
import string
# output=open("output.txt","w")
class wiki_handler(xml.sax.ContentHandler):

    def __init__(self):
        # my index dictionry
        self.index={}
        # stopwords dictionary
        self.stopwords={}
        words=stopwords.words('english')
        for word in words:
            self.stopwords[word]=1
        self.stopwords['0']=1
        self.stopwords['/ref']=1
        self.punc_list = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\""]

        self.replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
        self.email_regex=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        self.url_regex=re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        self.alphabets=re.compile(r"^[a-z]*$")
        self.digits=re.compile(r"^[0-9]*$")
        self.regex = re.compile(r'\d+\.?\d+|[a-zA-Z0-9]+')
        self.keyitems=re.compile(r'[a-zA-Z]+')
        self.numerics={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,0:1}
        self.specialchars={'!':1,'@':1,'#':1,'$':1,'%':1,'^':1,'&':1,'*':1,'(':1,')':1,'_':1,'+':1,'=':1}
        # list of content
        self.body_content=""
        self.title_content=""
        self.infobox_content=""
        # self.externallinks = [] 
        # self.references = [] 
        self.categories =""

        # variables
        self.current_tag=""
        self.docid=""
        self.doc_counter=0
        self.map_docid={}
        self.is_doc=0
        self.is_infobox=0
        self.is_ext=0
        self.is_ref=0



    # clear the content
    def clear(self):
        self.body_content=""
        self.title_content=""
        self.infobox_content=""
        # self.externallinks = [] 
        # self.references = [] 
        self.categories = ""
   
    def unset(self):
        self.is_infobox = 0
        self.is_ref=0
        self.is_ext=0


    def startElement(self, name, attrs):
        self.current_tag=name
        if(name=="page"):
            # clean lists
            self.clear()
        if(name=="title"):
            self.is_doc=1
        self.unset()
    
    def post_list(self,content,index):

        # print content
        # clean_item = re.sub(r"[^\P{P}-]+", " ", content)
        # clean_item=content.strip(string.punctuation)
        # item_list=clean_item.split()
        good_content=[]
        # item_list=regex.findall(item)

        # print type(content)
        content=content.encode('ascii', 'ignore')
        content.translate(None, string.punctuation)
        # content = content.translate(self.replace_punctuation)
        item_list=content.split()
        # good_content=[w for w in item_list if w not in self.stopwords and len(w)>=2]
        for word in item_list:
            if word in self.stopwords:
                continue
            else:
                good_content.append(word)
        for word in good_content:
            if not word.isalpha() and not word.isdigit():
                continue
            # if word in self.numerics:
            #     continue
            # if word in self.specialchars:
            #     continue
            if word.isalpha():
                word = PorterStemmer().stem_word(word)
            if word in self.stopwords:
                continue
            if word in self.index:
                if self.docid in self.index[word]:
                    self.index[word][self.docid][index]+=1
                else:
                    self.index[word][self.docid]=[0,0,0,0,0,0]
                    self.index[word][self.docid][index] = 1
            else:
                self.index[word] = {}
                # print "inserting ",word
                self.index[word][self.docid]=[0,0,0,0,0,0]
                self.index[word][self.docid][index] = 1

































        
        # keyitems=re.compile(r'[a-zA-Z]+')
        # for item in content:
        #     # urls=self.url_regex.findall(item)
        #     # item_list=item.split()
        #     # item_list1=re.split(r'[^a-zA-z0-9]+',item)
        #     # item_list=keyitems.findall(item)
        #     # item_list=self.regex.findall(item)
            
        #     clean_item = re.sub(r"[,.;@#?!&$]+\ *", " ", item)
        #     item_list=clean_item.split()
        #     good_content=[]
        #     # item_list=regex.findall(item)
        #     good_content=[w for w in item_list if w not in self.stopwords]
        #     for word in item_list:
        #         if word in self.stopwords:
        #             continue
        #         else:
        #             good_content.append(word)
        #         # if word.isalpha() or (word.isdigit() and len(word)==4 and word>='1800' and word<='3000'):
        #         #     good_content.append(word)
        #         # if self.url_regex.match(word):
        #         #     continue
        #         # if self.email_regex.match(word):
        #         #     continue
        #         # if (len(word)>=2 and word not in self.stopwords.keys() and ( self.alphabets.match(word) or ( self.digits.match(word) and word>='1500' and word<='3000' ) ) ):
        #         #     good_content.append(word)
        #         # if len(word)>0 and word not in self.stopwords.keys() and ( (word.isdigit() and (len(word)==4  and word>='1900' and word<='3000')) or word.isalpha()):
        #         #     good_content.append(word)
        #     # print good_content
        #     for word in good_content:
        #         if word in self.numerics:
        #             continue
        #         if word in self.specialchars:
        #             continue
        #         if word.isalpha():
        #             word = PorterStemmer().stem_word(word)
        #         # if '=' in word:
        #         #     pos=word.find('=')
        #         #     word=word[pos+1:]
        #         # if word in self.stopwords:
        #         #     continue
        #         # try:
        #         #     self.stopwords[word]
        #         #     continue
        #         # except:
        #         #     pass
        #         # word=word.encode('utf8').lower()
        #         # print "word = ",word

        #         if word in self.index:
        #             if self.docid in self.index[word]:
        #                 self.index[word][self.docid][index]+=1
        #             else:
        #                 self.index[word][self.docid]=[0,0,0,0,0,0]
        #                 self.index[word][self.docid][index] = 1
        #         else:
        #             self.index[word] = {}
        #             # print "inserting ",word
        #             self.index[word][self.docid]=[0,0,0,0,0,0]
        #             self.index[word][self.docid][index] = 1
                # try:
                #     self.index[word][self.docid]
                #     self.index[word][self.docid][index] += 1
                # except:
                #     try:
                #         # self.index[word]
                #         # print "inserting ",word
                #         self.index[word][self.docid]=[0,0,0,0,0,0]
                #         self.index[word][self.docid][index] = 1
                #         # print self.index[word]
                #     except:
                #         self.index[word] = {}
                #         # print "inserting ",word
                #         self.index[word][self.docid]=[0,0,0,0,0,0]
                #         self.index[word][self.docid][index] = 1
                        # print self.index[word]

    def endElement(self, name):
        self.current_tag=""
        if (name=="page"):
            self.post_list(self.title_content,0)
            self.post_list(self.body_content,1)
            self.post_list(self.infobox_content,2)
            self.post_list(self.categories,3)
            # self.post_list(self.externallinks,4)
            # self.post_list(self.references,5)
            # s = ""
            # for word in sorted(self.index):
            #     s = word + " "
            #     print "wordd is ",word
            #     print self.index[word]
            #     for docid in self.index[word]:
            #         print "doc id ",docid
            #         # s += str(format(int(self.map_docid[docid]),'02x'))
            #         s+=str(self.map_docid[docid])
            #         s += self.getter("T",self.index[word][docid][0])
            #         s += self.getter("X",self.index[word][docid][1])
            #         s += self.getter("i",self.index[word][docid][2])
            #         # s += self.getter("C",self.dic[word][docID][3])
            #         # s += self.getter("L",self.dic[word][docID][4])
            #         # s += self.getter("R",self.dic[word][docID][5])
            #         s += "|"
            #     s = s[:-1]
            #     print "writing ",s
            #     output.write(s+"\n")
            # self.index.clear()


    # def check_reftag(self,content):
    #     if(self.is_ref== 0):
    #         if(content == "==References=="):
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         if("{{" in content  or "==" in content or "[[" in content):
    #             return 0
    #         else:
    #             return 1
    # def exttag(self,content):
    #     if(self.is_ext == 0):
    #         if("==External links==" in content ):
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         if(content[0] != "*"):
    #             return 0
    #         else:
    #             return 1
    def check_infotag(self,content):
        if(self.is_infobox == 0):
            if("{{Infobox" in content):
                return 1
            else:
                return 0
        else:
            if(content == "}}"):
                return 0
            else:
                return 1
    def characters(self, content):
        # gc.disable()
        if(len(content) <=1):
            return
        cat_tag = 0
        if(self.current_tag == "title"):
            self.title_content+=content.lower()
            # self.title_content.append(content.lower())
        elif (self.current_tag == "id" and self.is_doc == 1):
            self.doc_counter += 1
            self.docid = content
            # self.docid=self.docid.encode('utf8')
            self.map_docid[self.docid] = self.doc_counter
            self.is_doc = 0
        elif(self.current_tag == "text"):
            # self.is_ref = self.check_reftag(content)
            # self.is_ext = self.exttag(content)
            cat_tag=0
            if("[[Category:" in content):
                cat_tag = content[11:-2]
            if(self.is_infobox == 0):
                if("{{Infobox" in content):
                    self.is_infobox = 1
                else:
                    self.is_infobox = 0
            else:
                if(content == "}}"):
                    self.is_infobox = 0
                else:
                    self.is_infobox =  1
            # self.is_infobox = self.check_infotag(content)
            if(self.is_infobox == 1):
                if("{{Infobox" in content):
                    self.infobox_content+=content[9:].lower()
                    # self.infobox_content.append(content[9:].lower())
                else:
                    self.infobox_content+=content[9:].lower()
                    # self.infobox_content.append(content.lower())
            # elif(self.is_ext == 1):
            #     if("==External links==" not in content):
            #         self.externallinks.append(content.lower())
            elif(cat_tag != 0):
                self.categories+=cat_tag.lower()
                # self.categories.append(cat_tag.lower())
            # elif(self.is_ref == 1):
            #     self.references.append(content.lower())
            else:
                self.body_content+=content.lower()
                # self.body_content.append(content.lower())
        # gc.enable()
    def getter(self,field,cnt):
        if(int(cnt) == 0):
            return ""
        else:
            return field + str(cnt)
    def write_output(self):
        output=open("output.txt","w")
        s = ""
        # print self.index
        for word in sorted(self.index):
            s = word + " "
            for docid in self.index[word]:
                # print docid,word
                # s += str(format(int(self.map_docid[docid]),'02x'))
                s+=str(self.map_docid[docid])
                # print self.index[word]
                # print self.index[word][docid]
                # print self.index[word][docid][0]
                count=[self.index[word][docid][0],self.index[word][docid][1],self.index[word][docid][2],self.index[word][docid][3],self.index[word][docid][4],self.index[word][docid][5]]
                s += self.getter("T",count[0])
                s += self.getter("B",count[1])
                s += self.getter("I",count[2])
                s += self.getter("C",count[3])
                # s += self.getter("E",count[4])
                # s += self.getter("R",count[5])
                s += "|"
            s = s[:-1]
            output.write(s.encode('utf8')+"\n")

def start_indexer(file_name,handler):
    file_obj = open(file_name,"r")
    xml.sax.parse(file_obj, handler)
    handler.write_output()

if __name__=="__main__":
    # print sys.argv[1]
    # import sys
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    gc.disable()
    file_name=sys.argv[1]
    handler=wiki_handler()
    start_indexer(file_name,handler)
    gc.enable()
    # handler.write_output()
    # print "index = "
    # print handler.index
    