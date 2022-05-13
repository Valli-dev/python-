def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func==None:
        s= sum(list_of_num)
        return s
    
    elif filter_func== even:
        even_list =even(list_of_num)
        print(even_list)
        x=sum(even_list)
        return x
    elif filter_func== odd:
        odd_list =odd(list_of_num)
        print(odd_list)
        x=sum(odd_list)
        return x
        
        
    #pass #Remove pass and write the logic here

def even(data):
    even_list=[]
    for i in data:
        if i%2 == 0:
            even_list.append(i)
    return even_list
    #pass #Remove pass and write the logic here

def odd(data):
    odd_list=[]
    for i in data:
        if (i%2) != 0:
            odd_list.append(i)
    return odd_list
    #pass #Remove pass and write the logic here

#sample_data = range(1,11)
sample_data= [10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(sum_of_numbers(sample_data,even))