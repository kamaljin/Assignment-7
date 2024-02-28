mm = int(input("number of a month: "))

ss = ("winter", "spring", "summer", "autumn")

if mm in (12, 1, 2):
    kk = ss[0]
elif mm in (3, 4, 5):
    kk = ss[1]
elif mm in (6, 7, 8):
    kk = ss[2]
elif mm in (9, 10, 11):
    kk = ss[3]
else:
    kk = "Invalid number"

print("The season is:", kk)