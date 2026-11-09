# MODEL — fila sequencial de agentes

Atualização: 2026-11-09. Regra atual do usuário: prosseguir tela a tela, com quatro papéis enfileirados, e liberar a próxima tela somente com nota **superior a 9,0/10** na comparação visual. Meta: 9,5/10. A condição >9,0 é mais estrita que o >=9,0 do handoff anterior e governa esta fila. Nota exatamente 9,0 não libera avanço.

## Estado da fila

| Ordem | Tela | Estado | Dependência para iniciar |
|---|---|---|---|
| 1 | 03 — Swipe / Descobrir | **APROVADA VISUALMENTE:9,13/10**, V2 **2.0.0-prototipo.7**, auditor03 concluído com três capturas finais e comparação. Sem P1 material no perfil estático de Enzo; P2 e limite das legendas raster documentados. | Gate >9,0 atingido. Preservar pacote/evidências da versão aprovada e seguir para planejador04. |
| 2 | 04 — Perfil do modelo | **APROVADA VISUALMENTE:9,30/10**, V1 **1.0.0-prototipo.1**; auditor04 independente concluído, soma9,295 e nenhum P1 material. | Gate04>9,0 atingido; evidências e limites em MODEL_tela_04_V1/AUDITORIA.md. Preservar03/04 aprovadas; próximo papel planejador05. |
| 3 | 05 — Portfólio | **APROVADA VISUALMENTE:9,34/10**, V1 **1.0.0-prototipo.1**; auditor05 independente concluído, soma9,335 e nenhum P1 material. | Gate05>9,0 atingido; preservar03/04/05 e evidências. Próximo papel planejador06 LIBERADO. |
| 4 | 06 — Chat / Negociação | **Planejamento LIBERADO; não iniciado.** | Tela05 aprovada9,34/10; iniciar pelo planejador06. |
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

## Registro atual — auditor03 ciclo7

- Versão avaliada: `MODEL_tela_03_V2/VERSION`, **2.0.0-prototipo.7**.
- Evidências: três capturas reais375×812,390×844,430×932, comparação390 e relatório final`passed` no Chromium156/DPR1. O auditor abriu as imagens finais e conferiu seus hashes.
- Auditoria atual: [APROVADA VISUALMENTE —9,13/10](../MODEL_tela_03_V2/AUDITORIA.md). Soma ponderada9,125; gate **>9,0** atingido, meta9,5 ainda não atingida.
- Assets03: fotografia203×404 com lacunas e torso genuíno; nome/localização em foregrounds deUIpor contorno, separados da foto, com matte contextual de1px documentado. Não há anatomia sintetizada ou referência integral usada como fundo com texto intacto.
- Limite do aceite: protótipo estático de Enzo. As legendas raster não são fonte genérica; H1/P semânticos e fallback nativo atômico existem para falha/opt-out/textos divergentes. Dados arbitrários ou modo nativo exigem revalidação visual, sem reaproveitar bitmap com outra semântica.
- **Estágio auditor03: concluído e aprovado.** P1 de legendas/informação resolvido materialmente nas capturas atuais. Permanecem P2 de borda do selo, acabamento dos chips, margem da informação e céu/base uniformes; sem bloqueador material do perfil estático.
- **Próxima ação: planejador04.** Tela04 está liberada para seu planejamento e implementação. O auditor não iniciou essa etapa nem publicou a V2; o coordenador deve preservar/publicar código, assets e evidências correspondentes à versão aprovada.
- Histórico: ciclo4:7,84; ciclo5:8,72; ciclo6:8,92; ciclo7:9,13. A nota7 não decorre do progresso obrigatório: as imagens finais foram avaliadas novamente. Ela não se transfere à Tela04 ou a qualquer outra implementação.
- As telas05–11 continuam aguardando seus gates sequenciais próprios.

## Estágio04 — planejamento entregue

- Referência04 e mockup geral abertos; medidas, conteúdo legível e incertezas documentados em `MODEL_tela_04_V1/DESIGN_SPEC.md`.
- Plano executável em `MODEL_tela_04_V1/PLANO.md`; sem código, assets novos ou nota nesta etapa.
- Assets04 concluído: hero monocromático correto e três thumbs completas+quarta parcial extraídos, seis SVGs locais e máscaras/proveniência em `MODEL_tela_04_V1/ASSETS.md` e `assets/manifest.json`. Tipografia sobre branco permanece nativa.
- Próximo papel: implementador04, seguido de auditor04 independente. A aprovação da03 não é nota da04; gate04 permanece>9,0.
- Tela05 e seguintes aguardam o gate próprio04; nenhum conteúdo05 foi planejado.

