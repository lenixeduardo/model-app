# Correção global do MODEL — plano e to-do

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Conectar os protótipos MODEL, corrigir os problemas comprovados e validar jornadas completas antes de declarar o aplicativo integrado.

**Architecture:** Preservar inicialmente HTML/CSS/JS e pastas por tela. Introduzir navegação e estado compartilhados em módulos pequenos, sem migração de framework como pré-requisito. Separar o marco de protótipo integrado do marco de serviços reais; armazenamento local não equivale a backend ou autenticação.

**Tech Stack:** HTML, CSS, JavaScript, Playwright, Chromium e axe-core4.14.0; serviços de produção terão contrato próprio antes de implementação.

**Spec:** [Validação global](../../VALIDACAO_GLOBAL.md), referências originais em `MODEL_assets_v1/referencias/`, especificações e auditorias por tela.

## Restrições globais

- Preservar identidade, fotografias genuínas, textos e composição do mockup; não substituir pessoas ou fabricar partes de imagem.
- Versionar cada tela alterada e preservar evidências anteriores; captura antiga não aprova implementação nova.
- Gate visual de avanço **>9,0/10**, meta9,5; capturas reais375×812,390×844,430×932,DPR1 e comparação proporcional.
- Fotografias/fonte insuficientes devem gerar limitação documentada, nunca nota inventada.
- Indicar demonstração nas ações locais enquanto não existir integração real.
- Critérios para protótipo integrado e produto real são distintos. Nenhuma tarefa abaixo foi executada por este plano.

## Foco de revisão

1. Entrada direta e recarregamento de qualquer tela: conteúdo acessível, retorno previsível e ausência de dependência de referrer.
2. Dados locais ausentes, antigos ou inválidos: recuperar estado inicial sem travar a aplicação.
3. Remover o último salvo e desfazer: lista, contador e ícones consistentes entre telas.
4. Filtros sem resultado ou com limites inválidos: validação e estado vazio, sem inventar dados disponíveis.
5. Teclado,320×568 e texto ampliado: controles alcançáveis e sem sobreposição; preservar acesso por rolagem.

## Estado da execução nesta publicação

- **Etapa1 implementada e revisada:** entrada, Telas01/02 e navegação. Auditoria visual01=9,23;02=9,10 no escopo da tarefa1.
- **Etapa2 implementada:** estado compartilhado e persistência local, incluindo correções da primeira revisão;21 testes de navegação/estado passaram. A revisão independente final desta rodada ainda está pendente.
- **Etapa3 pendente:** contraste, ARIA/rótulos e áreas de toque; não houve aprovação global de acessibilidade.
- Etapas4–6 e a nova auditoria visual das telas modificadas permanecem pendentes. A publicação dos avanços não equivale a aceite final.

## Ordem e marcos

| Ordem | Prioridade | Entrega | Dependência |
|---|---|---|---|
| 1 | P0 | Entrada, Telas01/02 e navegação completa | Referências e assets existentes |
| 2 | P0 | Estado único, salvos e filtros funcionais | Rotas definidas |
| 3 | P1 | Acessibilidade e áreas de toque | Pode começar enquanto1/2 avançam |
| 4 | P1 | Responsividade e acabamento | Integração estabilizada |
| 5 | P0 para aceite | Revalidação do protótipo integrado |1–4 concluídos |
| 6 | P0 para produção | Autenticação, persistência e serviços reais | Contratos de produto/backend definidos |

### 1. Entrada e navegação — P0

**Arquivos:** criar `index.html`, `shared/navigation.js`, `MODEL_tela_01_V1/`, `MODEL_tela_02_V1/` e `tests/e2e/navigation.spec.cjs`; alterar os controles de navegação de03–11 e seus READMEs.

**Interface:** `getRoutePath(route)` resolve nomes estáveis de rota para caminhos das onze telas; `goTo(route, {returnTo})` recebe apenas rotas conhecidas. Retorno direto usa fallback explícito, sem depender exclusivamente de `document.referrer`. Preservar links nativos quando possível.

- [ ] Registrar os destinos de todas as ações existentes antes de mudar links; definir entradas de Salvos e Notificações usando controles previstos no mockup, sem criar aba decorativa.
- [ ] Criar teste que demonstre as falhas atuais: raiz com listagem e jornadas desconectadas. Executar `npx playwright test tests/e2e/navigation.spec.cjs`; registrar falha do comportamento esperado antes da correção.
- [ ] Implementar ou recuperar01/Login e02/Descoberta a partir das referências; manter pessoas originais e submeter ambas à auditoria visual.
- [ ] Fazer `/` abrir a experiência do aplicativo; enquanto houver apenas demonstração, oferecer entrada identificada como demonstração, sem fingir autenticação.
- [ ] Conectar02→03→04,04→05/06 e07→08; tornar09/10/11 alcançáveis por controles coerentes com a referência.
- [ ] Substituir avisos de “área indisponível” somente quando a tela de destino realmente estiver implementada.
- [ ] Corrigir06: “Voltar ao perfil” deve levar ao perfil correspondente; corrigir10 para retornar corretamente também quando veio de11 ou de URL de pasta.
- [ ] Reexecutar o teste: todas as jornadas e entradas diretas devem passar, incluindo retorno após reload e URL sem `index.html`. Versionar e revisar a entrega.

