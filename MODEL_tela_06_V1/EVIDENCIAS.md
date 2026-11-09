# Evidências06 congeladas

Versão: 1.0.0-prototipo.1. Chromium: 156.0.8078.79. DPR1.

Execução: `python MODEL_tela_06_V1/render.py` e `python MODEL_tela_06_V1/compare.py` da raiz model-app.

Três capturas raw do estado inicial antes de interações. Console/rede normal sem erros; rede externa bloqueada. Cinco dialogs, Escape/foco, envio vazio/comum/literal/longo, reload e back05 passaram em cada viewport. Contexto separado com fotos bloqueadas e reduced-motion passou.

TDD: HTML ausente falhou explicitamente. Alvo input17px falhou e foi corrigido44px. Após apertar teste de overflow inicial, fallback revelou corrida de erro de foto anterior ao listener; correção também verifica complete/naturalWidth, suíte final verde.

Sem nota/publicação. Auditoria independente pendente.

| Arquivo | SHA256 |
|---|---|
| `app.js` | `ccadd36d45d5425d193b4c61369192e4ce8e2fe1bac2e754409ecea719e5e355` |
| `assets/avatar-header.png` | `fc4f7eb88e25e5b9b8d0e30c18fbd14266403cc2310491a9642fb7985c6ac738` |
| `assets/avatar-received-first.png` | `8bef69b99c8edcab97f8e966d68b4c44ba146dfbb6e410d728d41a7cba3ed244` |
| `assets/avatar-received-last.png` | `826f642277d26796703ad609e95b3b81f11b47b310ae649e74f6b5778ed5d066` |
| `assets/campaign-office.png` | `c44df16320d00cecd715108f74cb96a1f58ed26e222493c55615ce8d73abca65` |
| `assets/extract_assets.py` | `ef17016efd3608dbef50bdaf50bd258a5a4c73f6fc65efca030bad843edb0ab3` |
| `assets/manifest.json` | `b150c213dacffdd9231bd7f832bcf4a55698125f2ea459969979d16db676ac62` |
| `candidato-390.png` | `6c00f65f51660467777c309fd34e0e1ba0b1d22d75387107c0be8ef018f1bdf1` |
| `comparacao-390.png` | `eb681be84a7c2211ad0591b6cefb2c747a7972d4ea90cf0e94bc341c502b492a` |
| `compare.py` | `7faff1d022ed97f54cb2e7dd1dca3e8bb3d80a25df55e357a9f74ad8f17b8b54` |
| `index.html` | `c5a62e04807adcb9a2bb09b192cb1aa715910f1aeed925fb5b05674ca9789550` |
| `relatorio-browser.json` | `3e28ebe763e10d50847d8f7f43bfb939442aa4449c6c79b5ec64ce3732244dce` |
| `relatorio-candidato.json` | `e53f3468f38a8e31b8a12f4f4cf74854539a0fdb921993ea8c3758e75cb62af9` |
| `render.py` | `f9356d2d23e76c1bf617f65794db77de83f9f2d09d0f3cbedbe4d191fdab3804` |
| `screenshots/375x812.png` | `28f64c6b1955907564a1daaf391bdd9328fb3ae5f3fbe93c91d56827e044a38f` |
| `screenshots/390x844.png` | `aac6d46f3c49e1a96184c56671008a8102e664734fab12f6670ec8f1c088788f` |
| `screenshots/430x932.png` | `8116aac22690ba216934e1d6cddb417217a59bfe4c86b90226b052d34cc49e2e` |
| `styles.css` | `8f957776f3db962ded2696b5463d087397cb3ceca24c53055694e939a14dc622` |
