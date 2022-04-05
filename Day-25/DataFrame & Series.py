import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].tolist()
print(temp_list)

print("-------------------------------------------------")

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())
print(data["temp"].max())

print("-------------------------------------------------")

# Get the data in columns
print(data["condition"])
print("-------------------------------------------------")
print(data.condition)

print("-------------------------------------------------")

# Get the data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

print("-------------------------------------------------")

monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

print("-------------------------------------------------")

# Create a dataframe from scratch
data_dict_2 = {
    "students": ["Ayush", "Drashti", "Anand"],
    "scores": [75, 95, 70]
}
data = pandas.DataFrame(data_dict_2)
print(data)
data.to_csv("new_data.csv")