# Hackerrank: Anagram question
s="abab"

s1=s[:len(s)//2]
s2=s[len(s)//2:]
print(s1,s2)
if len(s1)!=len(s2):
    print(0)
else:
    temp=0
    density1={}
    for i in s1:
        if i not in density1:
            density1[i]=1
        else:
            density1[i]+=1
    density2={}
    for j in s2:
        if j not in density2:
            density2[j]=1
        else:
            density2[j]+=1
    print(density1,density2)

    for i in density1:

        if i in density2:

            delta=density1[i]-density2[i]

            if delta<=0: # both are equal lengths
                continue
            elif delta>0: # s1 is having more number of one characters than s2
                temp=temp+delta
        else:

            temp=temp+density1[i]
    print(temp)




