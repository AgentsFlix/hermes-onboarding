# Maton AI e Zernio com as chaves do hPanel

## Chaves existentes

Este fluxo parte de `MATON_API_KEY` e `ZERNIO_API_KEY` já configuradas. Não repita os exemplos dos READMEs das skills que pedem uma chave no chat ou mandam salvá-la no `.env`.

Verifique somente se cada variável está não vazia no ambiente real em que os scripts da skill vão executar. Um exemplo, depois de confirmar que o terminal pertence ao ambiente correto:

```python
import os
for name in ("MATON_API_KEY", "ZERNIO_API_KEY"):
    print(name + ": " + ("presente" if os.environ.get(name, "").strip() else "ausente"))
```

Não use o resultado de um terminal isolado como prova sobre o processo do Hermes. Se a variável estiver ausente nesse contexto, identifique a diferença sem ler seu valor. Oriente a pessoa a conferir se as variáveis foram salvas/aplicadas no aplicativo Hermes correto no hPanel. Se o painel exigir reaplicação ou reinício, explique que a sessão pode cair e deixe a pessoa concluir essa ação. Depois, repita a checagem no ambiente de execução.

Não copie chaves do hPanel, do processo ou de um `.env` para outro arquivo. Não preencha valores vazios. Presença não prova validade nem que haja contas conectadas.

## Instalação

Use as ferramentas de skills da versão instalada, no usuário e perfil ativos. No Telegram, priorize a rota nativa abaixo. O CLI é uma alternativa, não um pré-requisito. As versões de referência são:

| Skill | Versão | Commit |
|---|---|---|
| maton-operations | v0.2.0 | `4a0365654442ae7b5b26c7e07c337cab5da1fc59` |
| zernio-operations | v1.0.0 | `44efdb3458cf0f14623c74632f53e50e69d6bf91` |

### Rota nativa da conversa, inclusive Telegram

1. Descubra as ferramentas expostas na sessão e consulte seus schemas. Use `skills_list` para verificar o que já existe e `skill_view` para inspecionar uma skill existente. A lista de skills ativas não é uma lista do que você pode instalar.
2. Se houver ferramenta nativa do hub para importar uma URL com scanner, use-a com a revisão fixa abaixo. Caso a sessão exponha `skill_manage`, ela permite adicionar o conteúdo da skill sem executar `hermes` no terminal.
3. Leia o `SKILL.md` e todos os arquivos de apoio da revisão fixa pelos recursos de leitura web/arquivos disponíveis. Preserve o conteúdo integral, não resuma nem recrie a skill a partir da descrição. Não execute o conteúdo durante a importação.
4. Para uma skill ausente, use a operação `create` de `skill_manage` com nome e conteúdo completo, depois `write_file` para cada arquivo de apoio, com caminhos relativos à skill. Siga o schema real: algumas versões usam operações individuais, outras um lote `ops`. Não existe garantia de uma ação `install` nessa ferramenta.
5. Preserve verificações de conteúdo e aprovação da ferramenta. Uma escrita apenas proposta ou pendente não conta como instalação concluída. Não use a rota nativa para contornar uma recusa do scanner ou de permissões de outra rota. As verificações de `skill_manage` e do hub podem diferir; registre a rota usada e não afirme que houve scan do hub quando ele não ocorreu.
6. Releia a skill e cada arquivo salvo pelas ferramentas nativas e compare com a origem. Confirme a descoberta por `skills_list`/`skill_view`. Instalação incompleta fica pendente; não declare conclusão só porque o `SKILL.md` foi criado.

Os arquivos de apoio obrigatórios estão listados abaixo. Resolva scripts e referências a partir da pasta da skill na mesma revisão da URL, preservando caminhos e bytes. A política Zernio externa à pasta da skill continua sendo uma referência obrigatória de leitura, no link indicado abaixo.

Se as ferramentas nativas realmente não estiverem expostas, use o CLI somente se ele estiver disponível no ambiente correto. Se nenhuma rota existir, informe quais ferramentas foram procuradas e a operação impossível. Não reinstale Hermes, não altere o gateway e não peça SSH como primeira resposta. Concluir a instalação e não poder executar os scripts no terminal são resultados distintos.

### Rota de CLI, quando disponível

Com o CLI disponível no ambiente correto:

