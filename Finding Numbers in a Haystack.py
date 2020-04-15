import re
f=open('regex_sum_443844.txt','r')
n=[]
for line in f:
    line=line.rstrip()
    num=re.findall('[0-9]+',line)
    for i in range(len(num)):
        if num[i]!=' ':
            n.append(int(num[i]))
print(sum(n))

