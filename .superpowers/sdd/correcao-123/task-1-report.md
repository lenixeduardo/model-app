# Relatório — tarefa 1

Status: DONE_WITH_CONCERNS. Entrega de navegação demonstrativa e entrada 01/02; auditoria visual independente permanece pendente. Nenhuma nota visual atribuída.

## Evidências

- RED: `npx playwright test tests/e2e/navigation.spec.cjs --reporter=line` antes da implementação falhou porque `/` não continha entrada de demonstração e servia listagem de diretório; o teste de retorno também reproduziu o fluxo ausente.
- GREEN: mesmo comando após implementação: 4 testes passaram em Chromium `/usr/bin/chromium`, incluindo jornada Enzo, portfólio/chat, menus Salvos/Notificações, prévia de Gabriel, filtros, reload, URLs de pasta e fallback seguro.
- `node tests/e2e/capture.cjs`, com servidor Python 8878: seis capturas 375×812, 390×844 e 430×932 DPR1; logs em `docs/correcoes-123/capturas/log.json`. Nenhum erro de recurso/JS e nenhuma violação axe-core 4.14.0 nas seis telas iniciais sob tags WCAG2A/AA e 2.1A/AA. Isso não cobre outros estados nem substitui avaliação assistiva.
- Comparações proporcionais 390 em `docs/correcoes-123/capturas/01-comparacao-390.png` e `02-comparacao-390.png`; capturas históricas preservadas.

## Alterações

Raiz, `shared/navigation.js`, telas 01–11, testes Playwright CJS, documentação e versões por tela; mapa anterior e decisões em `docs/correcoes-123/DESTINOS.md`. Fotografias extraídas das referências locais sem geração, máscaras alpha e fundos escuros para áreas com texto; scripts, hashes e procedência documentados nos manifests e ASSETS das novas telas. SVGs de status e navegação reutilizados dos pacotes existentes.

## Limites e revisão própria

A referência para 01/02 tem baixa resolução (188/199×404); máscaras e zonas escuras em 02 deixam perda visível de conteúdo fotográfico e exigem auditoria visual. A comparação de 01/02 não autoriza nota ou aprovação do gate. A fotografia 01 exclui a faixa superior do status e usa suporte preto CSS, sem inventar corpo. O retrato 02 mantém proporção, quatro pessoas originais e rótulos nativos; pessoas sem perfil têm prévia honesta. Salvos, filtros e mensagens ainda são locais, sem estado compartilhado ou backend, conforme escopo da tarefa. Os testes automatizados não avaliam todos os controles, tecnologias assistivas ou navegadores. `07` usa o controle de busca existente para filtros, com rótulo correspondente. O registro dos destinos anteriores e as capturas são novos, sem alterar evidências históricas.

Commit: ver `git log -1` para o commit desta entrega (o relatório integra o mesmo commit).

## Rodada 1 — resposta à revisão

Os quatro achados foram tratados: fotos 02 mantêm os pixels fora de máscaras pontuais de texto e bookmark; 01 inclui o ombro até y=258, com máscara por glifo e CTAs posicionados segundo a referência; comparações novas mantêm escala uniforme (a área cinza corresponde à diferença de altura); hierarquia, ícones do cabeçalho e Home ativo foram recalibrados. Evidências da rodada 0 estão em `docs/correcoes-123/capturas/historico/round0/`, sem alteração dos bytes. A afirmação anterior de comparação proporcional refere-se às imagens antigas e foi corrigida: elas foram esticadas e não devem ser usadas para avaliar geometria. As seis novas capturas foram abertas para inspeção.

- `npx playwright test tests/e2e/navigation.spec.cjs --reporter=line`: **4 passed (5.9s)**.
- `python3 -m http.server 8878 --bind 127.0.0.1` e `node tests/e2e/capture.cjs`: seis capturas, sem erro JS/recurso nem violação axe-core 4.14.0 nas regras selecionadas; detalhes em `capturas/log.json`.
- `python3 tests/e2e/compare.py`: seis comparações com escala uniforme, por largura; área cinza não representa imagem.
- Comparação de pixels dos quatro crops 02 contra a referência, excluindo alpha transparente: **0 pixels divergentes** em cada retrato.

Limites: máscaras opacas ainda são visíveis em 02, e a baixa resolução e os pixels sob UI raster não permitem recuperar integralmente a fotografia. A transição e pequenos vestígios do logotipo 01 também precisam de revisão independente. Nenhuma nota é atribuída aqui; gate >9 permanece pendente.

SHA-256 das evidências desta rodada:

