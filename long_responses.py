import random

R_INTROJIRA1 = "jira é um aplicativo de software desenvolvido pela empresa de software australiana Atlassian que permite que as equipes rastreiem problemas, gerenciem projetos e automatizem fluxos de trabalho."

R_INTROJIRA2 = "A configuração do Jira Software depende de suas necessidades. Primeiro, você precisa criar um projeto para gerenciar seu trabalho. Depois, você pode adicionar usuários e definir as permissões de acesso. Você também pode personalizar os campos e as telas para atender às suas necessidades específicas. Além disso, você pode configurar fluxos de trabalho, notificações e integrações com outros sistemas."

R_INTROJIRA3 = "Acesse o site do Jira Software e faça login na sua conta.  2. Clique no botão Criar Projeto na parte superior da página inicial. 3. Selecione o tipo de projeto que você deseja criar (por exemplo, Agile, Scrum ou Kanban). 4. Insira um nome para o seu projeto e uma descrição opcional. 5. Selecione um modelo de projeto para ajudar a configurar as etapas do seu projeto (por exemplo, software, serviços ou marketing). 6. Selecione os membros da equipe que participarão do projeto e defina as permissões de acesso para cada um deles."

R_INTROJIRA4 = """1. Gerenciamento de Projetos: O Jira Software oferece recursos para ajudar os usuários a gerenciar projetos, como criação de quadros Kanban e Scrum, rastreamento de tarefas e controle de tempo, além de recursos avançados como relatórios e gráficos. 
                  2. Gerenciamento de Bugs: O Jira Software possui ferramentas robustas para ajudar os usuários a identificar, rastrear e resolver bugs rapidamente. 
                  3. Integração com outras ferramentas: O Jira Software pode ser facilmente integrado com outras ferramentas, como GitHub, Bitbucket, Slack e Confluence. Isso permite que os usuários trabalhem em conjunto em projetos sem ter que sair do ambiente do Jira Software.
                  4. Gerenciamento de Riscos: O Jira Software oferece recursos para ajudar os usuários a identificar e gerenciar riscos potenciais associados a um projeto ou atividade específica."""

R_INTROJIRA5 = """1. Crie um projeto: Primeiro, crie um projeto no Jira Software para gerenciar suas tarefas. Você pode usar modelos pré-configurados ou configurar seu próprio projeto. 
                  2. Adicione tarefas: Agora, adicione tarefas ao seu projeto. Você pode adicionar tarefas individuais ou criar grupos de tarefas relacionadas. 
                  3. Atribua tarefas: Atribua as tarefas aos usuários responsáveis usando a funcionalidade de atribuição do Jira Software. Isso permitirá que você saiba quem está trabalhando em qual tarefa e quando ela deve ser concluída. 
                  4. Acompanhe o progresso: Use o recurso de visualização do Jira Software para acompanhar o progresso das suas tarefas e verificar se elas estão sendo concluídas dentro do prazo previsto. 
                  5. Gerencie alterações: Use o recurso de controle de versão do Jira Software para gerenciar quaisquer alterações nas suas tarefas e manter todos os envolvidos informados sobre as atualizações mais recentes."""

R_INTROJIRA6 = """1. Acesse a página de relatórios do Jira Software. Você pode encontrá-la na barra lateral esquerda da sua tela inicial. 
                  2. Selecione o tipo de relatório que deseja criar, como por exemplo, um gráfico de barras, gráfico de pizza ou tabela de dados. 
                  3. Escolha as informações que deseja incluir no seu relatório, como por exemplo, o número total de tarefas concluídas, tempo médio para conclusão das tarefas e assim por diante. 
                  4. Selecione os filtros que deseja aplicar ao seu relatório, como por exemplo, data inicial e final do período de tempo que deseja analisar ou usuários específicos envolvidos nas tarefas. 
                  5. Clique em “Gerar Relatório” para visualizar os resultados em seu navegador."""

