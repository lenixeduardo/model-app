# Tela 03 — assets vigentes e proveniência

**Estado atual: ciclo7 aprovado visualmente9,13/10**, versão2.0.0-prototipo.7. A fotografia integral limpa continua não fornecida, mas os pixels reais de torso existentes no mockup foram extraídos; isso resolveu o antigo bloqueio do recorte parcial. O diagnóstico inicial abaixo é histórico, não o estado vigente.

Runtime atual:

- assets/enzo-mockup-foto-com-lacunas-precisas2.png:203×404,70.768pixels visíveis idênticos ao mockup;11.244transparentes comRGBzero. Sem nova anatomia ou inpainting.
- assets/ui/name-reference.png e location-reference.png: foregrounds individuais de UI por contornos,39,75%/35,07%de preenchimento, com antialias contextual conhecido. Foto/UI são camadas independentes; não é fonte original genérica.
- assets/icons/: ícones vetoriais locais; selo, informação e ações continuam SVG.
- Manifestos/scripts abaixo documentam coordenadas, hashes, variantes e limites. Experimentos tipográficos SVG/binários dos ciclos anteriores foram rejeitados e não são runtime.
- H1/P acessíveis, fallback atômico e opt-out mantêm a camada nativa quando os assets falham ou os dados mudam. Consulte README.md para integração.

A aprovação foi baseada nas três capturas reais e comparação abertas pelo auditor, não no teste de pixels ou no código. AUDITORIA.md registra notas, hashes e P2 remanescentes.

---

# Histórico da revisão de assets

Data: 2026-11-09. Papel: agente de assets, após planejamento. **Resultado do inventário inicial (ciclos1–4): fotografia integral limpa não encontrada.** Naquela etapa o runtime usava somente o recorte201×242; esse diagnóstico foi superado pela extração com lacunas nos ciclos5–7. Gate atualizado da fila: nota **>9,0**, meta9,5.

## Fontes efetivamente verificadas

Inventário por `rg --files` em `/workspace`, anexos em `/tmp/codex-remote-attachments`, `shared` e `library-files`; dimensões lidas com Pillow. Foram abertas visualmente as duas fontes originais, referência isolada, recorte parcial, descoberta, painel editorial e captura390. O mockup geral foi inspecionado integralmente para conferir também os pequenos retratos de perfil/portfólio/salvos.

Os dois anexos remotos são cópias byte a byte dos arquivos em `MODEL_assets_v1/originais/`; as duplicatas em `/workspace/MODEL_assets_v1/` também não representam novas fontes. Não há arquivo fotográfico independente com o enquadramento integral exigido.

| Arquivo relativo à raiz | Dimensões | Origem e uso permitido |
|---|---:|---|
| `MODEL_assets_v1/originais/mockup-geral.jpg` | 1179×753 | Anexo `2-Foto-2.jpg`. Mockup raster completo; textos, ícones e sobreposição fazem parte dos pixels. Fonte de comparação e recortes documentados, não fotografia limpa. |
| `MODEL_assets_v1/originais/login-referencia.jpg` | 430×932 | Anexo `1-Foto-1.jpg`. Fotografia/pose diferentes, monocromática, com UI de login incorporada. Não substitui o retrato colorido oficial. |
| `MODEL_assets_v1/referencias/referencia-tela-03.png` e `03-swipe.png` | 203×404 | Mesmo recorte `[420,0,623,404]` do mockup; interface incorporada. Referência oficial, não fundo independente. |
| `MODEL_assets_v1/assets/enzo-retrato-parcial.png` | 201×242 | Extração fiel `[421,28,622,270]`, única área grande limpa da foto oficial. Sem textos; termina no peito antes da área de nome/localização/chips. |
| `MODEL_tela_03_V2/assets/enzo-swipe-referencia.png` | 201×242 | Cópia exata do recorte acima; asset de runtime histórico, sem uso no ciclo7. Não é fotografia integral nem imagem em alta resolução. |
| `MODEL_tela_03_V2/assets/enzo-ceu-topo.png` | 201×8 | Faixa limpa `[421,14,622,22]` do mesmo mockup. Evidência de extração; não usada no runtime final porque sua ampliação produziu banding. |
| `MODEL_assets_v1/referencias/02-descoberta.png` | 199×404 | Cartão de Enzo com a mesma pose, em área fotográfica menor e também com texto incorporado. Não contém o torso integral limpo nem aumenta o detalhe da fonte. |
| `MODEL_assets_v1/referencias/04-perfil-modelo.png` | 192×404 | Retrato principal/miniaturas com outros recortes/poses; não recupera a camada original da foto03. |
| `MODEL_assets_v1/referencias/05-portfolio.png` | 172×404 | Mosaico de fotos/poses diferentes, resolução menor; não substitui o mesmo enquadramento03. |
| `MODEL_assets_v1/referencias/09-salvos.png` | 176×317 | Miniatura da mesma pose, menor e com cartão/UI incorporados. Não acrescenta a área de torso ausente. |
| `MODEL_assets_v1/referencias/painel-editorial.png` | 176×317 | Homem olhando para outro ângulo, com composição/pose diferentes. Não usar como substituição. |

