print("Ini adalah program python yang aku upload ke GitHub")
def pangkat(a: int, b: int):
    sum = 1
    for i in range(b):
        sum *= a
    return sum

print(pangkat(2, 3))
