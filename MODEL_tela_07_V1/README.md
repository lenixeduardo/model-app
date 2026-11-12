**Integração em andamento:** o runtime desta pasta foi alterado após a auditoria visual histórica. `AUDITORIA.md`, capturas antigas e seus manifests descrevem a versão pré-integração, recuperável no commit `b49b77d`; não certificam os arquivos atuais. Novas evidências e aceite final permanecem pendentes. Ver [estado da integração](../docs/correcoes-123/AVALIACAO_ATUAL.md).

**Estado vigente: APROVADA VISUALMENTE — 9,32/10**, versão 1.0.0-prototipo.2. Auditoria independente e hashes em AUDITORIA.md / EVIDENCIAS_RELEASE.json. Gate >9,0 atingido; a aprovação não certifica backend ou dispositivo físico.

# Castings — Tela07

Versão 1.0.0-prototipo.2. Protótipo HTML/CSS/JS nativo e isolado; abrir pela raiz do repositório com `python -m http.server 8000` e acessar `/MODEL_tela_07_V1/`.

Filtros reais, salvos apenas em memória e detalhes locais. Datas do mockup são estáticas. Mais, busca e perfil explicam a indisponibilidade local; nenhum cadastro ou candidatura é simulado. Navegação Descobrir03/Chat06 aponta aos pacotes aprovados.

Reproduzir: `python MODEL_tela_07_V1/render.py` e `python MODEL_tela_07_V1/compare.py` na raiz. Requer Python, Pillow, Playwright e `/usr/bin/chromium`. `--candidate` captura somente390. A raiz é servida para resolver links03/06.

Fotos extraídas do original, sem geração ou modificação de identidade. CSS exibe o frame integral com largura fluida e altura intrínseca; sem corte de laterais ou torso. Baixa resolução e matte JPEG são limites do original. SVGs locais aproximados. Veja ASSETS.md e EVIDENCIAS.md. Auditoria independente concluída em9,32/10; gate>9,0 atingido e versão aprovada publicada.

As capturas captura-375.png / captura-390.png / captura-430.png são os raw finais ou cópias idênticas dos raw em screenshots/, sem edição. Candidatos e versões anteriores são históricos, não prova da versão aprovada.


## Integração

Navegação integrada à demonstração local. Dados e ações permanecem locais; não há backend.
