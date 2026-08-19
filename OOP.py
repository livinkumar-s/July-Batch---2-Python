class Bottle:
    version="1.0.0.0"
    def __init__(self,c,h,r):
        self.color=c
        self.height=h
        self.radius=r

    def findVolume(self):
        print((22/7)*self.radius*self.radius*self.height)

    @classmethod
    def printVerion(cls):
        print(cls.version)

    @staticmethod
    def greet():
        print("Good morning")

    def __add__(self, other):
        return self.height+other.height
    
    
    

# 4 attr, 2 method

# print(Bottle.version)

# Bottle.version="1.0.0.1"

# Bottle.printVerion()

b1=Bottle("Black",40,3)
b2=Bottle("Blue",30,5)
b3=Bottle("red",25,10) 

print(b1+b2)

# b1.greet() #Bottle.greet()

# b1.color="Blue"
# b3.height=14
# b1.color="Black"

# print(b1.version)
# print(b2.version)
# print(b3.version)

# print(b1.color)
# print(b2.color)
# print(b3.color)

# b1.findVolume()
# b2.findVolume()
# b3.findVolume()

# a=1 # int obj
# b="Hello"
# c=[1,2,3]

# print(type(b1)) #<class "__main__.Bottle">

# a=1 #(what,methods,attri) 
# a=2 #(what,methods,attri)

# class Rect:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def findArea(self):
#         print(self.l*self.b)


# rec1=Rect(16,8)

a=1-3

int