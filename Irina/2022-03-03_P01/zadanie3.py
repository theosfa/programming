a = int(input("Input A :"))
b = int(input("Input B :"))
c = int(input("Input C :"))

if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie nieznaczone")
        else:
            print("Równanie sprzecne")
    else:
        print(f"Równanie liniowe x = {-c/b}")
else:
    delta = b*b - 4*a*c
