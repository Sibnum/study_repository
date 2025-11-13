def fizz_buzz(x: int):
    if x % 3 == 0 and x % 5 == 0:
        print('fizz buzz')
    elif x % 5 == 0:
        print('buzz')
    elif x % 3 == 0:
        print('fizz')
    else:
        print(x)


fizz_buzz(15)
fizz_buzz(2)
fizz_buzz(3)
fizz_buzz(5)
