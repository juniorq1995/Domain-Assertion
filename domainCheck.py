# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def emailCompare(s1,s2):
    if(s1 == ' ' or s2 == ' '):
        return False
    if(s1 == s2):
        return True
    
    #check if domains are equal
    email1 = s1.split('@')
    email2 = s2.split('@')
    if(email1[1] == email2[1]):
        #remove characters after plus sign
        email1RemovePlus = email1[0].split('+')[0]
        email2RemovePlus = email2[0].split('+')[0]
        #remove all periods
        email1RemovePeriod = email1RemovePlus.replace('.','')
        email2RemovePeriod = email2RemovePlus.replace('.','')
        #check if final local names are equal
        if(email1RemovePeriod == email2RemovePeriod):
            return True
    return False        

def solution(L):
    # write your code in Python 3.6
    count = 0
    for x in range(0,len(L)-1):
        incremented = False
        for y in range(x+1,len(L)):
            if(emailCompare(L[x],L[y])):
                L[y] = ' '
                if(not incremented):
                    count = count + 1
                    incremented = True
    return count

    #####2 input = [1,2,1,2,1,2,1] output = 7

    # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    maxCount = 2
    count = 2
    x = 1
    treeA = A[0]
    treeB = A[x]
    while(x+1 < len(A)):
        x = x + 1
        #print(str(x) + ' ' + str(len(A)))
        # If trees are same move Amy down the line of trees
        if(treeA == treeB):
            treeB = [x]
            count = count + 1
            if(count > maxCount):
                maxCount = count
        if(treeA != treeB):
            if(A[x] != treeA and A[x] != treeB):
                count = 0
                treeA = A[x-1]
                treeB = A[x]
            else:
                count = count + 1
                if(count > maxCount):
                    maxCount = count

    return maxCount
