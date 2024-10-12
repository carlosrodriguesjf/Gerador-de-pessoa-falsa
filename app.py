### GERADOR DE PESSOA FALSA ###

# importações
from faker import Faker

# instanciando a variável
fake = Faker('pt_BR')

# 1. Geração de Nome Completo:
nome = fake.name()

# 2. Geração de CPF Falso:
cpf = fake.cpf()

# 3. Geração de E-mail:
email = fake.email( domain = 'warmup.br')

# 4. Geração de Endereço Completo:
endereco = fake.address()

# 5. Geração de Número de Telefone:
telefone = fake.phone_number()

# 6. Exibição de Todos os Dados:
print(f'Nome: {nome}')
print(f'CPF: {cpf}')
print(f'E-mail: {email}')
print(f'Endereço: {endereco}')
print(f'Telefone: {telefone}')