myfile = open("workinghours.txt")

#Đọc file
lines = myfile.readlines()
print(lines)
myfile.close()

for line in lines:
    print(line)