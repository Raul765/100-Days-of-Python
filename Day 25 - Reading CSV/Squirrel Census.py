import pandas 

data=pandas.read_csv(r"Day25 - Reading CSV\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur=data[data["Primary Fur Color"]=="Gray"]
cinnamon_fur=data[data["Primary Fur Color"]=="Cinnamon"]
black_fur=data[data["Primary Fur Color"]=="Black"]

new_data={
    "Fur color":["Gray","Cinnamon","Black"],
    "Count":[len(gray_fur),len(cinnamon_fur),len(black_fur)]
}

new_dataframe=pandas.DataFrame(new_data)
new_dataframe.to_csv(r"Day25 - Reading CSV\Squirrel_color_count.csv")