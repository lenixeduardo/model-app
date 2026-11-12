# Tarefa 2 — estado compartilhado

Implementação: commit `667c21b` em `feat/correcoes-1-2-3`, baseado em `c546d85`. `shared/data.js` contém IDs e dados observados; `shared/store.js` fornece getState/dispatch/subscribe, normalização schema 1, persistência local e eventos entre abas. Quatro perfis começam salvos; castings começam sem salvos. Curtida e rejeição são independentes. Sem backend ou envio real.

## RED

`npx playwright test tests/e2e/state.spec.cjs --reporter=line` antes da implementação: jornada 07 → 09 falhou porque Campanha Inverno 2025 não aparecia em Salvos; jornada 03 → 04 também não compartilhava o botão. A jornada de perfil foi ajustada para verificar a remoção e restauração partindo dos quatro salvos iniciais coerentes.

## GREEN

`npx playwright test tests/e2e/navigation.spec.cjs tests/e2e/state.spec.cjs --reporter=dot`: **16 passed (14.8s)** após as alterações finais. Cobertura inclui remoção do último salvo/desfazer, reload, JSON inválido, campos e IDs inválidos, storage bloqueado, filtros em ambas as origens, lista vazia e limpar, mensagem renderizada por textContent, edição, leitura, armazenamento entre abas e ignorar/desfazer após reload. `git diff --check`: sem erros.

## Revisão e limites

Na primeira suíte integrada, dois testes detectaram sobreposição de controles de cartão e aviso de filtro; CSS foi corrigido e a suíte repetida. Filtros sem dados não são presumidos: distância e disponibilidade não são aplicadas; altura/categoria de perfis e cachê de castings somente quando informados. Dados ausentes permanecem nos resultados com explicação. Mensagens e alterações são locais e não são enviadas. Sem armazenamento, ações permanecem em memória na página e o fluxo pertinente alerta sobre possível perda ao navegar ou recarregar. As capturas anteriores não foram alteradas; não houve nova avaliação visual ou nota nesta tarefa. Navegação/acessibilidade restante e revisão independente ficam nas tarefas seguintes.

## Correção da revisão — rodada 1

Commit de implementação `0dbfa5f`. Alterados os consumidores 06, 07, 09, 10 e 11, o texto da tela 11, o CSS de foco/aviso da 09, versões/changelogs dessas telas e `tests/e2e/state.spec.cjs`. As telas assinam o store e as notificações partem do estado corrente antes de editar uma leitura. A edição de perfil despacha apenas campos alterados. Desfazer retorna foco ao controle restaurado; a confirmação em lote inclui eventual bloqueio de armazenamento; o diálogo explica a persistência local.

RED: `npx playwright test tests/e2e/state.spec.cjs --grep 'edição de nome|notificações em duas|salvos, chat|desfazer retorna|ações em lote' --reporter=dot` resultou em **5 failed**: os cinco cenários expuseram disponibilidade sobrescrita, notificações/listas desatualizadas, foco/controle encoberto e aviso antigo. Após a correção, o mesmo comando resultou em **5 passed (5.9s)**. A primeira suíte completa detectou sobreposição do aviso com outro cartão (20 passed, 1 failed); a área de clique foi ajustada.

GREEN final: `npx playwright test tests/e2e/navigation.spec.cjs tests/e2e/state.spec.cjs --reporter=dot` resultou em **21 passed (20.0s)**. `git diff --check` sem erros. Nenhuma nova captura ou nota visual foi produzida.
