import mymodule as mm
from mymodule import exercises as exer2

exer=exer2()

roots = exer.ex1(1, 5, 6)
print("Exercise 1: Roots")
print(roots)

recaman = exer.ex2(10)
print("Exercise 2: Recaman Sequence")
print(recaman)

arr= [1,-99,89,0,234,77,-748,11]
new_arr = exer.ex3(arr)
print("Exercise 3: Array sorting")
print(new_arr)

l1 = {1,2,3,4,5,6,7}
l2 = {11,5,6,7,8,9,10}
new_list = exer.ex4(l1,l2)
print("Exercise 4: Intersection of lists")
print(new_list)

factors = exer.ex5(10)
print("Exercise 5: Factors of a number")
print(factors)

phrase = "this is a phrase"
pal = exer.ex7(phrase)
print("Exercise 7: Palindrome")
print(pal)

import complexmodule
from complexmodule import Complex as cm
var1=cm(4,2)
var2=cm(2,3)
print("Addition:",var1+var2)
print("Subtraction:",var1-var2)
print("Multiplication:",var1*var2)
print("Division:",var1/var2)