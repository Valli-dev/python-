

def factorial(number):
    sum=1
    while number>0:
        sum=sum*number
        number -=1
    #print(sum)
    return sum

    if  number == 0:
        return 1
    
    
#factorial(8)

def find_strong_numbers(num_list):
    f=[]
    strong_number =0
    i=0
    for num in num_list:
        while num > 0:
            last_digit=num%10
            x=factorial(last_digit)
            strong_number=strong_number + x
            num=num//10
        if strong_number == num_list[i] and strong_number != 0 :
                f.append(strong_number)
                   
        i+=1
        strong_number=0
    return f
        

            
    #remove pass and write your logic to find and return the list of strong numbers from the given list


num_list=[145,375,100,2,10, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)


 