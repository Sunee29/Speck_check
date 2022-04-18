
import string
import pickle
from collections import Counter
d1 = {}
d2 = {}
d3 = {}
d4 = {}
#kval = int(input("Enter k value : "))
ms = input("Enter a word : ")
ms = ms.translate(str.maketrans('', '', string.punctuation)).lower()
kval=2
#Sample dictionary


def kgram(x,n):
    global d
    for i in range(len(x)-(n-1)):
        k=x[i:i+n]
        if not k in d:
            d[k] = []
        d[k].append(x)

def unique(list):
    output = []
    for x in list:
        if x not in output:
            output.append(x)
    return output

#converting string into kgrams list
with open("example1pickle","rb") as f:
    d1=pickle.load(f)




def kgramlist(words,n):
    word = words.split()
    l = []
    for i in word:
        for j in range(len(i) - (n-1)):
            l.append(i[j:j + n])
    return(l)

def len_kgram(words):
    word = words.split()
    l = []
    for i in word:
        for j in range(len(i) - 1):
            l.append(i[j:j + 2])
    return(len(l))

#getting related posting lists of misplet word
for i  in kgramlist(ms,kval):
        d2.update({i:d1.get(i,[])})


#converting dictonary of related posting lists into list
r=[]
for i in list(d2.values()):
    for j in i:
        r.append(j)

#counting the number of repeated word

for c in r:
    if c not in d3:
        d3[c]=1
    else:
        d3[c]=d3[c]+1

#Calculating jacab coefficient

for n in d3:
    jc = ((d3[n]) / (len_kgram(n) + len_kgram(ms) - d3[n]))
    d4.update({n:jc})

#printing corrected spelling having JC > threshold

v = d4.values()
mi = min(v)
ma = max(v)
for i in d4:
    d4[i] = ((d4[i]-mi)/(ma-mi))

d5={}
for _ in d4:
    if d4[_]>0.7:
        d5[_]=d4[_]
    else:
        continue

def ld(a,b):
   #print(a,b)
    if len(a)==0:
        return len(b)
    elif len(b)==0:
        return len(a)
    elif a[0] == b[0]:
        return ld(a[1:], b[1:])
    else:
        return 1 + min(ld(a[1:], b), ld(a,b[1:]), ld(a[1:], b[1:]))
d6={}
for i in d5:
    d6[i]=ld(ms,i)

d7_values = sorted(d6.values()) # Sort the values
d7 = {}

for i in d7_values:
    for k in d6.keys():
        if d6[k] == i:
            d7[k] = d6[k]
            break
count=0
cs=[]
for _ in d7:
    if count<3:
        cs.append(_)
        count=count+1


print("correct spelling=",cs)












