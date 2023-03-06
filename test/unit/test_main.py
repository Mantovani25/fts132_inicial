import pytest

from main import somar_dois_numeros, calcular_area_do_circulo


def testar_somar_dois_numeros():
    # - 1ª Erapa: Configura / Prepara / valores de entrada e saída
    # Dados / Valores
    # Entrada / Input
    num1 = 4
    num2 = 5
    # Saída / Output
    resultado_esperado = 9

    # - 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3ª Etapa; Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_circulo():
    raio = 2
    resultado_esperado = 12.56
    resultado_atual = calcular_area_do_circulo(raio)
    assert resultado_atual == resultado_esperado




    
