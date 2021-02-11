def vowelcount(str):
    str=str.lower()
    a=[0,0,0,0,0]
    for i in str:
        if str[i]=='a':
            a[0]+=1
        elif str[i]=='e':
            a[1]+=1
        elif str[i]=='i':
            a[2]+=1
        elif str[i]=='o':
            a[3]+=1
        elif str[i]=='u':
            a[4]+=1
        


str = input("Enter the string: ")
vowelcount(str)
