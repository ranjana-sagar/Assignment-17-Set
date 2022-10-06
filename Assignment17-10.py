print("Enter the set elements sepreted by comman:")
x={eval(i) for i in input().split(',')}
print(x,':',max(x),'is the maximum value of x')
print(x,':',min(x),'is the minium value of x')
