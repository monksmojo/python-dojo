'''f=open('pendulum.txt')
f.close()
for line in open ('pendulum.txt'):
    print(line)
    line_list=[]
    
for line in fopen('pendulum.tx'):
    line_list.append'''
    
'''f=open('hello_file.txt','w')
f.write('hello world\n')
f.close()

f=open('hello hell!.txt','w')
print("hello world", file=f)
f.close()

line="parse this     string"
line.split()
print(line.split())
r="a;01;jose r;083"
print(r.split(';'))

mark_str="1.25"
mark = float(mark_str)
print(type(mark))
print(type(mark_str))'''

math_b=[]
for line in open('sscl.txt'):
    field=line.split(";")
    reg_code=field[0]
    reg_code=reg_code.strip()
    
    math_mark_str=field[5]
    math_mark=float(math_mark_str)
    
if reg_code =="B":
    math_B.appemd(math_mark)

math_B=sum(math_B)/len(math_B)
print(math_B_mean)                
    
                        
