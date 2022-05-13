# nums=[5,6,7,8,9]
# for i in nums:
#     print(i)

# print("I am from Iterator method:")
# it = iter(nums)
# print(it.__next__())
# print(next(it))

class TopTen:
    def __init__(self):
        self.num =1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            i = self.num
            self.num += 1
            return i
        else:
            raise StopIteration
           

t= TopTen()

#print(next(t))
for i in t:
    #print(type(t))
    print(i)