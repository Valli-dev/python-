def grade(score_list):
    for score in score_list:
        
        if score >= 80 and score <= 100: 
            print( score,  "A")
        elif score >= 73 and score < 80:
            print(score, "B") 
        elif score >= 65 and score <= 72:
            print(score, "C") 
        elif score >= 0 and score <= 64:
            print (score, "D")
        else:
            print(score,"Z") 
            
    return 
        
        
grade([91, 56, 74, 9,67,42,'a'])