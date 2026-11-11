**Estado vigente: APROVADA VISUALMENTE — 9,27/10**, versão 1.0.0-prototipo.1. Auditoria independente e hashes em AUDITORIA.md / EVIDENCIAS_RELEASE.json. Gate >9,0 atingido; a aprovação não certifica backend ou dispositivo físico.

# Salvos — tela09

Versão 1.0.0-prototipo.1. HTML/CSS/JS nativos; quatro identidades originais, estado somente em memória. Recarregar restaura quatro salvos. A alternativa de demonstração mantém os cards desmarcados, com desfazer e círculo opaco intacto. Castings apresenta vazio local honesto. Previews só oferecem perfil04 para Enzo.

Executar na raiz do repositório: `./MODEL_tela_09_V1/serve.sh`; abrir `http://127.0.0.1:8099/MODEL_tela_09_V1/`. O servidor serve a raiz para preservar links03/04/06/07. Não há backend, persistência, publicação ou tela10.

Verificação: `python MODEL_tela_09_V1/test_initial.py`, `node MODEL_tela_09_V1/verify.cjs`, `node MODEL_tela_09_V1/verify-fallback.cjs` com Playwright instalado e Chromium em `/usr/bin/chromium`. Teste inicial falhou por HTML ausente antes da implementação e passa após entrega. JSON registra navegador real, dimensões, fontes100%, carregamento, erros e ações. Capturas DPR1 raw375×812,390×844,430×932. Candidata390 aberta antes das finais; as três finais e comparação foram abertas. Comparação normaliza referência à altura844 preservando proporção, sem stretch.

Limites: fonte Arial e ícones aproximados; imagens fonte74×63/65 ampliadas sem detalhes sintetizados. A substituição opaca por foto cobre a lacuna alpha, inclusive no estado desmarcado; nenhuma anatomia foi preenchida. Frame e círculo usam a mesma unidade de container, são recortados juntos nos cantos. Fotos usam largura100% e altura intrínseca; alvos44px independem do desenho. A referência proporcionalmente mais larga à altura844 evidencia os respiros extras entre fotos e metadados no viewport390, previstos no contrato. Não foi atribuída nota; aguarda auditor independente.

As capturas captura-375.png / captura-390.png / captura-430.png são os raw finais ou cópias idênticas dos raw em screenshots/, sem edição. Candidatos e versões anteriores são históricos, não prova da versão aprovada.
