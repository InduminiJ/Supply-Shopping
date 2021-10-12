#input for the character choice
job = int(input("Please choose a character\nPress the nunmber to confirm choice\n\n1.Teacher\n2.Principal\n3.Vice Principal\n\nEnter choice: "))

#input for user name
name = input("Please enter your name: \n")

#Input for the team member names
print("\nCan you please provide the names of the other 4 members of your team?\n1.", name)
t2 = input("2. ")
t3 = input("3. ")
t4 = input("4. ")
t5 = input("5. ")

#Display of items in store
print("\nThank you! It is now time to shop for supplies!")
print("\nThis is what the shop has to offer.")
print("\nMechanical Pencils \t...\t $1.99")
print("Tape \t\t\t...\t $0.99")
print("Pens \t\t\t...\t $1.00") 
print("Printer \t\t...\t $79.99")
print("Mouse \t\t\t...\t $19.99\n\n")

#Pricing for Mechanical Pencil and total
MP = int(input("How many mechanical pencils would you like (Each costs $0.99)? "))
total = (MP*1.99)
MPtot = (MP*1.99)
print("current total is: {:.2f}\n".format(total))

#Pricing for tape and total
tape = int(input("How many tapes would you like (Each costs $0.99)? "))
tapetot = (tape*0.99)
total = (total)+tapetot
print("current total is: {:.2f}\n".format(total))

#Pricing for pens and total
pens = int(input("How many pens would you like (Each cotst $1.00)? "))
penstot = (pens*1.00)
total = (total)+(penstot)
print("current total is: {:.2f}\n".format(total))

#Pricing for printer and total
printers = int(input("How many printers would you like (Each costs $79.99? "))
printerstot = (printers*79.99)
total = (total)+ printerstot
print("current total is: {:.2f}\n".format(total))

#Pricing for mouse and total
mouse = int(input("How many mice (mouse) would you like (Each costs $19.99)? "))
mousetot = (mouse*19.99)
total = (total)+mousetot
print("current total is: {:.2f}\n".format(total))

#Printing code for item reciept
print("Here is your reciept")
print("\nMechanical Pencils \t...\t{:.2f}".format(MPtot))
print("Tape \t\t\t...\t{:.2f}".format(tapetot))
print("Pens \t\t\t...\t{:.2f}".format(penstot)) 
print("Printer \t\t...\t{:.2f}".format(printerstot))
print("Mouse \t\t\t...\t{:.2f}".format(mousetot))
print("Total \t\t\t...\t{:.2f}".format(total))
print("Thank you for shopping! Have a great day :)")

