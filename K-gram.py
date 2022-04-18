import string
from collections import Counter
d = {}
d1 = {}
d2 = {}
d3 = {}
d4 = {}
kval = int(input("Enter k value : "))
ms = input("Enter a word : ")
ms = ms.translate(str.maketrans('', '', string.punctuation)).lower()
#Sample dictionary
words = "I wanted to write a love paragraph for my best friend, but it’s going to sound more like a gratitude diary. Spending time with you is " \
        "undoubtedly the greatest thing ever. It’s the most enjoyable thing I have ever done in my life. When I’m with you baby, I have the time " \
        "of my life and time flies by. The little things you say to me always put a smile on my face. But when we are apart, I really miss you and " \
        "couldn’t wait to see you again. I am truly blessed. I love you to infinity and beyond.I wanted to take the time to tell you just how much" \
        " you mean to me. You’ve become a rock in my life, something solid and secure I can lean on. Knowing you’re by my side makes me so eternally" \
        " grateful, that I can hardly put it into words. I had felt happiness before, but nothing prepared me for the happiness I feel when I’m. with" \
        " you. We understand each other. We listen to each other. We inspire each other to become stronger with each passing day. You are the best " \
        "boyfriend of all. You are so amazing, and you do everything to make sure I’m taken care of. I love you.There will be times when we will no " \
        "longer see each other as often as we used to; there will be a moment of ups and downs in our journey on the path of friendship; there will " \
        "be a time when the stormy weather of life will seem to break the bond between us and there will be a moment when we would want to call it " \
        "quits between us. I want you to know that I will not give up on us, at least not without a fight, because you’re the best thing that ever " \
        "happened to me in life and I won’t trade you for the finest pearl in the world. Come rain or the sunshine, you will always be my best friend " \
        "forever. I love you, bestie."
#Removing special characters and converting into lower case
words = words.translate(str.maketrans('', '', string.punctuation))
words = words.lower().split()

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
for word in words:
    kgram(word,kval)

#converting list in to Dictionary and postinglists
for q in d:
    a=[]
    a=d[q]
    a.sort()
    o=unique(a)
    d1.update({q:o})


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
for m in d1:
    for i  in kgramlist(ms,kval):
        if i==m :
            d2.update({i:d1[m]})
        else:
            continue

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

#Calculating jaccard coefficient

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
    if d4[_]>0.2:  #thresold value
        d5[_]=d4[_]
    else:
        continue

def ld(a,b):
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


print("dict=",d)
print("sorting=",d1)
print("related posting lists=",d2)
print("j.c= ",d4)
print("normalize="d5,)
print("edit distance = ",d6)













