for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a  count in 10s from 0 to 100:
print("a) count in 10s from 0 to 100: ")
for i in range (0,110,10):
    print(i,end=' ')
print()

#b count down from 20 to 1:
print("b) count down from 20 to 1: ")
for j in range (20,0,-1):
    print(j,end=' ')
print()

#c print a number of stars.
print("c) print a number of stars.")
number_of_stars = int(input("Enter number of stars: "))
while number_of_stars > 0:
    print("*", end='')
    number_of_stars -= 1
print()

#d print lines of increasing stars.
print("d) print lines of increasing stars.")

number_of_lines = int(input("Enter number of lines: "))
for i in range(1, number_of_lines +1 ):
        print("*" * i)


