import heapq

def getSol(N,K):
    arr = list(map(int,input().split()))
    p = arr[0]
    diff = []
    mydict = {}
    for x in arr[1:]:
        mydict[x-p] = mydict.get(x-p,[]) + [[x-p,1]]
        heapq.heappush(diff,p-x)
        p = x
    
    while K:
        #print(diff,'\n',mydict,'\n')
        x = -heapq.heappop(diff)
        if x == 1:
            return 1
        [a,b] = mydict[x].pop()
        if len(mydict[x]) == 0:
            del mydict[x]
        b += 1
        c = a//b + 1 if a%b else a//b
        mydict[c] =  mydict.get(c,[]) + [[a,b]]
        heapq.heappush(diff,-c)
        K -= 1
    
    return -heapq.heappop(diff)
        
#Read the values
T = int(input())
for x in range(T):
    [N,K] = list(map(int,input().split()))
    sol = getSol(N,K)
    print('Case #{}: {}'.format(x+1,sol))
