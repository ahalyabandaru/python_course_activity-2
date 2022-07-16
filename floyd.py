n = int(input("Enter the number of rows  : "))
number = 1

print("Floyd's Triangle :") 
print()
for i in range(1, n + 1):
    for j in range(1, i + 1):        
        print(number, end = ' ')
        number = number + 1
    print()
