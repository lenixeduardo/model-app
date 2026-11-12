## Integração de estado local (state1)

- Conecta os dados desta tela ao estado de demonstração persistido no dispositivo.

# Integração de navegação

- Conexões e retornos demonstrativos; estado compartilhado e backend permanecem pendentes. Versão 2.0.0-prototipo.7.integracao.1.

# Tela 03 V2 — 2026-11-09

## Implementação
- Criada nova V2 a partir do mockup e contrato, pois o código anterior nunca foi recebido.
- Separados HTML, CSS, JavaScript e assets SVG/PNG; sem fontes, bibliotecas ou recursos externos em runtime.
- Enzo preservado em imagem proporcional; removida a possibilidade de esticar o retrato em duas dimensões. Retrato parcial com máscara inferior, sem corpo gerado.
- Criados status, cinco segmentos, voltar/opções, selo, nome/localização, chips, três botões e indicador inferior.
- Clique/toque em favoritar/curtir alterna estado local acessível; ignorar permite desfazer sem inventar outro modelo. Navegação externa/back-end não integrados.
- Labels acessíveis, alvos >=44px, foco visível, diálogos nativos com Escape e retorno de foco, redução de movimento e fallback de falha de foto.
- Safe areas consideradas; status e gesto simulados ocultáveis via data-native-status="true" na integração nativa.

## Ciclos e evidências
1. Teste antes da implementação: falhou na ausência do título esperado, porque não havia index.html; o servidor retornava listagem de diretório.
2. V2 inicial: três capturas e testes verdes. Referência comparada com screenshot390: céu com emenda e informações um pouco baixas. Cópia da captura inicial em evidencias/ciclo-01-390.png.
3. Correção: céu extraído do mesmo mockup sem interface, transição suavizada, texto elevado em1,5% da altura e fundos dos controles superiores removidos.
4. Nova captura de todos os tamanhos; sem erros de console/rede, distorção geométrica do retrato ou overflow nos tamanhos exigidos. Hashes e resultados em relatorio-browser.json.

## Limite material
O retrato limpo tem201×242px. Ausência da parte inferior força dissolução para preto antes da referência. Esta implementação não pode ser considerada recuperação da fotografia integral. Auditoria visual separada define a nota e o estado do aceite; testes técnicos verdes não equivalem a aprovação visual.

5. Ciclo3: banding na faixa estreita de céu removido substituindo a ampliação por preenchimento CSS com as cores amostradas do retrato. Sem alteração do retrato. Recapturados todos os tamanhos.

## Ciclo4 — fila sequencial de agentes
- Conectada somente à ação ignorar a variante independente fechar-acao.svg em40×40px; diagonal ocupa aproximadamente26,7px em vez dos17px anteriores. O X dos diálogos permanece inalterado.
- Selo ampliado para aproximadamente25px na viewport390, preservando proporção e alinhamento.
- Chips com preenchimento vertical de8px, altura de aproximadamente32px na viewport390; textos/ordem/geometria dos botões preservados.
- Três capturas do ciclo3 preservadas em evidencias/ciclo-03-{375,390,430}.png antes da nova captura. Retrato, enquadramento e céu não alterados.
- Refinamentos de UI não resolvem fotografia parcial e não constituem aprovação. Auditor independente deve reavaliar as novas imagens sob gate>9,0.

