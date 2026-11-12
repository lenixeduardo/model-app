# Revisão independente — tarefa 1, rodada 2

Commit `c546d8583c247b17fb1122724cddd991c913c321`; diff `db87423..c546d85`. Escopo: achados abertos da rodada1, footer02 e eventual regressão introduzida pelo fix. Li o diff, Rodada2 do relatório e ruling de marca em `task-1-brief.md:40`; abri novamente as seis capturas finais e comparações390. Os5 testes GREEN, fallback e integridade de RGB são evidências relatadas, coerentes com o diff; a suíte não foi repetida. Somente este relatório foi escrito.

## Veredictos

**Spec: APPROVED. Quality: APPROVED WITH MINOR NOTES. Gate visual: APROVADO, 01=9,23 e02=9,10.** As duas telas superam estritamente9,0. A meta9,5 ainda não foi atingida. Esta aprovação vale para as imagens identificadas pelos hashes abaixo e para o escopo da tarefa1; não aprova estado compartilhado, backend ou auditoria posterior de acessibilidade.

## Verificação dos achados abertos

| Achado | Estado | Evidência |
|---|---|---|
|01 — marca fantasma e perda de continuidade do ombro|**ADDRESSED**|Hero parcial preserva fotografia+wordmark/divisor fornecidos, sem máscara de glifos nem segundo logo visual. O ombro permanece visível; não há duplicação escura nas três larguras.|
|02 — máscaras/apoios excessivos e alinhamento dos rótulos|**ADDRESSED**|Máscaras menores acompanham nome/cidade, sem as faixas completas ou grandes retângulos vazios da rodada1. Torso, roupa e áreas entre os rótulos voltaram a ser contínuos. Bookmarks têm apoio visual estreito e alvo transparente maior.|
|02 — peso e hierarquia dos nomes|**ADDRESSED**|`MODEL_tela_02_V1/styles.css:17` separa nome700 e cidade400; coordenadas individuais alinham os dois níveis à região original. Chips, Home ativo e fotografias proporcionais mantêm as correções anteriores.|
|02 — footer terminando antes do viewport|**ADDRESSED**|Barra ancorada ao fundo nas capturas375×812,390×844,430×932; não há área externa preta abaixo das bordas arredondadas nem sobreposição dos cards observável.|
|Comparações proporcionais|**RESOLVIDO PRESERVADO**|As novas comparações mantêm escala uniforme e faixa cinza de diferença de altura; não reabro o item já aprovado.|

O ruling está implementado de forma restrita em01: o hero não contém tagline, status nem botões. H1 continua no DOM; `hero-loaded` o oculta apenas visualmente após sucesso da imagem, deixando fallback nativo em falha. `ASSETS.md` e `DESIGN_SPEC.md` registram a arte estática, crop, limitação e procedência. Não vi extrapolação dessa exceção para legendas02 ou controles. Não há fotografia inventada, troca de pessoas, alongamento aparente dos corpos ou fotografia inteira ausente.

A diferença de altura entre a referência02 e o viewport é agora espaço interno antes da barra. É uma adaptação aceitável para preservar escala e proporção das fotos: não produz a antiga barra flutuando sobre uma faixa externa nem esconde controles. Não identifiquei novo defeito importante de navegação no fix.

## Nova avaliação visual ponderada

Subnotas0–10, pesos foto35%, geometria25%, tipografia20%, cores10%, responsividade10%. Pontuação julgada pelas capturas desta rodada, não herdada das anteriores nem derivada dos testes.

| Tela | Foto35% | Geometria25% | Tipografia20% | Cores10% | Responsividade10% | Total |
|---|---:|---:|---:|---:|---:|---:|
|01|9,7|9,3|8,3|9,2|9,3|**9,23**|
|02|9,5|9,0|8,6|8,8|9,2|**9,10**|

01: rosto, ombro e marca recuperam a composição original sem cicatrizes de máscara. A posição dos CTAs é próxima à referência; tagline e contratante ainda diferem em peso/tamanho, e o contratante fica um pouco abaixo do equivalente proporcional. Isso limita tipografia e impede9,5 global.

02: as quatro fotografias mantêm pose, escala e área corporal, com perdas localizadas na pequena UI raster já documentada. A grade e os textos recuperaram a hierarquia; os apoios pretos continuam mais duros que a sobreposição natural da referência. Essa diferença é visível, mas agora restrita à área dos rótulos/ícones, sem retirar blocos do corpo. Por isso cores e tipografia recebem notas menores; a alta nota fotográfica deriva da preservação das pessoas/composição, não de nitidez inventada. As três larguras são consistentes e não mostram colisão ou corte dos nomes/cidades.

## Notas menores remanescentes

- `MODEL_tela_01_V1/styles.css:11`: tagline/contratante e status não reproduzem exatamente o peso/escala do original. A fonte de baixa resolução dificulta equivalência fina; isso não impede o fluxo nem descaracteriza a composição.
- `MODEL_tela_02_V1/styles.css:17`: os pequenos fundos opacos dos rótulos ainda são perceptíveis. Não é possível recuperar honestamente a foto oculta pela UI raster apenas retirando o fundo. Refinamento adicional deve conservar os pixels fornecidos e a legibilidade, sem reconstrução ou substituir pessoas.
- `MODEL_tela_02_V1/assets/filter.svg:1`: o primeiro ícone do header ainda não é idêntico ao desenho da referência; mantém escala, posição e função coerentes. Diferença residual menor.

Essas notas justificam aprovação com ressalvas, sem declarar a meta9,5 atingida. Não é necessário reabrir os fluxos de navegação já validados para iniciar a próxima tarefa autorizada.

## SHA-256 das evidências abertas

- `MODEL_assets_v1/referencias/01-splash.png`: `ee9b8b3511592c36c66bd8da1b9d6936aeb0c1264b6fb97bdb8d830017126f80`
- `MODEL_assets_v1/referencias/02-descoberta.png`: `a152aeca87a53a5a1890f0bc04a9710bb7838741c076f999e3fa5c1d1a6d0a39`
- `docs/correcoes-123/capturas/01-375.png`: `c307bff5977f60c57889d33b646964e886eb25aa8e70b69644b99b2e434a0b6b`
- `docs/correcoes-123/capturas/01-390.png`: `8fea9068d893069cf6d5c4d7b0d33f9e05be2cc402914bc7bc502d70b2b5abf1`
- `docs/correcoes-123/capturas/01-430.png`: `063ff7d132635827c416e18325706e08ab377e2f43134bbb5f65c07fb2b49a6a`
- `docs/correcoes-123/capturas/01-comparacao-390.png`: `e547817157c54dd9f739bc64413e5c71fec062a078f390947b07314cb88ba8ab`
- `docs/correcoes-123/capturas/02-375.png`: `5b3ea04c628ab2a2b54603b92aabd1b4fa12e32cc835f8a0ce1a1426f7a15c0e`
- `docs/correcoes-123/capturas/02-390.png`: `786c54f3f58660346a3c04ded8e3e4825989fc381ec6b4d037c6bfa77e8c7b1f`
- `docs/correcoes-123/capturas/02-430.png`: `a41fbf838d05b57e03d53527d8426d09608681f4f2f640485b198ae229f09127`
- `docs/correcoes-123/capturas/02-comparacao-390.png`: `6b26bf0d2efa3152df5170e6ac03716fc4791acfc587c026fadc1d5b50d21eac`
