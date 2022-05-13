input= "consultadd"
output= "CNSLTDD"
out=""
input=str.upper(input)
print(input)
vow=['A','E','I','O','U']
for i in range(len(input)):
    if input[i]  in vow:
        pass
    else:
        out= out+input[i]
print(out)