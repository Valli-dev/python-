string1="ABCDEF"
string2="ghijkl"
string3=string1+string2
string5="Alphabets"
print("string3 (str1+str2)= ", string3)
string4= "   ".join((string3, string5))
print("string4(str3 join str5) = "+ string4) #Adding one string to another
string6=" ".join(string1)
print("string6 '' join string1: =" + string6)

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
textjoin=' '.join(text)
print(textjoin)
names="Anu"
dept=" IT "
deptjoin=''.join(dept)
namejoin=''.join(names)
print(deptjoin)
print(namejoin)
print(dept.join((names)))

test = {'2', '1', '3'}   
s = ', '
print(s.join(test)) # set is unordered set of collections so order is random 


test={'mat':1, 'that':2, 'sat':3 }
sep= '-->'
print(sep.join(test))  #dictionary iterables with join

est={'1': 'mat', '2':'that',  '3':'sat' }
sep= '-->'
print(est.keys())
print(est.items())

print(sep.join(est)) 
print(string1.isalpha())
print(textjoin.isalnum())
name="Monica3 "
print(name.isalnum())

fruits="banana\napple\ncitrus\njackfruit\n"
fruitlist=fruits.split('\n')
print(fruitlist)

