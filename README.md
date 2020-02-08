# collatz
**Program using while loop & conditional if, elif & else statements to execute simple formulas & iterate until the while loop condition is met.**

*Week 4 Programming & Scripting Task*

Program Overview:
- Program prompts the user to input a positive interger number 'x'.
  - input value 'x' must be a interger (strings & floats will not allow program to execute).
```
x = int(input("Input positive interger number: "))
```
- Initiate the while loop (end loop iterations when 'x = 1').
```
while x != 1:
```
- Conditional statement 1 - **if** input value 'x' is less than or equal to zero then end 'while' loop & print message "x is not a positive interger number" otherwise program continues to conditional statement 2 or 3.
```
  if x <= 0:
    print(x, "is not a positive interger number.")
    break
```
- Conditional statement 2 - **elif** input value 'x' is a even number (remainder of x / 2 = 0) then execute the formula x = x / 2 and output the new calculated value for x and reiterate the while loop.
```    
  elif x % 2 == 0:
    x = x / 2
    print(x)
```
- Conditional statement 3 - **elif** input value 'x' is a odd number (remainder of x / 2 ≠ 0) then execute the formula x = (x * 3) + 1 and output the new calculated value for x and reiterate the while loop.
```
  elif x % 2 != 0:
    x = x * 3 + 1
    print(x)
```
- Alternatively the above Conditional statement 3 could be replaced using an **else** statement to conclude the required conditions of the while loop.
```
  else:
    x= x * 3 + 1
    print(x)
```
- Provided the correct input is entered into the program at the start, the while loop will continue to interate through the formulas within the conditional statements 2 & 3, solving for a new value of x each time until the while loop condition is met i.e the value 'x' reaches 1.  

Example of input, interations & output of Program:
```
collatz.py
Input positive interger number: 10
5.0
16.0
8.0
4.0
2.0
1.0
```

References:

[Python While Loops](https://realpython.com/python-while-loop/)

[Python Conditional Statements if, elif, else](https://realpython.com/python-conditional-statements/)
 
