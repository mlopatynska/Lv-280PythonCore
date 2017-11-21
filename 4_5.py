k=(int(input("Day :")))
week = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
if k > 7:
    k=k%7
print(week[k])