n = int(input("Enter a number of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter an element:"))
    arr.append(num)

sum = 0
for i in range(n):
    sum += arr[i]

print("Sum of array elements =",sum)