R_INTROJIRA7 = """1. Crie uma estrutura de projetos eficaz: Defina as estruturas de projetos adequadas para seus times e crie fluxos de trabalho que ajudem a maximizar a produtividade. 
                  2. Utilize os recursos de gerenciamento de tempo: O Jira oferece recursos como o Gerenciamento de Tempo, que permite que os usuários rastreiem o tempo gasto em tarefas específicas. Isso ajuda a manter o controle do progresso dos projetos e identificar possíveis gargalos. 
                  3. Use as ferramentas de relatórios: O Jira oferece várias ferramentas para criar relatórios detalhados sobre o progresso dos projetos, incluindo gráficos, tabelas e outros tipos de visualização. Esses relatórios podem ser usados para identificar problemas e tomar decisões informadas. 
                  4. Utilize os recursos colaborativos: O Jira oferece várias ferramentas colaborativas, como discussões, comentários e tarefas compartilhadas entre membros do time. Isso facilita a comunicação entre os membros do time e melhora a produtividade geral. 
                  5. Use as notificações: O Jira oferece notificações por email para alertar os usuários sobre atualizações importantes nos projetos em andamento. Isso garante que todos estejam sempre atualizados sobre o progresso dos projetos e possam tomar decisões informadas rapidamente."""

R_INTROJIRA8 = "Para personalizar o layout do Jira, você pode usar o tema de interface do usuário do Jira. O tema permite alterar a cor e o estilo da interface do usuário para que seja mais adequado às suas necessidades. Você também pode criar seus próprios temas personalizados, adicionando imagens, fontes e outros elementos de design. Além disso, é possível alterar a disposição dos campos e das colunas na visualização de lista para melhorar a experiência do usuário."

R_INTROJIRA9 = "Os principais plugins para o Jira são: 1 - Tempo de Trabalho. 2 - Adaptavist ScriptRunner. 3 - Insight for Jira. 4 - Zephyr for Jira. 5 - Confluence for Jira. 6 - Xray Test Management for Jira. 7 - Portfolio for Jira. 8 - Structure for Jira. 9 - Automation for Jira. 10 - Advanced Roadmaps"

R_INTROJIRA10 = """1. Integração com ferramentas de comunicação: O Jira Software pode ser integrado com ferramentas de comunicação, como Slack, Microsoft Teams e Skype for Business. Isso permite que os usuários recebam notificações sobre atualizações no Jira e discutam problemas diretamente na plataforma de mensagens. 
                   2. Integração com ferramentas de gerenciamento de projetos: O Jira Software pode ser integrado a outras ferramentas de gerenciamento de projetos, como o Trello e o Asana. Isso permite que os usuários compartilhem informações entre as plataformas e aproveitem as melhores funcionalidades dos dois sistemas. 
                   3. Integração com ferramentas de colaboração: O Jira Software pode ser integrado a outras ferramentas de colaboração, incluindo o Google Drive, Dropbox e Box. Isso permite que os usuários compartilhem arquivos diretamente do Jira para outras plataformas e vice-versa."""

R_INTROJIRA11 = "Os principais recursos de seguranca do Jira Software incluem: autenticação de dois fatores, controle de acesso baseado em função, auditoria de log, criptografia de dados, autenticação SSO (Single Sign-On) e controle de acesso baseado em grupo."

R_INTROJIRA12 = "Jira Software é uma ferramenta de gerenciamento de projetos desenvolvida pela Atlassian. É usada para acompanhar e rastrear tarefas, bugs, problemas e outras demandas relacionadas a projetos. Ele fornece recursos de colaboração, como quadros Kanban, painéis de controle e relatórios para que os membros da equipe possam trabalhar em conjunto para alcançar seus objetivos."

R_INTROJIRA13 = "O Jira Software pode ajudar a sua equipe a gerenciar projetos, rastrear bugs e problemas, criar fluxos de trabalho personalizados e muito mais. Ele também pode fornecer relatórios e gráficos para ajudar a monitorar o progresso do projeto. Além disso, o Jira Software oferece recursos de colaboração que permitem que os membros da equipe trabalhem juntos em tempo real."

