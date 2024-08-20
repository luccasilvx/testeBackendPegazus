#Novidade! Atalhos do teclado … Os atalhos de teclado do Drive foram atualizados para oferecer navegação por letras iniciais
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

#lista para armazenar produtos filtrados
produtosExtraidos = []
#percorre loja na lista 'response'
for loja in response:
    #percorre cada produto na lista de produtos
    for produto in loja["produtos"]:
        #verifica  a condição do preço
        if produto["preço"]>30.00:
            #inclui a lista de produtos extraídos
            produtosExtraidos.append(produto)
print(produtosExtraidos)




#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

#percorre sobre a lista de produtos
for produto in responsejson["produtos"]:
    #verifica o nome do produto
    if produto["nome"] == "Produto B":
        print(produto["preço"])


#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

#utilizando a função sorted preservando a lista
listaCrescente = sorted(lista)
print(listaCrescente)




#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]

#utilizando uma list comprehension para uma nova lista com a função '.strip' para retirar os espaçõs em branco
retirarEspacos = [nome.strip() for nome in lista]
print(retirarEspacos)


#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

#removendo pelo índice
del lista[1]
print(lista)


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

#sequência de indices 
for i in range(len(lista)):
    #verifica o nome e substitui
    if lista[i]=="joão":
        lista[i]="maria"
print(lista)

#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

#cria a lista
lista = ["objeto 1","objeto 2","objeto 3", "objeto 4", "objeto 5"]
num = 1
#percorre a lista 
while num <= 5 and num <= len(lista):
    #imprime enquanto o valor for menor igual a 5
    print(lista[num-1])
    #iterando 1 na variavel
    num += 1

#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

import requests

def contagemTasks():

    #requisicão get ao endpoint
    url = "https://jsonplaceholder.typicode.com/todos"
    resposta = requests.get(url)

    #verifica se foi bem sucedida
    if resposta.status_code ==200:
        #converte o retorno em json
        dados=resposta.json()

        completo = 0
        pendente = 0

        #percorre cada tarefa na lista de dados
        for tarefa in dados:
            if tarefa["completed"]:
                completo += 1
            else:
                pendente += 1

        return completo, pendente
    else:
        #caso o retorno não seja 200, retorna exceção com erro
        raise Exception("Erro na requisição: Status code {}".format(resposta.status_code))

completadas, pendentes = contagemTasks()
print(f"Tarefas completadas: {completadas}")
print(f"Tarefas pendentes: {pendentes}")

#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra


import requests

def dadosUsuarios():
    #requisicão get ao endpoint
    url = "https://jsonplaceholder.typicode.com/users"
    resposta = requests.get(url)
    
    #verifica se foi bem sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        
        #criação de lista
        usuarios_info = []
        
        #percorre os usuários
        for usuario in dados:
            #dicionário com informações extraídas do JSON
            info_usuario = {
                "nome": usuario["name"],
                "username": usuario["username"],
                "email": usuario["email"],
                "rua": usuario["address"]["street"],
                "numero": usuario["address"]["suite"]
            }
            usuarios_info.append(info_usuario)
        
        return usuarios_info
    else:
        #caso o retorno não seja 200, retorna exceção com erro
        raise Exception(f"Erro na requisição: Status code {resposta.status_code}")

usuarios = dadosUsuarios()
for usuario in usuarios:
    print(usuario)

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

fila = []

#adiciona na fila
fila.append("Item 1")  # Adiciona Item 1
fila.append("Item 2")  # Adiciona Item 2
fila.append("Item 3")  # Adiciona Item 3

print("Fila após adição de itens:", fila)

#removendo da fila 
item_removido = fila.pop(0) #remove o mais antigo

print("Item removido:", item_removido)
print("Fila após remoção de um item:", fila)


#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

pilha = []

#adicionando
pilha.append("Item A")
pilha.append("Item B")
pilha.append("Item C")

print("Pilha após adição de itens:", pilha)

#removendo
item_removido = pilha.pop()  #remove o mais recente

print("Item removido:", item_removido)
print("Pilha após remoção de um item:", pilha)


#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

class ContaBancaria:
    _id_counter = 1  #auto-incremental
    
    #criação do construtor
    def __init__(self, nome, cpf):
        self.id = ContaBancaria._id_counter
        ContaBancaria._id_counter += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
    
    #':.2f' utilizado para apenas 2 casa decimais flutuantes 
    def depositar(self, valor):
        "Deposita valor na conta"
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        "Saca valor da conta"
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def exibir_saldo(self):
        "Exibe saldo atual da conta"
        print(f"Saldo atual: R${self.saldo:.2f}")
    
    #representa a conta como uma string de acordo com os detalhes da conta
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, CPF: {self.cpf}, Saldo: R${self.saldo:.2f}"

#método principal
def main():
    print("Criando conta...")
    conta1 = ContaBancaria("João Silva", "123.456.789-00")
    conta2 = ContaBancaria("Maria Oliveira", "987.654.321-00")
    
    conta1.depositar(500)
    conta1.exibir_saldo()
    conta1.sacar(200)
    conta1.exibir_saldo()
    
    #saque com saldo insuficiente
    conta1.sacar(400)
    
    #operações na segunda conta
    conta2.depositar(1000)
    conta2.exibir_saldo()
    conta2.sacar(300)
    conta2.exibir_saldo()

if __name__ == "__main__":
    main()









