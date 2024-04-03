with open('test_txt', 'r') as test_txt:
    text = test_txt.read()
with open('new_test.txt', 'w') as new_test:
    new_test.write(text)
print("Text copied successfully to new_test.txt")