R_INTROJIRA14 = """1. Gerenciamento de projetos: O Jira Software permite que os usuários criem e gerenciem projetos, acompanhem o progresso dos projetos, criem fluxos de trabalho personalizados, estabeleçam prioridades e muito mais. 
                   2. Gerenciamento de tarefas: O Jira Software oferece ferramentas para gerenciar tarefas, incluindo a criação de tarefas, a atribuição de tarefas a membros da equipe, o monitoramento do progresso das tarefas e o rastreamento do tempo gasto em cada tarefa. 
                   3. Relatórios: O Jira Software oferece vários relatórios para ajudar os usuários a entender melhor o progresso dos projetos e as atividades realizadas por membros da equipe. Os relatórios incluem gráficos de burndown, gráficos de velocidade e gráficos de tempo gasto em tarefas específicas. 
                   4. Integração com outras ferramentas: O Jira Software pode ser integrado com outras ferramentas para facilitar o fluxo de trabalho entre equipes. Por exemplo, é possível integrar o Jira Software com ferramentas de colaboração como Slack e Confluence para facilitar a colaboração entre equipes remotas."""

R_INTROJIRA15 = """1. O Jira Software é especialmente projetado para uso em equipes ágeis, enquanto outras ferramentas de gerenciamento de projetos são mais adequadas para uso em equipes tradicionais. 
                   2. O Jira Software oferece recursos avançados de rastreamento de bugs e problemas, enquanto outras ferramentas podem não ter esses recursos. 
                   3. O Jira Software oferece suporte a vários tipos de gráficos e relatórios, enquanto outras ferramentas podem não ter esses recursos. 
                   4. O Jira Software tem uma interface intuitiva que facilita o gerenciamento de projetos, enquanto outras ferramentas podem ser mais complicadas e difíceis de usar. 
                   5. O Jira Software tem um conjunto abrangente de APIs que permitem a integração com outros sistemas, enquanto outras ferramentas podem não ter essa capacidade."""

R_INTROJIRA16 = "O custo do Jira Software depende do número de usuários e do plano escolhido. Os preços começam em US$10 por mês para um plano básico de 10 usuários e vão até US$250 por mês para um plano avançado de 2.000 usuários."

R_INTROJIRA17 = """1. Integração com outros sistemas: O Jira Software oferece integrações com outros sistemas, como o GitHub, o Bitbucket, o Slack, o Confluence e muitos outros. 
                   2. Integração de APIs: O Jira Software também oferece APIs que permitem a integração com outras ferramentas e serviços. 
                   3. Integração de dados: O Jira Software permite que os usuários importem dados de outras ferramentas para serem usados no Jira. 
                   4. Integração de aplicativos: O Jira Software oferece vários aplicativos que podem ser instalados para adicionar recursos extras à plataforma."""

R_INTROJIRA18 = """1. Acesse o site do Jira Software e faça o download da versão mais recente. 
                   2. Execute o instalador para instalar o Jira Software em seu computador. 
                   3. Configure a conta de administrador do Jira Software, incluindo um nome de usuário e senha. 
                   4. Crie um novo projeto no Jira Software e adicione os membros da equipe a ele. 
                   5. Configure as configurações do projeto, como tipos de tarefas, prioridades, etiquetas e outras opções. 
                   6. Crie quadros Kanban para organizar as tarefas do projeto de acordo com seus requisitos específicos. 
                   7. Crie relatórios personalizados para acompanhar o progresso do projeto e identificar possíveis problemas antes que eles aconteçam. 
                   8. Configure os alertas para que você receba notificações sobre alterações importantes nos projetos em andamento."""

R_INTROJIRA19 = "A melhor maneira de importar dados para o Jira Software é usando o recurso de importação do Jira. Para isso, você precisará exportar os dados do seu sistema atual para um arquivo CSV (Comma Separated Values) e, em seguida, usar o Assistente de Importação do Jira para importá-los. O Assistente de Importação permite que você mapeie os campos do arquivo CSV para os campos correspondentes no Jira e faça ajustes finais antes da importação."

R_INTROJIRA20 = "A exportação de dados do Jira Software pode ser feita usando a ferramenta de exportação nativa do Jira. Para exportar os dados, você precisará acessar o menu Administração e selecionar a opção Exportar Dados. Em seguida, você poderá escolher qual tipo de dados deseja exportar (tarefas, usuários, etc.) e qual formato deseja usar (XML, CSV, etc.)."

R_INTROJIRA21 = "Sim, o Jira Software possui uma API RESTful que permite aos desenvolvedores criar aplicativos personalizados para integrar o Jira com outros sistemas. A API também pode ser usada para automatizar tarefas no Jira, como criar e atualizar tarefas, adicionar comentários e alterar o status de um ticket."

