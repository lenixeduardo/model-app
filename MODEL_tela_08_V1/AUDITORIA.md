# Auditoria independente08 — APROVADA VISUALMENTE

Versão **1.0.0-prototipo.1**, auditada em2026-11-11. Estimativa visual **9,23/10** (soma9,234615), gate **>9,0 atingido**, meta9,5 ainda não atingida. **Nenhum P1 material identificado no fluxo local. Próximo papel: planejador09 LIBERADO.** A nota não é medição pixel-perfect nem se transfere às próximas telas.

## Evidência examinada

Li DESIGN_SPEC.md, PLANO.md, ASSETS.md, README.md, relatorio-browser.json, EVIDENCIAS_SHA256.json, HTML/CSS/JS e os dois scripts de teste. Abri obrigatoriamente via view_image a referência oficial200×317, as três capturas375×812/390×844/430×932 e comparacao-390.png922×844. Conferi independentemente SHA256 dos11 arquivos do manifesto: todos correspondem. A comparação preserva referência532×844 e captura390×844, sem igualar artificialmente larguras. Referência: SHA256 `b2a0298f8990e50248b5e11bc1af49b72d468ec4ff11691f19d5f8ccce020d99`.

A documentação de assets registra crop[220,434,420,751] idêntico à fonte global e seis SVGs locais aproximados. Nenhuma foto ou UI rasterizada é utilizada. Fonte original não fornecida: Arial/Helvetica constitui aproximação explícita, sem alegação de identidade tipográfica exata.

## Rubrica adaptada

Fotografia/identidade/enquadramento: **N/A** por ausência de fotografia na fonte. Não atribuí10 gratuito. Nota=(25G+20T+10C+10R)/65; pesos normalizados38,4615%/30,7692%/15,3846%/15,3846%. Notas anteriores permanecem intactas.

| Critério | Nota | Fundamentação |
|---|---:|---|
| Geometria |9,35|Âncoras de localização, três trilhos, categorias em duas linhas, disponibilidade e CTA preservadas. Distribuição vertical proporcional mantém todos os controles; thumb idade ligeiramente mais à direita que a âncora visual original.|
| Tipografia/ícones/chips |9,00|Textos/valores/rótulos corretos, hierarquia e estados legíveis. Arial nativa mais fina e de desenho diferente do JPEG; status e lupa são vetores aproximados.|
| Cores/contraste |9,35|Papel quente, chips claros, trilhos e pretos coerentes. Cinzas dos valores escurecidos deliberadamente; não são reprodução exata do antialias original.|
| Responsividade/acabamento |9,30|Capturas sem cortes ou overflow nos três tamanhos, alinhamento e espaçamento consistentes; fonte baixa resolução limita conclusão subpixel.|

## Fluxo e semântica revisados

Default confere: São Paulo, SP/50km;18–35anos;1,70–1,95m;R$300–5.000; seis categorias, apenas Fashion ativa; três disponibilidades, Imediata ativa. Um thumb por faixa corresponde à fonte. Valores são texto nativo; categorias usam aria-pressed, disponibilidade radiogroup/radio. Limpar restaura todos os defaults em memória. Aplicar monta resumo por textContent e declara aplicação somente na demonstração. Reload não persiste dados; voltar é link real à07 aprovada, sem integração de backend.

Domínios visuais locais idade0–88/altura1,30–2,86/cachê0–670 estão documentados e correspondem ao DOM criado por app.js. Slider nativo anuncia intervalo integral por aria-valuetext e modifica limite inferior. O handler aplica clamp ao mínimo técnico e ao máximo selecionado; render expande max para incluir mínimo selecionado acima do domínio inicial. Dialog permite ambos extremos nos limites técnicos mais amplos (idade18–100, altura1–2,50, cachê0–100000/50), com validação nativa e erro mínimo>máximo. Não encontrei contradição que impeça editar ou aplicar os valores válidos.

