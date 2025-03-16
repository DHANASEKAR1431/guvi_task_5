#filter people above 18 and get names
people = [{'name': 'dhana', 'age':28},{'name': 'kumar','age': 20}, {'name': 'dhans', 'age':18},{'name':'pradeep', 'age':16},{'name': 'naveen', 'age':'14'}]
adults = list(filter(lambda person: int(person ['age'])  >= 18,people)) #filterout under 18
names = list(map(lambda person: person['name'], adults)) #extract names
print(names)

#product of all number in list
from functools import reduce
num = [1,2,3,4,5,6,7,8,9,10]
product = reduce(lambda x,y:x*y,num)
print(product)

#square of even number using list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
squ_even = [x**2 for x in numbers if (lambda x: x%2 == 0) (x)]
print(squ_even)

# check if given number is string
is_number = lambda s: s.isdigit()

print(is_number("123"))
print(is_number("4567"))
print(is_number("dhana"))

#extract year,date,day
from datetime import datetime
date = datetime(2024, 3, 17)
get_date_parts = lambda dt: (dt.year, dt.month, dt.day)
print(get_date_parts(date))

#fibonacci series
from functools import reduce
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1]) if n > 1 else [0] if n == 1 else []

print(fibonacci(5))  
print(fibonacci(8))
print(fibonacci(1))
print(fibonacci(0))