R_INTROJIRA22 = """1. Crie um projeto específico para sua equipe: O primeiro passo é criar um projeto específico para sua equipe, que permitirá a vocês organizar e gerenciar todos os seus trabalhos de forma mais eficiente.
                   2. Configure as opções de fluxo de trabalho: O Jira Software oferece várias opções de fluxo de trabalho que você pode configurar para atender às necessidades da sua equipe. Isso inclui definir etapas, prioridades, prazos e outras configurações relacionadas ao processo de trabalho.
                   3. Adicione campos personalizados: Você também pode adicionar campos personalizados ao seu projeto no Jira Software para armazenar informações específicas da sua equipe ou projeto. Isso permitirá que você tenha um maior controle sobre o andamento do seu trabalho.
                   4. Crie quadros Kanban: Os quadros Kanban são ótimas ferramentas para visualizar o progresso dos projetos da sua equipe e gerenciar melhor os recursos disponíveis. Você pode criar quadros Kanban no Jira Software com base nas necessidades da sua equipe e usá-los para acompanhar o progresso dos seus projetos."""

R_INTROJIRA23 = """1. Acesse o site do Jira Software e faça o login na sua conta.
                   2. Clique no botão "Criar projeto" na barra de navegação superior.
                   3. Selecione o tipo de projeto que deseja criar (por exemplo, Software, Serviço, etc.).
                   4. Insira um nome para o seu projeto e uma descrição opcional.
                   5. Selecione um modelo de projeto para começar (por exemplo, Scrum, Kanban, etc.).
                   6. Escolha as configurações de acesso para o seu projeto (público ou privado).
                   7. Clique no botão Criar."""

R_INTROJIRA24 = """1. Abra o Jira Software e faça login com suas credenciais.
                   2. Clique em "Criar" na barra de navegação superior.
                   3. Selecione a opção "Tarefa" para criar uma tarefa.
                   4. Insira as informações necessárias, como título, descrição, projeto e prioridade da tarefa.
                   5. Clique em "Criar" para salvar a tarefa criada no Jira Software."""

R_INTROJIRA25 = "Para atribuir tarefas no Jira Software, primeiro você precisa criar uma tarefa. Para fazer isso, vá para a guia Criar na parte superior da página inicial do Jira. Selecione a opção Tarefa e preencha os detalhes da tarefa. Quando terminar, clique em Criar. Depois de criar a tarefa, você pode atribuí-la a um usuário específico. Para fazer isso, clique no botão de edição na parte superior direita da tela. Na seção Atribuir para, selecione o usuário que deseja atribuir a tarefa e clique em Atualizar. A tarefa agora está atribuída ao usuário selecionado."

R_INTROJIRA26 = "Para definir prazos no Jira Software, você pode usar a função de planejamento de projetos. Esta função permite que você crie e gerencie tarefas, atribua datas de início e término para cada tarefa e visualize o progresso do projeto. Você também pode adicionar lembretes para que os membros da equipe sejam notificados quando um prazo estiver próximo."

R_INTROJIRA27 = "Para rastrear o progresso do projeto no Jira Software, você pode usar os recursos de relatórios e painéis. Os relatórios permitem que você visualize o progresso do projeto, enquanto os painéis permitem que você visualize as informações em tempo real. Você também pode usar o recurso de sprint para verificar o progresso de cada sprint individualmente. Além disso, é possível configurar alertas para que você receba notificações quando houver mudanças significativas no andamento do projeto."

R_INTROJIRA28 = """1. Crie um projeto Jira para o seu time: O primeiro passo para gerenciar equipes no Jira Software é criar um projeto Jira para o seu time. Isso permitirá que você organize e acompanhe todas as tarefas, bugs, problemas e outros itens relacionados à equipe.
                   2. Crie quadros de trabalho: Os quadros de trabalho permitem que você visualize e organize os itens que precisam ser concluídos pelo seu time. Você pode criar quadros de trabalho personalizados com várias colunas, como "Em andamento", "Concluído" e "Bloqueado".
                   3. Estabeleça metas: Estabelecer metas para o seu time é uma ótima maneira de motivá-los a alcançar objetivos específicos. Você pode usar o Jira Software para definir metas claras e mensuráveis ​​para ajudar a equipe a alcançar os resultados desejados.
                   4. Gerencie as tarefas: O Jira Software permite que você gerencie as tarefas da sua equipe de forma fácil e intuitiva. Você pode criar tarefas, atribuí-las a membros específicos da equipe, definir prioridades e monitorar o progresso dessas tarefas em tempo real.
                   5. Use relatórios: O Jira Software oferece uma variedade de relatórios que permitem que você visualize facilmente o progresso do seu time em relação às metas estabelecidas. Esses relatórios fornecem informações valiosas sobre quais áreas precisam melhorias e quais estão indo bem."""