```bash
hermes skills list
hermes skills install --help
hermes skills install https://raw.githubusercontent.com/AgentsFlix/hermes-maton/4a0365654442ae7b5b26c7e07c337cab5da1fc59/skills/integrations/maton-operations/SKILL.md
hermes skills install https://raw.githubusercontent.com/AgentsFlix/hermes-zernio/44efdb3458cf0f14623c74632f53e50e69d6bf91/skills/integrations/zernio-operations/SKILL.md
hermes skills list
```

Execute um comando por vez e verifique o resultado. Se o instalador pedir confirmação normal de instalação, ela faz parte do pedido. Use opções não interativas apenas se a ajuda local confirmar suporte e elas não dispensarem o scanner. Não use `--force`, não desabilite verificações, não copie manualmente um pacote bloqueado para a pasta de skills.

Antes de instalar, confira se a skill já existe. Se for a mesma revisão e estiver completa, preserve. Se for customizada, diferente ou mais nova, não sobrescreva nem rebaixe: informe a diferença e preserve até uma decisão específica. O número no frontmatter pode diferir da tag; confira a origem registrada e o hash quando disponíveis.

O instalador precisa trazer os arquivos de apoio referenciados. Depois da instalação, confira os arquivos no caminho real retornado pelo Hermes:

- Maton: `SKILL.md`, `scripts/inventory_maton.py`, `references/capability-map.md` e `references/action-classification.yaml`.
- Zernio: `SKILL.md`, `scripts/inventory_zernio.py` e `references/capability-map.md`.

Leia também a [política Zernio da mesma revisão](https://raw.githubusercontent.com/AgentsFlix/hermes-zernio/44efdb3458cf0f14623c74632f53e50e69d6bf91/policies/action-classification.yaml). Ela fica na raiz do repositório upstream e pode não ser copiada pelo instalador. Não invente que está instalada. Se não conseguir ler uma referência obrigatória ou faltar script, marque a skill incompleta; não rode código inventado para compensar nem atualize o Hermes neste onboarding.

## Inventário somente em leitura

Leia as duas skills e os scripts antes de executá-los. Rode cada script a partir do caminho instalado e com as variáveis herdadas do ambiente correto, sem expandir segredos em argumentos. Não instale SDKs ou MCPs adicionais para este onboarding.

- Maton: `scripts/inventory_maton.py`, chamadas GET de conexões e triggers.
- Zernio: `scripts/inventory_zernio.py`, chamadas GET de perfis, contas, posts e configuração de webhooks.

O script Zernio aceita `ZERNIO_API_URL`. Antes de executá-lo, confira por comparação booleana, sem imprimir o valor, que está ausente ou aponta exatamente para `https://zernio.com/api/v1` (com ou sem barra final). Se houver outro destino, pare a validação Zernio e informe divergência de endpoint. Não envie a chave para um destino alternativo.

Capture stdout e stderr da execução sem devolvê-los diretamente ao chat ou aos logs de ferramentas. Analise o JSON localmente e retorne apenas campos permitidos: estados, apps/plataformas, contagens e códigos HTTP numéricos. Ignore campos livres como `error` e `message`; em falha de parsing, informe apenas falha de leitura do resultado. Não execute com logs verbosos. Não exponha respostas brutas da API ou exceções que possam incluir conteúdo sensível. Os scripts retornam resumos; ainda assim, entregue somente estados, apps/plataformas e contagens, sem nomes pessoais, IDs, URLs de webhook ou conteúdo de posts. Se o código disponível não garantir uma saída segura no ambiente observado, marque a validação pendente.

Verifique os erros por endpoint, não apenas o código de saída ou o campo `ok`: o inventário Zernio pode ter sucesso parcial; uma conta vazia não significa necessariamente chave inválida. HTTP 401 indica falha de autenticação; 403 indica acesso recusado e pode ser restrição de escopo/plano. Rede, 429 e 5xx ficam como indisponibilidade temporária. Não invente sucesso ou classificação sem evidência.

Conta sem conexão ativa continua sem conexão. Não crie conexão, OAuth, trigger, webhook, post, mensagem, agenda ou automação como teste. Informe o que ficou disponível e o que precisa de um pedido posterior.

Fontes: [skills do Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/), [Maton](https://github.com/AgentsFlix/hermes-maton/tree/v0.2.0), [Zernio](https://github.com/AgentsFlix/hermes-zernio/tree/v1.0.0).
