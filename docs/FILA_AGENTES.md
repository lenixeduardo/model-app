# MODEL — fila sequencial de agentes

Atualização: 2026-11-09. Regra atual do usuário: prosseguir tela a tela, com quatro papéis enfileirados, e liberar a próxima tela somente com nota **superior a 9,0/10** na comparação visual. Meta: 9,5/10. A condição >9,0 é mais estrita que o >=9,0 do handoff anterior e governa esta fila. Nota exatamente 9,0 não libera avanço.

## Estado da fila

| Ordem | Tela | Estado | Dependência para iniciar |
|---|---|---|---|
| 1 | 03 — Swipe / Descobrir | V2 2.0.0-prototipo.4 funcional e capturada; auditor03 concluído no ciclo4: **7,84/10, não aprovada**. Revisão de assets confirmou ausência da fotografia integral limpa. X/selo/chips refinados e auditados; não resolvem o torso ausente. Fila pausada nesta tela. | Retomar em assets03 somente após receber/verificar a foto integral limpa do mesmo retrato. Plano registrado em [PLANO_REVISAO.md](../MODEL_tela_03_V2/PLANO_REVISAO.md). |
| 2 | 04 — Perfil do modelo | Aguardando gate da Tela 03; conteúdo não planejado e implementação não iniciada nesta fila. | Aprovação documentada da Tela 03, nota >9,0, evidências completas. |
| 3 | 05 — Portfólio | Não iniciada. | Aprovação documentada da Tela 04. |
| 4 | 06 — Chat / Negociação | Não iniciada. | Aprovação documentada da Tela 05. |
| 5 | 07 — Castings | Não iniciada. | Aprovação documentada da Tela 06. |
| 6 | 08 — Filtros | Não iniciada. | Aprovação documentada da Tela 07. |
| 7 | 09 — Salvos | Não iniciada. | Aprovação documentada da Tela 08. |
| 8 | 10 — Meu perfil | Não iniciada. | Aprovação documentada da Tela 09. |
| 9 | 11 — Notificações | Não iniciada. | Aprovação documentada da Tela 10. |

As telas 01/02 não integram esta fila de continuidade iniciada na 03. Os recortes já existentes das telas seguintes são referências; sua existência não significa planejamento, implementação ou aprovação.

## Ordem de execução por tela

**Planejador → agente de assets → implementador → auditor independente.** Os papéis trabalham em sequência para a mesma tela. Não despachar implementação antes das entregas de planejamento/assets aplicáveis; não iniciar uma tela posterior enquanto a atual não atravessar o gate. O agente responsável por um papel não se autoaprova no papel de auditor da própria implementação.

| Papel | Trabalho | Entrega que libera o próximo papel |
|---|---|---|
| Planejador | Abrir a referência oficial, conferir implementação e última auditoria, medir proporções e separar requisitos verificáveis de limitações dos insumos. | `DESIGN_SPEC.md` e plano de revisão com arquivos, critérios, mudanças permitidas e bloqueios. |
| Assets | Inventariar origens, identidade, resolução, proporção e pixels encobertos. Extrair recortes fiéis e produzir vetores locais que o mockup justifique. | `ASSETS.md` com proveniência, medidas, classificação de cada arquivo, assets independentes utilizáveis e lista explícita do que falta. A fotografia insuficiente gera bloqueio, não um substituto. |
| Implementador | Usar os assets aprovados, implementar a tela sem alterar identidade/composição, conferir interação/acessibilidade/safe areas e executar os testes no navegador. | Código separado, `CHANGELOG.md`, três capturas reais finais, relatório de console/rede/overflow/interações e comparação normalizada. |
| Auditor independente | Abrir referência, capturas e comparação; confrontar o que está visível com o contrato e revisar resultados técnicos. | `AUDITORIA.md` com pesos/notas, diferenças concretas, hashes das imagens avaliadas, bloqueios e decisão fundamentada. |

## Gate de avanço

Todas as condições abaixo são cumulativas:

