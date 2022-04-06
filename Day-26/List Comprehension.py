numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Ayush"
letter_list = [letters for letters in name]
print(letter_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension
names = ["Ayush", "Drashti", "Anand", "Keval", "Kunal", "Ranbir", "Salman", "Raj"]
short_names = [n for n in names if len(n) < 5]
print(short_names)

long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)