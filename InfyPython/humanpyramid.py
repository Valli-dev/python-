def human_pyramid(no_of_people):
   if no_of_people ==1:
       return 1*50
   else:
       return no_of_people * 50 + human_pyramid(no_of_people-2)  #remove pass and place the recursive code the you had written earlier for this function

def find_maximum_people(max_weight):
    no_of_people=0
    allowed_people=max_weight/50
    x=0
    level=1
    person =1
    for i in range(1,20,2):
       
            x= human_pyramid(i)
            if x <= max_weight: 
                #peoplenumber=int(x/50)
                print( "level= ", level)
                print("totalweight= " , x)
                print("person = ", person )

                level += 1 
                person +=2 
            else:
                break
            
    return person-2

#Provide different values for max_weight and test your program
max_people=find_maximum_people(500)
print(max_people)


