from sys import getsizeof
num = int(input("Enter a number: "))

print("Value :", num)
print("Data Type :", type(num))
print("Memory Address :", id(num))
print("Size in Bytes :", getsizeof(num))