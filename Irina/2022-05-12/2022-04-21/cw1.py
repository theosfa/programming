month = ["January\n", "February\n", "March\n", "April\n", "May\n", "June\n", "July\n", "August\n", "September\n", "October\n",
         "November\n", "December\n"]

dane = open("dane_c1.txt", "w+")
for i in range(0, 11):
    dane.write(month[i])

dane = open("dane_c1.txt", "r")
for k in dane:
    if 'M' in k.rstrip():
        print(k.rstrip())

dane = open("dane_c1.txt", "r")
wyniki = open("wyniki_c1.txt", "w")
for k in dane:
    if len(k.rstrip()) > 7:
        wyniki.write(k)
dane.close()
wyniki.close()

input()
