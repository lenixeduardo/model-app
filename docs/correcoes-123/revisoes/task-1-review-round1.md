# Revisão independente — tarefa 1, rodada 1

Escopo: diff `a82f179..db87423`, apêndice Rodada 1 de `task-1-report.md`, seis capturas finais375/390/430 e duas comparações390 abertas novamente. Revisão restrita aos quatro achados anteriores e regressões introduzidas pelo fix. Os quatro testes GREEN e capturas sem erros são evidência relatada; não repeti a suíte. Apenas este relatório foi escrito.

## Veredictos

**Spec: REQUEST CHANGES. Quality: REQUEST CHANGES. Gate visual: REPROVADO.**

A revisão proporcional foi corrigida e a remoção de faixas inteiras foi eliminada, mas permanecem artefatos visuais relevantes. As notas abaixo são nova avaliação das evidências desta rodada, sem transportar a pontuação anterior.

| Tela | Foto35% | Geometria25% | Tipografia20% | Cores10% | Responsividade10% | Total |
|---|---:|---:|---:|---:|---:|---:|
|01|8,7|9,2|8,4|9,0|9,0|**8,83**|
|02|8,5|9,0|8,0|8,4|8,0|**8,47**|

Nenhuma tela supera9,0. Meta9,5 permanece. Identidade, pessoas e proporção intrínseca dos retratos estão preservadas; não encontrei geração de pessoa ou fotografia inventada no fix. A baixa resolução existe, mas não explica os artefatos de máscara e composição restantes.

## Situação dos quatro achados anteriores

### 1. Faixas fotográficas ausentes02 — NOT ADDRESSED integralmente; correção parcial substancial

`MODEL_assets_v1/extrair_entrada.py:19`; `MODEL_tela_02_V1/styles.css:12` e`:14`.

As quatro faixas largas desapareceram e o torso/roupa voltou. Isso resolve o defeito específico de apagar toda a largura. Entretanto, as coordenadas iniciais aproximadas da revisão anterior foram aplicadas sem o refinamento solicitado: retângulos escuros ainda excedem os rótulos nativos e permanecem vazios abaixo/direita do texto, especialmente cidade de Enzo e Theo. Em390, o nome Enzo começa ~410 enquanto a referência proporcional começa ~417; a cidade também está acima. O fundo de nome/cidade em dois retângulos desconectados parece remendo, ausente na referência. Os bookmarks têm quadrados opacos de44px que cobrem torso e casaco.

Próximo ajuste concreto: refinar os bboxes na resolução fonte, medir posição/baseline de nome e cidade separadamente e alinhar a UI a esses limites, em vez de apenas usar `span top` único com line-height e margin. O crop/nome Enzo começa em fonte y~212, não208; o texto deve ocupar os pixels efetivamente mascarados, não deixar um rodapé vazio da máscara. Manter hit target44px transparente e dimensionar somente o apoio visual de bookmark à menor região raster necessária. Usar máscara pontual cuidadosamente registrada; não voltar às faixas nem preencher fotografia. O RGB original entre e ao redor dos textos deve permanecer.

O par fonte03 para Enzo e fonte05 de camisa aberta é candidato a fornecer área limpa da mesma composição fotográfica, caso um alinhamento documentado confirme a correspondência. Isso não autoriza trocar a pessoa/pose por foto09 nem transportar os rótulos inconsistentes entre telas. Persistindo lacunas exatamente sob a UI, registrá-las honestamente. A melhora é clara, mas os retângulos ainda impedem fidelidade >9.

### 2. Ombro/CTAs01 — NOT ADDRESSED integralmente; geometria corrigida, artefato novo

`MODEL_assets_v1/extrair_entrada.py:11` e`:15`; `MODEL_tela_01_V1/styles.css:15` e`:16`.

O ombro foi recuperado e as posições/alturas dos botões aproximaram-se da referência. O texto contratante continua menor e um pouco mais baixo, mas o principal problema agora é o **MODEL escuro duplicado/deslocado** sob o logotipo branco, visível nas três larguras, além do vestígio horizontal sob o traço. A máscara por limiar de brilho remove pixels claros dos glifos, deixa contorno/antialias escuro e cria lacunas pretas com formato de letra. O novo H1 está desalinhado em relação a essas lacunas. O gradiente reduz contraste do problema sem removê-lo.

Aumentar os bboxes/limiar ou apagar todo o bloco tende a remover mais ombro e não recuperar os pixels originais sob a marca. A correção precisa preservar a marca original ou alinhar precisamente uma solução nativa que cubra os vestígios sem alterar o retrato; o segundo caminho é difícil pela rasterização e pelas diferenças de desenho da fonte.

