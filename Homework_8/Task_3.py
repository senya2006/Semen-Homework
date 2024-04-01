result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
dict_count = {}

for dict in result_link:
    if dict in dict_count:
        dict_count[dict] += 1
    else:
        dict_count[dict] = 1
print(f'How many times an element is repeated in a line: {dict_count}')
