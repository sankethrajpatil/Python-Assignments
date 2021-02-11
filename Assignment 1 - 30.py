f = open("firstfile.txt", "w")
f.write("I am God \n God is me")
print("Writing success")
f.close()
print("Closing Success")

f = open("firstfile.txt", "r+")
str1 = f.read()
str2 = f.read(10)
print(str1)
print("\n"+ str2)
f.close()

