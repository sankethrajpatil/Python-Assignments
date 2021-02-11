list1 = [[2,3,5,4],
         [3,4,5,6],
         [4,4,6,3],
         ['e','r','t','t']]

for i in range(len(list1)):
    for j in range(len(list1)):
        print(list1[i][j], end=" ")
    print()

print("----------------------------")

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j], end=" ")
