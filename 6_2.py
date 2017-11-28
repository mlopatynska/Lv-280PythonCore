n = int(input())
x = int(input())
y = int(input())
z = int(input())
part1,part2,part3=0.0,0.0,0.0
a,b,c=[],[],[]
for g in range (1,n+2):
    a.append(g)
    b.append(g)
    c.append(g)
for d in range (0,n):
    
    part1+=(round(a[d]*(x**(n+1-d)),10))
part1=part1**2
    
for m in range (0,n):
    
    part2+=(round(b[m]*(y**(n+1-m)),10))

for q in range (0,n):
    part3+=(round(c[q]*((x+z)**(n+1-q)),10))
res=(part1-part2)/part3
res=round(res,2)
print(res)