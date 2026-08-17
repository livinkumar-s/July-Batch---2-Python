# file=open("text.txt","r")
# print(file)
# file.seek(5)
# content=file.read(10)
# content=file.read(5)
# print(file.tell())
# content=file.readline()
# content=file.readline()
# content=file.readline()
# content=file.readlines()
# content=file.readlines()[2]
# print(content)
# print(file.readable())
# file.close()

file=open("text/text.txt","a")

content="Hello\nHi\nWelcome...!"
# file.writable()
file.write(content)
# print(file.writable())

file.close()

# file = open("text/text1.txt","a")

# file.close()

# with open("text/text.txt") as f:
#     print(f.readable())
#     print(f.read())

# print("done")