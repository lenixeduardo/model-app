**Integração em andamento:** o runtime desta pasta foi alterado após a auditoria visual histórica. `AUDITORIA.md`, capturas antigas e seus manifests descrevem a versão pré-integração, recuperável no commit `b49b77d`; não certificam os arquivos atuais. Novas evidências e aceite final permanecem pendentes. Ver [estado da integração](../docs/correcoes-123/AVALIACAO_ATUAL.md).

# MODEL — Tela 03 V2

**Aprovada visualmente:9,13/10**, ciclo7, versão2.0.0-prototipo.7. Gate>9,0 atingido; meta9,5 permanece. Aceite do protótipo estático de Enzo, sem certificação de backend ou dados arbitrários.

## Abrir e verificar

Da raiz do repositório:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Abrir http://127.0.0.1:8765/MODEL_tela_03_V2/ ou index.html diretamente. Runtime HTML/CSS/JS, sem recursos externos.

```sh
python MODEL_tela_03_V2/render.py --chromium /usr/bin/chromium
python MODEL_tela_03_V2/compare.py
```

Dependências de desenvolvimento em requirements-dev.txt. O script inicia servidor local, captura375×812/390×844/430×932 emDPR1 e registra browser, erros, dimensões e hashes em relatorio-browser.json. Testa ações, foco, toque, overflow, proporção com cover, movimento reduzido, falha de foto, falhas individuais das legendas, opt-out e divergência textual. Não altera a página para a captura.

## Composição e integração

Reutilizar index.html, styles.css, app.js e assets/. Fotografia extraída do mockup com UI removida por transparência; os pixels conhecidos de rosto/ombros/torso são preservados. Não foi gerada pessoa/pele nem encontrada a fotografia original limpa. Cover proporcional e fades restritos ao céu/rodapé integram as camadas.

Somente nome/localização usam foregroundsPNG deUI por contornos, separados da fotografia, com franja contextual conhecida de1px. São recursos estáticos para este Enzo, não arquivos da fonte tipográfica original. Ícones, selo e botões permanecem SVG/CSS/HTML. Manifesto: assets/ui/reference-type-manifest.json; proveniência em ASSETS.md.

H1/P nativos são acessíveis e fonte semântica. As imagens visuais são decorativas e só ativam quando ambos osPNGs carregam e ambos os textos coincidem exatamente. Falha de qualquerPNG, alteração textual ou data-native-text="true" na .screen mantém as duas legendas nativas visíveis. Para nomes/localizações/traduções arbitrárias, usar esse opt-out e revalidar; não reutilizar a tipografia gráfica de Enzo com outro texto.

As escolhas ficam em memória; recarregar reinicia. Nenhuma API é chamada. Voltar/opções/informações usam painéis locais. data-native-status="true" oculta status e gesto simulados se o contêiner nativo já os apresentar.

## Evidências e limites

- captura-375.png, captura-390.png, captura-430.png: capturas reais finais do Chromium.
- comparacao-390.png: alturas normalizadas, proporções intactas; larguras diferentes porque o painel fonte tem razão203/404.
- AUDITORIA.md: aprovação independente9,13, rubrica, hashes e P2.
- DESIGN_SPEC.md / CHANGELOG.md / ASSETS.md: decisões, histórico e proveniência.
- evidencias/: candidatos e ciclos anteriores identificados como históricos, não prova da versão final.

P2 restantes: contorno do selo, diferença de nitidez dos chips, margem da informação e céu/base mais uniformes. UI raster tem resolução limitada e é específica deste perfil. Aparelho físico, VoiceOver e safe areas reais não certificados. Testes técnicos e aprovação visual são escopos diferentes.

A fila em ../docs/FILA_AGENTES.md libera a Tela04. Esta nota não se transfere às telas seguintes. Os PNGs e SVGs experimentais rejeitados não são dependências do runtime aprovado.


## Integração

Navegação integrada à demonstração local. Dados e ações permanecem locais; não há backend.
