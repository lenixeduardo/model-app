# MODEL — fila sequencial de agentes

Atualização: 2026-11-11 (America/Sao_Paulo). Regra atual do usuário: prosseguir tela a tela, com quatro papéis enfileirados, e liberar a próxima tela somente com nota **superior a 9,0/10** na comparação visual. Meta: 9,5/10. A condição >9,0 é mais estrita que o >=9,0 do handoff anterior e governa esta fila. Nota exatamente 9,0 não libera avanço.

## Estado da fila

| Ordem | Tela | Estado | Dependência para iniciar |
|---|---|---|---|
| 1 | 03 — Swipe / Descobrir | **APROVADA VISUALMENTE:9,13/10**, V2 **2.0.0-prototipo.7**, auditor03 concluído com três capturas finais e comparação. Sem P1 material no perfil estático de Enzo; P2 e limite das legendas raster documentados. | Gate >9,0 atingido. Preservar pacote/evidências da versão aprovada e seguir para planejador04. |
| 2 | 04 — Perfil do modelo | **APROVADA VISUALMENTE:9,30/10**, V1 **1.0.0-prototipo.1**; auditor04 independente concluído, soma9,295 e nenhum P1 material. | Gate04>9,0 atingido; evidências e limites em MODEL_tela_04_V1/AUDITORIA.md. Preservar03/04 aprovadas; próximo papel planejador05. |
| 3 | 05 — Portfólio | **APROVADA VISUALMENTE:9,34/10**, V1 **1.0.0-prototipo.1**; auditor05 independente concluído, soma9,335 e nenhum P1 material. | Gate05>9,0 atingido; preservar03/04/05 e evidências. Próximo papel planejador06 LIBERADO. |
| 4 | 06 — Chat / Negociação | **APROVADA VISUALMENTE:9,28/10**, V1 **1.0.0-prototipo.1**; auditor06 independente concluído, soma9,275 e nenhum P1 material. | Gate06>9,0 atingido; preservar03/04/05/06 e evidências. Próximo papel planejador07 LIBERADO. |
| 5 | 07 — Castings | **APROVADA VISUALMENTE:9,32/10**, soma9,315; versão1.0.0-prototipo.2, auditor07 concluído sem P1 material. | Gate07>9,0 atingido; preservar03–07 e evidências. Próximo papel planejador08 LIBERADO. |
| 6 | 08 — Filtros | **APROVADA VISUALMENTE:9,23/10**, soma9,234615; versão1.0.0-prototipo.1, auditor08 independente concluído sem P1 material. | Gate08>9,0 atingido; fotografia N/A e rubrica normalizada. Preservar03–08; próximo papel planejador09 LIBERADO. |
| 7 | 09 — Salvos | **Planejador09 LIBERADO** pelo gate08 de9,23/10. | Seguir quatro papéis sequenciais; gate09 próprio antes de10. |
| 8 | 10 — Meu perfil | Aguardando gate09. | Auditoria09 documentada >9,0; depois planejador10. |
| 9 | 11 — Notificações | Aguardando gate10. | Auditoria10 documentada >9,0; depois planejador11. |

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

## Estágio06 — planejamento entregue

- Referência06 e mockup geral abertos; painel global `[1018,0,1174,404]`,156×404, confirmado RGB idêntico à referência (bbox de diferença=None).
- Geometria, redação/horas originais, card de campanha, avatares, escritório, ícones, tipografia nativa e limites de proporção em `MODEL_tela_06_V1/DESIGN_SPEC.md`; sequência em `MODEL_tela_06_V1/PLANO.md`.
- Interações locais: voltar05 aprovada, dialogs telefone/opções/detalhes/imagem/clipe e envio somente em memória; sem backend/envio externo, contato ou conteúdo oculto inventado.
- **Planejador06 concluído. Próximo papel: assets06 LIBERADO**, seguido de implementador06 e auditor06 independente. Sem assets novos, implementação, capturas, nota ou publicação nesta etapa;03/04/05 preservadas.
- Tela07 e seguintes aguardam gate próprio06>9,0; meta9,5.

## Estágio06 — assets entregues

- Quatro PNGs RGBA originais: header e dois avatares recebidos preservados separadamente, mais escritório134×44. Dois avatares pequenos mostram a mesma identidade visual, mas não são RGB idênticos; sem deduplicação presumida.
- Painel global[1018,0,1174,404] idêntico à referência; todos pixels com alpha>0 mantêm RGB original; RGB oculto zero. Máscaras geométricas conservadoras, sem reconstrução de pixels ou UI incorporada.
- Onze SVGs locais aproximados, títulos acessíveis; incertezas dos pequenos pictogramas documentadas. ASSETS.md, assets/manifest.json e assets/extract_assets.py registram hashes, boxes, testes e limites.
- **Assets06 concluído. Próximo papel: implementador06 LIBERADO**, depois auditor06 independente; gate06>9,0 ainda pendente.03/04/05 preservadas; sem interface, capturas, nota ou publicação neste papel.07 permanece bloqueada.

## Estágio06 — implementação entregue