R_INTROJIRA29 = "No Jira Software, os papéis e permissões são definidos usando o Gerenciador de Permissões. O Gerenciador de Permissões permite que você crie grupos de usuários e atribua a eles diferentes níveis de acesso ao Jira. Por exemplo, você pode definir um grupo como Administrador Global, que terá acesso total a todos os recursos do Jira, ou um grupo como Usuário Básico, que terá apenas acesso limitado às tarefas. Você também pode criar papéis personalizados para atribuir permissões específicas para determinados projetos ou tarefas."

R_INTROJIRA30 = """Para criar um workflow no Jira Software, você precisa seguir os seguintes passos: 
                   1. Abra o Jira e vá para a página de configurações. 
                   2. Selecione o menu "Workflows" na barra lateral esquerda. 
                   3. Clique no botão "Criar workflow" na parte superior da página. 
                   4. Insira um nome para o seu workflow e clique em "Criar". 
                   5. Adicione etapas, transições e regras ao seu workflow usando os menus suspensos à direita da tela. 
                   6. Clique em "Salvar" quando terminar de configurar o seu workflow."""

R_INTROJIRA31 = "Para personalizar os workflows no Jira Software, você precisa acessar o menu Configurações e Fluxos de Trabalho. Aqui, você pode criar, editar e excluir fluxos de trabalho para atender às necessidades do seu projeto."

R_INTROJIRA32 = """1. Acesse o menu Configurações no Jira Software.
                   2. Clique em Fluxos de Trabalho na barra lateral esquerda.
                   3. Clique no botão Criar fluxo de trabalho para começar a criar um novo fluxo de trabalho.
                   4. Insira o nome do fluxo de trabalho e selecione o tipo de projeto para qual ele será aplicado.
                   5. Adicione os estados e transições necessários para o fluxo de trabalho, clicando no botão Adicionar Estado ou Adicionar Transição, conforme necessário.
                   6. Selecione as permissões necessárias para cada estado e transição, definindo quem pode executar as tarefas associadas a cada um dos elementos do fluxo de trabalho.
                   7. Clique em Salvar para salvar as alterações feitas no fluxo de trabalho e ativá-lo para uso imediato."""

R_INTROJIRA33 = """1. Abra o Jira Software e vá para a página de configurações.
                   2. Selecione o item "Campos" na barra lateral esquerda.
                   3. Clique no botão Criar campo personalizado.
                   4. Selecione o tipo de campo que você deseja criar (por exemplo, texto, número, data, etc.).
                   5. Insira um nome para o campo e uma descrição opcional.
                   6. Selecione as opções de configuração necessárias para o seu campo (por exemplo, obrigatório, visível a todos os usuários, etc.).
                   7. Clique em Salvar para criar o campo personalizado."""

R_INTROJIRA34 = """1. Abra o Jira Software e vá para Configurações > Gerenciar > Telas.
                   2. Clique em "Criar tela" para criar uma nova tela.
                   3. Insira um nome para a tela e selecione os campos que você deseja incluir na tela.
                   4. Clique em Salvar para salvar as alterações.
                   5. Para editar uma tela existente, clique no ícone de edição ao lado da tela desejada e faça as alterações necessárias.
                   6. Quando terminar, clique em Salvar para salvar as alterações feitas na tela."""

R_INTROJIRA35 = """1. Acesse o painel de administração do Jira Software e clique em Notificações.
                   2. Selecione a opção de notificação desejada (por exemplo, notificações por e-mail).
                   3. Configure os destinatários das notificações (por exemplo, usuários específicos ou grupos de usuários).
                   4. Selecione as ações que deseja que gerem notificações (por exemplo, comentar, atribuir tarefas, alterar status).
                   5. Salve as alterações para ativar as notificações no Jira Software."""