## Ciclo5 — pixels do torso preservados, lacunas de interface transparentes
- Integrada a extração203×404 `enzo-mockup-foto-com-lacunas-precisas2.png`, com70.768pixels RGB visíveis idênticos à fonte; UI removida por alpha, RGB oculto sanitizado. Não é fotografia integral limpa, nem screenshot intacto, nem reconstrução generativa.
- `object-fit:cover`, quadro100%×100%, posição horizontal8%: escala uniforme pela altura, com corte lateral. Removidas máscara que apagava o torso e sobreposição escura duplicada; o gradiente original já faz parte dos pixels conhecidos.
- DOM de nome/localização/chips/selo/informação calibrado pela unidadealtura/404; ações mantidas centradas na viewport para equilíbrio, sem deslocar o conjunto para esconder os buracos da foto.
- Nome/selo/localização e todos os controles seguem elementos independentes. Lacunas negras continuam visíveis sob parte do texto e status; não foram preenchidas com pele/céu sintéticos.
- Teste de proporção corrigido para validar `object-fit:cover`, escala uniforme, dimensões naturais, recorte e ausência de transform no retrato em vez de exigir razão da caixa igual à foto. Rota de falha de imagem aponta para a nova extração.
- Três capturas do ciclo4 preservadas em `evidencias/ciclo-04-{375,390,430}.png`; primeira tentativa do ciclo5 em `evidencias/ciclo-05-inicial-390.png`.
- Três capturas finais e comparação regeneradas; render.py passou em todos os tamanhos, inclusive interações/foco/movimento reduzido/foto quebrada. node --check e py_compile passaram. Auditoria independente pendente; nenhuma nota atribuída pelo implementador e Tela04 não iniciada.

## Ciclo6 — candidato nativo escolhido após teste vetorial
- Header substituído somente por céu CSS até29px-fonte, com transição até34px-fonte, antes do cabelo. Fade inferior332,9..343,8px-fonte removeu discos deslocados sem apagar torso atrás de nome/localização/chips. Base preta.
- Ações42u centradas na viewport, ícones internos calibrados; gesto34%/10,5pxda base; informação deslocada4px para dentro.
- Candidatos tipográficosSVGbinary/AAcapturados em390 e rejeitados por regressão pixelada. Texto nativoArial mantido, com sombra uniforme sutil.
- Três capturas finais6 geradas e testespassed; auditor independente atribuiu8,92, abaixo do gate>9,0. Visual6 congelado e preservado antes do ciclo7.

## Ciclo7 — glifos raster independentes com fallback nativo
- Integradas somente as camadasforegroundPNGporcontornos `assets/ui/name-reference.png` (66×21, origem11,272) e `location-reference.png` (108×16, origem11,292), projetadas pelo mesmou/offset da fotografia. Não são retângulos fotográficos com texto embutido: alpha ocupa39,75%/35,07%, com RGB transparente zero.
- Os glifos preservam os pixels já compostos da referência, incluindo a franja contextual deantialias1px que a máscara da foto havia removido. Essa técnica é uma limitação raster estática documentada, não descoberta da fonte original, recuperação de pele ou nova imagem de pessoa. Fonte/prova em `assets/ui/reference-type-manifest.json`. A fotografia de runtime permanece sem UI e os ícones seguemSVGindependentes.
- H1/Pnative permanecem fonte da verdade acessível. As duas imagens decorativas só se tornam visíveis juntas quando ambas carregaram e os textos exatos correspondem aEnzo,26/localização da referência. Qualquer erro deimagem, alteração de texto ou `data-native-text="true"` mantém/restaura os dois textos nativos, sem camada visual duplicada. Não reutilizar rasterpara nomes/locales arbitrários.
- Informação retorna a `right:0` para co-registro dohole, comSVG16u, sem reduzir alvo44px; badge14u preservado. Header/footer/ações do ciclo6 não alterados.
- Primeiro candidato390 capturado e aberto antes das três finais. Capturas6 preservadas em `evidencias/ciclo-06-{375,390,430}.png`.
- TesteREDantes da integração falhou corretamente na ausência do label independente. Suíte final passou:3viewports, interações antigas, fallback ao abortar cadaPNGindividualmente, opt-out, mismatch dos textos, foto indisponível e movimento reduzido. nodecheck/pycompile passaram. Novas capturas/comparação finais com hashes conferidos; aguardando auditor independente, sem nota atribuída pelo implementador.
