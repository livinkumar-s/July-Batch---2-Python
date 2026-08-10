# List 

# l1=[1,2,3,9.9,"Hello",False,1]
# print(len(l1))
# print(l1[2])
# l1[2]=5
# l1.append(55)
# l1.append(44)
# l1.insert(-2,-1)
# l1.extend([1,2,3,4,5])
# l1.remove(9.9)
# l1.remove(1)
# l1.pop(4)
# l1.pop()

# print(l1.index("hello"))
# l1=[1,2,3,9.9,234,342,1,2,0,-1]
# print(l1.count("hello"))
# l1.reverse()
# l1.sort(reverse=True)
# print(l1)

# a=3214234

# for i in a:
#     print(i)

# iterable + ordered ---> Sequence

# Tuple 

# t1=(1,2,3,1,2,3,"Hello")
# # t1[2]=33
# print(t1.index(4))

# person=["Leo",23,"SASE"]
# name,age,role=person

# print(role)

# a=1,2,3,4,5 #Tuple
# print(a)

# a,b=1,2

# Slicing

t1="Hello World"

# print(t1[5:])
# print(t1[2:-1]) #2,3
# print(t1[2:6:2]) #2,4
# print(t1[:4])
# print(t1[::-1])

# Set 
# s1={342,54,234,536,234,1,3,1,1,3}
# print(s1[0])
# s1.add(-1)
# s1.add(-2)
# s1.remove(342)
# print(s1)

# s1={2,1,3,4,5}
# s2={3,4,5,-1,8,9,10}

# print(s1.union(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))

# Dict 
# person={
#     "name":"Ben",
#     "age":44,
#     "isMarried":True,
#     "favMovies":[24,96]
# }

# print(person["favMovies"][0])

# print(person["age"])

# person["age"]=45
# person["role"]="FED"

# person.pop("isMarried")

# print(person.keys()) #dict_key
# print(person.values()) #dict_values
# print(person.items()) 

# for i in person:
#     print(person[i])

l1=[
    1,
    2,
    3,
    [
        "four",
        "five",
        [
            "six",
            "seven",
            "eight"
        ]
    ]
]

print(l1[-1][-1][-1][-1])