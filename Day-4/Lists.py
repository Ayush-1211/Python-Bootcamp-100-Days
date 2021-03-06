states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
                     "Hawaii"]

print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america[-2])
print(states_of_america)

states_of_america[0] = "India"
print(states_of_america)

states_of_america.append("Gujarat")
print(states_of_america)

states_of_america.extend(["Rajasthan", "Mumbai", "Delhi"])
print(states_of_america)


# Nested Lists
fruits = ["apple", "banana", "mango"]
vegetables = ["tomatoes", "potatoes", "garlic"]

nested_list = [fruits, vegetables]
print(nested_list)
