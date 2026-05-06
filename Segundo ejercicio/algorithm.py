myArray = [0,1, 5, 3, 0, 0,0, 3, 6, 4, 6, 8, 5, 0, 1,2,3,4,4,0,0,1,0,0]
resultado = []
buffer_ = []
was_zero = False

for v in myArray:
    if v == 0:
        if buffer_:
            resultado.append("".join(map(str, sorted(buffer_))))
            buffer_ = []
        elif was_zero:
            resultado.append("X")
        was_zero = True
    else:
        buffer_.append(v)
        was_zero = False

if buffer_:
    resultado.append("".join(map(str, sorted(buffer_))))

print(" ".join(resultado))
