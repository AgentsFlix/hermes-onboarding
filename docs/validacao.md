# Critérios de conclusão

Entregue um resumo baseado no que foi observado:

| Item | Evidência mínima |
|---|---|
| Ambiente | Perfil e pasta persistente identificados como os usados pela conversa |
| Identidade | Prévia aprovada, backup feito e mudanças relidas no SOUL.md correto |
| Preferências | Gravadas no mecanismo de usuário efetivamente carregado, sem apagar memórias |
| Maton: instalação | Skill descoberta pelo Hermes, origem verificada e arquivos de apoio presentes |
| Maton: acesso | Chave disponível no ambiente das ferramentas e resultado de leitura sem erro oculto |
| Zernio: instalação | Skill descoberta pelo Hermes, origem verificada e arquivos de apoio presentes |
| Zernio: acesso | Endpoint oficial, chave disponível e resultado de cada leitura distinguindo falhas parciais |
| Nova sessão | Identidade e skills reconhecidas; se ainda não testado, confirmação pendente |

Use estados claros: pronto, pendente ou falhou, com motivo breve. Diferencie identidade salva de identidade reconhecida em nova sessão. Skill instalada não equivale a API validada. API válida sem conta conectada não dá acesso aos apps da pessoa.

Feche com uma sugestão de pedido de leitura relacionado à primeira tarefa. Não diga que pode publicar ou enviar automaticamente porque a chave funciona.

## Cenários para revisar o roteiro

- Instalação padrão ou Docker com HERMES_HOME próprio: editar somente o perfil identificado, sem presumir caminho ou container.
- Terminal isolado da aplicação: não confundir ausência de chave nesse terminal com ausência no hPanel.
- SOUL e memória já personalizados: prévia incremental, backup, preservação e recusa de gravação antes do ok.
- Segunda execução: não duplicar seções, skills ou backups desnecessários.
- Chave ausente no processo: instalação pode seguir, validação fica pendente, sem coleta ou regravação.
- Skill mais nova/customizada: preservar, sem downgrade silencioso.
- Scanner bloqueado ou pacote incompleto: pendência explícita sem bypass.
- Chave inválida, rede indisponível, conta vazia e erro parcial: resultados separados, sem falso sucesso.
- ZERNIO_API_URL alternativo: não executar a chamada autenticada.
- Usuário pede tarefa com envio: onboarding não executa escrita externa.
- Sem acesso a terminal/arquivos: informar a limitação; não simular execução.

## Validação do repositório

Execute `python3 scripts/validate.py` e `python3 scripts/agent_work.py check` na worktree da tarefa. O primeiro verifica links locais, arquivos, sintaxe Python e ausência de arquivos pessoais versionáveis; o segundo verifica isolamento do trabalho. Nenhum deles instala Hermes ou acessa contas Maton/Zernio.

Uma revisão documental não comprova funcionamento numa VPS real. O teste de ponta a ponta deve ocorrer na instalação da pessoa, durante o onboarding, usando os critérios acima.
