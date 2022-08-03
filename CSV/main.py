# with open("weather_data.csv", mode="r") as file:
#     content = file.readlines()
#     print(content)

# import csv
#
# with open("weather_data.csv", mode='r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

data_temp = data["temp"]
data_temp_list = data_temp.to_list()
print(data_temp_list)

print(data_temp.mean())

max_temp = data_temp.max()
print(data[data.temp == max_temp])

print()
monday_data = data[data.day == "Monday"]
print(monday_data.condition)

print()
monday_temp = int(monday_data.temp)
monday_temp_f = monday_temp * 9 / 5 + 32
print(monday_temp_f)

