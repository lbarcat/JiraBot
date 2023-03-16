
from jiramain import *
from long_responses import *

username1 = input(str("Olá, como devo lhe chamar ? \n > "))
username = username1 +": "
print("Ola \033[1;31m", username1, "\033[0;0m!", "Seja bem vindo ao JiraBot!\nFaça uma pergunta para iniciar.")
# Testando o sistema de resposta
while True:
    print('\033[1;34mJiraBot: \033[0;0m' + get_response(input( "\033[1;31m" + username + "\033[0;0m")))