Demais recortes do mesmo mockup: `01-splash.png`188×404, `06-chat.png`156×404, `07-castings.png`201×317, `08-filtros.png`200×317, `10-meu-perfil.png`185×317 e `11-notificacoes.png`184×317. São telas com UI incorporada; não contêm o arquivo limpo do retrato03. Coordenadas de todos os recortes constam de `MODEL_assets_v1/manifest.json`.

### Identidade das fontes

SHA-256:

- Mockup geral: `9120f379280879ca9c7695eeccba7288630b6956b39708eb94311080dbedf3dd`.
- Login: `2a61473dc4535c17185fe431f5fddc1a6c3c03684e5db3d0bf560ce755e91238`.
- Retrato parcial e sua cópia de runtime: `0eba9a3a98add154419e5599836079909e6f15167a368566ef5e7685bcb1fb86`.
- Referência03 e `03-swipe.png`: `20078867f604b6771214ec52a7a55d12c3843c822721ceda1fd4561aab6dc409`.

## Classificação para implementação

**Extração fiel utilizável:** o retrato parcial preserva os pixels e a proporção naturais do rosto/ombros. Pode continuar no protótipo identificado como parcial. Não se deve esticar ou ampliar sua altura para aparentar o torso ausente. O céu extraído também é fiel, mas não supre o fundo integral.

**Aproximações identificadas:** sete SVGs locais (`voltar`, `opcoes`, `fechar`, `estrela`, `coracao`, `informacao`, `verificado`) foram reconstruídos, não exportados dos vetores originais. O preenchimento CSS do céu interpola cinco cores da fotografia; não é uma recuperação de textura fotográfica original. Não há arquivo de fonte tipográfica original fornecido.

**Insumo ausente:** imagem limpa do **mesmo retrato de Enzo**, com céu, cabeça, ombros e torso visíveis por trás do nome, localização e chips, sem textos, botões ou gradiente já incorporados. Preferível largura>=860px para DPR2; largura>=430px já melhora a entrega DPR1. Resolução maior não compensa pose ou enquadramento diferentes.

## Refinamento vetorial entregue

Criado `assets/icons/fechar-acao.svg`, variante independente proposta para a ação ignorar. `viewBox="0 0 24 24"`, traço1,8, diagonais entre4 e20. O X atual ocupa apenas12/24 da caixa; a referência mostra maior ocupação interna em relação ao círculo. A variante pode ser usada em uma caixa de40×40px dentro do círculo, ocupando aproximadamente26,7px de largura, sem mudar o alvo de toque. Ela **não foi conectada ao HTML** nesta etapa. O implementador deve compará-la na captura antes de decidir e não substituir o X de fechar diálogo indiscriminadamente.

Propostas adicionais ao implementador: ampliar o selo de cerca de23 para25px na viewport390 e calibrar chips com maior preenchimento vertical/borda. São aproximações verificáveis somente por nova captura. Nenhum vetor foi alterado in-place; estrela/coração/informação permanecem estáveis. Não há fundamento para retrabalhar todos os assets quando o bloqueio dominante é a fotografia.

## Bloqueio e decisão

Nenhuma fonte local resolve a ausência do torso integral limpo. Remover UI por geração/inpainting ou completar pixels do corpo criaria informação nova; não foi feito. Usar a captura inteira do mockup como fundo esconderia a dependência entre fotografia e interface; não foi feito. Também não foi substituída a pose pelo painel editorial ou login.

