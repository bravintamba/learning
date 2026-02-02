def right_justify(s):
    spaces = 70 - len(s)
    print(' ' * spaces + s)
right_justify('monty')


   #Functions as arguments
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')

do_twice(print_spam)

def do_twice(f, value):
    f(value)
    f(value)
def print_twice(s):
    print(s)
    print(s)
do_twice(print_twice, 'spam')   

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)


    #Drawing grids
def print_beam():
    print('+', '- ' * 4, '+', '- ' * 4, '+')

def print_post():
    print('|', '  ' * 4, '|', '  ' * 4, '|')

def print_beam():
    print('+ - - - - + - - - - +')

def print_post():
    print('|         |         |')
def print_grid():
    print_beam()
    for i in range(4):
        print_post()
    print_beam()
    for i in range(4):
        print_post()
    print_beam()
print_grid()


#4 x4 grid
def print_big_beam():
    print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+')

def print_big_post():
    print('|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')

def draw_big_grid():
    print_big_beam()
    for i in range(4):
        print_big_post()
    print_big_beam()
    for i in range(4):
        print_big_post()
    print_big_beam()
    for i in range(4):
        print_big_post()
    print_big_beam()
    for i in range(4):
        print_big_post()
    print_big_beam()