O relatório do implementador registra Chromium156.0.8078.79/DPR1, zero pageerrors/requestfailed, dimensões iguais ao viewport, alvos≥44px e fluxos de edição dos seis extremos, cidade/distância, categorias/disponibilidade, resumo, erro mínimo>máximo, reset, teclado, reload, Escape/restauração de foco do resumo e navegação real07. **Revisei esses registros e o script; não executei segunda sessão de navegador nem recapturei imagens.**

## P2 e limites concretos

- Em390, thumb de idade centro≈103px versus âncora proporcional≈95,6px (fonte49/200); trilho nativo inclui a largura do thumb na distribuição. Diferença pequena, sem segundo thumb inventado ou valor falso.
- CSS de preenchimento usa `(a-c.min)/(r.max-c.min)`, embora r.min possa diminuir. Ao editar altura inferior1,00m, r.min=1 mas --fill≈−19,23%; thumb nativo mantém valor correto, porém o segmento preto deixa de representar esse domínio expandido. Corrigir futuramente usando r.min efetivo no numerador/denominador e revalidar screenshot do estado alterado. Não bloqueia dialog, resumo ou aplicação local.
- Os sliders têm domínio DOM maior que o intervalo selecionado; tentativas além do limite superior ou abaixo do mínimo técnico são reconduzidas pelo clamp, podendo produzir trecho sem avanço ao teclado. É decisão local documentada; edição completa permanece disponível no dialog. Melhoria futura deve preservar aparência inicial e semântica honesta.
- Arial e ícones aproximados diferem em espessura/desenho da fonte JPEG. No default390, campos/categorias/CTA conservam composição, mas não há prova de fonte original exata.
- Evidência automatizada não demonstra tudo que a redação resumida do relatório sugere: zero pageerrors/requestfailed não equivale a console.error/http-status/checagem naturalWidth de cada asset; inspeção visual mostra ícones presentes nos defaults. O script verifica tamanhos de alvos, não ausência de sobreposição; não exercita Tab/foco contido, Escape do seletor, reset de cada campo por assert ou todos os limites extremos técnicos. Esses itens são limites da evidência revisada, não testes independentes aprovados. Dialogs nativos e CSS de foco existem; não atribuir cobertura não executada.
- Adaptação aprovada somente nos três viewports fornecidos. Backend, resultados de casting, busca remota e persistência não integrados; esse limite está comunicado honestamente no fluxo.

## Hashes do pacote examinado

- `VERSION`: `36db35c23849bf438a82d522c1202c664362e6157dc9e9276dbec672b6c06e8a`
- `README.md`: `585d08a96b8176365ac26ca95cdd647a3c9474a51547f65965728fb39bd95dc5`
- `CHANGELOG.md`: `172525a891610ddaccb97517d333bb76c1538aa4507a28c032ea1787aa3ef982`
- `index.html`: `3fe6c198f49695d7b1c0d910053c91988550fd0d6c2c25300a1c92345bf28ea9`
- `styles.css`: `d231f1573ecdfea85ee05048f489b651ebfee64b8eaeb0ab009e5efc0bb822e2`
- `app.js`: `eda0f86c6e2992262e745ae920b0709ed829625b0206a51569cfcacf920a8fe7`
- `relatorio-browser.json`: `0ad7c7613425b93c879f75c48935beb5f5d5f25b8e4e58d21ac3497b839c2451`
- `comparacao-390.png`: `169848c27f0b47ae1e953c025950b9db869e19107e3b2174a39ecaec0d016f76`
- `screenshots/captura-375.png`: `95e677c5445bb664340b377bd0af1c8b8c8a4678298512bea5166ffd2db10cf4`
- `screenshots/captura-430.png`: `3da7e8d70040b6872550b076511067dbfca99cc7c35e506c308539654673fe7e`
- `screenshots/captura-390.png`: `1c742fde2ac431e1c1ee07df3fed6fd823ff95f0f90a1f10617bea97f63ed3b2`

Código, assets, capturas e pacotes03–07 não foram alterados nesta auditoria; somente este documento e a fila foram atualizados. Sem publicação ou início09 pelo auditor.
