import string
d = {}
d1={}
d2={}
def bygram(x):
    global d
    for i in range(len(x) - 1):
        k = x[i:i + 2]
        if not k in d:
            d[k] = []
        d[k].append(x)


def unique(list):
    output = []
    for x in list:
        if x not in output:
            output.append(x)
    return output



words = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. " \
        "The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', " \
        "making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text," \
        " and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, " \
        "sometimes by accident, sometimes on purpose"
words=words.replace("'", '')
print("paragraph without '' =",words)
words = words.lower().split()
for word in words:
    bygram(word)

print("d=",d)
for q in d:
    a=[]
    a=d[q]
    a.sort()
    o=unique(a)
    d1.update({q:o})

print("d1=",d1)

def bigramlist(words):
    word = words.split()
    l = []
    for i in word:
        for j in range(len(i) - 1):
            l.append(i[j:j + 2])
    return(l)
def k_gram(words):
    word = words.split()
    l = []
    for i in word:
        for j in range(len(i) - 1):
            l.append(i[j:j + 2])
    return(len(l))

print("lovem bigram =",bigramlist("lovem"))
print(k_gram("lovem"))
p=[]
for i in words:
    p.append(i)
print("p=",p)

for m in d1:
    for i  in bigramlist("lovem"):
        if i==m :
            d2.update({i:d1[m]})
        else:
            continue
print("d2",d2)

r=[]
for i in list(d2.values()):
    for j in i:
        r.append(j)
#f=list(set(r))
print("r=",r)
g=unique(r)
print("g=",g)

d3=dict()
for c in r:
    if c not in d3:
        d3[c]=1
    else:
        d3[c]=d3[c]+1
print("d3=",d3)


'''
y=0
for n in d3:
    print(k_gram(n))
    jc=((d3[n])/(k_gram(n)+k_gram("lovem")-d3[n]))
    if jc>y:
        y=jc
    else:
        continue
print("y=",y)'''
d4={}
for n in d3:
    jc = ((d3[n]) / (k_gram(n) + k_gram("lovem") - d3[n]))
    d4.update({n:jc})

print("d4=",d4)
cs=[]
for _ in d4:
    if d4[_]>0.2:
        cs.append(_)

print("correct spelling=",cs)

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

for i in cs:
    print(ld("lovem",i))











