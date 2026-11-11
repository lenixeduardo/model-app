# Auditoria independente — Tela11 Notificações

Versão **1.0.0-prototipo.1**, auditada em 2026-11-11 após liberação final do implementador. **APROVADA VISUALMENTE: 9,27/10**, soma ponderada **9,2725**, gate estritamente >9,0 atendido; meta9,5 não atingida. Nenhum P1 material identificado. Nota própria desta tela, sem herança das anteriores.

## Avaliação visual

Abri visualmente a referência `../MODEL_assets_v1/referencias/11-notificacoes.png`, as três capturas finais e `comparacao-390.png`. Comparei as cinco fotografias, seis linhas, texto/tempos, quatro filtros e cinco destinos. Fotos mantêm rosto/cabelo/ombros integrais, mesma identidade visual e proporção1:1 nos três tamanhos. Não há substituição aparente nem deformação. Texto inicial corresponde às seis mensagens; linha6 completa, sem reticências. Perfil permanece ativo conforme fonte.

| Critério | Peso | Nota | Parcela | Fundamentação |
|---|---:|---:|---:|---|
| Fotografia/identidade/enquadramento |35%|9,65|3,3775|Cinco crops genuínos integrais; ampliação evidencia resolução limitada da fonte e pequena matte periférica.|
| Geometria |25%|9,20|2,3000|Âncoras e distribuição longitudinal corretas; respiro horizontal condicionado pela razão móvel, com pequenas diferenças em cabeçalho e escala dos controles.|
| Tipografia/ícones/chips |20%|8,65|1,7300|Conteúdo exato e legível; peso dos textos é mais leve e ícones da navbar menores na comparação à altura normalizada. Pictograma coral e mais superior diferem.|
| Cores/contraste/sobreposição |10%|9,15|0,9150|Papel quente, preto, cinzas e coral coerentes; disco coral plano perde variação tonal JPEG; aro cinza do mais superior é mais perceptível.|
| Responsividade/acabamento |10%|9,50|0,9500|Três tamanhos íntegros, seis linhas/nav sem colisão ou corte; alvos e ações documentados no navegador.|

### Diferenças P2 e limites

- A referência normalizada à altura844 preserva largura490; o app ocupa390. A diferença proporcional é intencional e não foi tratada como deformação. Mesmo considerando escala por largura, textos e alguns ícones parecem mais delicados; navbar tem menor presença visual. Arial é aproximação, não identificação da fonte original.
- O círculo coral mantém cor amostrada, mas é sólido e seu pictograma de linhas verticais não reproduz os traços ambíguos da miniatura. Aproximação declarada; sem logomarca ou letra inventada. O botão superior apresenta aro/cinza que não é tão evidente na fonte.
- Fotografias genuínas28×28 ficam pixeladas quando ampliadas; matte e borda da miniatura permanecem. Não há autorização para fabricar detalhe facial.
- Gate limitado aos três viewports móveis e protótipo local. Não comprova dispositivo físico, backend, notificações remotas ou publicação.

## Provas independentes e evidências revisadas

Executei leitura/verificação de hashes: **37 entradas SHA256SUMS OK**, incluindo EVIDENCIAS.json; seus36 hashes internos também conferidos. Pillow confirmou referência184×317 idêntica RGB ao crop global[805,434,989,751] do original1179×753, diferença bbox=None. Conferi independentemente cada pixel RGB visível dos cinco PNGs contra seu crop: **592 por foto,2960 no total**, suporte28×28, proporção1:1. Máscara/matte e limites constam no ASSETS e manifest. Confirmei dimensões das três capturas e igualdade exata das duas metades da comparação: referência redimensionada proporcionalmente490×844 à esquerda e captura390×844 à direita. Não editei runtime/assets/capturas.

Revisei `browser-report.json`, `EVIDENCIAS.json` e os asserts de `verify.cjs`; **não executei uma segunda sessão de navegador**. Evidência do implementador: Chromium156.0.8078.79, DPR1, viewports375×812/390×844/430×932; ausência de overflow, imagens carregadas e alvos≥44px sem interseção nos três. Registro errors[]/failedRequests[] vazio; o script exclui erro ERR_INVALID_URL esperado da imagem inválida forçada no teste de fallback. Não equivale a monitoramento contínuo de rede.

Asserts revisados cobrem filtros6/2/1/3 e aria-pressed, estado inicial “não informado”, leitura explícita/desfazer, marcar todas/reset/reload, contenção de Tab/Escape/restauração de foco, links da nav com HTTP200 (destinos03/07/06/10), preferência reduced-motion e fallback sem pessoa substituta. A evidência não inclui screenshot de cada estado de dialog nem teste de todos os links internos de cada dialog; o gate funcional se apoia no relatório e no escopo desses asserts, sem alegar execução própria adicional. Foco visível e nomes acessíveis são requisitos revisados documentalmente, não medição visual em captura de foco.

## SHA256 das capturas desta versão

- `captura-375.png`: `183a98dfd7136de5123b34ba883873ef68089b786737b992366956d7792d9db7`
- `captura-390.png`: `34eb41a1c41842f0e69971bcfa9c8011914ebb35336bc2baab809a0c9a9a65b2`
- `captura-430.png`: `ad6876332a487075e1a7d50e0de234cb53d065f5e502af065687200495261768`
- `comparacao-390.png`: `93cb33c406323982718e9b4c8a9c2ef7da4f53403cf24be24a9ff558b615cb0b`

**Decisão:** gate11 encerrado; últimas quatro telas08–11 aprovadas visualmente. Sem publicação neste papel e sem alteração03–10.
