def lenfunc(string):
    count=0
    for i in string:
      count=count+1

    print(count)
    return count


string=input("Enter string:")
print("Length of the string is:")
lenfunc(string)


