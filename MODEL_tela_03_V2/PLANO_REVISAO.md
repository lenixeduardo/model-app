# Tela 03 V2 — plano de revisão pela fila de agentes

Data: 2026-11-09. Papel: planejamento. Estado atual: implementação funcional e capturada, nota independente **7,74/10**, não aprovada. Critério atualizado do usuário: nota **superior a 9,0/10**; meta 9,5. Não iniciar conteúdo ou implementação da Tela 04 antes desse aceite.

## Diagnóstico com evidência visual

Foram lidos `DESIGN_SPEC.md`, `AUDITORIA.md`, `README.md` e `../docs/CODEX_TELA_03.md`. Foram abertas a referência oficial isolada (203×404) e a captura real de 390×844. Na referência, Enzo ocupa quase todo o fundo e seu torso permanece visível atrás de nome, localização e categorias. Na V2, o retrato limpo termina aproximadamente em 62% da altura, é dissolvido em preto e deixa o nome sobre uma área preta extensa. O rosto e os ombros conservam a proporção natural; isso não supre a área ausente.

A foto em runtime é `assets/enzo-swipe-referencia.png`, 201×242, originada do recorte limpo do mockup. A referência completa tem interface incorporada. O céu final é preenchimento CSS amostrado do retrato, não fotografia integral recuperada. Os testes técnicos passaram, mas esses resultados não resolvem a diferença de composição.

## 1. Entrega seguinte — agente de assets

Executar nesta ordem, sem alterar o código da tela:

1. Inventariar os arquivos fotográficos realmente disponíveis em `../MODEL_assets_v1/originais/`, `../MODEL_assets_v1/referencias/` e `assets/`; registrar caminho, dimensões, origem e o que contém interface incorporada. Abrir os arquivos relevantes, sem presumir que o anexo completo é o original limpo da fotografia.
2. Conferir se alguma fonte já fornecida contém **o mesmo retrato completo**, com o torso que a referência mostra. Recortes de outra pose, ainda que de Enzo, não atendem esse requisito. A foto de login não é substituta.
3. Se houver pixels suficientes em uma fonte limpa, exportar o asset preservando a proporção, documentar coordenadas e fornecer prévia. Não remover textos por geração/inpainting nem completar corpo oculto: isso fabricaria informação ausente, em conflito com o contrato atual.
4. Se não houver fonte suficiente, criar `ASSETS.md` registrando o bloqueio e a especificação do insumo faltante: foto original limpa do mesmo enquadramento, céu/ombros/torso completos, sem interface, idealmente resolução superior aos 430px da viewport (preferível >=860px de largura para DPR2). Resolução maior é desejável, não substitui o enquadramento correto.
5. Revisar os SVGs do X, selo e demais ações contra a referência. Entregar ajustes vetoriais permitidos como arquivos separados, com dimensões/espessuras propostas e indicação de que são aproximações. Não alegar vetor original.
6. Produzir `ASSETS.md` com três classes: original/extração fiel; aproximação vetorial/CSS identificada; insumo ausente. Entregar o inventário e a decisão sobre a fotografia ao implementador e ao auditor.

Se o torso não estiver disponível, essa etapa termina em **bloqueio fotográfico documentado**. Não criar uma fotografia alternativa para manter a fila andando.

## 2. Refinamentos de UI que podem ser implementados

Esses ajustes são independentes da obtenção do original e podem melhorar a V2, mas não asseguram nota >9:

- Comparar traço e escala interna do X/estrela/coração com a referência, preservando os alvos de toque >=44px e a geometria dos círculos.
- Calibrar o selo em relação ao nome; a auditoria observa selo um pouco pequeno.
- Calibrar altura, preenchimento, espaçamento e borda dos chips; a auditoria observa chips mais finos/compactos.
- Reavaliar a evidência dos controles superiores em relação ao painel oficial, preservando a presença de voltar/opções exigida no contrato.
- Manter textos, hierarquia, cinco segmentos e comportamento local; não adicionar novos modelos, rótulos ou navegação para a Tela 04.
- A fonte permanece aproximação até receber o arquivo ou identificação verificável da família original. Não alegar correspondência exata apenas por semelhança.

O implementador registra as mudanças em `CHANGELOG.md`. Se optar por entregar somente refinamentos com a foto parcial, preservar a versão anterior e marcar a nova como **não aprovada / limitação fotográfica mantida**.

## 3. Integração quando existir fotografia suficiente

1. Validar origem, identidade e proporção com o agente de assets.
2. Substituir somente o asset correspondente; usar `object-fit: cover`/`object-position` ou enquadramento proporcional equivalente, sem definir largura/altura independentes que deformem Enzo.
3. Recalibrar a escala/posição do rosto, cabeça, ombros e torso em cada viewport. Mostrar a fotografia por trás das informações como na referência; não usar preto para esconder uma área que o novo original contém.
4. Recalibrar a sobreposição escura para legibilidade sem apagar o torso; verificar o conjunto antes de mexer em tipografia/ícones.
5. Aplicar os refinamentos de UI e executar a verificação abaixo.

## 4. Verificação e auditoria da nova versão

Executar:

```sh
python MODEL_tela_03_V2/render.py --chromium /usr/bin/chromium
python MODEL_tela_03_V2/compare.py
```

Se o sandbox bloquear sockets/Chromium, registrar o erro e usar apenas a estratégia permitida pelo ambiente. Não substituir captura por montagem do mockup.

Entregar os três PNGs finais (375×812, 390×844, 430×932), `relatorio-browser.json`, comparação de390 com proporções preservadas, changelog e versão. Conferir imagens/SVGs, console/rede, overflow, estados de curtir/favoritar, ignorar/desfazer, teclado/foco, áreas de toque, redução de movimento e fallback de foto. Testes de Chromium não certificam VoiceOver ou safe areas reais de aparelho físico; documentar a limitação.

O auditor independente deve abrir referência e capturas finais e atribuir as cinco notas com pesos35/25/20/10/10. A nota atual não se transfere à nova versão. Nenhum bloqueador material, captura ausente ou deformação pode ser compensado pela média. Só nota **>9,0** e evidência completa libera a Tela04. Nota9,0 exata continua abaixo do gate atualizado.

## 5. Limite e condição de parada

A nota de fotografia atual é6,2/10, peso35%. Mesmo com todos os demais critérios hipoteticamente em10, a média seria8,67. Esse cálculo é apenas uma demonstração do peso do bloqueio; não é uma previsão de nova nota. A auditoria deve avaliar cada nova versão pelas imagens.

Enquanto faltar a fotografia suficiente, não existe fundamento para prometer >9 somente com CSS/ícones. O resultado correto é entregar o que foi implementado, registrar o bloqueio e manter a fila pausada na Tela03. Retomar após receber/verificar o insumo, ou após nova instrução explícita do usuário que altere o contrato de fidelidade.

## Checklist de handoff para assets

- [ ] Inventário com dimensões e origem de cada candidato fotográfico.
- [ ] Confirmação visual de identidade/pose do retrato oficial.
- [ ] Fonte limpa integral encontrada, ou declaração demonstrada de ausência.
- [ ] Asset fiel exportado com coordenadas, se possível; nenhuma fotografia fabricada.
- [ ] Propostas de ajustes dos SVGs independentes e identificadas como aproximações.
- [ ] `ASSETS.md` entregue e estado da fotografia comunicado ao implementador/auditor.

O arquivo `../docs/FILA_AGENTES.md` mantém a ordem das telas e os gates. O conteúdo da Tela04 permanece fora deste plano.
