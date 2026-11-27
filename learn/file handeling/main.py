a= input("enter your message")
file = open("file.txt","w")
file.write(a)
file.close()
print("hi")

file= open("file.txt","r")
print(file.read())
file.close()