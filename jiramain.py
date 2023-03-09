"""Este código é um chatbot que responde à entrada do usuário. 
Ele usa o módulo "long_responses" importado para armazenar respostas mais longas e o módulo "re" para dividir a entrada do usuário em palavras individuais. 
A função "message_probability" calcula a porcentagem de palavras em uma mensagem do usuário que correspondem às palavras reconhecidas, e a função "check_all_messages" verifica todas as mensagens predefinidas e retorna aquela com a maior probabilidade. 
A função "get_response" é usada para obter uma resposta do chatbot e chama ambas as funções. Finalmente, há um loop while que permite aos usuários interagir com o chatbot."""


import re
import long_responses as long
import os
import pwd
import io

username1 = input(str("Olá, como devo lhe chamar ? \n > "))
username = username1 +": "
print("Ola \033[1;31m", username1, "\033[0;0m!", "Seja bem vindo ao JiraBot!\nFaça uma pergunta para iniciar.")

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Conta quantas palavras estão presentes em cada mensagem predefinida
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calcula a porcentagem de palavras reconhecidas em uma mensagem do usuário
    percentage = float(message_certainty) / float(len(recognised_words))

    # Verifica se as palavras necessárias estão na string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Deve ter as palavras necessárias ou ser uma única resposta
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifica a criação da resposta / adiciona ao dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #respostas -------------------------------------------------------------------------------------------------------
    response('Ola! Bem Vindo ao JiraBot', ['ola', 'Oi', 'Oii', 'oi', 'hey', 'Oie','Bom', 'Boa', 'bom', 'boa', 'Dia','dia','Tarde','tarde','noite','Noite'], single_response=True)
    response('Ate logo!', ['sair','quit','exit','Sair','tchau', 'ate','abraco','vemos','xau','falou','flw'],single_response=True)
    response('Estou bem e voce?', ['como', 'tudo', 'voce', 'esta','tudo bem','Tudo bem','bem','Bem'], required_words=['tudo', 'bem'])
    response('Por nada!', ['obrigado', 'muito obrigado','grato','vlw','valeu','tmj'], single_response=True)
    response('Otimo! Vamos la! O que posso ajudar?', ['estou', 'bem'], required_words=['estou'])
    #response('Sinto muito, espero que melhore logo! De qualquer forma, vamos la! O que posso ajudar?', ['estou', 'mal','triste','doente'], required_words=[''])
    response('Posso sim! Insira a pergunta que eu vou te ajudar!', ['pode', 'ajudar','me'], required_words=['pode','ajudar'])
    response('Tudo bem! Insira a pergunta que eu vou armazena-la e aprende-la!', ['tentar', 'novamente', 'perguntar'], required_words=['tentar','perguntar'])

    # Respostas mais longas
    response(long.R_INTROJIRA1, ['jira', 'que', 'e'], required_words=['que', 'e', 'jira'])
    response(long.R_INTROJIRA2, ['configurar', 'jira', 'Jira', 'como'], required_words=['configurar'])
    response(long.R_INTROJIRA3, ['novo', 'projeto', 'jira'], required_words=['novo', 'projeto'])
    response(long.R_INTROJIRA4, ['quais', 'principais', 'funcionalidades'], required_words=['principais', 'funcionalidades'])
    response(long.R_INTROJIRA5, ['como', 'gerenciar', 'tarefas'], required_words=['gerenciar', 'tarefas'])
    response(long.R_INTROJIRA6, ['recursos', 'relatorio', 'jira'], required_words=['recursos', 'relatorio'])
    response(long.R_INTROJIRA7, ['melhores', 'praticas', 'jira'], required_words=['melhores', 'praticas'])  
    response(long.R_INTROJIRA8, ['personalizar', 'layout'], required_words=['personalizar', 'layout'])
    response(long.R_INTROJIRA9, ['principais', 'plugins', 'jira'], required_words=['plugins'])
    response(long.R_INTROJIRA10, ['integrar', 'outras', 'ferramentas'], required_words=['integrar', 'ferramentas'])
    response(long.R_INTROJIRA11, ['principais', 'recursos', 'seguranca'], required_words=['recursos', "seguranca"])
    response(long.R_INTROJIRA12, ['finalidade', 'jira', 'software'], required_words=['finalidade', 'jira'])
    response(long.R_INTROJIRA13, ['util', 'equipe', 'jira', 'minha'], required_words=['util', 'equipe'])
    response(long.R_INTROJIRA14, ['recursos', 'jira', 'software'], required_words=['recursos', 'jira'])
    response(long.R_INTROJIRA15, ['diferencas', 'outras', 'ferramentas'], required_words=['diferencas', 'outras', 'ferramentas', 'jira'])
    response(long.R_INTROJIRA16, ['custo', 'jira', 'software'], required_words=['custo', 'jira'])
    response(long.R_INTROJIRA17, ['opcoes', 'integracao', 'jira', 'software'], required_words=['opcoes', 'integracao'])
    response(long.R_INTROJIRA18, ['instalar', 'configurar', 'jira'], required_words=['instalar', 'configurar'])
    response(long.R_INTROJIRA19, ['importar', 'dados', 'para', 'jira'], required_words=['importar', 'dados'])
    response(long.R_INTROJIRA20, ['exportar', 'dados', 'para', 'jira'], required_words=['exportar', 'dados'])
    response(long.R_INTROJIRA21, ['api', 'jira', 'tem'], required_words=['api', 'jira'])


    #Local para perguntas mais longas desenvolvidas por pessoas
    #-
    #-

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Usado para obter a resposta
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    if check_all_messages(split_message) == "Ate logo!":
        print("Obrigado por utilizar o JiraBot. ", check_all_messages(split_message))
        exit()
    with io.open("perguntas_novas.txt", "a", encoding="utf-8") as f: #cria o arquivo para armazenar as pergunta feitas pelo usuário
        f.write(user_input + "\n")  # adiciona uma nova linha depois de cada entrada
    return response

# Testando o sistema de resposta
while True:
    print('\033[1;34mJiraBot: \033[0;0m' + get_response(input( "\033[1;31m" + username + "\033[0;0m")))


