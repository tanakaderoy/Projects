# Hello World program in Python
    

def flip(text):
    size = len(text)
    best = size
    for i in range(size+1):
        count = 0
        for j in range(0,i):
            if text[j] == "y":
                count += 1
        for j in range(i,size):
            if text[j] == "x":
                count += 1
        if count < best:
            best = count
    return best
            
        
def flip2(text):
    size = len(text)
    xList = [0] * (size+1)
    yList = [0] * (size+1)
    
    for i in range(size):
        if text[i] == "y":
            yList[i+1] = yList[i] + 1
        else:
            yList[i+1] = yList[i]
    for i in range(size-1,-1,-1):
        if text[i] == "x":
            xList[i] = xList[i + 1] + 1
        else:
            xList[i] = xList[i +1]
    
    best = len(xList)
    
    for i in range(len(xList)):
        sumPair = xList[i] + yList[i]
        if sumPair < best:
            best = sumPair
    return (best)
print("Printing flip 1 \n")
print(flip("xyxxxyxyy"))
print(flip("xxxxxxxx"))
print(flip("yyyyyyyy"))
print(flip("xyxyxyxy"))
print(flip(""))
print("Printing flip2 \n")
print(flip2("xyxxxyxyy"))
print(flip2("xxxxxxxx"))
print(flip2("yyyyyyyy"))
print(flip2("xyxyxyxy"))
print(flip2(""))
    
