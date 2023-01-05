A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Rotor():
    def __init__(self, type) -> None:
        if type == "I":
            output = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            displase_key = A.index('Q')
        elif type =="II":
            output = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            displase_key = A.index('E')
        elif type == "III":
            output = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            displase_key = A.index('V')
        self.type = type
        self.displase_key = displase_key
        self.input = dict(zip((A.index(a) for a in A), (A.index(i) for i in output)))
        self.output = dict(zip((A.index(i) for i in output), (A.index(a) for a in A)))

class Mirror():
    def __init__(self, type) -> None:
        if type == "A":
            Ukw = "EJMZALYXVBWFCRQUONTSPIKHGD"
        elif type == "B":
            Ukw = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        elif type == "C":
            Ukw = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
        self.type = type
        self.input = list(A.index(u) for u in Ukw)


def cript(text = "HELLO", keys = ('A','A','A'), type_rotors = ('I','I','I'), type_mirror = 'B'):
    Rotor1 = Rotor(type_rotors[0])
    Rotor2 = Rotor(type_rotors[1])
    Rotor3 = Rotor(type_rotors[2])
    Ukw = Mirror(type_mirror)
    displace_R1 = A.index(keys[0])
    displace_R2 = A.index(keys[1])
    displace_R3 = A.index(keys[2])

    
    res = ""

    for i in text:
        if i != " ":
            if Rotor2.displase_key == displace_R2:
                displace_R3 = (displace_R3 + 1) % 26
            if Rotor1.displase_key == displace_R1:
                displace_R2 = (displace_R2 + 1) % 26

            displace_R1  = (displace_R1 + 1) % 26

            id = A.index(i)
            id = (Rotor1.input[(id + displace_R1)%26] - displace_R1 + 26)%26
            id = (Rotor2.input[(id + displace_R2)%26] - displace_R2 + 26)%26
            id = (Rotor3.input[(id + displace_R3)%26] - displace_R3 + 26)%26
            id = Ukw.input[id]
            id = (Rotor3.output[(id + displace_R3)%26] - displace_R3 + 26)%26
            id = (Rotor2.output[(id + displace_R2)%26] - displace_R2 + 26)%26
            id = (Rotor1.output[(id + displace_R1)%26] - displace_R1 + 26)%26
            res += A[id]
        else: 
            res += " "
    return res

txt = input("Введите текст: ")
print("Готово ", cript(txt))
