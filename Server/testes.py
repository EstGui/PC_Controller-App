import ctypes, subprocess

def atalho(a, b=""):
    keys = {
        "Backspace": 0x08,
        "Tab": 0x09,
        "Shift": 0x10,
        "Ctrl": 0x11,
        "Alt": 0x12,
        "CapsLock": 0x14,
        "Space": 0x20,
        "PgUp": 0x21,
        "PgDn": 0x22,
        "End": 0x23,
        "Home": 0x24,
        "Esquerda": 0x25,
        "Cima": 0x26,
        "Direita": 0x27,
        "Baixo": 0x28,

        "0": 0x30,
        "1": 0x31,
        "2": 0x32,
        "3": 0x33,
        "4": 0x34,
        "5": 0x35,
        "6": 0x36,
        "7": 0x37,
        "8": 0x38,
        "9": 0x39,

        "A": 0x41,
        "B": 0x42,
        "C": 0x43,
        "D": 0x44,
        "E": 0x45,
        "F": 0x46,
        "G": 0x47,
        "H": 0x48,
        "I": 0x49,
        "J": 0x4A,
        "K": 0x4B,
        "L": 0x4C,
        "M": 0x4D,
        "N": 0x4E,
        "O": 0x4F,
        "P": 0x50,
        "Q": 0x51,
        "R": 0x52,
        "S": 0x53,
        "T": 0x54,
        "U": 0x55,
        "V": 0x56,
        "W": 0x57,
        "X": 0x58,
        "Y": 0x59,
        "Z": 0x5A,

        "Win": 0x5B,
        "Enter": 0x0D,
        "Próximo": 0xB0,
        "Anterior": 0xB1,
        "Play/Pause": 0xB3,
    }

    if b != "":
        ctypes.windll.user32.keybd_event(keys[a], 0, 0, 0)
        ctypes.windll.user32.keybd_event(keys[b], 0, 0, 0)
        ctypes.windll.user32.keybd_event(keys[a], 0, 2, 0)
        ctypes.windll.user32.keybd_event(keys[b], 0, 2, 0)
    else:
        ctypes.windll.user32.keybd_event(keys[a], 0, 0, 0)
        ctypes.windll.user32.keybd_event(keys[a], 0, 2, 0)

