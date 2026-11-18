n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

result = []

# Add all non-zero elements first
for element in arr:
    if element != 0:
        result.append(element)

# Add zeros at the end
for element in arr:
    if element == 0:
        result.append(element)

print("Original array:", arr)
print("Array after moving zeros:", result)