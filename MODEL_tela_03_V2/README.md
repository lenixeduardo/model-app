# MODEL — Tela 03 V2

Protótipo funcional de Swipe / Descobrir com assets independentes. Implementação nova com base no mockup, sem o código V2 anterior.

## Abrir

Da raiz do repositório:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Acessar http://127.0.0.1:8765/MODEL_tela_03_V2/.

Ou abrir index.html diretamente; todos os assets são relativos e não há dependências externas.

## Reproduzir a validação

Python3, Playwright para Python, Pillow e Chromium são as dependências de desenvolvimento. No ambiente desta entrega já estavam instaladas. Runtime da página usa somente navegador.

```sh
python MODEL_tela_03_V2/render.py --chromium /usr/bin/chromium
python MODEL_tela_03_V2/compare.py
```

O renderizador inicia servidor HTTP local em porta livre, captura os três viewports em DPR1 e testa cliques/toques, toggles, desfazer, diálogo, teclado, imagem quebrada, redução de movimento, alvos de toque e overflow. Não altera o CSS para as capturas. O arquivo relatorio-browser.json registra versão do Chromium, dimensões, fontes efetivas, imagens, erros e hashes. Fonte local Arial/Helvetica/sans-serif; não foi fornecido arquivo da fonte original.

## Integração

Reutilizar index.html, styles.css, app.js e assets/. As escolhas ficam somente em memória; recarregar reinicia os estados. Nenhuma API é chamada. Back e opções abrem painéis locais; não há navegação para a Tela04. Em um contêiner nativo que já apresenta status/gesto, aplicar data-native-status="true" no elemento .screen.

## Evidências e limites

- captura-375.png, captura-390.png, captura-430.png: screenshots reais do Chromium.
- comparacao-390.png: mesma altura entre referência e captura, sem alterar suas proporções. As larguras diferem porque o painel do mockup tem razão203/404.
- AUDITORIA.md: nota visual e decisão de aceite.
- DESIGN_SPEC.md e CHANGELOG.md: critérios e alterações.
- evidencias/: primeiro ciclo e erro reproduzível do sandbox.

Fotografia disponível é parcial201×242px e não deve ser confundida com a foto original integral. Não usar a referência completa como fundo: ela já contém textos e botões. A aprovação visual permanece sujeita à rubrica, independentemente dos testes técnicos.

## Fila e última revisão

Versão2.0.0-prototipo.4. Os quatro papéis executaram o ciclo: planejamento → assets → implementação → auditoria independente. Nota final7,84/10, não aprovada. O gate atual exige nota superior a9,0. Ver ../docs/FILA_AGENTES.md.

As capturas históricas ciclo03 estão preservadas somente no pacote local desta entrega; o repositório contém as capturas finais e os históricos ciclo01/02 explicitamente autorizados.

O recorte histórico assets/enzo-ceu-topo.png também fica somente no pacote local. O runtime final usa preenchimento CSS para o céu; esse PNG não é dependência da página. O retrato enzo-swipe-referencia.png é cópia exata do asset já público MODEL_assets_v1/assets/enzo-retrato-parcial.png (mesmo blob Git).
