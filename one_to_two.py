firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file: ")

file1 = open(firstfile, 'a')
file2 = open(secondfile, 'r')

print("Content of the first file before appending -\n", file1.read())
print("Content of the second file before appending -\n", file2.read())

file1.close()
file2.close()

file1 = open(firstfile, 'a+')
file2 = open(secondfile, 'r')

file1.write(file2.read())

file1.seek(0)
file2.seek(0)

print("Content of the first file after appending -\n", file1.read())
print("Content of the second file before appending -\n", file2.read())

file1.close()
file2.close()