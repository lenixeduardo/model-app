# Tela04 V1 — APROVADA VISUALMENTE: 9,30/10

Auditoria independente em 2026-11-09. Versão avaliada: `1.0.0-prototipo.1`. Soma ponderada **9,295/10**; gate **>9,0 atingido**, meta9,5 ainda não atingida. **Nenhum P1 material identificado nas capturas avaliadas.** Tela05 liberada para planejamento pelo coordenador; não foi iniciada nesta auditoria. Aprovação03 preservada.

## Evidências e método

Abri com `view_image` a referência04 original192×404, as capturas375×812,390×844 e430×932 e `comparacao-390.png`. A nota resulta da inspeção dessas imagens, acompanhada da leitura de DESIGN_SPEC, ASSETS, PLANO, manifesto, relatórioJSON e código de renderização/interação. Não executei navegador independente: testes de interação/console/rede são evidência do implementador, confrontada com o script, e não uma alegação de reteste meu.

Conferi independentemente dimensões e SHA-256 abaixo. As capturas finais têm exatamente os viewports exigidos, não192×404. `render.py` usa Chromium real via Playwright, DPR1, servidor local e `page.screenshot` antes de interagir; não captura o arquivo de referência. `compare.py` normaliza somente para a comparação, mantendo proporções. Verifiquei por igualdade de bytes dos pixels que a metade direita da comparação, caixa[417,30,807,874), é a captura390 inteira. As diferenças de fonte/ícones entre screenshot e referência também confirmam que não se trata de um recorte do mockup. O JSON não incorpora hashes nem versão do executável Chromium: os hashes desta auditoria vinculam os artefatos inspecionados, mas não são uma assinatura de execução do navegador.

Também verifiquei hashes de todas as cinco fotos contra o manifesto e igualdade RGB de todos os pixels preservados com seus crops na fonte original. Nenhum pixel fotográfico novo foi necessário. Código/assets/capturas não foram alterados por este auditor.

| Critério | Peso | Nota | Parcela |
|---|---:|---:|---:|
| Fotografia, identidade e enquadramento |35%|9,5|3,325|
| Geometria e hierarquia |25%|9,4|2,350|
| Tipografia, ícones e chips |20%|8,9|1,780|
| Cores, contraste e sobreposição |10%|9,1|0,910|
| Responsividade e acabamento |10%|9,3|0,930|
| **Total** |100%|**9,295**|**9,295**|

## Resultado visual e conteúdo

O retrato principal é o B&W correto da04, com a mesma identidade/pose; cabeça, olhos, ombro e fundo seguem a referência. `cover` absorve a diferença pequena de razão de viewport com crop proporcional; não há estiramento anatômico observado. Três thumbs completas e quarta parcial permanecem no enquadramento e não se transformam em oito fotos. A baixa resolução é a da fonte fornecida. Status, voltar e opções têm leves fundos/halos uniformes decorrentes de alpha sobre fundo escuro, mas não há UI duplicada legível ou buraco material atravessando rosto. A pill nativa recobre a máscara1/8 nos três tamanhos.

Na captura390, fim do hero≈y326, fim da galeria≈430, nome≈453, chips≈519, números≈587, título da bio≈668 e ações≈780–829. Relações foto/galeria/conteúdo e margens estão muito próximas da composição planejada. Em375 e430 a composição conserva o mesmo equilíbrio e as ações permanecem inteiras. Não há painel integral de referência usado como fundo: nome/local/chips/dados/bio são DOM sobre fundo claro.

Conteúdo correto: Enzo,26; São Paulo,SP; Fashion/Editorial/Comercial/Fitness; 1,84m/78kg/42; bio com **editoriais** no plural e CTA Solicitar contato. Arial/Helvetica é aproximação declarada, não identificação da fonte original. A fonte e alguns pesos/contrastes diferem da referência, sobretudo no nome, labels e bio; isso reduz a nota tipográfica.

## P2 concretos — não bloqueadores

- **Implementador04, contador390 x≈326–378,y≈271–314:** pill visualmente maior/mais clara que a referência normalizada (aproximadamente44×34 versus52×43 atuais). Mantém conteúdo1/8 e cobre a máscara, portanto não é falta de informação; refinamento exige preservar cobertura do alpha.
- **Implementador04, status/cabeçalho390 y≈12–85 e selo x≈145–163,y≈454–473:** sinal/bateria maiores e selo mais pontudo/claro que a fonte. Controle superior direito é aproximação de símbolo incerto; não se afirma ícone original.
- **Implementador04, conteúdo390 x≈24–366,y≈450–751:** família/antialiasing, pesos e distribuição dos chips diferem levemente; bio usa quebras distintas da referência. Compartilhar/salvar/avião na faixa y≈780–829 têm traço e forma próprios, sobretudo compartilhar. Ajustes são opcionais e não autorizam rasterizar labels.
- **Implementador04, fundo e miniaturas:** fundo uniforme e recortes suaves preservam composição, mas o bege/contraste e contornos claros das thumbs não reproduzem exatamente a fonte comprimida. Sem recorte fotográfico incorreto material.

## Evidência técnica e limites

O relatório registra nos três tamanhos: documento igual ao viewport, todas as11imagens carregadas, `errors:[]`, `networkErrors:[]`, alvos>=44px e sucesso de salvar, quatro recortes, quatro diálogos, Escape, retorno de foco e link real03. O script contém essas asserções; o link aponta `../MODEL_tela_03_V2/`. Os diálogos e salvar são locais, sem backend/envio real ou oito arquivos inventados. O JSON não testa Enter explicitamente, zoom/texto ampliado, VoiceOver, aparelho físico ou bloqueio de imagem. A regra de altura reduzida permite scroll por revisão de CSS; isso não constitui teste independente desses cenários. `viewport-fit=cover` está declarado, mas não há inset `env(safe-area-inset-*)`: safe area física requer validação posterior. Nenhuma dessas limitações invalida os três viewports atuais.

## SHA-256 das evidências avaliadas

- Referência04: `5df981d7a9b77331c263fd15502208d6fa82ab9838ee42c0c5fe7342d917c18b`
- Captura375: `5caa8cc19f9b60489407056faba862c88b705d20d8fe6d5966e31cd98e3f75aa`
- Captura390: `51b44781ebb87fde8be24abdca34b8e6ef1ac00b812e26e617b5df7eb9fb9931`
- Captura430: `69058529d18140344cb688fdaefba92d1c9a58993711d162b6ec9579129239ac`
- Comparação390: `b143b230ac873a8a80a6fc009c80840462588595fb52c906a94c5d3da0288b5d`
- RelatórioJSON: `bb34bf59d9d2f6b3765d89b6cbe9b42ecfe6e1ea16b0846d0fa94e1331583c90`

Decisão limitada a esta versão/capturas e ao perfil estático fornecido. Uma mudança visual exige novas evidências; a nota não é transferida à05 nem ao produto em dispositivos não avaliados. Não houve publicação.
