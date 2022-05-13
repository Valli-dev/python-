f = open("mypic.jpg", "rb")
#print(f.read())
#print(f.read())
#print(f.readline(6))
# print(f.readline(),end="")
# print(f.readline())
# print(f.readline())
f1=open("file.jpeg", 'wb')
#f1=open("file1", 'a')
#f1.write("\nsomething new")

#print(f.readlines())
# for i in f:
#     print(i)

for data in f:
     f1.write(data)