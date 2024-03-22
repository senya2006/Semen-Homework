my_list = [1, 5, 68, 0]
# my_list = [1,2,3,4,6,7,8]
for i in range(1, len(my_list)):
    if my_list[i] != my_list[i-1] + 1:
        print("Non-consecutive number in the list: ", my_list[i])
        break
else:
    print("The list contains consecutive numbers!")
