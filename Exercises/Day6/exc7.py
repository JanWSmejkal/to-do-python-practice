member = input("Add a new member: ")

file = open(r"C:\Users\Jan Smejkal\Downloads\members.txt", "a")
file.write(f"{member}\n")
file.close()

"OR:"

file = open(r"C:\Users\Jan Smejkal\Downloads\members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()