**Avaliação da opção proposta pelo controlador, ainda não autorizada para implementação:** tratar o wordmark MODEL fornecido como arte de marca é tecnicamente uma solução melhor que reconstruir pixels do ombro. Um recorte parcial do hero contendo somente fotografia, wordmark e traço originais pode preservar composição e antialias, com H1 semântico nativo acessível e fallback visível se a imagem falhar. Tagline, botões, status e interações devem continuar nativos; não usar a tela inteira como fundo nem incluir os CTAs raster. Extrair a marca como alpha e deixar seu negativo no retrato não resolveria: a solução deve preservar o conjunto original na região da marca. Exige ruling explícito do controlador para a exceção de marca, documentando procedência/crop/hash. Esta revisão avalia a alternativa; não a autoriza, não altera o brief e não aprova antecipadamente sua nota.

### 3. Comparação deformada — ADDRESSED

`tests/e2e/compare.py:8`.

O resize agora usa uma escala uniforme por largura e altura calculada; as imagens390 mostram corretamente a área excedente cinza. O apêndice corrige a afirmação anterior. Não há mais deformação geométrica imposta pela comparação. A aprovação deste item não implica que a implementação atual seja fiel nem modifica automaticamente sua nota.

### 4. Hierarquia/ícones02 — NOT ADDRESSED integralmente; escala e Home corrigidos

`MODEL_tela_02_V1/styles.css:12`.

A escala dos chips, nomes/cidades e Home preenchido melhorou. Contudo `font-weight:normal` foi aplicado tanto a nomes como cidades; os nomes perdem o peso e a hierarquia da referência. Eles devem ter regra própria, calibrada por comparação, mantendo cidades mais leves. A posição individual dos rótulos também precisa do alinhamento descrito no item1. Os dois controles do header agora são SVGs, mas o primeiro ainda tem outro desenho; isso é residual menor frente a texto e máscaras. Não é necessário redesenhar as fotografias para corrigir a UI.

## Nova regressão no fix

**Important — barra inferior02 deixa uma faixa vazia fora do aplicativo.** `MODEL_tela_02_V1/styles.css:12`, novas regras de altura fixa proporcional e `.bottom`.

A barra inferior termina aproximadamente y=769/800/883 nas capturas375/390/430, mas os viewports têm812/844/932. Surgem ~43–49px pretos sob as bordas arredondadas, enquanto a navegação fica acima do fim da tela. A comparação proporcional pode legitimamente ter cinza excedente na referência; a UI real ainda deve resolver o espaço adicional do viewport. Recomendo ancorar a barra ao fundo do viewport/aplicativo, distribuindo a diferença numa área de layout apropriada sem esticar fotos, cortar labels ou mudar sua proporção. Reavaliar375/390/430 após essa mudança.

Nenhum novo defeito funcional crítico de navegação foi identificado no fix, que não altera as rotas/handlers. Backend e estado compartilhado continuam fora desta revisão.

## SHA-256 das evidências abertas

- `MODEL_assets_v1/referencias/01-splash.png`: `ee9b8b3511592c36c66bd8da1b9d6936aeb0c1264b6fb97bdb8d830017126f80`
- `MODEL_assets_v1/referencias/02-descoberta.png`: `a152aeca87a53a5a1890f0bc04a9710bb7838741c076f999e3fa5c1d1a6d0a39`
- `docs/correcoes-123/capturas/01-375.png`: `1e0c1ab41ac260bb772354d6979fc8c4c93a0ef9ab2cb2f06f9ba389c9184a17`
- `docs/correcoes-123/capturas/01-390.png`: `3f403c3319139dbf5ced261cbc7fdae736ed0c5a51a37f9645a15c59e61f45b7`
- `docs/correcoes-123/capturas/01-430.png`: `5fc60fdbaed714095e410bca5afb8e6c6db98dd1cf06d6eb3c5202fcfe30ac0b`
- `docs/correcoes-123/capturas/01-comparacao-390.png`: `7a01536f52f92fc11e21de1108a5aaac1813527341a4b5089ddd0ea54398d0fe`
- `docs/correcoes-123/capturas/02-375.png`: `98f8740844003b7498d18970822dcd5fff233905052f3af311904170e2fded44`
- `docs/correcoes-123/capturas/02-390.png`: `11efc01ae0f50b75badb67a040cfc989b5739c14e7f62512507b41ef0ffe21f6`
- `docs/correcoes-123/capturas/02-430.png`: `7271b9e2c3fb6bb8fd277e3a3f384f7b4e5211afcb9f2d9572048031c4b72494`
- `docs/correcoes-123/capturas/02-comparacao-390.png`: `ff211a83f5a25bcdc9f7809cd78f533d58cbb8c2756065a7fa219e2aaf5bb39f`
