test = [ "kiwi", "melon", "apple", "lemon" ]

def checkAnagram(str1,str2):
    return sorted(str1) == sorted(str2)
    
def getList(arr):
    res = []
    for word in arr:
        for i in arr:
            if i!=word and word not in res:
                if checkAnagram(word,i):
                    res.append(word)
    return sorted(res)

print(getList(test))
