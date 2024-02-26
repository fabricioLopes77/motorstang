import requests
import json

def consulta_cnpj(cnpj):

    url=f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"Xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","cnpj":"0699059000123","plugin":"RF"}

    response = requests.request("GET", url, params=querystring)
    resp = json.loads(response.text)
    
    #print(resp['nome'])
    #print(response.text)
    
    return resp['situacao'],resp['nome'],resp['porte'],resp['logradouro'],resp['numero'],resp['municipio'],resp['bairro'],resp['uf'],resp['cep'],resp['email'],resp['telefone'],resp['status']
#teste = consulta_cnpj('45016964000166')
#teste = consulta_cnpj('06698091000590')
#teste = consulta_cnpj('11325330000173')
#teste = consulta_cnpj('06698091000590')
#print(teste)