- Versão1.0.0-prototipo.1 em `MODEL_tela_06_V1/`: HTML/CSS/JS nativos, assets originais separados, compositor somente em memória e dialogs locais; retorno real05.
- Candidata390 inspecionada antes das três capturas finais375×812,390×844,430×932. Testes Chromium DPR1 verdes; relatório, comparação proporcional, documentação e evidências entregues. Sem overflow inicial, erros de console/rede externa ou recursos ausentes no contexto normal; falha de fotos/reduced-motion verificada separadamente.
- **Implementador06 concluído. Próximo papel: auditor06 independente.** Nenhuma nota ou publicação;07 aguarda gate06>9,0. Pacotes03/04/05 preservados.

## Estágio06 — auditor independente concluído

- **APROVADA VISUALMENTE:9,28/10**, soma9,275; versão1.0.0-prototipo.1. Meta9,5 não atingida; gate>9,0 atingido e nenhum P1 material.
- Referência, três capturas raw e comparação abertas via view_image; dimensões, hashes atuais, colagem exata390 e RGB dos quatro crops conferidos independentemente.
- Evidência técnica do implementador revisada, sem segunda navegação/browser pelo auditor. P2: foto proporcional exige conteúdo de card compacto, último avatar≈20px alto, diferenças de fonte/ícones e acabamento. Limites completos em [AUDITORIA06](../MODEL_tela_06_V1/AUDITORIA.md).
- **Auditor06 concluído. Próximo papel: planejador07 LIBERADO.**03/04/05 preservadas; código/assets/capturas06 intactos; sem publicação ou início07 nesta auditoria. Registros anteriores de bloqueio06 são históricos e superados por esta decisão.

## Estágio07 — planejamento entregue

- Referência07 e mockup geral abertos; painel global `[11,434,212,751]`,201×317, confirmado RGB idêntico (bbox=None).
- Geometria, textos/datas/valores, três fotografias distintas, SVGs locais, adaptação sem distorção e interações em `MODEL_tela_07_V1/DESIGN_SPEC.md`; sequência TDD/implementação/capturas/auditoria em `MODEL_tela_07_V1/PLANO.md`.
- Filtros/saves/dialogs somente em memória; tabbar com cinco ícones originais, links03/06 aprovados e painéis locais honestos; sem iniciar02 ou08–11. Nenhuma seta de retorno inventada.
- **Planejador07 concluído. Próximo papel: assets07 LIBERADO**, depois implementador07 e auditor independente. Sem código, assets novos, capturas, nota ou publicação.03/04/05/06 preservadas.08 aguarda gate07>9,0, meta9,5.

## Estágio07 — assets entregues

- Três fotos originais independentes62×59,62×64,62×65; boxes refinados e provas separadas no manifest. Painel global[11,434,212,751] idêntico à referência; RGB visível idêntico ao JPEG, RGB oculto zero; cantos geométricos e matte residual documentados.
- Treze SVGs locais aproximados, incluindo cópias de04/06 por hash; sem glifos, legendas PNG ou UI embutida nas fotografias. ASSETS.md, assets/manifest.json e assets/extract_assets.py entregues e verificados.
- **Assets07 concluído. Próximo papel: implementador07 LIBERADO**, depois auditor independente; gate07>9,0 pendente, meta9,5.03–06 preservadas; sem interface, capturas, nota, publicação ou início08.

## Coordenação final — 2026-11-11 (America/Sao_Paulo)

07 retoma implementação; sua nota permanece pendente até auditoria independente das evidências finais. A fila executável08→09→10→11 e os quatro papéis por tela estão em [PLANO_ULTIMAS_QUATRO.md](PLANO_ULTIMAS_QUATRO.md). Essa coordenação não antecipa planejamento de conteúdo, assets ou implementação08.

A execução já está autorizada, incluindo dependências necessárias e publicação no GitHub do pacote correspondente à versão aprovada. Não exige nova reunião ou confirmação. O agente trabalha no workspace e não dispõe de capacidade para mudar o modo da interface ou transferir a sessão para ChatGPT Work.

## Estágio07 — implementação entregue

- Versão1.0.0-prototipo.1 em `MODEL_tela_07_V1/`: HTML/CSS/JS nativos, três fotos originais com cover proporcional e SVGs locais. Filtros, saves/reset, dialogs honestos, navegação03/06.
- Candidata390 aberta e espaçamento revisado; finais raw375×812/390×844/430×932 e comparação proporcional abertas. Chromium DPR1 e relatório JSON, SHA256SUMS e EVIDENCIAS.md entregues; limites de crop/resolução e da fase RED registrados.
- **Implementador07 concluído. Próximo papel: auditor07 independente.** Gate>9,0/meta9,5 pendente; sem nota própria ou publicação.03–06 preservadas.08–11 não iniciadas por este papel.

## Estágio07 — auditor independente concluído, correção necessária

