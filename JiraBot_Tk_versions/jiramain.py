"""Este código é um chatbot que responde à entrada do usuário. 
Ele usa o módulo "long_responses" importado para armazenar respostas mais longas e o módulo "re" para dividir a entrada do usuário em palavras individuais. 
A função "message_probability" calcula a porcentagem de palavras em uma mensagem do usuário que correspondem às palavras reconhecidas, e a função "check_all_messages" verifica todas as mensagens predefinidas e retorna aquela com a maior probabilidade. 
A função "get_response" é usada para obter uma resposta do chatbot e chama ambas as funções. Finalmente, há um loop while que permite aos usuários interagir com o chatbot."""


import re
import long_responses as long
#import os #inativos
#import pwd #inativos
import io

#username1 = input(str("Olá, como devo lhe chamar ? \n > "))
#username = username1 +": "
#print("Ola \033[1;31m", username1, "\033[0;0m!", "Seja bem vindo ao JiraBot!\nFaça uma pergunta para iniciar.")


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
    response('Ate logo!', ['sair','quit','exit','Sair','tchau', 'ate','abraco','vemos','xau','falou','flw'], single_response=True)
    response('Estou bem e voce?', ['como', 'tudo', 'voce', 'esta'], required_words=['tudo', 'bem'])
    response('Por nada!', ['obrigado', 'muito obrigado'], single_response=True)
    response('Otimo! Vamos la! O que posso ajudar?', ['estou', 'bem'], required_words=['estou'])
    response('Posso sim! Insira a pergunta que eu vou te ajudar!', ['pode', 'ajudar', 'duvida'], required_words=['pode','ajudar'])
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
    response(long.R_INTROJIRA22, ['personalizar', 'jira', 'equipe'], required_words=['personalizar', 'jira'])
    response(long.R_INTROJIRA23, ['criar', 'projetos', 'jira'], required_words=['criar', 'projetos'])
    response(long.R_INTROJIRA24, ['criar', 'tarefas', 'jira'], required_words=['criar', 'tarefas'])
    response(long.R_INTROJIRA25, ['atribuir', 'tarefas', 'jira'], required_words=['atribuir', 'tarefas'])
    response(long.R_INTROJIRA26, ['definir', 'prazos', 'jira'], required_words=['definir', 'prazos'])
    response(long.R_INTROJIRA27, ['rastrear', 'progresso', 'projeto', 'jira'], required_words=['progresso', 'projeto'])
    response(long.R_INTROJIRA28, ['gerenciar', 'equipes', 'jira'], required_words=['gerenciar', 'equipes'])
    response(long.R_INTROJIRA29, ['definir', 'papeis', 'permissoes', 'jira'], required_words=['definir', 'papeis', 'permissoes'])
    response(long.R_INTROJIRA30, ['criar', 'workflows', 'jira'], required_words=['criar', 'workflows'])
    response(long.R_INTROJIRA31, ['personalizar', 'workflows', 'jira'], required_words=['personalizar', 'workflows'])
    response(long.R_INTROJIRA32, ['configurar', 'fluxos', 'trabalho', 'jira'], required_words=['configurar', 'fluxos', 'trabalho'])
    response(long.R_INTROJIRA33, ['configurar', 'campos', 'personalizados', 'jira'], required_words=['configurara', 'campos', 'personalizados'])
    response(long.R_INTROJIRA34, ['configurar', 'telas', 'jira'], required_words=['configurar', 'telas'])
    response(long.R_INTROJIRA35, ['configurar', 'notificacoes', 'jira'], required_words=['configurar', 'notificacoes'])
    response(long.R_INTROJIRA36, ['definir', 'prioridades', 'jira'], required_words=['definir', 'prioridades'])
    response(long.R_INTROJIRA37, ['gerenciar', 'sprints', 'jira'], required_words=['gerenciar', 'sprints'])
    response(long.R_INTROJIRA38, ['configurar', 'relatorios', 'jira'], required_words=['configurar', 'relatorios'])
    response(long.R_INTROJIRA39, ['usar', 'paineis', 'jira'], required_words=['usar', 'paineis'])
    response(long.R_INTROJIRA40, ['usar', 'filtros', 'jira'], required_words=['usar', 'filtros'])
    response(long.R_INTROJIRA41, ['usar', 'painel', 'controle', 'jira'], required_words=['usar', 'painel', 'controle'])
    response(long.R_INTROJIRA42, ['configurar', 'integracoes', 'outras', 'ferramentas', 'jira'], required_words=['configurar', 'outras', 'ferramentas'])
    response(long.R_INTROJIRA43, ['usar', 'jira', 'github'], required_words=['jira', 'github'])
    response(long.R_INTROJIRA44, ['usar', 'jira', 'bitbucket'], required_words=['jira', 'bitbucket'])
    response(long.R_INTROJIRA45, ['usar', 'jira', 'confluence'], required_words=['jira', 'confluence'])
    response(long.R_INTROJIRA46, ['usar', 'jira', 'slack'], required_words=['jira', 'slack'])
    response(long.R_INTROJIRA47, ['usar', 'jira', 'trello'], required_words=['jira', 'trello'])
    response(long.R_INTROJIRA48, ['usar', 'jira', 'google', 'sheets'], required_words=['jira', 'google', 'sheets'])
    response(long.R_INTROJIRA49, ['usar', 'jira', 'salesforce'], required_words=['jira', 'salesforce'])
    response(long.R_INTROJIRA50, ['usar', 'jira', 'zendesk'], required_words=['jira', 'zendesk'])
    response(long.R_INTROJIRA51, ['usar', 'jira', 'microsoft', 'teams'], required_words=['jira', 'microsoft', 'teams'])
    response(long.R_INTROJIRA52, ['usar', 'jira', 'power', 'bi'], required_words=['jira', 'power', 'bi'])
    response(long.R_INTROJIRA53, ['usar', 'jira', 'zapier'], required_words=['jira', 'zapier'])
    response(long.R_INTROJIRA54, ['usar', 'jira', 'microsoft', 'project'], required_words=['jira', 'microsoft', 'project'])
    response(long.R_INTROJIRA55, ['usar', 'jira', 'asana'], required_words=['jira', 'asana'])
    response(long.R_INTROJIRA56, ['usar', 'jira', 'monday'], required_words=['jira', 'monday'])
    response(long.R_INTROJIRA57, ['usar', 'jira', 'gitlab'], required_words=['jira', 'gitlab'])
    response(long.R_INTROJIRA58, ['usar', 'jira', 'jenkins'], required_words=['jira', 'jenkins'])
    response(long.R_INTROJIRA59, ['usar', 'jira', 'bamboo'], required_words=['jira', 'bamboo'])
    response(long.R_INTROJIRA60, ['usar', 'jira', 'docker'], required_words=['jira', 'docker'])
    response(long.R_INTROJIRA61, ['usar', 'jira', 'kubernetes'], required_words=['jira', 'kubernetes'])
    response(long.R_INTROJIRA62, ['usar', 'jira', 'aws'], required_words=['jira', 'aws'])
    response(long.R_INTROJIRA63, ['usar', 'jira', 'azure', 'devops'], required_words=['jira', 'azure', 'devops'])
    response(long.R_INTROJIRA64, ['usar', 'jira', 'circle', 'ci'], required_words=['jira', 'circle', 'ci'])
    response(long.R_INTROJIRA65, ['usar', 'jira', 'travis', 'ci'], required_words=['jira', 'travis', 'ci'])
    response(long.R_INTROJIRA66, ['usar', 'jira', 'sonarqube'], required_words=['jira', 'sonarqube'])
    response(long.R_INTROJIRA67, ['usar', 'jira', 'new', 'relic'], required_words=['jira', 'new', 'relic'])
    response(long.R_INTROJIRA68, ['usar', 'jira', 'datadog'], required_words=['jira', 'datadog'])
    response(long.R_INTROJIRA69, ['usar', 'jira', 'splunk'], required_words=['jira', 'splunk'])
    response(long.R_INTROJIRA70, ['usar', 'jira', 'dynatrace'], required_words=['jira', 'dynatrace'])
    response(long.R_INTROJIRA71, ['usar', 'jira', 'pagerduty'], required_words=['jira', 'pagerduty'])
    response(long.R_INTROJIRA72, ['usar', 'jira', 'servicenow'], required_words=['jira', 'servicenow'])
    response(long.R_INTROJIRA73, ['usar', 'jira', 'jfrog'], required_words=['jira', 'jfrog'])
    response(long.R_INTROJIRA74, ['usar', 'jira', 'ansible'], required_words=['jira', 'ansible'])
    response(long.R_INTROJIRA75, ['usar', 'jira', 'terraform'], required_words=['jira', 'terraform'])
    response(long.R_INTROJIRA76, ['usar', 'jira', 'puppet'], required_words=['jira', 'puppet'])
    response(long.R_INTROJIRA77, ['usar', 'jira', 'chef'], required_words=['jira', 'chef'])
    response(long.R_INTROJIRA78, ['usar', 'jira', 'nagios'], required_words=['jira', 'nagios'])
    response(long.R_INTROJIRA79, ['usar', 'jira', 'prometheus'], required_words=['jira', 'prometheus'])
    response(long.R_INTROJIRA80, ['usar', 'jira', 'grafana'], required_words=['jira', 'grafana'])
    response(long.R_INTROJIRA81, ['usar', 'jira', 'elk', 'stack'], required_words=['jira', 'elk', 'stack'])
    response(long.R_INTROJIRA82, ['usar', 'jira', 'apache', 'kafka'], required_words=['jira', 'apache', 'kafka'])
    response(long.R_INTROJIRA83, ['usar', 'jira', 'rabbitmq'], required_words=['jira', 'rabbitmq'])
    response(long.R_INTROJIRA84, ['usar', 'jira', 'redis'], required_words=['jira', 'redis'])
    response(long.R_INTROJIRA85, ['usar', 'jira', 'mongodb'], required_words=['jira', 'mongodb'])
    response(long.R_INTROJIRA86, ['usar', 'jira', 'postgreesql'], required_words=['jira', 'postgreesql'])
    response(long.R_INTROJIRA87, ['usar', 'jira', 'mysql'], required_words=['jira', 'mysql'])
    response(long.R_INTROJIRA88, ['usar', 'jira', 'oracle'], required_words=['jira', 'oracle'])
    response(long.R_INTROJIRA89, ['usar', 'jira', 'sqlserver'], required_words=['jira', 'sqlserver'])
    response(long.R_INTROJIRA90, ['usar', 'jira', 'salesforce', 'marketing', 'cloud'], required_words=['jira', 'salesforce', 'marketing', 'cloud'])
    
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

    ### Adicionando condição para que se a mensagem for respondida com até logo ele finalize o programa
    #if check_all_messages(split_message) == "Ate logo!":
    #    print("Obrigado por utilizar o JiraBot.", check_all_messages(split_message))
    #    exit()
    
    with io.open("perguntas_novas.txt", "a", encoding="utf-8") as f: #cria o arquivo para armazenar as pergunta feitas pelo usuário
        f.write(user_input + "\n")  # adiciona uma nova linha depois de cada entrada
    return response

# Testando o sistema de resposta
#while True:
    #print('\033[1;34mJiraBot: \033[0;0m' + get_response(input( "\033[1;31m" + username + "\033[0;0m")))