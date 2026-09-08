# Identidade e preferências

## Perguntas

Leia o `SOUL.md` do perfil ativo e as preferências que o Hermes realmente carrega. Não busque em todo o histórico ou exporte memórias. Confirme informações existentes que forem relevantes, sem repetir perguntas já respondidas.

Pergunte uma coisa por vez, aceitando uma resposta livre:

1. Como você quer ser chamado?
2. Que nome quer dar ao seu Hermes?
3. O que você faz no dia a dia?
4. Como prefere as respostas: mais diretas, detalhadas, formais ou informais?
5. Qual idioma e fuso horário quer usar? Aceite cidade para confirmar o fuso IANA correspondente. Não deduza só pelo idioma.
6. Qual é a primeira tarefa em que quer ajuda?

Aceite pular uma resposta e preserve o padrão existente nesse caso. Não transforme a conversa numa entrevista longa.

## Separar identidade de dados pessoais

`SOUL.md` guarda nome, papel, tom e princípios do agente. O caminho é o `HERMES_HOME` efetivo da instância, não a pasta de trabalho do terminal. O nome canônico usa maiúsculas: `SOUL.md`.

Para preferências da pessoa, use o mecanismo de memória de usuário reconhecido pela versão instalada. Confira o caminho efetivamente carregado: em versões atuais, o perfil de usuário usa `memories/USER.md` dentro do Hermes home. Não crie um `USER.md` na raiz só porque outro instalador o fazia. Preserve conteúdo preexistente e limites de memória da versão. Se não puder comprovar o destino, mantenha esta parte pendente e não crie arquivo que o Hermes não lê.

Registre idioma e fuso como preferências. Não altere o fuso do sistema ou invente chaves no `config.yaml` para isso. A primeira tarefa orienta o uso, não vira cron nem autorização permanente de escrita.

## Prévia e gravação

Mostre apenas os trechos que pretende acrescentar ou mudar. Não exponha detalhes privados preexistentes sem necessidade. Uma proposta mínima de identidade contém:

- Nome escolhido e papel de assistente pessoal.
- Tom e nível de detalhe combinados.
- Pedir esclarecimento quando faltar informação e distinguir fato de suposição.
- Usar Maton e Zernio pelas skills instaladas, começando por leitura e respeitando autorização para escrita.
- Proteger credenciais e não tratá-las como memória pessoal.

A prévia é personalizada com as respostas, sem campos fictícios. Pergunte se pode salvar e espere o ok. Se houver correção, atualize a prévia. Se a pessoa não aprovar, não grave e mantenha identidade pendente.

Antes de gravar, faça backup dos arquivos que serão alterados em uma pasta privada local, fora de repositórios e dentro de armazenamento persistente. Registre quais arquivos não existiam. Use diretório exclusivo por execução, permissões restritas (`700` na pasta e `600` nos arquivos em sistemas POSIX), mantendo acesso para o usuário que roda o Hermes.

Releia os arquivos antes da escrita. Se mudaram desde a prévia, reconcilie e peça aprovação apenas do novo conteúdo. Edite somente os trechos combinados, com escrita atômica quando disponível, mantendo dono e permissões. Releia para confirmar o conteúdo salvo sem despejar o arquivo inteiro no chat. Não substitua arquivo existente por um template completo.

Ao repetir o onboarding, aproveite os trechos já aplicados. Se não houver mudança, não grave nem duplique seções. Um backup anterior não autoriza sobrescrever modificações posteriores.

## Ativação e recuperação

O Hermes carrega a identidade ao iniciar uma sessão. Peça uma nova conversa para verificar nome e tom; arquivo salvo sozinho não prova que a sessão atual recarregou a identidade. A pessoa pode testar: "Como você se chama e como combinamos que você vai me responder?".

Para desfazer, identifique o backup desta execução, compare com o arquivo atual e restaure somente a mudança solicitada, preservando edições posteriores. Arquivos criados nesta execução só podem ser removidos após conferir que não receberam conteúdo novo e que a pessoa pediu a reversão.

Fontes oficiais: [SOUL.md](https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes) e [memória](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/). A versão instalada decide os caminhos e ferramentas suportados.
