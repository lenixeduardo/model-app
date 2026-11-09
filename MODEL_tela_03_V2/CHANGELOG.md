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
