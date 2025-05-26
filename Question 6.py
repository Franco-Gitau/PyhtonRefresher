numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}:"))
    numbers.append(num)

avg = sum(numbers) / len(numbers)
print(f"Average of the entered numbers: {avg}")