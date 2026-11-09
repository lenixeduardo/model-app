# Auditoria independente — Tela 03 V2, ciclo 4

Data: 2026-11-09. Versão avaliada: **2.0.0-prototipo.4**. Estado: **NÃO APROVADA VISUALMENTE**. Estimativa ponderada: **7,84/10**. Gate atual do usuário: nota **superior a 9,0/10**; meta: 9,5/10. Nota exatamente 9,0 não libera a próxima tela. A implementação e os testes técnicos não constituem aprovação visual.

## Evidências inspecionadas

O auditor abriu novamente a referência `../MODEL_assets_v1/referencias/referencia-tela-03.png` (203×404 px), as três capturas reais finais desta pasta — `captura-375.png` (375×812), `captura-390.png` (390×844) e `captura-430.png` (430×932) — e `comparacao-390.png`, com alturas normalizadas sem deformar as proporções. Foram lidos `ASSETS.md`, `PLANO_REVISAO.md`, `../docs/FILA_AGENTES.md` e o relatório de navegador atualizado. A análise do ciclo anterior não foi reutilizada como comprovação da versão atual.

Renderização documentada: Chromium 156.0.8078.79, Playwright, servidor HTTP local, DPR1, contexto mobile com toque. O relatório atual termina em `result: passed`; dimensão do documento igual à viewport nos três tamanhos; erros de console/rede vazios. O auditor inspecionou as capturas e os registros do implementador, sem alegar uma segunda execução independente do navegador.

Hashes SHA-256 dos arquivos efetivamente avaliados, conferidos contra `relatorio-browser.json`:

| Captura | SHA-256 |
|---|---|
| 375×812 | `50b1d1f954128d866c3bbd73573378ed5118c7ccd43fef729c28354abb410694` |
| 390×844 | `981ef3f0a3168ecb2543d81d5aac73c804ba4bd3396db3d2391c39244e27971a` |
| 430×932 | `11953911334780b2edbecdbee0eed3cc5ca502e38c59ec1a1e2cbdc068082e46` |

## Rubrica final do ciclo 4

| Critério | Peso | Nota | Parcela | Diferenças e evidências visíveis |
|---|---:|---:|---:|---|
| Fotografia, identidade e enquadramento | 35% | 6,2 | 2,17 | É Enzo, com céu azul e rosto/ombros de proporção natural. O retrato limpo de 201×242 continua terminando perto de 62% da altura da captura e é dissolvido em preto antes do nome. Na referência, o torso permanece visível atrás de nome, localização e chips. A grande área preta substitui parte importante da composição fotográfica. A baixa resolução é visível em cabelo/rosto ampliados. O ciclo 4 não alterou essa limitação. |
| Geometria e posicionamento | 25% | 8,6 | 2,15 | Margens, nome, categorias, três círculos e gesto inferior conservam a hierarquia. Os círculos permanecem alinhados nos três tamanhos. A relação do nome e dos chips com o retrato continua diferente porque a foto acaba cedo. Os controles superiores são mais evidentes que no pequeno painel oficial. A proporção da referência difere das viewports exigidas; a comparação preserva ambas, sem estirar a imagem para coincidir largura e altura. |
| Tipografia, ícones e chips | 20% | 8,9 | 1,78 | O X maior agora ocupa melhor o círculo e se aproxima da referência; o selo ampliado mantém melhor relação com o nome; os chips ganharam altura e acabamento, sem perda de alinhamento nos três tamanhos. Textos e ordem das categorias permanecem corretos, ícones vetoriais sem glifos substitutos. Ainda há diferenças de desenho/espessura dos símbolos e tipografia: Arial é aproximação, sem fonte original comprovada. Os vetores são reconstruções, não exports originais. |
| Cores, contraste e sobreposição | 10% | 8,2 | 0,82 | Branco, preto, céu azul e vermelho são coerentes e legíveis. O céu superior é mais liso/uniforme que a referência, mas sem as estrias do ciclo 2. A sobreposição apaga mais informação fotográfica que no mockup e a faixa inferior preta permanece dominante. |
| Responsividade e acabamento | 10% | 9,2 | 0,92 | Três capturas finais com dimensões corretas, sem rolagem indevida ou controles cortados. O relatório registra alvos >=44px e foco sólido. Safe areas em iPhone físico, VoiceOver e continuidade com a implementação da Tela02 não foram certificadas. |
| **Total** | **100%** | | **7,84** | **Abaixo do gate >9,0.** |

A pontuação é estimativa visual fundamentada, não métrica automatizada pixel-perfect. O ganho em relação a 7,74 no ciclo3 decorre dos refinamentos visíveis em ícones/selo/chips. O critério fotográfico continua em 6,2 porque o asset é idêntico e o torso necessário continua ausente.

## Qualidade técnica verificada nos registros e imagens

- Documento igual à viewport: 375×812, 390×844 e 430×932; nenhum overflow documentado.
- Retrato natural 201×242; proporção mantida nas renderizações, sem estiramento anatômico observado.
- Nenhuma fotografia ou SVG quebrado nas capturas finais. Nenhum erro de console/rede nos fluxos normais registrados.
- Favoritar e curtir alternam `aria-pressed`; ignorar e desfazer retiram/restauram o perfil; painéis locais, Escape e foco visível foram testados.
- Movimento reduzido e fallback de fotografia indisponível passaram segundo o relatório. O fallback desativa as ações; é teste proposital separado do fluxo normal sem erros.
- A variante `fechar-acao.svg` pertence à ação ignorar; o X de fechar diálogo não foi substituído indiscriminadamente.
- Não foi identificada falha técnica material no escopo revisado. São interações em memória, sem backend, autenticação, persistência ou contratação integrada.
- CSS com safe areas e captura mobile Chromium não substituem ensaio em aparelho físico ou tecnologia assistiva.

## Bloqueio concreto e condição de retomada

`ASSETS.md` documenta que os anexos e recortes locais foram inventariados e que não existe fotografia independente limpa com o mesmo retrato completo. O recorte integral da tela contém UI incorporada e não serve como fundo independente. Login, painel editorial e outras poses não substituem o retrato oficial.

É necessário obter a **foto limpa do mesmo retrato de Enzo**, com céu/cabeça/ombros/torso presentes na composição, sem textos/controles ou gradiente incorporado; preferível largura>=860px para DPR2. Recebido o arquivo, o agente de assets deve verificar origem, identidade, pose e extensão antes da integração. Depois: recalibrar enquadramento/sobreposição, executar novas capturas dos três tamanhos, comparar e reauditar.

Não há fundamento para novos ciclos cosméticos com objetivo de alcançar >9 enquanto esse insumo faltar. Mantida a nota de fotografia6,2, mesmo todos os outros critérios hipoteticamente em10 resultariam em8,67; isso é demonstração do peso do bloqueio, não nova nota. Ajustes de X/selo/chips tiveram melhora verificável e agora atingem um ponto de retorno pequeno. Continuar trocando espaçamentos ou ícones não recuperará o torso. Não fabricar corpo, não gerar outra pessoa e não usar a captura inteira como fundo para aparentar fidelidade.

## Decisão final da fila

**Auditor03 concluído: V2 funcional e capturada, fidelidade visual não aprovada, nota7,84/10. Fila pausada na Tela03 por bloqueio fotográfico documentado.** A Tela04 não está liberada para planejamento de conteúdo nem implementação. Só nova auditoria com nota **>9,0**, evidências completas e ausência de bloqueador material poderá liberar o avanço. Publicação desta V2, se realizada pelo agente principal, deve preservar explicitamente o estado de não aprovação; o auditor não publicou arquivos nem alterou implementação ou capturas.
