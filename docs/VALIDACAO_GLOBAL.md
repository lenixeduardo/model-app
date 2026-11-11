# Validação global do MODEL

Data: 11/11/2026. Base examinada: commit `849c24ac2d706f305a8578d0b70b6759f6756663`. Auditoria nova, com navegador e revisão independente de integração. Nenhum runtime, asset ou captura aprovada foi modificado.

**Parecer: o conjunto funciona como nove protótipos isolados; ainda não está aprovado como aplicativo integrado.** As notas visuais individuais acima de9 não comprovam navegação completa, estados compartilhados, acessibilidade AA ou backend. Não foi atribuída nota global nem recalculada uma média visual para disfarçar essas lacunas.

## Evidência nova e resultados

Chromium156.0.8078.79, Playwright, DPR1, servidor HTTP local na porta8877; axe-core4.14.0 com regras WCAG2A/AA e2.1A/AA. Telas03–11 visitadas em375×812,390×844,430×932; explorações adicionais320×568,768×1024 e1440×900. Total54 combinações, com27 novas screenshots nos tamanhos-alvo. [Mosaico das capturas390](validacao-global/mosaico.png).

| Verificação | Resultado observado |
|---|---|
| Carregamento das nove telas | Todas abriram; nenhuma imagem visível quebrada nos54 estados iniciais |
| Dimensões móveis contratadas | Sem overflow horizontal/vertical de documento nas27 combinações; isso não exclui áreas internas roláveis |
| Links presentes no repouso |17 ocorrências locais responderam HTTP200; ausência de links de fluxo é problema separado |
| Botões visíveis no repouso |94 cliques executados sem timeout; isso não certifica todas as combinações ou controles de dialogs |
| Dialogs abertos por esses botões |57 verificações de Escape e retorno de foco passaram |
| Cenários específicos |8 verificações funcionais locais passaram; uma verificação adicional reproduziu a ausência de compartilhamento07→09 |
| Erros |Sem exceções JavaScript observadas; Tela08 emitiu erro de recurso404, associado à ausência de favicon. Nenhuma imagem/CSS/JS do runtime teve HTTP>=400 capturado |
| Acessibilidade automatizada |10 grupos regra/tela,39 ocorrências em nós; oito telas com alertas, somente05 sem violação automática nesse estado |
| Evidências anteriores |Hashes das27 capturas finais encontrados nas respectivas evidências;116 entradas dos manifestos07–11 conferidas, sem divergência |

Não se deve contar o cenário que reproduz uma lacuna como aprovação da funcionalidade de integração. Os testes de mensagens06 e edição10 confirmaram uso seguro de texto nos dois caminhos exercitados, não constituem auditoria de segurança completa.

Relatórios brutos: [navegador](validacao-global/browser.json), [cenários funcionais](validacao-global/funcional.json), [manifestos](validacao-global/hashes.json), [capturas anteriores](validacao-global/capturas_anteriores.json). Os avisos axe são evidência automatizada; precisam ser resolvidos e reavaliados com navegação assistiva, inclusive possíveis ambiguidades em rótulos de cartões compostos.

## Pendências de integração — prioridade alta

1. **Entrada e telas ausentes.** A raiz apresenta `Directory listing for /`, não uma aplicação. Não há index/roteador agregador. Telas01/02 têm referência, mas não implementação neste workspace. Evidência: [README](../README.md), resposta real da raiz no relatório browser.
2. **Fluxo desconexo.**03 não oferece saída para04;04 não abre05/06;07 não abre08.09 e11 não recebem links de entrada das outras telas;10 só recebe entrada de11. Há botões de perfil que continuam abrindo avisos embora10 já exista. Referências: [03app.js](../MODEL_tela_03_V2/app.js), [04app.js](../MODEL_tela_04_V1/app.js), [07app.js](../MODEL_tela_07_V1/app.js), [09app.js](../MODEL_tela_09_V1/app.js). Links200 não corrigem a ausência dessas conexões.
3. **Estado fragmentado.** Favoritos03/04 e salvos09 não compartilham dados. Salvar casting07 não alimenta a aba Castings09: o teste de navegador salvou uma campanha e encontrou a lista vazia em09. Filtros08 só exibem resumo, sem alterar07. Recarregar/navegar elimina alterações. Referências: [07app.js](../MODEL_tela_07_V1/app.js), [08app.js](../MODEL_tela_08_V1/app.js), [09app.js](../MODEL_tela_09_V1/app.js), relatório funcional.
4. **Camada de aplicação ausente.** Não há autenticação, persistência, API/backend ou envio real. Chat, notificações, edição e contratação são demonstrações locais. Essa condição já era declarada; a aprovação visual não a resolve. O produto completo depende da definição e implementação dessas integrações.