A nota fotográfica da auditoria do ciclo4 era6,2 com peso35%. Mantida essa nota, mesmo supondo todos os demais critérios em10, a média seria `6,2×0,35 + 10×0,65 = 8,67`. Isso é um teto **ilustrativo sob essa hipótese**, não uma pontuação nova nem uma previsão de auditoria. Demonstra por que polir ícones sozinho não sustenta a promessa de>9.

Entrega de assets concluída como revisão e variante vetorial. **A obtenção do asset fotográfico suficiente está bloqueada.** O implementador pode avaliar o refinamento vetorial como protótipo não aprovado, mas não deve iniciar ciclos infinitos ou liberar a Tela04. Retomar o enquadramento final quando chegar a foto original limpa do mesmo retrato, ou se o usuário alterar explicitamente o contrato que proíbe fabricar a fotografia ausente.

Nenhuma captura, CSS/JS, auditoria visual ou publicação foi alterada por este agente.

## Publicação
O inventário acima descreve os arquivos locais. O recorte histórico de céu enzo-ceu-topo.png não é usado no runtime final e fica somente no pacote local. A cópia de runtime enzo-swipe-referencia.png reutiliza exatamente o blob já público de enzo-retrato-parcial.png, sem novos pixels.

## Nova rota — preservar os pixels de torso existentes entre os overlays

Após a revisão de rota do planejador, foi produzida uma extração adicional do **painel completo**. A conclusão anterior permanece correta quanto à ausência de uma foto integral limpa, mas precisa desta precisão: **há muitos pixels reais de torso no painel raster fora da interface; eles podem ser preservados sem inventar os pixels ocultos**. O recorte201×242 não os aproveitava.

Essa tentativa não está coberta pela nota6,2 do asset anterior; o teto ilustrativo8,67 acima aplica-se à hipótese de manter a avaliação fotográfica anterior. A nova variante precisa ser integrada, capturada e julgada de novo. Não é aprovação e não garante>9.

### Entregas e operação

| Arquivo | Uso |
|---|---|
| `assets/enzo-mockup-foto-com-lacunas.png` | Variante conservadora203×404 RGBA; regiões de UI inteiras transparentes. |
| `assets/mask-manifest.json` | Fonte, coordenadas e hashes da variante conservadora. |
| `assets/enzo-mockup-foto-com-lacunas-precisas.png` | Variante203×404 RGBA com máscaras de nome/selo/localização reduzidas aos contornos. Candidata prioritária para teste. |
| `assets/mask-manifest-preciso.json` | Método de seleção dos contornos, contagens e hashes. |
| `assets/derivados/mask_torso.py` | Script reproduzível da variante conservadora, máscara raster e controle SVG. |
| `assets/derivados/mask_torso_preciso.py` | Script reproduzível da variante precisa; mantém conservadora intacta. |
| `assets/derivados/enzo-painel03-preview-preto.png` e `enzo-painel03-preview-quadriculado.png` | Prévias conservadoras, não screenshots de navegador. |
| `assets/derivados/enzo-painel03-preview-preto-preciso.png` e `enzo-painel03-preview-quadriculado-preciso.png` | Prévias da variante precisa, abertas visualmente nesta revisão. |
| `assets/derivados/enzo-painel03-alpha.png` e `enzo-painel03-alpha-preciso.png` | Máscaras raster binárias efetivamente aplicadas. |
| `assets/derivados/enzo-painel03-mascara.svg` | Controle geométrico das regiões conservadoras; não é fotografia. O raster alpha é a referência de pixels exata. |

Origem de ambas: crop`[420,0,623,404]` do JPEG original1179×753, bordas direita/base exclusivas. Dimensão final203×404, sem reamostragem. Os scripts **copiam os valores RGB visíveis decodificados da fonte, sem interpolar, clonar, gerar ou preencher**. A máscara define alpha0 ou255. Na variante conservadora, o RGB invisível ainda corresponde ao recorte original; na variante precisa final, o RGB invisível é zerado para remover literalmente a UI oculta do armazenamento. As verificações percorrem todos os pixels: RGB com alpha255 idêntico à fonte; RGB com alpha0 da precisa igual a zero. A sanitização não altera a máscara nem qualquer pixel fotográfico visível.

