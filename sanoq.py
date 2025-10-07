def binary_to_decimal(bin_str):
    total = 0
    steps = []
    for i, bit in enumerate(reversed(bin_str)):
        val = int(bit) * (2 ** i)
        total += val
        steps.append(f"{bit}×2^{i}={val}")
    print(" + ".join(reversed(steps)))
    print("Jami =", total, "_10")
    return total

def binary_to_hex(bin_str):
    pad = (-len(bin_str)) % 4
    bin_str = "0"*pad + bin_str
    groups = [bin_str[i:i+4] for i in range(0, len(bin_str), 4)]
    hex_map = {
        "0000":"0","0001":"1","0010":"2","0011":"3",
        "0100":"4","0101":"5","0110":"6","0111":"7",
        "1000":"8","1001":"9","1010":"A","1011":"B",
        "1100":"C","1101":"D","1110":"E","1111":"F"
    }
    hex_digits = [hex_map[g] for g in groups]
    print("4-bit guruhlar:", " ".join(groups))
    print("Har birining 16-lik qiymati:", " ".join(hex_digits))
    print("Natija:", "".join(hex_digits), "_16")
    return "".join(hex_digits)

def decimal_to_binary(num):
    steps = []
    n = num
    while n > 0:
        steps.append(str(n % 2))
        print(f"{n} ÷ 2 = {n//2}, qoldiq = {n%2}")
        n //= 2
    binary = "".join(reversed(steps)) or "0"
    print("Natija:", binary, "_2")
    return binary

def decimal_to_hex(num):
    steps = []
    n = num
    hex_chars = "0123456789ABCDEF"
    while n > 0:
        steps.append(hex_chars[n % 16])
        print(f"{n} ÷ 16 = {n//16}, qoldiq = {hex_chars[n%16]}")
        n //= 16
    hex_num = "".join(reversed(steps)) or "0"
    print("Natija:", hex_num, "_16")
    return hex_num

def hex_to_decimal(hex_str):
    hex_str = hex_str.upper()
    hex_chars = "0123456789ABCDEF"
    total = 0
    steps = []
    for i, ch in enumerate(reversed(hex_str)):
        val = hex_chars.index(ch)
        total += val * (16 ** i)
        steps.append(f"{ch}×16^{i}={val * (16 ** i)}")
    print(" + ".join(reversed(steps)))
    print("Jami =", total, "_10")
    return total

def hex_to_binary(hex_str):
    hex_str = hex_str.upper()
    hex_map = {
        "0":"0000","1":"0001","2":"0010","3":"0011",
        "4":"0100","5":"0101","6":"0110","7":"0111",
        "8":"1000","9":"1001","A":"1010","B":"1011",
        "C":"1100","D":"1101","E":"1110","F":"1111"
    }
    binaries = [hex_map[c] for c in hex_str]
    print("Har bir belgining 2-lik qiymati:", " ".join(binaries))
    result = "".join(binaries)
    print("Natija:", result, "_2")
    return result

def main():
    print("=== Sanoq tizimlari o‘giruvchi dastur ===")
    num = input("Sonni kiriting: ").strip()
    print("Qaysidan qaysiga o‘girmoqchisiz?")
    print("1) 2 → 10")
    print("2) 2 → 16")
    print("3) 10 → 2")
    print("4) 10 → 16")
    print("5) 16 → 10")
    print("6) 16 → 2")
    tanlov = input("Tanlov raqamini kiriting (1-6): ")

    if tanlov == "1":
        binary_to_decimal(num)
    elif tanlov == "2":
        binary_to_hex(num)
    elif tanlov == "3":
        decimal_to_binary(int(num))
    elif tanlov == "4":
        decimal_to_hex(int(num))
    elif tanlov == "5":
        hex_to_decimal(num)
    elif tanlov == "6":
        hex_to_binary(num)
    else:
        print("Xato tanlov!")

if __name__ == "__main__":
    main()
