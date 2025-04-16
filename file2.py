file1 = open('my_file2.txt', 'w')

writing_file =  file1.write('This is my python code, which i am learning')

print(file1)
file1.close()

file1 = open('my_file2.txt','a')
appending_file = file1.write('I am learning other stuff as well')
print(appending_file)
file1.close()

file1 = open('my_file2.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()





