#  use for small files only
# import os
# def merge_files(file1,file2,out_file):
#     with open(file1) as f1, open(file2) as f2:
#         sources = [f1, f2]
#         with open(out_file, "w") as dest:
#             l1 = f1.next()
#             l2 = f2.next()
#             # print "l1 is ",l1
#             # print "l2 is ",l2 
#             s1 = l1.split()
#             s2 = l2.split()
#             while(1):
#                 # print s1[0]+" "+s2[0]
#                 if(s1[0] < s2[0]):
#                     dest.write(l1)
#                     try:
#                         l1 = f1.next()
#                         s1 = l1.split()
#                     except:
#                         while(1):
#                             try:
#                                 t2 = f2.next()
#                                 dest.write(t2)
#                             except:
#                                 break
#                         break
#                 elif(s1[0] > s2[0]):
#                     dest.write(l2)
#                     try:
#                         l2 = f2.next()
#                         s2 = l2.split()
#                     except:
#                         while(1):
#                             try:
#                                 t1 = f1.next()
#                                 dest.write(t1)
#                             except:
#                                 break
#                         break
#                 else:
#                     line = s1[0] + " " + s1[1] + "|" + s2[1]
#                     dest.write(line + '\n')
#                     # print "Line is ",line
#                     try:
#                         l1 = f1.next()
#                         s1 = l1.split()
#                     except:
#                         # print "exception"
#                         while(1):
#                             try:
#                                 t2 = f2.next()
#                                 # print "wring ",t2
#                                 dest.write(t2)
#                             except:
#                                 # print "2nd"
#                                 break
#                         break
#                     try:
#                         l2 = f2.next()
#                         s2 = l2.split()
#                     except:
#                         dest.write(l1)
#                         while(1):
#                             try:
#                                 t1 = f1.next()
#                                 dest.write(t1)
#                             except:
#                                 break
#                         break

# counter = 1
# end = len(os.listdir("./Output_files")) + 1
# while counter < end-1:
#     merge_files('./Output_files/index'+str(counter)+'.txt','./Output_files/index'+str(counter+1)+'.txt','./Output_files/index'+str(end)+'.txt')
#     os.remove('./Output_files/index'+str(counter)+'.txt')
#     os.remove('./Output_files/index'+str(counter+1)+'.txt')
#     print counter,counter+1
#     counter += 2
#     end += 1