## Pendências de qualidade — prioridade média

- **Contraste de texto:**04 (localização, medidas e bio),06 (horários e status online),08 (Limpar e valores),09 (cidades),10 (chips),11 (horários). Exemplos medidos em390:09=3,64:1;11=3,17:1; requisito usado4,5:1. Seletores, cores e valores completos no browser.json.
- **Semântica e nomes acessíveis:**03 `.progress` usa `aria-label` em `div` sem papel apropriado;07 cartões,08 botões de valores e11 notificações receberam `label-content-name-mismatch`. Rever os nomes para contemplar o rótulo visível e confirmar com tecnologia assistiva.
- **Sobreposição de toque em08:** sliders `#age`/`#height` intersectam `#value-height`/`#value-fee` em375/390. Em390, altura sobreposta≈2,80px, larguras≈85,91/100,23px; `elementFromPoint` atinge o botão da linha seguinte nessa região. Todos têm44px, mas as áreas não são independentes.430 não reproduziu o problema. Esse achado novo limita a declaração anterior de ausência de sobreposição; notas históricas permanecem estimativas visuais.
- **Retorno inconsistente:**06 anuncia “Voltar ao perfil”, mas aponta para05/Portfólio ([HTML](../MODEL_tela_06_V1/index.html)).10 só usa history.back para referrer03–09 terminado em `index.html`; vindo de11 ou de URL de pasta cai em09 ([app.js, linha12](../MODEL_tela_10_V1/app.js#L12)).
- **Semântica de Salvos09:** remover favorito mantém o card e muda ícone/contador. Isso foi documentado como alternativa demonstrativa com desfazer; para o produto, definir se itens removidos saem da lista e alinhar com o estado compartilhado.
- **Tamanhos extras:** em320×568 há sobreposição de controles em06/07/08 e alvos abaixo44 em04/11. Rolagem vertical em telas compactas não é, sozinha, defeito; precisa preservar acesso a tudo. Em1440×900 apareceram sobreposições09/11. Não declarar compatibilidade desktop apenas porque não houve overflow horizontal.

## Ordem de correção e novo aceite

1. Recuperar/implementar01/02 e definir entrada/rotas; conectar descoberta→swipe→perfil→portfólio/chat, castings→filtros e áreas salvos/perfil/notificações com retorno correto.
2. Definir um estado compartilhado de perfis, salvos, filtros e conversa; decidir persistência local e contratos reais de backend. Preservar a indicação de demonstração enquanto não houver integração.
3. Corrigir contraste, rótulos/ARIA e interseções de toque. Ajustar layouts compactos e definir explicitamente o suporte a tablet/desktop.
4. Reexecutar testes de jornada completa e acessibilidade. Qualquer mudança visual deve gerar novas capturas e auditoria da versão alterada, preservando as referências e o gate>9.

Aceite global: entrada utilizável, nenhuma área implementada inacessível pelo fluxo previsto, filtros e salvos coerentes entre telas, retorno semântico correto, testes de teclado/assistividade, ausência de falhas materiais nos viewports suportados e funcionalidades reais claramente diferenciadas da demonstração.

## Reprodução e limites

Servir a raiz com `python3 -m http.server 8877 --bind 127.0.0.1`. Scripts [validar.cjs](validacao-global/validar.cjs) e [funcional.cjs](validacao-global/funcional.cjs) usam Playwright e Chromium em `/usr/bin/chromium`. O primeiro espera axe em `/tmp/model-audit-deps/node_modules/axe-core/axe.min.js`: instalar isoladamente com `npm install --prefix /tmp/model-audit-deps axe-core@4.14.0 --no-save --ignore-scripts`. Copiar os scripts para uma pasta de evidências, criar sua subpasta `capturas`, executar por Node. Eles gravam relatórios nessa pasta; não sobrescrever as evidências entregues. A versão axe usada consta no JSON; instalação futura sem pin pode diferir.

Esta validação usou Chromium headless em ambiente local. Não verificou Safari/Firefox, dispositivo físico/safe areas reais, leitor de tela, rede móvel, backend, implantação pública nem todos os estados combinatórios. As notas visuais03–11 são históricas por tela; esta auditoria não lhes atribui certificação de acessibilidade ou integração.
