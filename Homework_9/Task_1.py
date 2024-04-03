with open('test_txt.txt', 'r') as test_txt:
    with open('new_test.txt', 'w') as new_test:
        new_test.write(test_txt.read())
