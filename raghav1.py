n=input("Enter Expression \n =>") # a=b+c*23-56^2
total_token,var,operater,const = 0,0,0,0
for i in range(len(n)):
    if n[i].isalpha():
        var+=1
    elif ord(n[i]) == ord('+') or ord(n[i]) == ord('-') or ord(n[i]) == ord('^') or ord(n[i]) == ord('=') or ord(n[i]) == ord('/') or ord(n[i]) == ord('*') :
        operater+=1
    elif n[i].isnumeric():
        if n[i-1].isnumeric():
            pass
        else:
            const+=1
print(f"operators = {operater}\nvariables = {var}\nConstant = {const}")
print(f"total Tokens = {operater+var+const}")
