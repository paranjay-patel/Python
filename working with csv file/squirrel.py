import pandas

data = pandas.read_csv("working with csv file/squirrel.csv")

# print(len(data[data["Primary Fur Color"]=="Gray"]))
# print(len(data[data["Primary Fur Color"]=="Cinnamon"]))
# print(len(data[data["Primary Fur Color"]=="Black"]))

gray_len = len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_len = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_len = len(data[data["Primary Fur Color"]=="Black"])

data_dict = {"squirrel": ["gray","cinnamon","black"] , 
             "population": [gray_len,cinnamon_len,black_len]}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("working with csv file/squirrel_color.csv")

# grey = data[data["Primary Fur Color"]=="gray"]
# print(grey)