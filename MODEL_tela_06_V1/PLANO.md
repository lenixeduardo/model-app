# Tela06 — Chat / Negociação Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking. Execução já autorizada pelo usuário: assets → implementador → auditor independente, sem nova confirmação. Este planejador não implementa nem despacha subagentes.

**Goal:** Reproduzir a conversa06 com os assets originais e interações honestas em memória.

**Architecture:** Pacote frontend independente na pasta06; assets locais com proveniência e UI semântica nativa. Estado JS transitório apenas para mensagens/dialogs, sem backend ou publicação.

**Tech Stack:** HTML, CSS, JavaScript, PNG/RGBA e SVG locais; navegador real DPR1 para validação.

**Spec:** [DESIGN_SPEC.md](DESIGN_SPEC.md).

## Global Constraints

- Preservar integralmente03/04/05 aprovadas; não iniciar07. Gate06>9,0, meta9,5.
- Estado inicial segue texto/horas/fotos/card da fonte; Arial nativa, sem rasterizar textos de UI.
- Fotos sem síntese/extensão/reidentificação; provar RGB e coordenadas. Não usar screenshot inteiro como interface.
- Viewports375×812,390×844,430×932 DPR1; fotos proporcionais, alvos44px, foco/Escape/reduced-motion.
- Sem rede externa, chamada telefônica, upload, backend, recibo ou resposta automática; envio somente memória.

## Review Focus

- Foto baixa resolução e discos pequenos: pixels opacos iguais à fonte, nenhuma pessoa trocada ou UI incorporada.
- Razão156/404 versus telas maiores: escritório sem distorção e card sem colisão entre texto/CTA.
- Mensagem longa, vazia ou com HTML: envio seguro, quebra de linha, scroll correto, sem criar backend/recibo.
- Dialogs e teclado: Escape/fechar/foco contido/restaurado, sem ativar chamada externa.
- Viewport menor/falha de imagem: compositor utilizável, fallback local honesto, sem overflow ou ícone quebrado.

---

### Task1 — Assets06 verificáveis (próximo papel)

**Files:** criar `MODEL_tela_06_V1/ASSETS.md`, `assets/manifest.json`, `assets/extract_assets.py`, PNGs de avatar/escritório e SVGs locais descritos na spec. Não criar interface nesta tarefa.

**Interfaces:** consome painel RGB[1018,0,1174,404] do JPEG oficial; produz paths estáveis, boxes finais, dimensões, hashes, limites e classificação dos arquivos para implementação.

- [x] Conferir novamente bbox RGB=None para o painel inteiro e refinar boxes fotográficos da spec, excluindo UI.
- [x] Extrair escritório e três discos de avatar; só deduplicar discos se repetição de origem comprovada. Registrar limites reais/alpha/matte, sem completar cantos ou pixels ocultos.
- [x] Criar SVGs locais finos conforme lista da spec; identificar aproximações, sem emojis/fontes remotas.
- [x] Executar prova RGB em todos pixels opacos contra crops de origem; reportar igualdade e hashes. Abrir os arquivos para verificar ausência de texto/balão/CTA incorporado.
- [x] Entregar ASSETS/manifest/script e declarar bloqueio se fotografia suficiente não puder ser isolada. Não substituir pessoa ou foto. Liberar implementador somente após entrega utilizável.

### Task2 — Interface06 e estado local

**Files:** criar `MODEL_tela_06_V1/index.html`, `styles.css`, `app.js`, `VERSION`, `CHANGELOG.md`, `README.md`; consumir assets de Task1 sem alterar03/04/05.

**Interfaces:** `app.js` mantém `messages` somente em memória; formulário adiciona `{text, time}` após trim não vazio. Dialogs compartilham abrir/fechar com restauração de foco; markup semântico e texto via textContent. Paths exatos dos assets vêm do manifest entregue.

