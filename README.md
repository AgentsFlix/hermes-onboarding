# Onboarding do Hermes | AgentFlix

Seu Hermes já está funcionando. Agora ele vai conhecer você e ganhar as skills de Maton AI e Zernio.

## Como usar

Abra a conversa do seu Hermes, no painel ou canal que você já usa, e cole o conteúdo de [PROMPT.md](PROMPT.md). Ele vai ler este repositório e conduzir a configuração. Não precisa clonar no seu computador.

Você precisa ter o Hermes respondendo e as variáveis `MATON_API_KEY` e `ZERNIO_API_KEY` já configuradas no hPanel da Hostinger. O Hermes precisa conseguir ler este repositório e acessar os arquivos e as ferramentas da própria instalação. Se esse acesso estiver indisponível, ele informa a etapa pendente.

## O que acontece

1. O Hermes identifica o perfil e a pasta de dados que estão em uso.
2. Pergunta como chamar você, nome do agente, trabalho, tom, idioma/fuso e primeira tarefa. Aproveita respostas já conhecidas.
3. Mostra a proposta de identidade e preferências. Depois do seu ok, faz backup local e salva somente as mudanças combinadas.
4. Instala `maton-operations` e `zernio-operations` com a verificação de segurança do Hermes.
5. Confere as chaves existentes e faz um inventário de leitura das integrações. Entrega o que está pronto e o que depende de você.

As chaves ficam onde você já configurou. Se uma variável não chegar ao ambiente das ferramentas, o Hermes orienta a conferir sua aplicação no hPanel, sem pedir a chave pelo chat.

A primeira tarefa serve para orientar a configuração. Enviar mensagens, publicar, agendar, conectar contas ou criar automações exige um pedido específico depois do onboarding.

## Arquivos

- [PROMPT.md](PROMPT.md): texto para copiar.
- [AGENTS.md](AGENTS.md): procedimento do agente.
- [Identidade](docs/identidade.md): perguntas, prévia, gravação e recuperação.
- [Integrações](docs/integracoes.md): versões, instalação, chaves existentes e validação.
- [Validação](docs/validacao.md): critérios de conclusão e cenários de revisão.

Este repositório contém instruções de onboarding. Não instala o Hermes, não provisiona VPS e não guarda respostas pessoais. Para desenvolvimento do repositório, siga [CONTRIBUTING.md](CONTRIBUTING.md).
