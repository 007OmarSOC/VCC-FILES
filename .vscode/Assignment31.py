hrs =  input("Enter Hours")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
if h > 40:
    x = (r*1.5)*(h-40)+(40*r)
if h <= 40:
    x = (h*r)
xxr = float(x)
print(xxr) 