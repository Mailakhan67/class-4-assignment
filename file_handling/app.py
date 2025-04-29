# file=open("demo.txt", "w")
# file.write("hello world\n")
# file.write("hello pakistan\n")
# file.close()

file=open("demo.txt" , "r+")
file.write("Maila\n")
text=file.read()
print(text)
file.close()



website=['maila\n','naila\n','kashaf\n']
file=open("demo.txt","a")
file.writelines(website)
file.close()
