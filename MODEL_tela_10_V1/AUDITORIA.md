# Auditoria independente — Tela10 V1

**APROVADA VISUALMENTE: 9,28/10**, soma ponderada **9,2825**. Versão `1.0.0-prototipo.1`, auditoria de 2026-11-11. Gate estritamente >9,0 atendido; meta9,5 não atingida. Nenhum P1 material identificado. Planejador11 liberado; esta auditoria não iniciou11 nem publicou o pacote.

## Rubrica aplicada às capturas reais

| Critério | Peso | Nota | Parcela | Fundamentação |
|---|---:|---:|---:|---|
| Fotografia/identidade/enquadramento |35%|9,55|3,3425|Matheus correto, frame circular integral em1:1, cabelo/rosto/ombros preservados; resolução77px e matte JPEG visíveis na ampliação. Suporte editar oculta área indisponível sem inventar foto.|
| Geometria |25%|9,00|2,2500|Hierarquia, três tags, medidas, cinco linhas e navbar mantidas. A adaptação à tela mais alta deixa mais espaço entre avatar e identidade e altera a densidade horizontal relativa à fonte; menus compactados para44px na375.|
| Tipografia/ícones/chips |20%|8,90|1,7800|Texto nativo legível e pesos coerentes. Arial aproxima a fonte; pictogramas reinterpretados e editar com lápis preto maior/mais dominante que o original, pin e status mais finos.|
| Cores/contraste/sobreposição |10%|9,60|0,9600|Papel quente/chips claros próximos da fonte; preto e selo preto corretos. Overlay opaco claro fica visualmente mais marcado que na miniatura original.|
| Responsividade/acabamento |10%|9,50|0,9500|Três capturas reais sem cortes horizontais; cinco menus e nav íntegros, avatar proporcional. Limites fora dos tamanhos-alvo e safe-area de aparelhos físicos não demonstrados.|

As notas não foram herdadas da09. O suporte editar dominante recebe desconto em tipografia/ícones e acabamento cromático; não é motivo para elevar a avaliação por cumprir cobertura técnica. Os P2 acima permanecem e impedem afirmar9,5 ou equivalência pixel a pixel.

## Evidência visual examinada

Abertos individualmente com `view_image`: referência `MODEL_assets_v1/referencias/10-meu-perfil.png` (185×317), `captura-375.png` (375×812), `captura-390.png` (390×844), `captura-430.png` (430×932) e `comparacao-390.png` (883×844). A comparação conserva referência493×844 e app390×844, sem deformação; por terem proporções de tela diferentes, a fotografia na referência normalizada por altura fica maior que no app. A escolha do app por largura intrínseca preserva o frame e cumpre o contrato, mas muda respiros e densidade perceptual, penalizados em geometria.

São cinco menus fonte, sem bio ou sexto menu; Matheus Silva,24, São Paulo/SP, Fashion/Editorial/Comercial e1,85m/80kg/42 estão presentes. Selo preto, perfil ativo preto e demais ícones locais. HTML/CSS/JS revisados: textos nativos, sem captura integral como fundo. Avatar com largura fluida e altura automática77×77; overlay com mesmo box e viewBox77×77; centro64,5/64, raio opaco13,5 cobre footprint12,5. Suporte CSS independente permanece se SVG não aparece. Nenhum recorte por cover divergente, pessoa substituta ou síntese fotográfica observado.

## Conferências independentes e limites

Executado Python/Pillow/hashlib pelo auditor, sem regenerar assets ou capturas: os46 hashes de `EVIDENCIAS_RELEASE.json` coincidem com arquivos atuais; referência é RGB idêntica ao crop global[612,434,797,751] do mockup geral (`ImageChops` bbox=None); todos os4386 pixels com alpha>0 do avatar mantêm RGB da região local[53,39,130,116]. Dimensão77×77. Painel direito da comparação é exatamente a captura390 (bbox=None).

`EVIDENCIAS.json`, `EVIDENCIAS_EXTRA.json` e scripts Playwright foram revisados. Chromium156.0.8078.79/DPR1 reporta três documentos sem overflow, assets carregados, avatar1:1/frame100%, alvos≥44px e sem interseções, zero console errors/networkFailures/badResponses. Relatório registra cinco menus/Adicionar, edição segura/cancelar/reload, disponibilidade em memória, Escape/restauração/contenção de foco, navegação03/07/06/retorno09, reduced-motion, fallback avatar e overlay permanente. Código confirma dialogs locais sem backend, preços/métricas ou portfólio de outra pessoa inventados; escrita de dados via textContent e selo removido após edição.

**Distinção de escopo:** o auditor abriu as imagens reais e executou conferências de arquivos/pixels/hashes; não executou segunda sessão Chromium, não refez interações nem recapturou. Interações/overflow/erros são evidência executada pelo implementador, corroborada por revisão de código, não teste independente duplicado. Falha de overlay foi simulada por visibility:hidden, não por resposta HTTP quebrada; coverage geométrica e suporte permanente são verificáveis no código. Safe-area física, leitores de tela e larguras/alturas fora dos três alvos não estão integralmente cobertos. `min-height:780px` permite rolagem em janelas mais baixas e não prova ajuste universal.

## SHA256 das evidências abertas

- `captura-375.png`: `0ca8893f94aab07a750074c1e0693a00cd8104fa2521d64e833dbf26ba7193c4`
- `captura-390.png`: `a312ea9b53d4e1f2714a19ecc071ce80579fe7654d84312de42d9f4e265f4c4e`
- `captura-430.png`: `6e0a478203e79e8885261d2474ccdfd431e51bcf8d2240169109baae7e68b61a`
- `comparacao-390.png`: `d53f4c6f2080c5e1e29f6ea442cee7f43536615276d993daa9135c1d36e14d8f`
- `EVIDENCIAS.json`: `22e6942711d8cf36169b9ac9f19f91e89eb1fbe7f07eb8827e2bac26e82efb13`
- `EVIDENCIAS_EXTRA.json`: `0554c6fe1a0fe0c5d3bc9e70f653834647d09f26fc1d5c6e8a1628a378cbda90`
- `EVIDENCIAS_RELEASE.json`: `5fda312c93029d6158ad20648d20cdbeacb068ef21459ec75a0a88d83da8676e`
- `assets/matheus-avatar.png`: `d097b8d18b094325bcebc2ccbbb600614292c4006400d45131febe9607f5b40d`
- `assets/edit-overlay.svg`: `6ccd59628e2f133c876d0db6b9962918a21b64f094873bf2f2d5aa2162fddc95`

## Decisão e preservação

Gate10 aprovado>9,0, sem P1 material; **próximo papel: planejador11 LIBERADO**. P2 não bloqueantes acima ficam registrados. Runtime, assets, capturas10 e pacotes03–09 não foram alterados pelo auditor. Somente este relatório e a fila foram escritos. Nenhuma publicação ou início11 nesta etapa.
