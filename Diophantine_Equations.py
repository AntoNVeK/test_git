def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve_diophantine(a, b, c):
    gcd_ab = find_gcd(abs(a), abs(b))

    if abs(c) % gcd_ab != 0:
        return "Нет решений"

    gcd_abc = find_gcd(gcd_ab, abs(c))
    dev = c // gcd_abc

    i = 0
    arr_r = [abs(a // gcd_abc), abs(b // gcd_abc)]
    arr_q = []
    arr_x = [1, 0]
    arr_y = [0, 1]
    r_i = arr_r[-1]
    while r_i != 1:
        q_i = arr_r[-2] // arr_r[-1]
        arr_q.append(q_i)
        r_i = arr_r[-2] - q_i * arr_r[-1]
        arr_r.append(r_i)
        x_i = arr_x[-2] - arr_q[i] * arr_x[-1]
        y_i = arr_y[-2] - arr_q[i] * arr_y[-1]

        arr_x.append(x_i)
        arr_y.append(y_i)
        i += 1

    x_s = 1 if a > 0 else -1
    y_s = 1 if b > 0 else -1

    x_ch = arr_x[-1] * x_s * dev
    y_ch = arr_y[-1] * y_s * dev

    x_o = b // gcd_abc
    y_o = -a // gcd_abc

    str_x = str(x_ch)
    if x_o > 0:
        str_x += " + " + str(x_o) + " * k"
    else:
        str_x += " - " + str(abs(x_o)) + " * k"

    str_y = str(y_ch)
    if y_o > 0:
        str_y += " + " + str(y_o) + " * k"
    else:
        str_y += " - " + str(abs(y_o)) + " * k"

    print(str_x)
    print(str_y)

    k = 0

    x = x_ch + x_o * k
    y = y_ch + y_o * k

    if x > 0:
        while x > 0:
            if x_o > 0:
                k -= 1
            else:
                k += 1
            if x_ch + x_o * k > 0:
                x = x_ch + x_o * k
                y = y_ch + y_o * k
            else:
                break
    else:
        while x < 0:
            if x_o > 0:
                k += 1
            else:
                k -= 1
            x = x_ch + x_o * k
            y = y_ch + y_o * k

    return x, y

a, b, c = map(int, input().split())

result = solve_diophantine(a, b, c)

if result == "Нет решений":
    print(result)
else:
    x0, y0 = result
    print(f"{x0} {y0}")
