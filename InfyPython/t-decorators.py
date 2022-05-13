class Square:
    def __init__(self, h,w):
        self.__height=h
        self.__width=w
    def setsides(self, newside):
        self.__height= newside
        self.__width= newside
    @property    
    def height(self):
        return self.__height
    
    @height.setter
    def set_height(self, new_value):
        if new_value >=0:
            self.__height=new_value
        else:
            raise Exception ("Value needs to be greater than or equal to zero")
square= Square(5,5)
square.__height=3
print(square.__height)

def div(a,b):
    print(a/b)


def dec_div(div):
    def swap(a,b):
        if(a<b):
            a,b = b,a
        return div(a,b)
    return swap


div = dec_div(div)

div(2,4)