**Aceite:** abrir a raiz e percorrer todas as áreas previstas sem digitar URLs; nenhum link morto, destino incompatível com o rótulo ou retorno condicionado a uma forma específica de URL.

### 2. Estado compartilhado, salvos e filtros — P0

**Arquivos:** criar `shared/data.js`, `shared/store.js`, `tests/e2e/state.spec.cjs`; adaptar `app.js` de03/04/06/07/08/09/10/11. A listagem02 também deve consumir os mesmos perfis.

**Interface:** `getState()`, `dispatch(action)` e `subscribe(listener)`; estado versionado com `savedProfileIds`, `savedCastingIds`, `likedProfileIds`, `dismissedProfileIds`, `filters`, `profile`, `messages` e `notificationReadStates`. Perfis e castings têm IDs estáveis. `filters` contém cidade, distância, intervalos, categorias e disponibilidade. Favoritar/salvar compartilham estado; curtir permanece uma ação distinta. Persistência local do protótipo usa chave `model:state:v1` e recuperação de JSON inválido.

- [ ] Criar testes que falhem para07→09 e03/04→09, demonstrando o estado atualmente isolado.
- [ ] Centralizar dados e ações; definir estado inicial coerente, preservando fixtures visuais de auditoria separadas do estado usado nas jornadas.
- [ ] Fazer favoritar/salvar/remover um perfil refletir em03/04/09; salvar casting07 deve aparecer na aba Castings09.
- [ ] Fazer a lista Salvos remover o item desmarcado e oferecer desfazer; cobrir último item, lista vazia, contador e reversão em todas as telas afetadas.
- [ ] Persistir as alterações locais acordadas entre navegação e reload. Quando armazenamento estiver indisponível, manter a sessão funcional e informar a limitação na ação pertinente.
- [ ] Aplicar filtros08 à listagem de origem e preservar os critérios no retorno; validar mínimo≤máximo e oferecer limpar/estado vazio.
- [ ] Implementar somente critérios para os quais há dados; critérios indisponíveis não podem ser apresentados como efetivamente aplicados. Sem geodados, distância real depende do marco6.
- [ ] Sincronizar edição10, mensagens06 e leitura11 através do store local, mantendo a indicação de demonstração e sem alegar envio.
- [ ] Executar `npx playwright test tests/e2e/state.spec.cjs`: cobrir JSON inválido, reload, último salvo/desfazer e filtro sem resultado. Versionar e revisar a entrega.

**Aceite:** uma ação tem o mesmo efeito nas telas que representam esse dado; reload segue a política definida; aplicar filtros modifica resultados de forma verificável.

### 3. Acessibilidade e toque — P1

**Arquivos:**03`index.html`;04/06/08/09/10/11`styles.css`;07/08/11`app.js`; criar `tests/e2e/accessibility.spec.cjs`. Ajustar arquivos adicionais apenas se a nova verificação os identificar.

- [ ] Registrar testes de regressão para os achados axe e para as interseções de08 antes de corrigir.
- [ ] Corrigir contraste em04 (localização, medidas/bio),06 (horários/status),08 (valores/Limpar),09 (cidades),10 (chips) e11 (horários): texto pequeno≥4,5:1, preservando a identidade visual.
- [ ] Corrigir o papel/nome de `.progress` em03 sem anunciar progresso interativo inexistente.
- [ ] Revisar os nomes acessíveis de cartões07, valores08 e notificações11 para contemplar os rótulos visíveis; confirmar manualmente os alertas em cartões compostos.
- [ ] Eliminar a interseção dos sliders08 com os botões da linha seguinte em375/390; manter alvos≥44×44px independentes.
- [ ] Conferir Tab/Shift+Tab, foco visível, abertura/fechamento/Escape, retorno de foco e leitura dos dialogs após a integração.
- [ ] Executar `npx playwright test tests/e2e/accessibility.spec.cjs` e validação manual com leitor de tela. Registrar alertas resolvidos ou falsos positivos justificados; não ignorar regras para obter aprovação.

**Aceite:** sem violações materiais conhecidas pendentes; controles nomeados e operáveis por teclado, textos com contraste e áreas de toque sem interseção nos tamanhos suportados.

### 4. Responsividade e acabamento — P1

**Arquivos:** CSS das telas04/06/07/08/09/10/11 e navegação compartilhada; criar `tests/e2e/responsive.spec.cjs`; adicionar favicon comum e referências no HTML.

