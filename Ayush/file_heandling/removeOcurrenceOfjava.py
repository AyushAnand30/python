f = open("practice.txt" , "r")
data = f.read()
new_data = data.replace("java" , "python")
print(new_data)
#file overriding means replace old data with new data
f = open("practice.txt","w")
data = f.write(data.replace("java","python"))
f.close()
#find the word "learning in the data
f = open("practice.txt" , "r")
data = f.read()
if(data.find("learning ")!=-1):
    print("found")
else:
    print("not found: ")


