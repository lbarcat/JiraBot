import random

R_INTROJIRA1 = "jira é um aplicativo de software desenvolvido pela empresa de software australiana Atlassian que permite que as equipes rastreiem problemas, gerenciem projetos e automatizem fluxos de trabalho."
R_INTROJIRA2 = "A configuração do Jira Software depende de suas necessidades. Primeiro, você precisa criar um projeto para gerenciar seu trabalho. Depois, você pode adicionar usuários e definir as permissões de acesso. Você também pode personalizar os campos e as telas para atender às suas necessidades específicas. Além disso, você pode configurar fluxos de trabalho, notificações e integrações com outros sistemas."
R_INTROJIRA3 = "Acesse o site do Jira Software e faça login na sua conta.  2. Clique no botão Criar Projeto na parte superior da página inicial. 3. Selecione o tipo de projeto que você deseja criar (por exemplo, Agile, Scrum ou Kanban). 4. Insira um nome para o seu projeto e uma descrição opcional. 5. Selecione um modelo de projeto para ajudar a configurar as etapas do seu projeto (por exemplo, software, serviços ou marketing). 6. Selecione os membros da equipe que participarão do projeto e defina as permissões de acesso para cada um deles."




def unknown():
    response = ["Eu nao entendi, poderia tentar novamente?",
                "Hum, nao encontrei essa informacao",
                "Preciso verificar!",
                ][
        random.randrange(4)]
    return response