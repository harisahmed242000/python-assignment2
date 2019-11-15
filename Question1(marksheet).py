print(".----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
print("| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. ")
print("| | ____    ____ | || |      __      | || |  _______     | || |  ___  ____   | | | |    _______   | || |  ____  ____  | || |  _________   | || |  _________   | || |  _________   | ")
print("| ||_   \  /   _|| || |     /  \     | || | |_   __ \    | || | |_  ||_  _|  | | | |   /  ___  |  | || | |_   ||   _| | || | |_   ___  |  | || | |_   ___  |  | || | |  _   _  |  | ")
print("| |  |   \/   |  | || |    / /\ \    | || |   | |__) |   | || |   | |_/ /    | | | |  |  (__ \_|  | || |   | |__| |   | || |   | |_  \_|  | || |   | |_  \_|  | || | |_/ | | \_|  | ")
print("| |  | |\  /| |  | || |   / ____ \   | || |   |  __ /    | || |   |  __ \    | | | |   '.___`-.   | || |   |  __  |   | || |   |  _|  _   | || |   |  _|  _   | || |     | |      | ")
print("| | _| |_\/_| |_ | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  _| |  \ \_  | | | |  |`\____) |  | || |  _| |  | |_  | || |  _| |___/ |  | || |  _| |___/ |  | || |    _| |_     | ")
print("| ||_____||_____|| || ||____|  |____|| || | |____| |___| | || | |____||____| | | | |  |_______.'  | || | |____||____| | || | |_________|  | || | |_________|  | || |   |_____|    | ")
print("| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | ")
print("| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' ")
print(" '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'")

#input for bio
name = input("Enter Your Full Nme\n")
fname = input("Father's Name\n")
roll_no = input("Enter Your Roll Number:\n")

#input for marks
print("please enter you marks below accordingly out of 100\n")
maths = int(input("Enter your marks in Mathematics\n"))

phys = int(input("Enter your marks in Physics\n"))

chem = int(input("Enter your marks in Chemistry\n"))

urdu = int(input("Enter your marks in Urdu\n"))

pst = int(input("Enter your marks in PakistanStudies out of 50\n"))


tot = maths + phys + chem + urdu + pst

per = tot/450 * 100

 

if(per>100):
    
    print("Error")

if(per>=80 and per<100):
        
        print("Great job youv'e got A+ Grade")

        
if(per>=70):
       
        print("Great but could have done better you got A Grade")

            
if(per>=60):
       
        print("Good but you can do much more you got B Grade")

        
if(per>=50):
        
        print("You can do a lot better than this just dont giveup you got C Grade")

if(per>=40):
        
        print("You can do a lot better than this just dont giveup you got D Grade")

        
if(per<40):
        
        print("Sorry you failed but don't give up you can improve with practice and persistence you are Fail")


# print("-------------------------------------------------------------------------------------------------------")
# print("|                                              Report                                                 |")
# print("|                                                                                                     |")
# print("-------------------------------------------------------------------------------------------------------")

print("Name = ",name)
print("Roll Number = ",roll_no)
print("Total marks obtained = ",tot)
print("Your percentage = ",per)



            

 




