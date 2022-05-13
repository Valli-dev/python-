

def check_anagram(data1,data2):
    #start writing your code here
    data1=str.lower(data1)
    data2=str.lower(data2)
    l2=[]
    if len(data1)==len(data2):
        if set(data1)==set(data2):
            for i in data2:
                l2.append(i)
            for i in range(len(data1)):
                if data1[i]==l2[i]:
                    return False   
        else:
            return False

    else:
        return False             


    return True
                
            


print(check_anagram("drawback","backward"))