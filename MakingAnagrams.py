# Making Aanagrams
# Hackerank Strings lesson.

s1="ccccdeaa"
s2="aaaaabc"
density1={} # dictionaries for character density
density2={}
for i in s1:
    if i not in density1:
        density1[i]=1
    else:
        density1[i]+=1
for j in s2:
    if j not in density2:
        density2[j]=1
    else:
        density2[j]+=1

common={} # finds the common characters in both the strings.
for i in density1:
    if i in density2:
        if (density1[i]<density2[i]):
            common[i]=density1[i]
        else:
            common[i]=density2[i]
temp=sum(common.values()) # number of common characters

deletions=len(s1)+len(s2)-2*temp # number of deletions
print(deletions)