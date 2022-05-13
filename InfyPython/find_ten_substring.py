def find_ten_substring(num_str):
    result_list=[]
    
    for i in range(len(num_str)):
        sum=0 
        num=""

        for j in range(i, len(num_str)):
            sum=sum+int(num_str[j])
            if sum<10:
                num=num+num_str[j]
            elif sum==10:
                num=num+num_str[j]
                result_list.append(num)
            else:
                break


    return result_list
       
#num_str="280253"
num_str="2825302"
#num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)