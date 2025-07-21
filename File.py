# Write to a File

# Open (or create) a file in write mode
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, this is a sample file.\n")
file.write("You can write multiple lines using write().\n")
file.write("This file was created using Python.\n")

# Close the file
file.close()

print("Content has been written to 'example.txt'")
