l1 = float(input("Enter the length of the first side: "))
l2 = float(input("Enter the length of the second side: "))
l3 = float(input("Enter the length of the third side: "))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print("The triangle is valid")
    if l1 == l2 and l2 == l3:
        print("The triangle is equilateral")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("The triangle is isosceles")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("The triangle is scalene")
else:
    print("The triangle is invalid")