- [x] Construir status/header/conversa/card/compositor com todos textos e horas da spec; link voltar05 real. Conferir leitura das três mensagens e ausência de conteúdo extra inicial.
- [x] Aplicar geometria fluida e Arial; manter proporção do escritório/avatar, calibrar altura card e espaços sem escala anisotrópica das fotos. Conferir375/390/430 sem colisão.
- [x] Implementar dialogs locais telefone/opções/detalhes/imagem/clipe: mesmos dados visíveis, explicação de protótipo dentro do dialog, nenhum contato/briefing inventado.
- [x] Implementar envio em memória com Enter/botão e scroll da conversa; vazio não adiciona, HTML aparece como texto, input mantém foco, reload restaura estado original. Nenhuma resposta/recibo inventado.
- [x] Conferir teclado/labels/alvos>=44px sem sobreposição; Escape/fechar/foco; reduced-motion; falhas locais de imagem/SVG e viewport menor mantêm controles utilizáveis.

### Task3 — Verificação e capturas da versão final

**Files:** criar `MODEL_tela_06_V1/render.py`, `compare.py`, `relatorio-browser.json`, `screenshots/375x812.png`, `screenshots/390x844.png`, `screenshots/430x932.png`, `comparacao-390.png`; atualizar CHANGELOG/README/VERSION com versão real e procedimento.

**Interfaces:** consome pacote final Task2 e referência oficial; produz screenshots de navegador reais e relatório reproduzível da mesma versão. Reutilizar padrões de ferramentas anteriores somente lendo-os; não alterar os pacotes aprovados.

- [x] Servir raiz model-app localmente; executar render.py em Chromium real DPR1 e documentar comando/versão. Carregar06 com rede externa desabilitada; zero assets ausentes, console errors e overflow horizontal.
- [x] Verificar telefone/opções/detalhes/foto/clipe por clique/teclado, Escape e restauração de foco; voltar abre05 aprovada. Confirmar ausência de navegação/chamada/upload externos.
- [x] Verificar envio vazio, texto comum, texto longo e `<img onerror=alert(1)>`: texto literal, uma nova bolha por envio válido, sem execução HTML, sem resposta/recibo, conversa rolável e reload limpo.
- [x] Capturar estado inicial limpo nos três tamanhos após fontes/assets carregarem; não usar estado com mensagem nova para prova visual inicial. Abrir e inspecionar capturas antes de entregar.
- [x] Executar compare.py: alinhar referência e screenshot390 por altura igual, conservar proporções individuais e rotular dimensões. Foto não pode ser esticada para “encaixar” na comparação.
- [x] Registrar hashes/versionamento das imagens e limites; entregar ao auditor independente. Nenhuma nota do implementador ou publicação.

### Task4 — Auditor independente e gate06

**Files:** criar `MODEL_tela_06_V1/AUDITORIA.md`; atualizar `docs/FILA_AGENTES.md` após decisão fundamentada, preservando registros anteriores.

**Interfaces:** consome spec, ASSETS, versão final, screenshots/comparação e relatório; produz nota ponderada e decisão própria06, sem reaproveitar nota05.

- [ ] Abrir referência, três capturas e comparação; conferir hashes/dimensões, identidade dos avatares, escritório, redação/horas, proporções e cromia.
- [ ] Conferir evidências técnicas, fallback, alvos/foco/dialogs/envio local; distinguir testes revisados de testes repetidos pelo auditor.
- [ ] Atribuir pesos35/25/20/10/10 da spec e listar diferenças concretas. Aprovar somente nota>9,0 sem bloqueador material; meta9,5.
- [ ] Se reprovar, devolver correções ao papel responsável, recapturar e reauditar nova versão; se insumo impossível, documentar bloqueio. Só liberar planejador07 após gate06 aprovado. Não publicar nesta etapa.

## Handoff do planejador

Spec e plano cobrem conteúdo, fotos/ícones, UI fluida, estado local, acessibilidade e gate. Próximo papel: **assets06**. Nenhum asset, HTML/CSS/JS, screenshot, nota ou publicação foi produzido pelo planejador.
