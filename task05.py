omonat = int(input("Omonat summasini kiriting: "))

if omonat < 100000:
    print("5%")
elif 100000 <= omonat <= 500000:
    print("7%")
else:
    print("10%")