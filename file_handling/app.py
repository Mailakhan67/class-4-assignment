# file=open("demo.txt", "w")
# file.write("hello world\n")
# file.write("hello pakistan\n")
# file.close()

# file=open("demo.txt" , "r+")
# file.write("Maila\n")
# text=file.read()
# print(text)
# file.close()



# website=['maila\n','naila\n','kashaf\n']
# file=open("demo.txt","a")
# file.writelines(website)
# file.close()




# file = open("new_file.txt", "w")
# file.write("Hello, world!\n")  # \n creates a new line
# file.write("This is another line.\n")
# file.close()



# lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
# file = open("new_file.txt", "a") # run with mode w, and see the result
# file.writelines(lines)
# file.close()


#file = open("my_file.txt", "r")

# file = open("new_file.txt", "r")  # Opens "my_file.txt" in read mode ("r")
# content = file.read()
# print(content)



# line = file.readline()
# print(line)

# print("Position after seek(0):", file.tell())



# file.seek(0) # First move the pointer to the start

# lines = file.readlines()
# for line in lines:
#     print(line)


# file = open("new_file.txt", "r")
# for line in file:  # Iterating directly over the file reads line by line
#     print(line.strip()) # .strip() removes leading/trailing whitespace

# file.close()


# lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
# with open("my_file.txt", "a") as file:
#     for line in lines:
#         file.write(line)    # file mein likhna
#         print(line.strip()) # terminal pe print karna (strip() new line hata deta hai)





# file = open("new_file.txt", "r")
# for line in file:  # Iterating directly over the file reads line by line
#     print(line.strip()) # .strip() removes leading/trailing whitespace

# file.close()







# # Exclusive creation (x)
# # try:
# #     with open('unique.txt', 'x') as file:
# #         file.write('Created exclusively!')
# #         print("File created successfully!")
# # except FileExistsError:
# #     print("File already exists.")


# # with open("new_file.txt", "r") as file:
# #     content = file.read()
# #     print(content)
# # File is automatically closed here
# #file.tell() # will produce error, file is already closed because of with statement



# i=0
# with open("new_file.txt", "r") as file:
#   print(file.tell())     # 0


#   while True:
#     content = file.read(10)
#     if not content:
#       print("End of file")
#       break
#     print(content)
#     i+=1


#            # reads 5 characters
#   print(file.tell())     # now at position 5
#   file.seek(0)           # back to start




#   with open("new_file.txt", "rb") as f:
#     print("Tell: ", f.tell())        # ➤ 0
#     f.seek(5)              # same as f.seek(5, 0)
#     print("Tell: ", f.tell())        # ➤ 5

#     f.seek(2, 1)           # move 2 bytes forward from current
#     print("Tell: ", f.tell())        # ➤ 7

#     f.seek(-3, 2)          # go 3 bytes *before* end of file
#     print("Tell: ", f.tell())        # ➤ near the end





# # copying file

    
# def copy_file(source_path, destination_path):
#     try:
#         with open(source_path, "r") as source_file, open(destination_path, "w") as dest_file:
#             for line in source_file:
#                 dest_file.write(line)
#         print(f"File '{source_path}' copied to '{destination_path}' successfully.")
#     except FileNotFoundError:
#         print(f"Error: Source file '{source_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# copy_file("unique.txt", "unique_copy.txt")




# # image binary 

# def copy_image(source_path, destination_path):
#     try:
#         with open(source_path, 'rb') as source_file:
#             with open(destination_path, 'wb') as destination_file:
#                 while True:
#                     chunk = source_file.read(1024)  # Read in chunks
#                     if not chunk:
#                         break
#                     destination_file.write(chunk)
#         print(f"Image copied successfully from '{source_path}' to '{destination_path}'")
    
#     except FileNotFoundError:
#         print(f"Error: Source file '{source_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage (replace with your file paths)
# copy_image("Apollo11.jpg", "Copy_Apollo11.jpg")









# Create and write to a file
with open('demo.txt', 'w') as file:
    file.write('Python File Handling\n')
    file.write('Line 1\nLine 2\n')

# Read and print content
with open('demo.txt', 'r') as file:
    print("Content:")
    print(file.read())

# Append a new line
with open('demo.txt', 'a') as file:
    file.write('Appended line\n')

# Read lines using seek
with open('demo.txt', 'r+') as file:
    file.seek(0)
    print("First line:", file.readline())
