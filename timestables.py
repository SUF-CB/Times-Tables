name = input("What's your name?")# First the user will get asked to input their name.
print("Hi, " + name + "!")# welcomes user
def Loop():
     num = int(input(" please enter a number of your choice to find the timestables of "+ name + ">>"))
     print("Multiplication Table of", num)

     for i in range(1, 13):
      print(num,"X",i,"=",num * i)
     repeat = input("Do You want to enter another number? Yes or No >> ")#The user will be asked to input either Yes/NO if they want to input another number.
     if repeat == "Yes": # if the user inputs Yes as their answer it will output the message and praise the user by saying well done along with their  name.
                Loop()
     else: #  if the user inputs No it will end and close the program automatically.
      exit()# The user has said "No".Therefore, the program will close with the exit function. 
Loop()
