week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
s = input("enter day of week ")
a = s.lower()
if a[:3] in week:
    print(True)
else:
    print(False)
    