- **NÃO APROVADA:8,76/10**, soma8,755, versão1.0.0-prototipo.1. Gate>9,0 não atingido; P1 material de enquadramento: cover preserva razão dos pixels, mas amplia cabeça/corpo37–39% e recorta27–28% da largura original nos três frames.
- Referência, três capturas e comparação abertas; RGB dos três crops originais, dimensões, hashes atuais e colagem390 conferidos independentemente. Relatório Chromium revisado, sem segunda renderização pelo auditor.
- Coordenadas, correção CSS e P2 do hash antigo da comparação no JSON em [AUDITORIA07](../MODEL_tela_07_V1/AUDITORIA.md). **Próximo papel: implementador07 para correção, nova versão/capturas e reauditoria.08 permanece aguardando.**
-03–06 preservadas; nenhum código, asset ou captura alterado, nenhuma publicação ou planejamento08 nesta auditoria.

## Estágio07 — revisão de implementação V2 entregue

- Auditoria V1 reprovou8,76 pelo P1 de crop. Versão1.0.0-prototipo.2 passa a mostrar os três frames integrais, com largura fluida/altura natural, mantendo âncoras, textos, cores e navbar.
- Regressão de área-fonte visível falhou na V1 (72,73% na foto01) e passou na V2 (100% nas três fotos/três viewports). Três finais raw e comparação atualizadas; hashes JSON/SHA256SUMS consistentes. V1 preservada em histórico.
- **Próximo papel: auditor07 independente para V2.** Sem nota própria/publicação;03–06 preservadas;08 não iniciada.

## Estágio07 — reauditoria V2 aprovada

- **APROVADA VISUALMENTE:9,32/10**, soma9,315, versão1.0.0-prototipo.2. Gate>9,0 atingido, meta9,5 não atingida; nenhum P1 material. A decisão negativa8,76 da V1 acima é histórica e foi superada após correção e novas capturas.
- Referência, três novas capturas V2 e comparação reabertas; enquadramentos integrais e proporção das três pessoas preservados. RGB dos crops, dimensões, hashes JSON/SHA256SUMS e colagem390 conferidos independentemente. Evidência Chromium atual revisada, sem segunda renderização/browser pelo auditor.
- P2: fotos proporcionais mais baixas que rows/metadados, fonte/ícones e matte/resolução do original. Escopo e hashes em [AUDITORIA07](../MODEL_tela_07_V1/AUDITORIA.md).
- **Auditor07 concluído. Próximo papel: planejador08 LIBERADO.**03–06 preservadas; código/assets/capturas07 intactos na auditoria. Não houve publicação ou início de conteúdo08 por este papel.

## Estágio08 — planejamento entregue

- Referência08 e original abertos; crop global[220,434,420,751],200×317, confirmado RGB idêntico(bbox=None). Geometria, textos, estados, faixas e contratos locais em `MODEL_tela_08_V1/DESIGN_SPEC.md`; execução em `MODEL_tela_08_V1/PLANO.md`.
- Sem fotografias: rubrica08 registra fotografia N/A e normaliza65% restantes(25geometria/20tipografia/10cores/10responsividade), sem10 gratuito ou alteração das notas anteriores.
- **Planejador08 concluído. Próximo papel: assets08 LIBERADO**, depois implementador08 e auditor independente. Gate08>9,0, meta9,5;09–11 aguardam.03–07 preservadas; sem assets novos, código, capturas, nota ou publicação neste papel.

## Estágio08 — assets entregues

- Referência200×317 e original1179×753 abertos com zoom; crop global[220,434,420,751] RGB idêntico comprovado. Sem fotografia, fotografia N/A e rubrica normalizada conforme DESIGN_SPEC. Nenhum PNG de interface ou fotografia produzido.
- Seis SVGs aproximados: voltar, lupa do campo(location.svg), chevron, celular, Wi-Fi e bateria. Cinco cópias byte idênticas06/07 e chevron novo, com hashes/proveniência; cores exatas amostradas, boxes e limites JPEG em ASSETS.md/assets/manifest.json. Script prepare_assets.py reproduz prova e inventário.
- **Assets08 concluído. Próximo papel: implementador08 LIBERADO**, depois auditor independente. Gate08>9,0 pendente, meta9,5.03–07 preservadas; sem código de interface, capturas, nota, publicação ou início09.


## Estágio08 — auditor independente concluído

- **APROVADA VISUALMENTE:9,23/10**, soma9,234615; versão1.0.0-prototipo.1. Gate>9,0 atingido, meta9,5 não atingida; nenhum P1 material. Fotografia N/A, rubrica (25G+20T+10C+10R)/65 sem nota gratuita.
- Referência, três capturas e comparação abertas via view_image; dimensões e11 hashes conferidos. Logs/scripts Chromium156/DPR1 revisados, sem segunda sessão de browser ou recaptura independente.
- P2 e limites: fonte/ícones aproximados, thumb idade≈7px deslocado na390, preenchimento negativo quando altura inferior fica abaixo do domínio visual inicial, clamp dos sliders e cobertura parcial de acessibilidade/rede no script. Detalhes e hashes em [AUDITORIA08](../MODEL_tela_08_V1/AUDITORIA.md).
- **Auditor08 concluído. Próximo papel: planejador09 LIBERADO.**03–07 e código/assets/capturas08 preservados; sem publicação ou planejamento09 neste papel. Registros anteriores de pendência08 são históricos, superados por esta decisão.
