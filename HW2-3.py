season = dict =  {1 :'winter', 2 :'spring', 3 :'summer', 4 : 'autumn'}

month = int(input('ВВедите месяц от 1-12'))
if month ==1 or month ==12 or month ==2:
    print(season.get(1))
elif month ==3 or month ==4 or month ==5:
    print(season.get(2))
elif month ==6 or month ==7 or month ==8:
    print(season.get(3))
elif month ==9 or month==10 or month ==11:
    print(season.get(4))
