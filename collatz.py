# Week 4 Task
# Input positive interger, 
# if input value is even (divide input value by 2)
# if input value is odd (multiple input value by 3 & add 1)
# end program if current value = 1

x = int(input("Input positive interger number: "))

print(int(x), end=' ') # print input valued as part of output & output all on same line

while x != 1:

    if x <= 0:
        print(int(x), "is not a positive interger number.")
        break

    elif x % 2 == 0:
        x = x / 2
        print(int(x), end=' ') # print output all on same line
  
    else:
        x = x * 3 + 1
        print(int(x), end=' ') # print output all on same line