1. Capturas reais da versão final em **375×812**, **390×844** e **430×932**, com navegador, DPR, procedimento e versão documentados. Recorte do mockup não é screenshot do aplicativo.
2. Comparação da captura de 390 com a referência, alturas normalizadas sem deformar a proporção de nenhuma das imagens.
3. Nenhuma falha de carregamento da fotografia ou dos SVGs, distorção anatômica, overflow indevido ou glifo substituto; cliques/toques exigidos, foco visível e alvos de toque conferidos.
4. `AUDITORIA.md` avalia as imagens finais, com fotografia/identidade/enquadramento **35%**, geometria **25%**, tipografia/ícones/chips **20%**, cores/contraste/sobreposição **10%**, responsividade/acabamento **10%**. Nota final é a soma ponderada e deve ser **>9,0**. Meta 9,5.
5. Código, assets independentes, especificação, changelog, auditoria, capturas e comparação correspondem à mesma versão e estão no pacote versionado. Publicação incompleta deve ser registrada, sem declarar que os arquivos ausentes estão no repositório.
6. Não há bloqueador material de fidelidade, mesmo que uma média ultrapasse o limiar. A decisão do auditor não se baseia somente no código ou em testes técnicos.

O agente auditor documenta a estimativa visual; não se trata de uma métrica pixel-perfect automatizada. Não elevar a nota para cumprir a fila. Uma nova implementação exige nova captura e nova auditoria; não reutilizar nota ou screenshot de uma versão anterior como prova da atual.

## Ciclo de correção e bloqueio

- Auditoria abaixo do gate, com diferença corrigível e insumos suficientes: devolver apontamentos ao planejador/assets/implementador responsável, corrigir somente o necessário, recapturar os três tamanhos e reauditar.
- Ausência de fotografia original suficiente, navegador sem captura após estratégias permitidas ou outra dependência incontornável: registrar erro/insumo faltante, evidência reproduzível e condição concreta de retomada. Pausar a fila na tela atual.
- Não iniciar ciclos cosméticos infinitos quando o bloqueio fotográfico impede atingir o gate. Melhorias técnicas podem ser entregues como versão não aprovada, com esse estado explícito.
- Recebido o insumo faltante, o agente de assets valida a origem e a adequação antes de devolver à implementação. Só a nova auditoria pode liberar a próxima tela.

## Limites de criação de assets

Preservar Enzo e o retrato oficial. Não substituir por outra pessoa ou por outra fotografia. Não inventar corpo, textura, pixels ocultos, rótulos, abas ou decoração para aparentar fidelidade. Recortes preservam proporção e registram coordenadas; SVGs reconstruídos são identificados como aproximações vetoriais. Ampliar uma imagem não recupera detalhe inexistente. A referência completa com textos/controles incorporados não pode ser usada como fundo para simular uma implementação independente.

A autorização de gerar assets não é prova de que existe a fotografia integral. A autorização de publicação também não altera a nota ou resolve uma lacuna visual. Restrições de ferramenta/publicação devem ser registradas separadamente da fidelidade.

## Registro atual

- Evidências da V2: `MODEL_tela_03_V2/captura-375.png`, `captura-390.png`, `captura-430.png`, `comparacao-390.png`, `relatorio-browser.json`.
- Auditoria independente atual: [7,84/10 — ciclo4 não aprovado](../MODEL_tela_03_V2/AUDITORIA.md).
- Condição de retomada principal: fotografia limpa e integral do **mesmo retrato** de Enzo, contendo céu/ombros/torso necessários à composição, ou constatação documentada de que um arquivo já fornecido realmente contém essa informação sem interface incorporada.
- Assets03: revisão concluída em `MODEL_tela_03_V2/ASSETS.md`; variante independente `assets/icons/fechar-acao.svg` entregue. Nenhuma fonte local contém o torso integral limpo. A implementação pode avaliar o refinamento vetorial como protótipo não aprovado; a fotografia suficiente permanece pendente.
- Implementação03: ciclo4 concluído tecnicamente, com refinamentos de X/selo/chips e três capturas finais novas. render.py passou; comparação regenerada.
- **Estágio auditor03: concluído.** Referência, três capturas finais e comparação foram abertas; hashes conferidos no relatório. Decisão final: **7,84/10, não aprovado**. O gate >9,0 não foi atingido; nota exatamente9,0 também não liberaria.
- **Próxima ação: aguardar o insumo fotográfico e retomar em assets03.** Novos ciclos cosméticos não se justificam como caminho ao gate: o torso ausente não é recuperável por CSS/ícones. Não iniciar planejamento de conteúdo ou implementação da Tela04.
