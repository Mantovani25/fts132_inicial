import pytest


# Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2


def subtrair_dois_numeros(num1, num2):
    return num1 - num2


def multiplicar_dois_numeros(num1, num2):
    return num1 * num2


def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2


def calcular_area_do_quadrado(lado):
    return lado ** 2


def calcular_area_do_retangulo(lado1, lado2):
    return lado1 * lado2


def calcular_area_do_triangulo(lado1, lado2):
    return lado1 * lado2 / 2


def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2


if __name__ == '__main__':
    # Garçom - Requisições / Chamadas
    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')  # <-- Prato

    resultado = subtrair_dois_numeros(7, 5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(8, 5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(9, 3)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é {resultado}')

    resultado = calcular_area_do_retangulo(4, 7)
    print(f'A área do retângulo é {resultado}')

    resultado = calcular_area_do_triangulo(6, 8)
    print(f'A área do triângulo é {resultado}')

    resultado = calcular_area_do_circulo(2)
    print(f'A área do circulo é {resultado}')


    # Degustador / Teste
'''
def testar_somar_dois_numeros():
    # - 1ª Erapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saída / Output
    resultado_esperado = 17

    # - 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3ª Etapa; Confirma / Check / Valida
    assert resultado_atual == resultado_esperado
'''



