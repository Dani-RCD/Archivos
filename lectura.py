
file = open("myfile.txt","w")
L = ["Hello world \n","Welcome \n","Python \n"]


file.write("Hello There \n")
file.writelines(L)
file.close()

file = open("myfile.txt","r+") 
print("Output of the Read function is ")
print(file.read())
print()

file.seek(0)  

print( "The output of the Readline function is ")
print(file.readline()) 
print()
  
file.seek(0)
  

print("Output of Read(12) function is ") 
print(file.read(12))
print()

file.seek(0)
  
print("Output of Readline(8) function is ") 
print(file.readline(8))
  
file.seek(0)
# Función de lectura de líneas
print("Output of Readlines function is ") 
print(file.readlines()) 
print()
file.close()
