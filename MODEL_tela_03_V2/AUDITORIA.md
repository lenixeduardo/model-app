# Auditoria independente — Tela 03 V2, ciclo 7

Data:2026-11-09. Versão final avaliada: **2.0.0-prototipo.7**. Resultado: **APROVADA VISUALMENTE — 9,13/10** (soma ponderada9,125, arredondada). Gate vigente **>9,0** atingido; meta9,5 ainda não atingida. A aprovação aplica-se ao protótipo estático de Enzo e às evidências abaixo, com as limitações de integração documentadas; não certifica uma fonte genérica nem um aplicativo integrado ao backend.

## Evidências abertas e verificadas

O auditor abriu novamente:

- Referência oficial `../MODEL_assets_v1/referencias/referencia-tela-03.png`,203×404.
- `captura-375.png`,375×812; `captura-390.png`,390×844; `captura-430.png`,430×932.
- `comparacao-390.png`, referência e captura final com alturas normalizadas, sem deformar proporções.

Também abriu uma ampliação das legendas da captura390 para conferir costuras/halos, leu método/limitações em `ASSETS.md`, `DESIGN_SPEC.md` e `README.md`, conferiu a integração dos H1/P e das imagens decorativas e verificou o relatório final. O auditor não executou outra rodada de navegador nem confundiu a composição de inspeção em203px com screenshot real.

Renderização registrada: Chromium156.0.8078.79, Playwright, servidor HTTP local, DPR1, resultado`passed`. Documento=viewport e console/rede vazios nos três tamanhos.

| Captura final avaliada | SHA-256 conferido contra o JSON |
|---|---|
| 375×812 | `785b97112705d0b79deb10be2158e904deb10f3b88eec10801e0eb65ff2543e1` |
| 390×844 | `e3873b6bed0892bb40261c4b840f3d4479604df9896773adac2c5587f7fddf64` |
| 430×932 | `6a53548cd0df0a437bfa2e560d291c19b7f8c6df2fb4614ae1cb2e67fd855b66` |

## Método de composição e escopo do aceite

A fotografia de runtime continua sendo a extração203×404 com lacunas transparentes onde havia UI; preserva os pixels genuínos de Enzo, inclusive o torso antes descartado. Não houve geração de pessoa/pele, preenchimento de corpo ou troca da pose. O cover proporcional recorta lateralmente para as viewports mais estreitas, sem estirar o retrato. O gradiente escuro já presente na fonte permanece nos pixels conhecidos; fades de alpha restritos ao topo/rodapé integram a faixa do status e a base preta.

Somente nome e localização usam dois foregrounds raster de **UI independentes da fotografia**, extraídos por contornos, não um retângulo de foto+texto. O nome ocupa39,75%de sua caixa e a localização35,07%; o restante é transparente. O RGB dos contornos e de sua franja contextual conhecida de1px vem da referência. Isso preserva o antialias do JPEG, mas **não é recuperação da fonte tipográfica original nem um sistema tipográfico genérico**. O selo e demais ícones continuam SVGs locais separados.

Os H1/P nativos permanecem noDOMacessível como fonte semântica; as imagens visuais são decorativas, com`alt=""`/`aria-hidden`. A camada raster só ativa se os dois arquivos carregarem e ambos os textos coincidirem exatamente com o perfil fixo da referência. O relatório cobre falha individual dos PNGs, opt-out e divergência dos textos, com fallback nativo atômico. Para dados arbitrários/tradução, usar o modo nativo e revalidar a aparência; não reutilizar o bitmap de Enzo com outra semântica.

O teste de igualdadeRGBem203px foi considerado evidência de proveniência/separação, **não prova suficiente de fidelidade visual**. O aceite abaixo se apoia nas três capturas reais e na comparação final.

## Rubrica independente do ciclo 7

