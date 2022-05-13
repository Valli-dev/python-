def find_pairs_of_numbers(num_list,n):
    count=0
    s=set()
    print("empty set : ", s)
    print(type(s))
    for i in (range(len(num_list))):
        j=i+1
        while j < len(num_list):
            if num_list[i] + num_list[j] == n:
                if (num_list[i] and num_list[j]) not in s:
                    s.add(num_list[i])
                    s.add(num_list[j])
                    count += 1 
            j+=1 
    print(s)       
    return count
     
 
    #Remove pass and write your logic here

#num_list=[1, 2, 4, 5, 6]
num_list=[4, 5, 2, 3, 1, 0, 6, 7, 8]
#n=10
n=8
print(find_pairs_of_numbers(num_list,n))