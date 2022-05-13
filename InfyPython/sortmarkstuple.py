list_of_marks=(12,18,25,24,2,5,18,20,20,21)
#list_of_marks=(25, 25, 25, 25, 25, 25, 25, 25, 25, 25)
#list_of_marks=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
def find_more_than_average():
    m_avg=[]
    average =sum(list_of_marks)/10
    print(average)
    for mark in list_of_marks:
        if mark >average:
            m_avg.append(mark)
    print("marks greater than average",m_avg)
    print(len(m_avg)/10)
    percentage = (len(m_avg)/10)*100
    print("percentage of students:",percentage )
    return percentage
    #Remove pass and write your logic here

def sort_marks():
    return sorted(list_of_marks)
    #Remove pass and write your logic here

def generate_frequency():
    freq=[]
    count=0
    i=0
    for marks in range(0,26):
        for i in range(len(list_of_marks)):
            if marks ==list_of_marks[i]:
                count +=1
        freq.append(count)
        count=0
    return freq


print(find_more_than_average())
print(generate_frequency())
print(sort_marks())

s=("greeks")
s1=tuple(s)
print(s1)

n="1234"
n1=tuple(n)
print(n1)