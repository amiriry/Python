width=int(input("original width:"))
hieght=int(input("original hieght:"))

ratio=width/hieght

base=input("calculate by h|w:")
if base not in ("w", "h"):
    print("only h or w are exceptable")
else:
    if base == 'h':
        new_hieght=int(input("new hieght:"))
        new_width = round((ratio *  new_hieght), 2)
        print("new width:",new_width)
    elif base == 'w':
        new_width=int(input("new width:"))
        new_hieght = round((new_width / ratio), 2)
        print("new hiehgt:", new_height)
    else:
        print("only h or w are acceptable")


