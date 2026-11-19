
#str1="abbcccd"
#str1 = "abc"
str1 = "aabbccc"
str2 = ""
counter =1
endpoint = len(str1)

for c in range(1, len(str1)):
    if str1[c] != str1[c-1]:
        str2 += str1[c]

        if counter >1:
            str2 +=str1[counter]

