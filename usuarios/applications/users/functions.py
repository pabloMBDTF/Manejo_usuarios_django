import random
import string

# def generarCodigo():
#     codigo = random.randint(100000, 999999)
#     codigo_str = str(codigo)
#     return codigo_str

def codeGenerator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))