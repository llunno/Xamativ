import csv

class Endereco:
  def __init__(self, id, numero, rua, bairro, cidade, estado, referencia, CEP):
    self.id = id
    self.numero = numero
    self.rua = rua
    self.bairro = bairro
    self.cidade = cidade
    self.estado = estado
    self.referencia = referencia
    self.CEP = CEP

  @staticmethod
  def getFromCSV():
    todosEnderecos = []
    with open('./Enderecos.csv', 'r', encoding='utf-8') as enderecosCSV:
      reader = csv.DictReader(enderecosCSV, delimiter=',')
      for linha in reader:
        endereco = Endereco(
          linha['id'],
          linha['numero'],
          linha['rua'],
          linha['bairro'],
          linha['cidade'],
          linha['estado'],
          linha['referencia'],
          linha['CEP']
        )
        todosEnderecos.append(endereco)
    return todosEnderecos