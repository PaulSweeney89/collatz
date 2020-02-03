# Week 4 Task
# Input positive interger, 
# if input value is even (multiple input value by 2)
# if input value is odd (multiple input value by 3 & add 1)
# end program if current value = 1

x = int(input("input positive interger number: "))


#Test Code
#while x > 0:
    
    #if x % 2 == 0:
        #calc = x * 2
        #print(x, "is a even number!", "calculation = ", x, "x 2 = ", calc)

    #if x % 2 != 0:
        #calc = (x * 3) + 1
        #print (x, "is a odd number!", "calculation = ", x, "x 3 + 1", calc)
    #break


while x > 1:
    if x % 2 == 0:
        x = x * 2
    
    if x % 2 != 0:
        x = x * 3 + 1

    break
 


