def multiplay(value):
    v1 = value
    def inter_f(mul):
        print(f"Умножение {v1} на {mul} =", v1* mul)
    return inter_f
f_2 = multiplay(2)
f_2(5)

