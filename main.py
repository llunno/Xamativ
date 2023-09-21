from fastapi import FastAPI
from domain.Endereco import Endereco
from domain.Departamento import Departamento
from domain.Usuario import Usuario
from domain.Chamado import Chamado
from domain.Fornecedor import Fornecedor
from domain.Ativo import Ativo
import subprocess
import gerenciarDados
import sysInfo

#subprocess.run("pymake -i -s dev", shell=True)

# Gerar dados CSV
gerenciarDados.gerarArquivosCSV()

# Obter dados CSV para objetos
todosUsuarios = Usuario.getFromCSV()
todosChamados = Chamado.getFromCSV()
todosDepartamentos = Departamento.getFromCSV()
todosEnderecos = Endereco.getFromCSV()
todosFornecedores = Fornecedor.getFromCSV()
todosAtivos = Ativo.getFromCSV()

# Gerar tabelas SQL e inserir objetos
gerenciarDados.gerarTabelasSQL()
gerenciarDados.insertObjectsInSQLTables(todosUsuarios, todosChamados, todosDepartamentos, todosEnderecos, todosFornecedores, todosAtivos)

app = FastAPI()

# Default root endpoint
@app.get("/")
async def root():
  print(sysInfo.mostrarMemoria())
  return {"message": "Hello world"}


@app.get("/usuarios")
async def getTodosUsuarios():
  usuarios_departamentos = gerenciarDados.getUsuarios_Departamentos()
  print(sysInfo.mostrarMemoria()) 
  return usuarios_departamentos

@app.get("/chamados")
async def getTodosChamados():
  todosChamados = gerenciarDados.getChamados()
  print(sysInfo.mostrarMemoria())
  return todosChamados

@app.get("/enderecos")
async def getTodosEnderecos():
  todosEnderecos = gerenciarDados.getEnderecos()
  print(sysInfo.mostrarMemoria())
  return todosEnderecos

@app.get("/ativosfornecedores")
async def getTodosAtivos():
  ativos_fornecedores = gerenciarDados.getAtivos_Fornecedores()
  print(sysInfo.mostrarMemoria())
  return ativos_fornecedores

@app.get("/ativos")
async def getTodosAtivosSeparados():
  ativos = gerenciarDados.getAtivos()
  print(sysInfo.mostrarMemoria())
  return ativos

@app.get("/fornecedores")
async def getFornecedoresSeparados():
  fornecedores = gerenciarDados.getFornecedores()
  print(sysInfo.mostrarMemoria())
  return fornecedores

@app.get("/ativosfornecedoresdetatched")
async def getRelationAtivosFornecedores():
  ativos_fornecedores = gerenciarDados.getAtivosFornecedoresDetatched()
  print(sysInfo.mostrarMemoria())
  return ativos_fornecedores

@app.get("/memoria")
async def obterStatusMemoria():
  dictMemoria = {'memoria':sysInfo.mostrarMemoria()}
  print(sysInfo.mostrarMemoria())
  return dictMemoria