```text
1e0c1ab41ac260bb772354d6979fc8c4c93a0ef9ab2cb2f06f9ba389c9184a17  docs/correcoes-123/capturas/01-375.png
3f403c3319139dbf5ced261cbc7fdae736ed0c5a51a37f9645a15c59e61f45b7  docs/correcoes-123/capturas/01-390.png
5fc60fdbaed714095e410bca5afb8e6c6db98dd1cf06d6eb3c5202fcfe30ac0b  docs/correcoes-123/capturas/01-430.png
98f8740844003b7498d18970822dcd5fff233905052f3af311904170e2fded44  docs/correcoes-123/capturas/02-375.png
11efc01ae0f50b75badb67a040cfc989b5739c14e7f62512507b41ef0ffe21f6  docs/correcoes-123/capturas/02-390.png
7271b9e2c3fb6bb8fd277e3a3f384f7b4e5211afcb9f2d9572048031c4b72494  docs/correcoes-123/capturas/02-430.png
fcfaac3cf51a1191e726ef165c8e418dcb3fe8c1ffd9065219c17a55e005fd2a  docs/correcoes-123/capturas/01-comparacao-375.png
7a01536f52f92fc11e21de1108a5aaac1813527341a4b5089ddd0ea54398d0fe  docs/correcoes-123/capturas/01-comparacao-390.png
79a35b4c69f62746ae85a4570c4dc8502f9bbfdb1c54820ef50ef8c58eed1623  docs/correcoes-123/capturas/01-comparacao-430.png
62b90e58dd267f54d1d5c014b53ea90c2aeb68b105c148c05d12917bb7837d32  docs/correcoes-123/capturas/02-comparacao-375.png
ff211a83f5a25bcdc9f7809cd78f533d58cbb8c2756065a7fa219e2aaf5bb39f  docs/correcoes-123/capturas/02-comparacao-390.png
8b3152c66e5a35561565ed8d954de264eedff415956323ccf7c78b8e05a96871  docs/correcoes-123/capturas/02-comparacao-430.png

```

## Rodada 2 — resposta à revisão

Hero parcial 01 `(1,18,187,249)` preserva RGB, wordmark e divisor originais sem máscara; título nativo acessível, com fallback visual em falha do arquivo. Essa marca é arte estática de baixa resolução, não texto editável. Tagline, status e controles permanecem nativos. Em 02, máscaras foram estreitadas e alinhadas aos rótulos com posições e pesos separados; apoios dos bookmarks são pequenos, com área de toque transparente de pelo menos 44px. A barra inferior está ancorada ao fundo sem esticar as fotos. Capturas e comparações anteriores foram preservadas em `capturas/historico/round1/`. As seis capturas novas foram abertas.

- `npx playwright test tests/e2e/navigation.spec.cjs --reporter=line`: **5 passed (6.7s)**, incluindo erro de imagem/fallback e posição da barra e área de toque nos três tamanhos.
- `python3 -m http.server 8878 --bind 127.0.0.1` + `node tests/e2e/capture.cjs`: seis capturas; zero erros JS/recurso e zero violações axe nas regras selecionadas, em `capturas/log.json`.
- `python3 tests/e2e/compare.py`: seis comparações com escala uniforme, área cinza mostra diferença de altura.
- `python3 tests/e2e/verify_assets.py`: `01 hero RGB: idêntico ao recorte original`; `enzo`, `gabriel`, `theo`, `rafael`: `0 pixels divergentes fora das máscaras`.
- Hero SHA-256: `dbfa6e9bdc5faf64aca4b57c231fcb151cbaff94e5d4f21de21b6c550fb52d7d`; referência 01: `ee9b8b3511592c36c66bd8da1b9d6936aeb0c1264b6fb97bdb8d830017126f80`.

Persistem pequenas áreas opacas exatamente sobre a UI de origem, onde a fotografia é desconhecida. Avaliação visual independente e gate >9 permanecem pendentes; nenhuma nota é atribuída.

SHA-256 das novas evidências:

```text
c307bff5977f60c57889d33b646964e886eb25aa8e70b69644b99b2e434a0b6b  docs/correcoes-123/capturas/01-375.png
8fea9068d893069cf6d5c4d7b0d33f9e05be2cc402914bc7bc502d70b2b5abf1  docs/correcoes-123/capturas/01-390.png
063ff7d132635827c416e18325706e08ab377e2f43134bbb5f65c07fb2b49a6a  docs/correcoes-123/capturas/01-430.png
5b3ea04c628ab2a2b54603b92aabd1b4fa12e32cc835f8a0ce1a1426f7a15c0e  docs/correcoes-123/capturas/02-375.png
786c54f3f58660346a3c04ded8e3e4825989fc381ec6b4d037c6bfa77e8c7b1f  docs/correcoes-123/capturas/02-390.png
a41fbf838d05b57e03d53527d8426d09608681f4f2f640485b198ae229f09127  docs/correcoes-123/capturas/02-430.png
37dde03e8afe49fe97e2aa9bf9662ce899cfdc38f31b6ccb2a27dcef7f50dd49  docs/correcoes-123/capturas/01-comparacao-375.png
e547817157c54dd9f739bc64413e5c71fec062a078f390947b07314cb88ba8ab  docs/correcoes-123/capturas/01-comparacao-390.png
38c8478e89c1bd8c3a66020a1c61a9eeb6761068c64c91b10e65581bb31e0fc9  docs/correcoes-123/capturas/01-comparacao-430.png
72359a3c2fe294a3678d1f2d3b7a657c3749b8dba27a1798bbf6d57c38724dc4  docs/correcoes-123/capturas/02-comparacao-375.png
6b26bf0d2efa3152df5170e6ac03716fc4791acfc587c026fadc1d5b50d21eac  docs/correcoes-123/capturas/02-comparacao-390.png
cee0b62849a7f8b6b9a32a0d85c497aef45b1475060a858ac5abc3aa1200e940  docs/correcoes-123/capturas/02-comparacao-430.png

```