A referência já contém gradiente escuro incorporado à fotografia. Esse gradiente continua nos pixels preservados; a extração não o reverte nem recupera informação fotográfica anterior ao mockup.

### Coordenadas conservadoras

Caixas locais à imagem203×404. Os endpoints de máscara são inclusivos, segundo Pillow; o crop fonte usa right/bottom exclusivos.

| Região removida | Geometria | Caixa local |
|---|---|---|
| Hora | Retângulo | `[14,2,44,17]` |
| Ícones de status | Retângulo | `[151,2,195,17]` |
| Segmentos | Retângulo | `[12,20,191,28]` |
| Nome/idade/selo | Retângulo | `[11,272,94,292]` |
| Localização/altura | Retângulo | `[11,292,118,307]` |
| Informação | Elipse | `[170,281,192,303]` |
| Fashion | Retângulo arredondado, raio10 | `[11,310,60,333]` |
| Editorial | Retângulo arredondado, raio10 | `[62,310,111,333]` |
| Comercial | Retângulo arredondado, raio10 | `[113,310,176,333]` |
| Ignorar | Elipse | `[26,340,75,390]` |
| Favoritar | Elipse | `[77,340,126,390]` |
| Curtir | Elipse | `[128,340,178,390]` |
| Gesto | Retângulo | `[66,392,139,403]` |

O contorno externo usa retângulo arredondado`[0,0,202,403]`, raio14, para retirar o bege dos cantos do painel. A variante conservadora preserva64.634pixels e torna17.378transparentes. Regiões inteiras de nome/localização produzem remendos retangulares evidentes sobre preto; por isso não são a primeira opção de teste.

### Precisão adicional em nome, selo e localização

A variante precisa restaura o alpha dos dois retângulos de legenda e retira apenas os contornos identificados **dentro deles**. Critério de semente neutra:`maxRGB>=120 && minRGB>=100 && maxRGB-minRGB<=60`; critério azul do selo:`B>R+15 && G>R+15 && B>125`. A união é dilatada em1pixel com`MaxFilter(3)` para retirar antialiasing da UI. As grades de pixels foram inspecionadas antes da exportação: a seleção identifica as formas de letras/números/selo, sem uma área de pele adicional reconhecível nos bounds. Trata-se de uma máscara local revisada visualmente, não um algoritmo universal de segmentação de interface.

- Nome/selo:317pixels-semente;699pixels após dilatação.
- Localização:195pixels-semente;606pixels após dilatação.
- Total da imagem:66.737pixels preservados,15.275transparentes; **2.103pixels fotográficos adicionais** preservados em relação à variante conservadora.

Chips e círculos continuam com sua região completa retirada, porque o preenchimento dessas peças também é interface incorporada. Selecionar somente seus contornos deixaria o fundo modificado dos botões na suposta fotografia. Nenhuma textura/pele foi criada para ocupar as lacunas.

### Hashes finais desta extração

- Variante conservadora e cópia raiz:`0f07951bf0db194f4bb4cb3024288fa560dd1a6a0a7e30c833f2d6514137dab9`.
- Alpha conservador:`484b5f3d9d5f6f9647f72ddc4010df309e04cd24848148ba959a63d7319f0d5c`.
- Variante precisa e cópia raiz:`457ce5eea85460635937551c64368d1d5fc0d54febcdb433b93af626b2bfe448`.
- Alpha preciso:`b7bc57ea8586bc107edc98869baf15853b6fe78954fe7e295cb0ba2865701894`.

### Handoff para implementação e auditoria

Usar prioritariamente a variante precisa para um teste reversível. `cover` proporcional pode aproveitar a altura; calibrar posição horizontal para que rosto/torso e lacunas coincidam com o DOM. **Não definir largura e altura independentes que deformem a pessoa.** Exibir a imagem sobre preto não recupera os pixels removidos: as letras viram silhuetas negras e as peças deixam lacunas. O DOM precisa ser independente e alinhado, e o auditor deve procurar halos, remendos, UI duplicada e escurecimento excessivo.

