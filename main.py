from endereco import Endereco

data = Endereco('59082310')

print(data.mensagem())

print(data.total())

print(data.resultados())

print(data.resultados()[0]['uf'])
print(data.resultados()[0]['localidade'])
print(data.resultados()[0]['locNoSem'])
print(data.resultados()[0]['locNu'])
print(data.resultados()[0]['localidadeSubordinada'])
print(data.resultados()[0]['logradouroDNEC'])
print(data.resultados()[0]['logradouroTextoAdicional'])
print(data.resultados()[0]['logradouroTexto'])
print(data.resultados()[0]['baiNu'])
print(data.resultados()[0]['nomeUnidade'])
print(data.resultados()[0]['cep'])
print(data.resultados()[0]['tipoCep'])
print(data.resultados()[0]['numeroLocalidade'])
print(data.resultados()[0]['situacao'])
print(data.resultados()[0]['faixasCaixaPostal'])
print(data.resultados()[0]['faixasCep'])
