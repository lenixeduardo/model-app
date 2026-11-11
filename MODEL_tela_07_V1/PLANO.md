# Tela07 — Castings Implementation Plan

Execução já autorizada: planejamento → assets → implementação → auditor independente. Este papel entrega apenas documentação, sem confirmação extra, subagentes, código, assets, capturas, notas ou publicação.

**Objetivo:** reproduzir07 com três fotografias originais, UI nativa e interações locais honestas.
**Arquitetura:** frontend isolado HTML/CSS/JS com PNG/SVG locais, estado de filtros/salvos/dialogs somente em memória. Contrato: [DESIGN_SPEC.md](DESIGN_SPEC.md).

## Restrições

Preservar03–06 aprovadas.08–11 bloqueadas. Gate07>9,0, meta9,5. Nenhum texto rasterizado sobre papel, pessoa sintetizada, corpo reconstruído, screenshot de fundo, nova aba ou CTA.375×812/390×844/430×932, DPR1, fotografias proporcionais. Sem backend/rede externa/publicação.

### 1 — Assets07 (próximo papel)

Arquivos: `ASSETS.md`, `assets/manifest.json`, `assets/extract_assets.py`, três PNGs e SVGs locais definidos na spec.

- [ ] Reconfirmar crop global[11,434,212,751] RGB idêntico à referência; refinar boxes fotográficos.
- [ ] Extrair três fotos distintas sem UI; provar RGB nos pixels alpha>0, registrar coordenadas/dimensões/hashes e limites de detalhe/matte. Abrir crops e conferir identidades/cantos; não gerar pixels.
- [ ] Criar SVGs locais finos e documentar aproximações. Entregar proveniência e paths estáveis.
- [ ] Bloquear se insumo fotográfico insuficiente; só liberar implementador após entrega utilizável.

### 2 — TDD e implementação07

Arquivos: `index.html`, `styles.css`, `app.js`, `VERSION`, `README.md`, `CHANGELOG.md`, verificação funcional reproduzível.

- [ ] Antes da lógica, criar e executar verificações comportamentais que falhem pela ausência de interface: filtros01/02/01+03, save isolado, reload, dialog/Escape/foco e navegação06. Não testar detalhes internos espelhando código.
- [ ] Implementar status/header/filtros/três cards/tabbar, texto exato e fotos proporcionais; todos textos nativos. Sem back-arrow novo.
- [ ] Implementar filtros e saves em memória, sem eventos cruzados; card/foto em dialog com mesmos dados. Mais abre explicação local; tabbar conforme spec e links aprovados03/06. Nenhuma implementação08 ou02.
- [ ] Aplicar44px/foco/labels, dialogs com foco contido/restaurado e Escape, safe-area, fallback foto/SVG e reduced-motion. Conteúdo local via textContent, sem backend/persistência.
- [ ] Rodar testes comportamentais até verde e conferir manualmente composição nos três tamanhos. Não alterar pastas aprovadas.

### 3 — Verificação real e evidências finais

Arquivos: `render.py`, `compare.py`, `relatorio-browser.json`, `screenshots/375x812.png`, `screenshots/390x844.png`, `screenshots/430x932.png`, `comparacao-390.png`; atualizar documentação/versionamento.

- [ ] Servir raiz local e usar navegador real DPR1; verificar assets, console/rede externa/overflow, texto,44px e foco. Registrar navegador e comando.
- [ ] Testar cada filtro, toggle save duas vezes, persistência apenas em memória/reload, abertura de cards, plus, painéis e links03/06; Escape/fechar/restauração de foco, teclado. Foto com erro e reduced-motion em verificações separadas.
- [ ] Capturar candidata390 real e abri-la; corrigir diferenças antes de capturar as três finais limpas (Todos, salvos vazios, dialogs fechados).
- [ ] Produzir comparação normalizada à mesma altura preservando proporções. Abrir três capturas e comparação; registrar hashes/versão e limitações. Não atribuir nota própria.

### 4 — Auditor independente

Arquivos: `AUDITORIA.md`, atualização de `docs/FILA_AGENTES.md`.

- [ ] Abrir referência, screenshots e comparação finais; conferir dimensões/hashes, fotografias/identidade/crop, conteúdo exato, geometria e adaptação.
- [ ] Rever evidências técnicas e distinguir testes repetidos dos apenas revisados.
- [ ] Avaliar pesos35/25/20/10/10, diferenças concretas e bloqueadores. Aprovar apenas>9,0, meta9,5; sem herdar nota06.
- [ ] Se reprovar: correção pelo papel responsável, nova versão/capturas/auditoria; insumo impossível gera bloqueio documentado. Só aprovação07 libera planejador08; não publicar.

## Handoff

Planejamento07 concluído; próximo papel **assets07**. Nenhum asset/interface/captura/nota foi produzido. Aprovações03–06 preservadas;08 permanece bloqueada.
