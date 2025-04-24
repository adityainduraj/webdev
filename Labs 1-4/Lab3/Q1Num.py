numbers = []
print("Enter number of inputs: ")
n = int(input())
for i in range(0, n):
    print("Enter number: ")
    num = int(input())
    numbers.append(num)
mean = sum(numbers) / len(numbers)
variance = sum((i - mean) ** 2 for i in numbers) / len(numbers)
sd = variance ** 0.5
print(f"Mean = {mean:.2f}")
print(f"Variance = {variance:.2f}")
print(f"Standard Deviation = {sd:.2f}")
