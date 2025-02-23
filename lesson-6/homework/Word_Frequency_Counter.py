try:
    with open("sample.txt","r") as file:
        a=file.read()
        file.seek(0)
except Exception:
    with open("sample.txt","w") as file:
        text=input()
        file.write()
        file.seek(0)
    with open("sample.txt","r") as file:
        a=file.read()
a=a.lower()
l=[]
m=0
punc=[".",",","?","!",":",";"]
for i in a:
    if i in punc:
        a=a.replace(i,"")
words = a.split()
for word in words:
    l.append(word)
new_l=[]
for j in l:
    count=l.count(j)
    p=(count,j)
    new_l.append(p)
ms="Total words: "+str(len(new_l))+"\n"
    
new_l=set(new_l)
new_l=list(new_l)
new_l=sorted(new_l)
new_l=new_l[::-1]


ms=ms+"Top 5 most common words:\n"
if len(new_l)>=5:
    for i in range(5):
        ms+=new_l[i][1]+" - "+str(new_l[i][0])+" times\n"
else:
    for i in range(len(new_l)):
        ms+=new_l[i][1]+" - "+str(new_l[i][0])+" times\n"
with open("word_count_report.txt","w") as new_file:
    ss="Word Count Report\n"
    new_file.write(ss)
with open("word_count_report.txt","a") as new_file:
    new_file.write(ms)



