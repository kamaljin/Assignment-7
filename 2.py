nn = set()

while True:
    na = input("Enter name or press enter to end : ")
    if na == "":
        break
    elif na in nn:
        print("Existing name")
    else:
        print("New name")
        nn.add(na)

print("\n names List :")
for na in nn:
    print(na)