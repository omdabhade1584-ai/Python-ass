n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

arr.sort()

print("Smallest =", arr[0])
# print("Second Smallest =", arr[1])
print("Largest =", arr[-1])
# print("Second Largest =", arr[-2])