from random import sample #sample() function returns a list of random elements from the original list.
n = (tuple(sample(range(1, 10), 5))) #tuple() function converts a list into a tuple.
print(n)
print('-=' * 15)
print(f'The largest value in the tuple is {max(n)} and the smallest value is {min(n)}')
print('-=' * 15) 
print(f'The first value is {n[0]} and the last value is {n[-1]}')