| Critério | Peso | Nota | Parcela | Constatação visual final |
|---|---:|---:|---:|---|
| Fotografia, identidade e enquadramento | 35% | 9,1 | 3,185 | Enzo, céu, cabeça, ombros e torso reais ocupam a composição e mantêm proporção natural. A relação entre torso e informações está próxima da referência, sem a grande faixa preta que antes substituía o corpo. Limites residuais: resolução reduzida da fonte, recorte horizontal por cover e céu superior mais uniforme. |
| Geometria e posicionamento | 25% | 9,2 | 2,300 | Nome/localização foram registrados à geometria fonte, chips e ações estão organizados e o grupo de círculos permanece centrado. O aumento da informação recobre sua lacuna e aproxima a escala da referência. Persiste diferença menor de margem direita e da relação entre as razões do painel e das viewports. Não há controle cortado ou desalinhamento material nas três capturas. |
| Tipografia, ícones e chips | 20% | 9,1 | 1,820 | Os foregrounds se aproximam do peso/antialias dos rótulos da referência e eliminam o contorno negro irregular dominante do ciclo6. Não foi observada costura retangular ou segundo glifo nas capturas finais. Chips/ícones continuam mais nítidos que os rótulos raster, e o selo tem borda escura um pouco mais marcada; são diferenças menores. Os textos continuam legíveis e corretos. |
| Cores, contraste e sobreposição | 10% | 9,0 | 0,900 | Preto/branco, céu/pele e coração vermelho preservam a identidade; status e rodapé ficaram limpos. O torso é visível atrás das informações, com contraste suficiente. Pequeno matte escuro ao redor do selo e das pills, céu superior liso e base inferior mais uniformemente preta permanecem como refinamentos, sem remendo dominante ou perda material do enquadramento. |
| Responsividade e acabamento | 10% | 9,2 | 0,920 | Três resoluções corretas, sem overflow registrado; imagem/SVGs carregados e ações/foco/alvos de toque verificados. O registro das camadas de texto é consistente em375/390/430. Limites de aparelho físico, VoiceOver e safe areas reais não foram certificados. |
| **Total** | **100%** | | **9,125 ≈9,13** | **Gate >9,0 atingido.** |

A nota é estimativa visual fundamentada, não métrica pixel-perfect automatizada. Não foi elevada por exigência de continuidade nem atribuída só pelo código/JSON. A correção visual dos rótulos é observável em relação à referência e remove o P1 que impediu o aceite anterior.

## P1 anterior e diferenças P2 atuais

**Não foi identificado P1 material nas imagens finais deste perfil estático.** As áreas anteriormente críticas em390 foram reinspecionadas: nome/selo`x24..184,y573..604`, localização`x24..231,y619..640` e informação`x359..389,y597..625`. Os blocos/recortes negros irregulares do nome e da localização foram resolvidos materialmente; a informação apresenta contorno mais coerente. Nenhum segundo texto, faixa retangular de fotografia ou costura de camada reconhecível foi observado nesses recortes finais.

P2/documentação para refinamentos futuros:

1. Selo: em390, aproximadamente`x157..184,y573..602`, a borda escura segue mais marcada que a referência. Refinar somente se houver melhora visual demonstrada, sem reintroduzir o halo anterior.
2. Chips: aproximadamente`x26..350,y652..693`, traço e tinta são mais definidos que os rótulos raster originais; pequena borda/matte escura permanece ao redor das peças. Não bloqueia leitura ou hierarquia.
3. Informação: o círculo termina próximo da borda direita, especialmente em430. Qualquer ajuste de margem deve continuar considerando a lacuna da fotografia, e não mover isoladamente o ícone.
4. Céu/topo e base: faixa superior mais uniforme e rodapé mais preto que o raster normalizado; a transição atual não apaga torso relevante nem forma um remendo dominante. O aspect ratio diferente exige algum recorte horizontal; não estirar para igualar largura/altura.
5. UI raster estática: desfaz a dependência da fotografia, mas não substitui a fonte necessária a nomes/localizações dinâmicos. Fallback visual nativo existe e foi testado; sua aparência com novos dados exige auditoria própria. Essa limitação de integração não é uma divergência visual bloqueadora do perfil Enzo aqui aprovado.

## Verificação técnica e decisão da fila

Relatório final`passed`: carregamento de fotografia/SVGs/camadas deUI; console/rede vazios; documento=viewport; curtir/favoritar, ignorar/desfazer, diálogos/Escape, foco e toque; movimento reduzido; fallback de fotografia; fallback atômico de cadaPNGde legenda; opt-out e divergência de metadados. O revisor conferiu a presença de H1/P semânticos e a ocultação decorativa dos raster. Não existe alegação de persistência/backend. Dispositivo físico e tecnologia assistiva permanecem não certificados.

**Auditor03 ciclo7 concluído:APROVADA VISUALMENTE,9,13/10.** As evidências finais verificáveis ultrapassam o gate>9,0 e não apresentam bloqueador material no escopo estático acordado. O planejamento e a implementação da Tela04 estão **liberados para a próxima etapa da fila**, mantendo planejador→assets→implementador→auditor e sem transferir esta nota para a tela seguinte. Meta9,5 permanece objetivo de refinamento, não motivo para inventar pontuação. O coordenador deve preservar esta versão e seus arquivos no pacote/publicação; o auditor não publicou, não alterou código/capturas e não iniciou a Tela04.
