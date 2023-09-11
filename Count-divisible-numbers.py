# 6 kyu Count the divisible numbers
# https://www.codewars.com/kata/55a5c82cd8e9baa49000004c/train/python

divisible_count=lambda x,y,k:(y//k)-((x-1)//k)


print(divisible_count(6,11,2),3)
print(divisible_count(19, 20, 2), 1)
print(divisible_count(0, 1, 7), 1)
print(divisible_count(20, 20, 2), 1)
print(divisible_count(11, 14, 2), 2)