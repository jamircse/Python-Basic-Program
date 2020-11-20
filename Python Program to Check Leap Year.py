year=int(input("Enter the year to check leaf year or Not : "));
if((year%4==0 and year%100!=0)or year%400==0):
    print(year," is a leaf year");

else:
    print(year,"  is  not leaf year");
    
