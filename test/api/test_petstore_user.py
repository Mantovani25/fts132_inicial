# Bibliotecas
import pytest  # Framework de Teste Unitário - Engine
import requests  # Framework de Teste de API - Requests / Responses

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'aplication/json'}


# Os testes
def testar_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = "1008"

    # Executa
    resposta = requests.post(  # Faz a requisição, passando:
        url=base_url,  # O endpoint da API
        data=open('C:/Users/jmvma/PycharmProjects/fts132_inicial/test/db/user1.json', 'rb'),  # O body Jsom
        headers=headers  # O header com o Content-Type
    )

    # Formatação
    corpo_da_resposta = resposta.json()  # Formata como JSON
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
    # Configura
    status_code = 200
    id = 1008
    username = 'stevemaster'
    firstName = 'steve'
    lastName = 'stifler'
    email = 'steve.stifler@teste.com'
    password = '123456'
    phone = '11986390745'
    userStatus = 0

    # Executa
    resposta = requests.get(
        #
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Formatação
    corpo_da_resposta = resposta.json()  # Formata como JSON
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone


def testar_alterar_usuario():
    # Configura
    username = 'stevemaster'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1008'

    # Executa
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C:/Users/jmvma/PycharmProjects/fts132_inicial/test/db/user2.json', 'rb'),
        headers=headers
    )

    # Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    # Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_excluir_usuario():
    # Configura
    username = 'stevemaster'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'stevemaster'

    # Executa
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Formatação

    match resposta.status_code:
        case 200:
            corpo_da_resposta = resposta.json()
            print(resposta)
            print(resposta.status_code)
            print(corpo_da_resposta)

            # Validação
            assert resposta.status_code == status_code_esperado
            assert corpo_da_resposta['code'] == codigo_esperado
            assert corpo_da_resposta['type'] == tipo_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada

        case 400:
            print('username fornecido incorretamente!')

        case 404:
            print('usuário não encontrado!')


