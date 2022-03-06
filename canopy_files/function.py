def f(x):
    return x*x

print(f(4))
print(f(1+2j))

## second function to print
def greet():
    print("hello world \n bye ")
        
        
print(greet())        


## third function to print
def avg(a,b):
    x=(a+b)/2
    return(x)
 
print("the average is",avg(2,2)) 


## fourth function
def circle(r):
    pi=3.14
    area=pi*r*r
    perimeter= 2*pi*r
    return (area,perimeter)

print("area and perimeter ",circle(2))
s='hello'
print(s.split(','))


## fifth function

def welcome(greet,name):
    print(greet,name)

welcome("hello","james")
welcome("hi",name="world")
welcome(name="world",greet="holla")
### welcome(greet="bonjour","bella") non keyword argument after keyword argument not accepted   


## 6th function

def change(n):
   n=5
   print(n)
   
print(change(1))## variable is local

## 7th function
n=3
def change():
    n=10
    print(n)

change()

n=15
def change():
    n=10
    print(n)
change()
print (n)

name =['mr.','steve','gosling']
def change_name(x):
    x=[1,2,3]
    print(x,'in change')
    
change_name(name)
print(name)
    
def change1_name(x):
    x[0]='dr'
    print(x,'in change1')
    
change1_name(name)
print(name)      

        
def what(n):## for perfect square
    i=1
    while i*i <n:
        i+=1
    return i*i==n,i
    
print("the no is",what(16))

    
def what1(x,n):
    if n<0:
        n=-n
        x=1.0/x
        
    z=1.0
    while n>0:
        if n%2==1:
            z*=x
        x*=x
        n=n//2
    return z
             
print(what1(2,3))


def f(x):
        def g(x):
            return x+1
    
        return g(x)**2                    
        
def f():
    def g(x):
        return x+1
    return g


func=f()
print(func(1))
f()(1)         



def prompt():
    name=input()
    print("Hello ",name)
    
prompt()    
        
                
                                                            
                                            
                
                
                