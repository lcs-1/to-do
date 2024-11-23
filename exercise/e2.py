import csv

with open("unique_city_temperature.csv","r") as file:
    data = list(csv.reader(file))
    
city = (input("Enter the city name you want to know the temperature of:")).title()

for row in data:
    if city == row[0]:
        print(f"The current temperature in {row[0]} is {row[1]}")