## Estágio04 — implementação técnica pronta

- Versão `1.0.0-prototipo.1`: HTML/CSS/JS independentes em `MODEL_tela_04_V1/`; assets recebidos preservados, bio com “editoriais”, sem alterações à03 aprovada.
- Candidato390 inspecionado antes das três capturas finais375×812,390×844,430×932. `render.py`, `compare.py`, `relatorio-browser.json` e `comparacao-390.png` entregues; testes de carregamento/console/rede/overflow/alvos/ações/foco/back passaram no Chromium real DPR1.
- Próximo papel: **auditor04 independente**. Sem nota ou publicação nesta etapa. Tela05 permanece bloqueada até gate04>9,0 e ausência de bloqueadores.

## Estágio04 — auditor independente concluído

- **APROVADA VISUALMENTE:9,30/10**, soma ponderada9,295; versão1.0.0-prototipo.1. Meta9,5 não atingida; gate>9,0 atingido, nenhum P1 material.
- Auditor abriu referência04, três screenshots reais e comparação; conferiu dimensões, hashes, correspondência integral da captura390 com a comparação e RGB preservado dos cinco crops. Relatório técnico do implementador revisado; não houve reteste independente em browser.
- Evidências, notas, P2 de contador/tipografia/ícones e limites de safe-area/dispositivos em [AUDITORIA04](../MODEL_tela_04_V1/AUDITORIA.md). Nenhum código, asset, screenshot ou arquivo03 foi alterado nesta auditoria.
- **Próximo papel: planejador05**, autorizado pelo gate04. A05 não foi iniciada e não houve publicação. Registros anteriores de bloqueio04 acima são históricos e ficam superados por esta decisão.

## Estágio05 — planejamento entregue

- Referência05 e original abertos; painel global `[836,0,1008,404]` confirmado pixel a pixel. Sete regiões fotográficas visíveis: cinco caixas completas e duas parciais inferiores; sem contador total no estado inicial.
- Geometria, conteúdo, coordenadas, limites fotográficos e interações locais em `MODEL_tela_05_V1/DESIGN_SPEC.md`; sequência verificável em `MODEL_tela_05_V1/PLANO.md`.
- **Próximo papel: assets05**, depois implementador05 e auditor05 independente. Não foram gerados assets, implementação, capturas ou nota.03/04 aprovadas preservadas.
- Tela06 e seguintes aguardam gate próprio05>9,0; meta9,5.

## Estágio05 — assets entregues

- Sete PNGs RGBA: cinco caixas completas e dois parciais inferiores, RGB idêntico aos crops do JPEG oficial; somente alpha geométrico de borda. Painel `[836,0,1008,404]` confirmado idêntico à referência.
- Coordenadas refinadas, limites, dimensões, proveniência e hashes integrais em `MODEL_tela_05_V1/ASSETS.md` e `assets/manifest.json`; extração reproduzível em `assets/extract_assets.py`. Três SVGs locais; título/abas/hora ficam nativos.
- **Próximo papel: implementador05**, depois auditor independente. Sem fotografias sintetizadas, código de interface, capturas, nota ou publicação.03/04 preservadas. Tela06 aguarda gate05>9,0; meta9,5.

## Estágio05 — auditor independente concluído

- **APROVADA VISUALMENTE:9,34/10**, soma9,335; versão1.0.0-prototipo.1. Meta9,5 não atingida, gate>9,0 atingido e nenhum P1 material.
- Referência, três screenshots e comparação abertos via view_image; dimensões raw, hashes e colagem conferidos. Sete crops RGB idênticos à fonte oficial, cinco caixas completas e dois parciais, sem extensão inventada.
- Relatório real do implementador revisado; auditor não executou segunda renderização/browser. P2 e limites em [AUDITORIA05](../MODEL_tela_05_V1/AUDITORIA.md).
- **Estágio auditor05 concluído. Próximo papel: planejador06 LIBERADO.** Nenhum planejamento06, publicação ou alteração03/04 realizada pelo auditor. Registros anteriores de bloqueio05 são históricos, superados por esta decisão.
