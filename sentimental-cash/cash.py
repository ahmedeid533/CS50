# TODO
while (1):
    height = input("Change owed: ")
    try:
        height = float(height)
    except:
        continue
    if (height > 0):
        break
# Gready algorithm O(1)
height *= 100
coins = int(height / 25)
height %= 25
coins += int(height / 10)
height %= 10
coins += int(height / 5)
height %= 5
coins += int(height / 1)
height %= 1
print(coins)