import fileinput
try:
    with open('my_file.txt', 'r') as file1:
        for idx, line in enumerate(file1, start=1):
         print(f"Line {idx}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file does not exist.")

#2nd way
#with open('my_file.txt','w') as file2:
# reading_file = file1.read()