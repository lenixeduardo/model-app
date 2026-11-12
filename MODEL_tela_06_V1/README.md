**Integração em andamento:** o runtime desta pasta foi alterado após a auditoria visual histórica. `AUDITORIA.md`, capturas antigas e seus manifests descrevem a versão pré-integração, recuperável no commit `b49b77d`; não certificam os arquivos atuais. Novas evidências e aceite final permanecem pendentes. Ver [estado da integração](../docs/correcoes-123/AVALIACAO_ATUAL.md).

# MODEL tela06 — protótipo local

Versão1.0.0-prototipo.1. **Aprovada visualmente em9,28/10**, auditoria independente semP1 material; gate>9,0 atingido. HTML/CSS/JavaScript nativos, sem dependências de runtime. Servir **a raiz model-app**, por exemplo `python -m http.server 8000`, e abrir `/MODEL_tela_06_V1/`. O link voltar aponta para05 aprovada.

Texto inicial e status reproduzem o mockup; não indicam presença real. Enviar por Enter/botão acrescenta texto somente em memória, sem backend, recibos, resposta automática ou persistência. Recarregar remove mensagens novas. Telefone, opções, detalhes, foto e clipe abrem dialogs locais; não iniciam chamadas, uploads ou envio externo.

## Verificação reproduzível

`python MODEL_tela_06_V1/render.py` usa Playwright Python/Chromium em `/usr/bin/chromium`, serve a raiz do repositório e captura375×812,390×844,430×932 DPR1 antes de qualquer interação. `python MODEL_tela_06_V1/compare.py` gera comparação de altura844 preservando proporções. A candidata390 foi inspecionada antes das finais. `relatorio-browser.json` contém versão do navegador, dimensões, alvos, geometria/fit das fotos, hashes e resultados funcionais. O fallback com quatro fotos bloqueadas e reduced-motion é um contexto separado.

TDD red observado: render.py recusou HTML inexistente com AssertionError explícito. Teste de alvo mínimo detectou input de17px; corrigido para44px e suíte verde. Estado inicial sem overflow; mensagens adicionadas podem rolar internamente. HTML literal permanece texto; nenhuma hora/recibo fictício é criado para mensagens novas.

## Decisões e limites

Fotos têm somente22×22,18×19 e134×44 de origem; não existe detalhe maior comprovado. Avatares pequenos separados, `contain`, razão18/19; escritório `cover` em razão134/44 sem corte adicional. O escritório ocupa110px em390, em vez de≈92px por escala vertical da fonte: o conteúdo interno do card foi compactado para respeitar a proporção original. A comparação conserva a largura proporcional da referência, enquanto a interface adapta horizontal e verticalmente aos viewports pedidos.

Dialogs concentram as explicações de protótipo para preservar o conteúdo inicial. Erro de foto remove o glifo quebrado e mantém a geometria e o texto acessível. Pacotes03–05 preservados. Auditoria06 concluída em9,28/10; planejamento07 liberado. Consulte AUDITORIA.md para rubrica, hashes, limites eP2.

## Nomes de entrega

Os raw originais permanecem em screenshots/. Para os nomes captura-375.png/captura-390.png/captura-430.png, executar `python MODEL_tela_06_V1/exportar_capturas.py` após render.py. O exportador copia os mesmos bytes, sem editar imagens; EVIDENCIAS.json registra os pares e SHA-256. A comparação usa os raw originais.


## Integração

Navegação integrada à demonstração local. Dados e ações permanecem locais; não há backend.
