prompt="enter a number:"
while True:
    try:
        x=int(input(prompt))
        break
    except ValueError:
        print('invalid input try again')    