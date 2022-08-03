import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_color_rows = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels = len(gray_color_rows)

cinnamon_color_rows = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels = len(cinnamon_color_rows)

black_color_rows = data[data["Primary Fur Color"] == "Black"]
black_squirrels = len(black_color_rows)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

count_data = pandas.DataFrame(data_dict)
count_data.to_csv("squirrel_count.csv")
