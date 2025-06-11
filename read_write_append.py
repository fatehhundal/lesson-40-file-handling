file_read = open('first_document 2.txt', 'r')
print("File in read mode...")
print(file_read.read())
file_read.close()

file_write = open('first_document 2.txt', 'w')
print("File in write mode...")
file_write.write("Hi! I am Penguin. I am 1 year old. ")
file_write.close()

file_append = open('first_document 2.txt', 'a')
print("\nFile in append mode...")
file_append.write("Hi! I am Penguin. I am 1 year old.")
file_append.close()