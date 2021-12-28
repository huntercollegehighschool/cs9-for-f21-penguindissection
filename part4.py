"""
******
PART 4
******

Write a program that prompts the user to enter a numbers. The program will then go through all the numbers from 1 to the input itself and:

- print "fizz" if the number is divisible by 3
- print "buzz" if the number is divisible by 5
- print "fizzbuzz" if the number is divisible by both 3 and 5
- print the number itself if it does not fall into any of the categories above
  
(Tip: order matters!)

What should appear on the console when this program runs:

Enter a number: 21
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz

"""

melancholy = int(input("Enter a number: "))

for melancholy in range(1, melancholy + 1):
  if melancholy % 5 == 0 and melancholy % 3 == 0:
    print("fizzbuzz")
  elif melancholy % 5 == 0:
    print("buzz")
  elif melancholy % 3 == 0:
    print("fizz")
  else:
    print(melancholy)