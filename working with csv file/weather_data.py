import pandas

data = pandas.read_csv("working with csv file/weather_data.csv")
# print(data)
# data_dict  = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

#get data in columns
# print(data["temp"])
# print(data.temp)

#get data in row
# print(data[data.day == "monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "monday"]
# print((monday.temp * 9/5) + 32) 

 

















# import csv

# with open("working with csv file/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1]!= "temp":
#             temperature.append(row[1])
# print(temperature)