R_INTROJIRA36 = """1. Crie uma lista de prioridades. Avalie os requisitos e crie uma lista de prioridades com base nos objetivos do projeto.
                   2. Estabeleça um critério de priorização. Defina um critério para classificar as tarefas em ordem de prioridade, como importância, urgência ou impacto no projeto.
                   3. Atribua as tarefas às pessoas certas. Atribua as tarefas às pessoas certas para garantir que elas sejam concluídas dentro do prazo estipulado.
                   4. Use a funcionalidade Priorização no Jira Software para definir a ordem das tarefas e gerenciar o fluxo de trabalho do projeto. A funcionalidade Priorização permite que você classifique as tarefas em ordem de prioridade, atribuindo pontuações a cada uma delas e definindo quais são mais importantes para o sucesso do projeto."""

R_INTROJIRA37 = """1. Crie um novo projeto no Jira Software.
                   2. Configure o projeto para usar o Quadro de Sprint.
                   3. Crie uma equipe de desenvolvimento para trabalhar no projeto.
                   4. Crie um sprint e adicione tarefas a ele.
                   5. Assigne as tarefas aos membros da equipe de desenvolvimento.
                   6. Acompanhe o progresso do sprint monitorando os indicadores do quadro de sprint, como horas trabalhadas, tarefas concluídas e taxa de conclusão estimada.
                   7. Replaneje o sprint se necessário, adicionando mais tarefas, alterando prioridades e atribuindo novas pessoas às tarefas existentes.
                   8. Conclua o sprint quando todas as tarefas estiverem concluídas e faça uma retrospectiva para avaliar o que foi bem-sucedido e onde houve falhas durante o processo de desenvolvimento do produto."""

R_INTROJIRA38 = ""
R_INTROJIRA39 = ""
R_INTROJIRA40 = ""
R_INTROJIRA41 = ""
R_INTROJIRA42 = ""
R_INTROJIRA43 = ""
R_INTROJIRA44 = ""
R_INTROJIRA45 = ""
R_INTROJIRA46 = ""
R_INTROJIRA47 = ""
R_INTROJIRA48 = ""
R_INTROJIRA49 = ""
R_INTROJIRA50 = ""
R_INTROJIRA51 = ""
R_INTROJIRA52 = ""
R_INTROJIRA53 = ""
R_INTROJIRA54 = ""
R_INTROJIRA55 = ""
R_INTROJIRA56 = ""
R_INTROJIRA57 = ""
R_INTROJIRA58 = ""
R_INTROJIRA59 = ""
R_INTROJIRA60 = ""
R_INTROJIRA61 = ""
R_INTROJIRA62 = ""
R_INTROJIRA63 = ""
R_INTROJIRA64 = ""
R_INTROJIRA65 = ""
R_INTROJIRA66 = ""
R_INTROJIRA67 = ""
R_INTROJIRA68 = ""
R_INTROJIRA69 = ""
R_INTROJIRA70 = ""
R_INTROJIRA71 = ""
R_INTROJIRA72 = ""
R_INTROJIRA73 = ""
R_INTROJIRA74 = ""
R_INTROJIRA75 = ""
R_INTROJIRA76 = ""
R_INTROJIRA77 = ""
R_INTROJIRA78 = ""
R_INTROJIRA79 = ""
R_INTROJIRA80 = ""
R_INTROJIRA81 = ""
R_INTROJIRA82 = ""
R_INTROJIRA83 = ""
R_INTROJIRA84 = ""
R_INTROJIRA85 = ""
R_INTROJIRA86 = ""
R_INTROJIRA87 = ""
R_INTROJIRA88 = ""
R_INTROJIRA89 = ""
R_INTROJIRA90 = ""

def unknown():
    response = ["Eu nao entendi, poderia tentar novamente?",
                "Hum, nao encontrei essa informacao!",
                "Preciso verificar! Nos envie um e-mail com a sua pergunta para: lcbarcat@gmail.com",
                "Sou programado apenas para responder perguntas relacionadas ao Jira, caso sua pergunta seja sobre o jira e não foi respondida, envie um email para: lcbarcat@gmail.com",
                ][
        random.randrange(4)]
    return response