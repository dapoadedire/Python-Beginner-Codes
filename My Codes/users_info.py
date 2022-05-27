name = input("Name: ")
school = input("School: ")
age = int(input("Age: "))


f = open("users_info.txt","a")
f.write(f"\nName: {name} \nSchool: {school} \nAge: {age} ")
 #We are using \n so that if we store multiple passwords then we must be able to identify the different passwords
print("Your information is successfully stored in the file users_info.txt")
f.close()