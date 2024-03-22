my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
devided_num = int(input("Enter number you want to be devided: "))
new_list = []
for number in my_list:
    if number % devided_num == 0:
        new_list.append(number)

print(new_list)


