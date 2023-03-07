import pytest

from main import somar_dois_numeros, calcular_area_do_circulo, multiplicar_dois_numeros, \
    calcular_volume_do_paralelograma


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
# anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio,resultado_esperado',[
    # valores
                             (1,3.14),   # teste n°1
                             (2,12.56),  # teste n°2
                             (3,28.26),  # teste n°3
                             (4,50.24),  # teste n°4
                             ('a', 'Falha no calculo - raio não é um número'),  # teste n°5
                             (' ', 'Falha no calculo - raio não é um número')   # teste n°6
                         ])
def testar_calcular_area_do_circulo(raio, resultado_esperado):
    #raio = 2
    #resultado_esperado = 12.56
    resultado_atual = calcular_area_do_circulo(raio)
    assert resultado_atual == resultado_esperado

def testar_calcular_volume_do_paralelograma():
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)
    assert resultado_atual == resultado_esperado




    
