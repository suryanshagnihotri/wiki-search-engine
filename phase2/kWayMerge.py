# suryansh agnihotri

# prerequisite : increase number of file that can be openened in linux for user
import heapq,os
from collections import defaultdict

offsetSize =0
countFinalFile = 0
def kWayMerge(folderPath, fileCount):
	global offsetSize
	try:
		os.remove(folderPath+ "finalIndex.txt")
	except:
		pass
	listOfWords={}
	indexFile={}
	topOfFile={}
	flag=[0]*fileCount
	data=list()
	heap=[]
	countFinalFile=0
	offsetSize = 0
	for i in xrange(fileCount):
		fileName = folderPath+'/index'+str(i+1)+'.txt'
		indexFile[i]= open(fileName, 'rb')
		flag[i]=1
		topOfFile[i]=indexFile[i].readline().strip()
		listOfWords[i] = topOfFile[i].split(' ')
		if listOfWords[i][0] not in heap:
			heapq.heappush(heap, listOfWords[i][0])        

	count=0        
	lastKey = ""
	addstr = ""
	f = open('finalIndex.txt','ab')
	while any(flag)==1:
	    temp = heapq.heappop(heap)
	    count+=1
	    for i in xrange(fileCount):
	        if flag[i]:
	            if listOfWords[i][0]==temp:

	                if lastKey == temp:
	                	addstr += '|' + listOfWords[i][1]
	                else:
	                	if len(addstr) > 0:
	                		f.write(addstr + '\n')
	                	addstr = ""
	                	addstr = temp + ' ' + listOfWords[i][1]	
	                	lastKey = temp
	     
	                topOfFile[i]=indexFile[i].readline().strip()   
	                if topOfFile[i]=='':
	                        flag[i]=0
	                        indexFile[i].close()
	                        os.remove(folderPath+'/index'+str(i+1)+'.txt')
	                else:
	                    listOfWords[i] = topOfFile[i].split(' ')
	                    if listOfWords[i][0] not in heap:
	                        heapq.heappush(heap, listOfWords[i][0])
   	if len(addstr) > 0:
   		f.write(addstr)
   	f.close()


n = next(os.walk(os.getcwd()+ '/Output_files'))[2]

kWayMerge('./Output_files', len(n))