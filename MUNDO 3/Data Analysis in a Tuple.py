num = (int((input("Enter a number: "))), 
int((input("Enter another number: "))), 
int((input("Enter with more one  number: "))), 
int((input("Enter a last number: "))))
print(f'You typed {num}')
print(f'The 9th element is appeared {num.count(9)} times')
if 3 in num:
    print(f'The 3rd element is appeared in position {num.index(3)+1}°')
else:
    print(f'The 3 is not in the list')
for n in num:
    if n % 2 == 0:
        print(f'The number {n} is pair')