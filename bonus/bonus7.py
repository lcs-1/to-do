def get_average():
    with open(r'bonus\file\data.txt','r') as file:
        content = file.readlines()
    data = content[1:]
    data = [float(i) for i in data]
    total = sum(data) / len(data)
    return total


average = get_average()
print(average)
