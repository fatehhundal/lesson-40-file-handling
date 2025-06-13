file_read = open('assignment.txt', 'r')
print("File in read mode...")
print(file_read.read())
file_read.close()

file_write = open('assignment.txt', 'w')
print("File in write mode...")
file_write.write("My name is Roy! I am in year 8 and I am the class monitor. I am currently trying to work on my classmate's profiles, so I decided to start with my own.")
file_write.close()

file_append = open('assignment.txt', 'a')
print("\nFile in append mode...")
file_append.write("\nMy favourite subject is science.")
file_append.close()