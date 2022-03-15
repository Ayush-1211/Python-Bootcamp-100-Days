import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
num_choice = random.randint(0, num_items-1)

person_who_will_pay_bill = names[num_choice]

print(person_who_will_pay_bill + " is going to buy the meal today!")