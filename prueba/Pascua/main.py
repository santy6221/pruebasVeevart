###### TEST 18 ######
###### TEST 18 ######
###### TEST 18 ######

from datetime import date, timedelta, datetime

def main():
    print("Ingrese el año para el cual calcular la fecha de pascua")
    year = input()
    golden_number = (int(year)%19)+1
    #epact = (11*(golden_number-1))%30
    c = int(year)//100
    #s = (3*(c+1))//4
    h = (c - (c//4) - ((13+(8*c))//25) + (19*(golden_number-1)) + 15)%30
    i = (h - (h//28)*(1 - (29//(h+1)) * (21 - (golden_number-1))//11))
    j = (int(year) + (int(year)//4) + i + 2 - c + (c//4))%7
    l = i-j
    easter_month = 3+((l+40)//44)
    easter_day = l + 28 - 31 *(easter_month//4)

    easter_date = date(int(year), easter_month, easter_day)

    print(easter_date)



if __name__ == "__main__":
    main()
