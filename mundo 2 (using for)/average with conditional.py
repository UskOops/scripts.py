from numpy import average


n1 = float(input("Enter a note average: "))
n2 = float(input("Enter a note average: "))
average = (n1 + n2) / 2
print("The average is: ", average)
if average >= 7:
    print("The student is approved")
elif average < 7 and average >= 5:
    print("The student is approved with a warning")
else:
    print("The student is disapproved")
print("End of program")
