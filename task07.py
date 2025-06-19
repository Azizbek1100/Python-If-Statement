email = input("Email manzilini kiriting: ")

if "@" in email and "." in email[email.index("@"):] and " " not in email:
    print("Email manzili to‘g‘ri")
else:
    print("Email manzili noto‘g‘ri")