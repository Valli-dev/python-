f=open('file.jpeg', 'rb')
f1= open('copydata1.jpeg', 'ab')
for i in f:
    f1.write(i)
#f1.write("I learnt file handling now!!!!!!")