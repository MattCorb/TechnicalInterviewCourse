
# x = 121
# if x < 0:
#     print(False)
# xList = [i for i in str(x)]
# reversedList = []

# for i in range(0,len(str(x)) ):
#     reversedList.append(xList[(len(xList) - 1) - i])
    
# if xList == reversedList:
#     print(True)
# else:
#     print(False)

# def PalindromeTF(x):
#     if x < 0:
#         return False
#     xList = [i for i in str(x)]

#     if len(xList) == 1:
#         return True
        
#     firstHalfIndex = len(xList) // 2
#     firstHalf = xList[:firstHalfIndex]
#     secondHalf = xList[-1 * firstHalfIndex:]


    
#     if firstHalf == secondHalf[::-1]:
#         return True
#     else:
#         return False

# print(PalindromeTF(1001))


from cgi import test


def anagramCheck(x,y):
    if len(x) != len(y):
        return False

    for char in x:
        if char in y:
            y=y.replace(char,"",1)
        else:
            return False
    return True
        
strs = ["stop","pots","reed","","tops","deer","opts",""]
def anagramList(strs):
    output = []
    hold = []
    
    while len(strs) > 0:
        hold = []
        if len(strs) == 1:
            output.append(list(strs))
            strs.pop()

        
        for i in range(0,len(strs)):
            if anagramCheck(strs[0],strs[i]) == True:
                hold.append(strs[i])
        
        
        if hold != []:
            output.append(hold)
            for i in hold:
                strs.remove(i)


    return output




print(anagramList(strs))
    


tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
  ("suraj", 20), ("akhil", 25), ("ashish", 30)]
out = {}
def tup(tups):
    for t in tups:
        out[t[0]] = t[1]

# print(tup(tups))

def tupsComp(tups):
    return {t[0]:t[1] for t in tups }

# print(tupsComp(tups))
test_dict = {'B' : 4, 'Y' : 2, 'U' : 5}

def reverseDictionary(test_dict):
    output = {v:k for k,v in test_dict.items()}
    return output

# print(reverseDictionary(test_dict))

test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

def nestedKeys(test_dict):
    output = {}
    for i in test_dict:
        noeliasmom = dict(sorted(test_dict[i].items(), key=lambda dict_item: dict_item[1], reverse=False))
        output[i] = noeliasmom
    return output
# print(nestedKeys(test_dict))

test_dict = {'Manjeet' : [1, 4, 5, 6],
			'Akash' : [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}
def removeDups(test_dict):
    master = {}
    for i,j in test_dict.items():
        for x in j:
            if x in master:
                pass
            else:
                master[x] = [i,x]

