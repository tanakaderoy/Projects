def find3k(arr,k):
    #[20,303,3,4,25]
    hashTable = set(arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            difference = k - ( arr[i] + arr[j])
            if difference != arr[i] and difference != arr[j] and difference in hashTable:
                print(arr[i],arr[j],difference)
                
                return True
    return False

    
find3k([20,303,3,4,25],49)
