# MODEL — fila executável das quatro últimas telas

Atualização: 2026-11-11 (America/Sao_Paulo). A execução está autorizada; este documento organiza o despacho sem solicitar nova confirmação. Não define conteúdo, medidas ou layout das telas08–11 antes de seus gates. As referências fornecidas já existem e serão abertas pelo planejador de cada tela quando liberado.

A Tela07 está retomando implementação e precisa de auditoria independente **>9,0/10** antes de iniciar conteúdo08. A meta de cada tela é **9,5/10**; exatamente9,0 não libera avanço. Preservar integralmente03–06 aprovadas (9,13/9,30/9,34/9,28), seus pacotes publicados e evidências.

## Despacho sequencial

| Tela | Estágio1 — planejador | Estágio2 — assets | Estágio3 — implementador | Estágio4 — auditor independente | Liberação |
|---|---|---|---|---|---|
| 08 — Filtros | planejador08, somente após gate07 | assets08, após entrega do planejador08 | implementador08, após assets08 utilizáveis | auditor08, após evidências finais08 | Gate08>9,0 libera planejador09 |
| 09 — Salvos | planejador09, somente após gate08 | assets09, após entrega do planejador09 | implementador09, após assets09 utilizáveis | auditor09, após evidências finais09 | Gate09>9,0 libera planejador10 |
| 10 — Meu perfil | planejador10, somente após gate09 | assets10, após entrega do planejador10 | implementador10, após assets10 utilizáveis | auditor10, após evidências finais10 | Gate10>9,0 libera planejador11 |
| 11 — Notificações | planejador11, somente após gate10 | assets11, após entrega do planejador11 | implementador11, após assets11 utilizáveis | auditor11, após evidências finais11 | Gate11>9,0 encerra a fila visual |

Executar os quatro papéis por tela, em sequência. Não abrir planejamento de conteúdo, medir layout, criar assets ou código da tela seguinte durante o gate pendente. Auditor independente não pode ser o implementador da versão avaliada. O coordenador atualiza o estado real da fila a cada entrega; despacho não equivale a aprovação.

## Contrato de entrega de cada papel

1. **Planejador:** abrir referência oficial e contexto anterior aprovado; registrar requisitos verificáveis, medidas, incertezas e interações locais em `DESIGN_SPEC.md` e `PLANO.md` no pacote versionado da tela. Indicar arquivos e critérios para o próximo papel, sem inventar conteúdo ilegível.
2. **Assets:** usar os insumos fornecidos. Entregar `ASSETS.md`, manifest com origem/coordenadas/dimensões/hashes, extração reproduzível e arquivos locais independentes. Preservar identidade e proporção; não gerar pessoas, corpos ou pixels ocultos. Identificar SVGs aproximados. Fotografia insuficiente bloqueia a tela; não usar screenshot integral como fundo para simular UI.
3. **Implementador:** entregar frontend nativo HTML/CSS/JS local, sem backend, com estado/interações locais explícitos, acessibilidade e navegação verificáveis. Instalar dependências necessárias está autorizado. Entregar código, `VERSION`, `README.md`, `CHANGELOG.md`, verificação funcional, relatório técnico, capturas e comparação da mesma versão. Não atribuir nota própria.
4. **Auditor independente:** abrir referência e imagens finais, conferir versão/hashes e revisar evidências técnicas; registrar diferenças concretas, limites, pesos/notas e decisão em `AUDITORIA.md`. Distinguir testes executados dos apenas revisados. A nota não é herdada da tela anterior nem elevada para cumprir a fila.

## Evidência e gate cumulativos

- Três screenshots reais finais em **375×812**, **390×844** e **430×932**, **DPR1**, com navegador, procedimento e versão documentados. Recortes de referência não são screenshots do app.
- Comparação da captura390 com a referência em altura normalizada, preservando proporções sem deformação; abrir as três capturas e a comparação antes da entrega.
- Conferir carregamento de fotos/SVGs, anatomia/proporção, ausência de overflow indevido, erros de console/rede, textos/ícones, foco, alvos de toque, safe areas e interações previstas. Registrar fallbacks e limitações efetivamente verificadas.
- Rubrica: fotografia/identidade/enquadramento **35%**; geometria **25%**; tipografia/ícones/chips **20%**; cores/contraste/sobreposição **10%**; responsividade/acabamento **10%**. A soma ponderada deve ser **>9,0/10**, com meta9,5 e nenhum bloqueador material.
- Código, assets, documentação, auditoria, screenshots, comparação e hashes devem corresponder à mesma versão. Preservar versões anteriores e evidências; não sobrescrever pacotes aprovados para encaixar uma tela nova.

Reprovação corrigível retorna ao papel responsável, seguida de nova versão, três capturas e auditoria. Dependência incontornável gera bloqueio documentado com prova e condição objetiva de retomada, mantendo as telas posteriores aguardando. Nenhuma correção permite reaproveitar nota ou captura antiga como prova da versão atual.

## Versionamento, publicação e execução

Usar pacotes separados por tela e versões explícitas; manter03–06 intactas. A publicação no GitHub já foi autorizada e deve incluir o conjunto completo correspondente à versão aprovada, sem declarar publicado o que não foi enviado. Publicação não substitui gate visual nem libera conteúdo da tela seguinte sem auditoria. Este papel de coordenação não publica, não produz assets, HTML, capturas ou notas.

O agente pode executar o trabalho no workspace e coordenar os papéis autorizados. Não tem capacidade de alterar o modo da interface ou mover a sessão para ChatGPT Work; isso não impede a continuidade local já autorizada.

**Próximo despacho:** concluir implementador07_retomada → auditor07 independente. Assim que `AUDITORIA.md` da07 registrar gate>9,0 sem bloqueador material, liberar **planejador08** para abrir a referência fornecida e entregar sua especificação e plano; depois assets08 → implementador08 → auditor08, sem nova confirmação.
