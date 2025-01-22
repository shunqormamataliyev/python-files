#Fayl o'qish rejimida ochish
file = open("example.txt","r")  #read rejim
content = file.read() #faylni ichini o'qish
print(content)
file.close()

with open("example.txt","r") as file:
    content = file.read()
    print(content)
    #