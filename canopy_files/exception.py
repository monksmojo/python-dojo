prompt='enter  number(q to quit):'
a=input(prompt)
#num = int(a) if a!='q' else 0
try:
    num=int(a)
    print(num)
except:
    if a=='q':
        print('exciting')
    else:
        print('wrong input')        