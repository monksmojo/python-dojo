some_var = 1
def fib(n=10):
    a,b=0,1
    while b<30:
        print(b)
        next=a+b
        a=b
        b=next   
if __name__=="__main__" :       
    fib(10)        