As prévias foram abertas sobre preto e quadriculado. Não foi observada UI branca/azul reconhecível sobrevivendo nas regiões removidas; os vazios da variante precisa naturalmente preservam a silhueta dos glifos removidos. Se o alinhamento não esconder essas lacunas ou a composição ficar materialmente alterada, rejeitar a variante para aceite. Esta é **extração parcial com lacunas**, não fotografia limpa original, restauração ou reconstrução generativa.

Nenhuma autorização de reconstrução generativa foi presumida; ImageGen não foi usado. Nenhum HTML/CSS/JS, screenshot ou nota de auditoria foi modificado nesta etapa. O gate continua>9,0 com evidência nova.

### Sanitização da variante precisa

RGB foi zerado somente nos15.275pixelsalpha0 da variante precisa e de sua cópia de runtime. Os66.737pixelsalpha255 mantêm exatamente o RGB da fonte. Alpha e contagens não mudaram; conservadora intacta. A aparência composta não muda, mas o arquivo preciso deixa de armazenar letras/ícones originais escondidos em pixels totalmente transparentes. Esta operação não recupera nem fabrica anatomia. Scripts e manifestos foram atualizados para reproduzir o asset sanitizado.

## Variante precisa2 — contornos de status/progresso/informação e geometria mais justa

O primeiro teste em navegador mostrou que as máscaras conservadoras ainda usadas em parte da variante precisa1 criavam áreas sem textura maiores que as peças reais. O refinamento abaixo **não preenche essas áreas**: volta a expor somente os pixels genuínos da fonte que não pertencem aos overlays. A conservadora e a precisa1 foram preservadas para comparação.

Candidata atual: `assets/enzo-mockup-foto-com-lacunas-precisas2.png`. Manifesto: `assets/mask-manifest-preciso2.json`. Script reproduzível: `assets/derivados/mask_torso_preciso2.py`. Prévia sobre preto/quadriculado: `assets/derivados/enzo-painel03-preview-{preto,quadriculado}-preciso2.png`; ambas abertas e inspecionadas.

Mudanças em relação à precisa1:

- Hora e ícones do status: retirados por contornos claros, usando`maxRGB>=120 && minRGB>=100 && rangeRGB<=60`, dentro dos bounds originais, dilatação de1px. O céu entre os glifos passa a ser preservado, em vez de ficar em um retângulo transparente.
- Progresso: dentro de`x12..191,y21..26`, retirados somente os pixels com contraste vertical local `meanRGB(y) - average(meanRGB(y-3),meanRGB(y+3)) >=9` e`rangeRGB<=80`; dilatação de1px. A linha incorporada se destaca das amostras de céu próximas. Não se usa mais a faixa inteira de8px como buraco.
- Informação: só contornos claros em`[171,282,191,302]`, critério`maxRGB>=90 && minRGB>=75 && rangeRGB<=45`, dilatação1px. O interior do círculo volta a expor os pixels fonte; não se apaga mais um disco de22px.
- Nome/selo e localização: o mesmo método de contornos da precisa1, sem mudança.
- Pills completos, porque têm preenchimento de UI: Fashion`[12,311,60,331]`, Editorial`[61,311,110,331]`, Comercial`[112,311,170,331]`, raios10. Bounds foram refinados após zoom de pixels da referência: as peças visíveis estão aproximadamente entrey312e330, com1px de margem para antialiasing. A terceira máscara deixa de se estender atéx176, onde já havia fotografia sem peça.
- Círculos: centros`(50,365)`, `(101,365)`, `(152,365)`, raio22. A máscara anterior tinha semieixos de25/26px. O raio22 cobre o círculo original de cerca de21px mais a borda suavizada.
- JPEG vermelho: um halo vermelho escuro fora do terceiro círculo ainda era visível na primeira prévia. Retirado por contornos de cor apenas no entorno`[126,339,178,391]`, com`R>16 && R>=1,8G+5 && R>=1,3B+3`, dilatação1px. Assim não foi necessário ampliar uniformemente os três círculos.
- Gesto: bounds reduzidos para`[69,395,135,401]`.

Todas as seleções são locais e foram inspecionadas visualmente; não se propõe o threshold como segmentador universal. Não foram observados traços de UI brancos, azuis ou vermelhos reconhecíveis sobrevivendo nas prévias finais. Os vazios negros ainda conservam a silhueta dos glifos que foram retirados; isso é ausência de pixels, não texto incorporado. O auditor deve procurar desalinhamento entre essas lacunas e a interface real na nova captura.

