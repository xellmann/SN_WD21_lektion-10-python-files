with open("data.txt", "r") as data_file:
    lines = data_file.read().splitlines()
    for i in lines:
        print(i)
