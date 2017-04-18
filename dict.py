
dict1={'a':1,'b':0,'c':3}
print(dict1.values())
print(sorted(dict1.items(),key=lambda dict1:dict1[1]))
print([v for v in sorted(dict1.values())])