Validação pixel a pixel: **70.768pixels visíveis** com RGB idêntico ao recorte original; **11.244pixels transparentes** com RGB zerado. São **4.031pixels reais adicionais** preservados em relação à precisa1 e6.134em relação à conservadora. Sem resampling, clonagem, preenchimento, ImageGen ou anatomia gerada. O gradiente escuro já presente no mockup continua incorporado aos pixels preservados.

Hashes da precisa2:

- PNG derivado e cópia de runtime:`7a7bd30d8de86d6c6c20b27f9bef49c6d6b23f389335934c961d0c15e286d592`.
- Alpha:`7103e6a799fc277c477168d302e018e1687ac78399a8327da72e4deb7aaa766f`.
- Prévia preta:`c0f58e02072ad2fbd337f85ac8327c1d534882d16dcf22c51a82ef17a0863149`.
- Prévia quadriculada:`9c7ab2f0f174b9cbe4a0481aebb81b100d18e6fc3aaa93a2bd3adf154bc2b7df`.

O implementador foi informado do novo arquivo e hash antes de capturar. Esta entrega de assets não altera a nota nem libera a Tela04; exige nova renderização e auditoria independente.

## Ciclo6 — inspeção do status e candidata de UI tipográfica

A inspeção de RGB corrigiu a hipótese de que o threshold anterior apagava um retângulo arbitrário de nuvem. Dentro das caixas de status, a hora tem58sementes e135pixels após dilatação, bounds`x17..34,y5..13`; ícones têm118sementes e229pixels, bounds`x159..193,y5..12`. São glifos e halos JPEG/antialias da UI. O limite`rangeRGB<=25` deixaria parte do sinal celular, cujos pixels brancos são tingidos pelo azul (por exemploRGB221,240,255, range34). Não foi exportada uma variante precisa3 de status que presumisse correção sem inspeção. O plano6 do implementador utiliza um fade de alpha restrito ao céu superior; isso é decisão de integração, não geração de foto por este agente.

Foram criados `assets/name-type.svg` e `assets/location-type.svg` com paths de suporte dos glifos, sem fotografia, `<image>`, raster embutido, fonte remota ou RGB fotográfico. As caixas fonte estão em `assets/ui-type-manifest.json`: nome`(11,272,66,21)`, localização`(11,292,108,16)`. O SVG deve ser projetado com a mesma escala/offset da foto; uma nova baseline nativa não garante co-registro.

A primeira candidata binária foi rejeitada como candidata final após inspeção em navegador pelo implementador: as escadas dos pixels do mockup geraram aparência de pixel-font, especialmente na localização. Esses arquivos não recebem nota de fidelidade por si.

Foi então entregue **somente o nome para um teste AA geométrico**, conforme orientação do controlador:225pixels de core branco opaco,326pixels de anel geométrico de1px comopacity0,2, e`feGaussianBlur stdDeviation="0.35"` em unidades fonte. Não são699pixels opacos nem cópia das cores da pele/céu. O fill continua uniforme`#fafafa`; a suavização é exclusivamente tipográfica. Script reproduzível `assets/derivados/soften_name_type.py`; prévia neutra `name-type-aa-preview.png`. Reproduzir após `extract_ui_type.py`, pois a extração base gera a candidata binária anterior. O manifest identifica a versão AA atual e seu hash.

Essa candidata deve ser aceita ou rejeitada por comparação real com a referência e com a versão de texto nativo. Não foi alterada a fotografia precisa2, não foram preenchidas as suas lacunas e nenhuma captura ou auditoria foi modificada por este agente. `location-type.svg` permanece candidata binária não final até a decisão sobre o método AA. O arquivo experimental `verification-type.svg` também não foi aprovado para runtime: a verificação de sementes mostrou que o check do badge original é escuro, não branco, e a regra inicial de branco não extraiu um check. Manter o SVG de selo previamente usado até uma alternativa vetorial correta ser verificada; não tratar esse experimento como vetor original.

## Ciclo7 — foregrounds raster de UI por contorno

O coordenador alterou a estratégia de implementação do plano6: a regra de «somente paths» para a tipografia era uma decisão técnica daquele plano, não uma proibição específica do usuário a texto raster independente. Os SVGs de glifos binários/AA ficaram como experimentos não aprovados; não foram usados para anunciar nota>9. Os ícones continuam sendo vetores separados.