- [ ] Corrigir controles sobrepostos em06/07/08 e alvos pequenos em04/11 em320×568; permitir rolagem quando necessária, sem ocultar conteúdo para passar no teste.
- [ ] Corrigir sobreposições09/11 em1440×900 e definir container móvel adequado em telas largas; validar também768×1024.
- [ ] Testar zoom/texto ampliado e safe areas; verificar teclado virtual, orientação e rolagem de dialogs em aparelhos reais.
- [ ] Adicionar favicon e eliminar o404 observado em08.
- [ ] Conferir tipografia, tamanhos de ícones e navegação compartilhada; cada ajuste deve respeitar as diferenças intencionais do mockup.
- [ ] Executar `npx playwright test tests/e2e/responsive.spec.cjs`:375×812,390×844,430×932 e os tamanhos adicionais320×568/768×1024/1440×900. Versionar e revisar a entrega.

**Aceite:** nenhum controle inacessível ou sobreposto; sem distorção de retratos ou overflow horizontal; rolagem vertical útil é permitida. Documentar explicitamente os navegadores e tamanhos suportados.

### 5. Gate do protótipo integrado — obrigatório

**Arquivos:** criar configuração Playwright e dependências de teste em `package.json`/lockfile, incorporadas na primeira tarefa que precisar delas; `tests/e2e/`; novas evidências em `docs/validacao-integrada/`; atualizar README e status sem sobrescrever a auditoria histórica.

- [ ] Executar `npx playwright test tests/e2e` cobrindo jornadas reais, não apenas HTTP200 ou cliques sem efeito.
- [ ] Validar login demonstrativo→descoberta→perfil→portfólio/chat; salvar/remover/desfazer; casting→filtros→resultados; editar perfil e ler notificações.
- [ ] Verificar Chromium, Firefox e WebKit, além de ao menos Safari/iOS e Chrome/Android reais para comportamentos de dispositivo.
- [ ] Capturar cada tela alterada em375/390/430,DPR1; abrir as imagens, comparar com a referência e atualizar auditoria ponderada por versão.
- [ ] Exigir auditor independente, sem bloqueadores materiais e nota visual>9,0 por tela alterada; repetir correção/captura/auditoria quando necessário.
- [ ] Conferir console/rede, imagens/fontes/SVGs, links, acessibilidade, manifests/hashes e conteúdo do pacote versionado.
- [ ] Publicar o relatório de aceite com limitações explícitas; mudar o estado global somente quando as evidências comprovarem os critérios.

**Marco1 concluído:** protótipo conectado e coerente, acessível nos critérios verificados, com armazenamento local documentado e sem se apresentar como serviço real.

### 6. Serviços reais — P0 antes de produção

Esta etapa é um subprojeto próprio. As decisões abaixo produzem uma especificação de backend e um plano separado; não autorizam inventar valores comerciais, dados pessoais ou integrações inexistentes.

- [ ] Definir o escopo real: autenticação por e-mail/Apple/Google, perfis, portfólio, salvos, filtros, conversas, propostas e notificações; distinguir o que entra na primeira versão.
- [ ] Documentar provedor, modelo de dados, propriedade/acesso por usuário, migrações, contratos de API, estados de erro e critérios de teste em `docs/ESPECIFICACAO_SERVICOS.md`.
- [ ] Criar plano de implementação dos serviços com testes de integração antes de conectar os adaptadores do frontend ao backend escolhido.
- [ ] Implementar autenticação/sessão e recuperação de acesso; verificar expiração e isolamento entre contas.
- [ ] Persistir perfis, portfólio, salvos e critérios suportados; usar dados/arquivos legítimos e manter identidade e propriedade dos assets.
- [ ] Implementar envio/recebimento de mensagens, leitura de notificações e solicitações/propostas com estados de carregamento, sucesso e falha comprovados.
- [ ] Validar busca/distância real somente com dados geográficos e critérios implementados; remover a indicação de demonstração apenas das operações efetivamente integradas.
- [ ] Configurar ambientes e implantação; testar a URL pública, persistência entre sessões e recuperação de falhas, atualizando a documentação.
- [ ] Executar nova auditoria ponta a ponta contra os serviços reais e emitir aceite de produção separado do marco1.

**Marco2 concluído:** jornadas reais funcionam entre sessões/contas conforme contratos definidos; frontend não confirma operações que o serviço não concluiu.

## Papéis e acompanhamento

Preservar o método solicitado: planejador fecha o contrato da tarefa → agente de assets atua apenas quando necessário → implementador entrega versão testável → auditor independente verifica evidências. Itens dependentes aguardam o aceite da etapa anterior. Cada tarefa concluída deve registrar commit, testes executados, resultados e pendências; checkbox só é marcado após verificação.

Próxima tarefa executável: **1 — entrada e navegação**, começando pelo mapa de destinos e testes que reproduzem as desconexões. A criação deste documento não inicia a implementação.
