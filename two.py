a=134358698464
print(a)
b="sdjbsdj"
print(b)
print(f'the type of a is: {type(a)}')
print(f'the type of a is: {type(b)}')


n=18
m= 76
add= m+n
print(f'addition of m and n is : {add}')
sub= m-n
print(f'subtraction of m and n is : {sub}')
product= m*n
print(f'product of m and n is : {product}')
div= m/n
print(f'division of m and n is : {div}')
exp= m**n
print(f'exponential of m and n is : {exp}')
mod= m%n
print(f'modulus of m and n is : {mod}')

q=89
def f():
    print(f'inside f(): {a}')
f()
def g():
    r=99
    print(f'inside g(): {r}')
g()

def h():
    global q
    q= 5
    print(f'inside h(): {q}')
h()

