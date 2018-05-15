while True:
    print('1. square')
    print('2. circle')
    print('3. trapezoid')
    print('4. parallelogram')
    print('5. triangle')
    print('quit')
    users_options = input('please press one of the following choices:  ')

    if users_options == '1':
        print('1')
        print('please tell me how wide the room is:')
        width = float(input())
        print('please tell me how long the room is:')
        length = float(input())
        area = width*length
        perimeter = (width+length)*2
        print('the area is:')
        print(area)
        print("the perimeter is:")
        print(perimeter)

    elif users_options == '2':
        print('2')
        radius = input('please enter the radius of your circle:  ')
        radius = float(radius)
        diameter = radius*2
        print('the diameter is:')
        print(diameter)
        pi = 3.1415926
        circumference = radius**2*pi
        print('the area if your circle is:')
        print(circumference)
        perimeter = diameter*pi
        print('the perimeter of your circle is:')
        print(perimeter)

    elif users_options == '3':
        upperline = input('the upper or topline of the trapezoid is:  ')
        upperline = float(upperline)
        bottomline = input('the bottomline of the trapezoid is:  ')
        bottomline = float(bottomline)
        height = input('the height of the trapezoid is:  ')
        height = float(height)
        area = (upperline+bottomline)*height/2
        print('the area of the trapezoid is:')
        print(area)
    elif users_options == '4':

        height = input('the height of the parallelogram is:  ')
        height = float(height)
        base = input('the base of the parallelogram is:  ')
        base = float(base)
        area = height*base
        print(area)
    elif users_options == '5':

        height = input('the height of the triangle is:  ')
        height = float(height)
        base = input('the base of the triangle is:  ')
        base = float(base)
        area = height*base/2
        print(area)

    elif users_options == 'quit':
        print('Bye, have a nice day. Thank you for veiwing')
        break

    else:
        print('please choose the correct options')
