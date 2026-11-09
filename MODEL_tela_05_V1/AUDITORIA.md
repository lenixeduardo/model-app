# Auditoria independente05 — APROVADA VISUALMENTE: 9,34/10

Avaliação em2026-11-09 da versão `1.0.0-prototipo.1`. Soma ponderada9,335; gate **>9,0 atingido**, meta9,5 não atingida. Nenhum P1 material encontrado. Planejamento06 **LIBERADO**. A aprovação cobre o protótipo local e as três dimensões documentadas; não significa backend integrado ou publicação.

## Inspeção visual e nota

O auditor abriu obrigatoriamente por `view_image` a referência oficial172×404, as capturas375×812,390×844,430×932 e `comparacao-390.png`. As sete fotos mostram a mesma pessoa, pose e composição fonte; cinco caixas completas e dois recortes inferiores permanecem identificáveis. Não há fotografia gerada, extensão anatômica ou UI raster integral. Hora9:41, títuloPortfólio, Fotos ativa, Vídeos e Trabalhos aparecem em HTML nativo; voltar, busca e sinais são SVGs locais. Não há contador, tab bar ou home indicator inventados.

| Critério | Peso | Nota | Contribuição | Fundamentação visual |
|---|---:|---:|---:|---|
| Fotografia/identidade/enquadramento |35%|9,40|3,290|Sete crops exatos, identidade e pontos focais preservados; cover encurta discretamente as extremidades verticais.|
| Geometria |25%|9,50|2,375|Bento, colunas, posições verticais e separadores seguem a referência; largura proporcional cresce com viewport.|
| Tipografia/ícones/abas |20%|9,00|1,800|Texto nativo correto; fonte e peso diferem da referência comprimida, pill ativa um pouco alta em375 e ícones mais limpos/finos.|
| Cores/contraste |10%|9,50|0,950|Preto quente, branco e abas escuras coerentes; fotografia mantém RGB fonte.|
| Responsividade/acabamento |10%|9,20|0,920|Três capturas consistentes e sem overflow visível; perda vertical por cover e arredondamentos discretos são limites.|
| **Total** |100%||**9,335 →9,34**|**Aprovada, sem bloqueador material.**|

As notas são julgamento visual independente, não métrica pixel-perfect nem média ajustada para liberar fila. A meta9,5 não foi atingida.

## Diferenças concretas restantes — P2

- Em390, foto01 ocupa aproximadamente x7–247/y161–535 e foto02 x252–383/y161–341, coerentes com âncoras previstas. A razão viewport390/844≈0,462 difere da referência172/404≈0,426. A largura escala2,267 e a altura2,089: `object-fit:cover` preserva proporção e descarta cerca de7,9% da altura fonte, aproximadamente4% por extremidade com posição central. Na foto01 equivale a≈7px fonte por extremidade; foto07≈3px. Cabelos, olhos, rostos, ombros e pose sentada continuam reconhecíveis nos três tamanhos. Isso não é stretching, mas a apresentação fica um pouco mais fechada que o original.
- Título nativo em390≈19,3px e tabs≈14,7px têm contorno mais regular que o JPEG ampliado. Em375 o mínimo de44px nas abas supera a altura nominal≈38px; a base da pill fica cerca de6px abaixo da âncora proporcional. Não colide com o mosaico.
- Status/chevron/lupa são aproximações vetoriais; peso, espaçamento da bateria e geometria do Wi-Fi diferem levemente. O raio externo≈22,7px em390 acompanha a referência, mas o fundo externo da página tem a mesma cor e reduz a percepção do canto superior.

Não há P1 que justifique bloquear a06 ou alterar03/04.

## Evidências e verificações independentes

O auditor leu DESIGN_SPEC.md, ASSETS.md, PLANO.md, relatorio-browser.json, EVIDENCIAS.json, código CSS/JS, scripts de render/compare e manifesto. Verificou por Python/Pillow, sem regravar imagens:

- Todos os hashes listados em EVIDENCIAS.json conferem com os arquivos presentes, inclusive HTML/CSS/JS, scripts, relatórios e screenshots.
- Painel global `[836,0,1008,404]` do JPEG é RGB idêntico à referência. Os sete PNGs correspondem integralmente ao RGB dos crops do manifesto, inclusive pixels sob alpha, e têm dimensões/hashes declarados. Cinco caixas completas e dois parciais:106×179,58×86,58×81,106×101,58×80,106×44,58×75. Apenas alpha geométrico remove bordas; não há novos pixels fotográficos.
- Comparação765×874 contém referência redimensionada proporcionalmente para359×844 emx0/y30 e screenshot390×844 integral emx375/y30. Ambos conferidos pixel a pixel; separação16px e cabeçalho30px. O recorte-fonte é referência, nunca prova de render.

| Imagem avaliada | Dimensões raw | SHA-256 |
|---|---|---|
| Referência05 |172×404|8e3caac689d1e17c5c62f56f30ff99e9b028244849fc2825bb9082485bf6634b|
| captura-375.png |375×812|e17d292e865132f17e1fa64c45d062a84808a62150211595f208f8b777de1340|
| captura-390.png |390×844|3349b232f8297f37749c44a6d8f3042c31bb81e0f0b98407a705bcf8b08fbd7c|
| captura-430.png |430×932|871c6198f0788f2a9f6988fb2c97f35bf89918c8ae9d56e4c46c7a7875db895c|
| comparacao-390.png |765×874|2c88bd4a4e72569257188e525a3a7836af38cd731366f145e5e942e80a3bf14d|

## Validação técnica e limites

O relatório do implementador registra Chromium156.0.8078.79/DPR1, screenshots reais via Playwright, sete imagens carregadas com cover, dimensões de documento iguais ao viewport, alvos>=44px, console/rede sem erros e ações de abas, sete dialogs, Escape, restauração de foco, busca local e back real04 aprovadas. O script de captura foi revisado e separa captura inicial das ações. **O auditor não executou um segundo teste/browser/render independente**; conferiu os registros reais e artefatos entregues pelo implementador. Foco preso depende do dialog modal nativo; o script entregue verifica restauração, sem teste explícito de ciclo completo de Tab. Isso permanece limite da cobertura técnica, não evidência de defeito visual.

Busca, modais e estados vazios são frontend local; não existe backend, vídeos/trabalhos integrais ou busca de servidor. Originais fotográficos em alta resolução e extensões inferiores06/07 não estão disponíveis; dialogs exibem apenas os mesmos recortes genuínos. Ampliar não recupera detalhe. Não houve publicação, alteração de código/assets/capturas, início de planejamento06 ou modificação das telas03/04 nesta auditoria.
