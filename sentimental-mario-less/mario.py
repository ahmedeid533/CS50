# TODO print mario blocks


while (1):
    height = input("Height: ")
    if (not height.isdigit()):
        continue
    height = int(height)
    if (height > 0 and height <= 8 ):
        break


for  i in range(height):
    i += 1
    print((" " * (height - i)) + "#" * i)