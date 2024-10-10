print("welcom to place the raabit\n")
filde=[[ "'🍀'" , "'🍀'" , "'🍀'" ],[ "'🍀'" , "'🍀'" , "'🍀'" ],[ "'🍀'" , "'🍀'" , "'🍀'" ]]
print(f"{filde[0]}\n,{filde[1]}\n,{filde[2]}\n")
print("where shoulde the rabbit go ?🐇")
posation=input("please choose a row an column")
row=int(posation[0])
colume=int(posation[1])
filde[row-1][colume-1]="🐇"
print("\n succes ........")
print(f"{filde[0]}\n,{filde[1]}\n,{filde[2]}\n")1