O candidato7 usa duas camadas de **UI foreground independentes da fotografia**:

| Asset | Caixa fonte `(x,y,w,h)` | Alpha opaco | Fill da caixa | SHA-256 |
|---|---|---:|---:|---|
| `assets/ui/name-reference.png` | `(11,272,66,21)` | 551/1.386pixels | 39,75% | `30a8fd4a3448a7cb4006518668e04ac44170496fd55b1b4428648864df6e0bb9` |
| `assets/ui/location-reference.png` | `(11,292,108,16)` | 606/1.728pixels | 35,07% | `610a71b6567fb02663d45e6dc11a45d66fb658a23f2d67c7b1081e0ea70f45da` |

Fonte: o mesmo crop203×404`[420,0,623,404]` do mockup original. As caixas são,respectivamente,`[11,272,77,293)` e`[11,292,119,308)`, com borda direita/base exclusivas. O nome não inclui o selo azul. A camada de fotografia permanece `enzo-mockup-foto-com-lacunas-precisas2.png`, sem texto ou rótulo visível incorporado nas regiões retiradas.

### Método e limitação do matte

Seja`D` a máscara dos pixels removidos da foto precisa2. Dentro de cada caixa, o foreground usa alpha255 somente onde`D=1`; seu RGB é copiado do **pixel real correspondente da UI na fonte**. Fora desse contorno, alpha e RGB são zero. Isso não exporta o retângulo fotográfico inteiro:60,25%da caixa do nome e64,93%da localização são transparentes. Não há arquivo de foto+texto retangular em runtime, nem captura completa usada como fundo.

O suporte de`D` já inclui uma faixa de1pixel de dilatação ao redor do núcleo do glifo. Nas bordas antialias do JPEG, o RGB existente já combina a letra com o contexto de pele/gradiente; essa faixa é um **matte contextual conhecido da referência**, não uma fonte tipográfica original ou transparência de fonte recuperada. O candidato inicial não expandiu essa faixa além de`D`. Nenhuma cor foi gerada, interpolada, clonada ou estimada para o corpo. A separação preserva dados existentes e pode sofrer costuras ao escalar as duas camadas; a captura real precisa verificar isso.

Script reproduzível: `assets/derivados/extract_ui_reference.py`. Manifesto com fonte, hashes, caixas, fill e testes: `assets/ui/reference-type-manifest.json`. Prévias individuais sobre neutro e a composição de inspeção estão em`assets/derivados/`. A composição de inspeção não é screenshot do navegador e não deve ser usada como fundo da implementação.

### Testes executados

- Todos os pixels opacos de cada foreground têm RGB idêntico ao pixel da fonte na mesma coordenada.
- Todos os pixels transparentes têm RGB zero; o PNG não esconde uma foto inteira nas áreas transparentes.
- Foto precisa2 sobre preto + foreground correspondente, em resolução nativa, resulta em **RGB idêntico à fonte em todos os pixels das duas caixas**. A asserção percorreu ambas as caixas por inteiro.
- Os dois arquivos e a composição foram abertos visualmente: tipografia original suavizada do JPEG preservada, sem o efeito de pixel-font da candidata vetorial binária.

### Integração e aceite

Projetar os foregrounds pela mesma escala proporcional e pelo mesmo offset da foto. Manter`h1` e`p` nativos como conteúdo acessível verdadeiro, com fallback de fonte nativa se uma imagem de UI não carregar; não duplicar a leitura por leitor de tela. As imagens não devem interceptar toque/click.

Essa solução é específica para os rótulos fixos «Enzo,26» e «São Paulo,SP ·1,84m» desta referência. **Não é um sistema de fonte reutilizável para nomes, localidades ou idiomas arbitrários.** A integração de dados dinâmicos deve usar a fonte adequada ou criar uma alternativa documentada; não reutilizar o bitmap de Enzo com dados semânticos diferentes.

O teste em resolução nativa comprova proveniência e separação, não fidelidade após escala no navegador. O implementador recebeu arquivos/caixas/hashes antes de capturar o candidato7. Aceite depende de novas capturas e auditoria independente; não foi atribuída nota por este agente.
