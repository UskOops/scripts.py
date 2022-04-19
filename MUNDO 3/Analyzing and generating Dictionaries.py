from random import randint as rand

inf = {}


def data(*grade, situ=True):

    # main
    a = 0
    inf["Total"] = len(grade)
    inf["biggest"] = max(grade)
    inf["smallest"] = min(grade)
    inf["average"] = sum(grade)/len(grade)
    if situ:
        if inf["average"] >= 7:
            print(f'The average is {inf["average"]} and the student is approved')
            inf["Approved"] = True
        elif inf["average"] < 7:
            print(
                f'The average is {inf["average"]} and the student is disapproved')
            inf["Approved"] = False
        else:
            print(
                f'The average is {inf["average"]} and the student is not approved')
        inf["Approved"] = False
    else:
        print(f'The average is {inf["average"]}')
data(rand(1, 15),rand(1, 15),rand(1, 15), situ=True)
print(inf)