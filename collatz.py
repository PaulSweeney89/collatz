# Week 4 Task
# Input positive interger, 
# if input value is even (divide input value by 2)
# if input value is odd (multiple input value by 3 & add 1)
# end program if current value = 1

# input must be a interger number or program will not run
x = int(input("Input positive interger number: "))

# run 'while loop' until condition is met
while x != 1:

# conditional statement 1 - input number must be positive & greater than 0 for program to continue
    if x <= 0:
        print(x, "is not a positive interger number.")
        break

# conditional statement 2- if input number is even execute below formula 
    elif x % 2 == 0:
        x = x / 2
        print(x)

 # conditional statement 3- if input number is odd execute below formula    
    elif x % 2 != 0:
        x = x * 3 + 1
        print(x)