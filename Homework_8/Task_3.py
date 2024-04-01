result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
dict_count = {}

for element in result_link:
    if element not in dict_count:
        dict_count[element] = result_link.count(element)

print(f'How many times an element is repeated in a line: {dict_count}')
