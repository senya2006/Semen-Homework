result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
dict_count = {}

for dict1 in result_link:
    if dict1 in dict_count:
        dict_count[dict1] += 1
    else:
        dict_count[dict1] = 1
print(f'How many times an element is repeated in a line: {dict_count}')
