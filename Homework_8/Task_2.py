params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'

for key, value in params.items():
    initial_str += f'{key}={value}&'  # looked on the Internet how to do this with this symbol "&"

result = initial_str.strip('&')

print(f'Adding a string to a dictionary: {result}')
