# Tela 03 — especificação vigente, ciclo7

Versão2.0.0-prototipo.7. **Aprovada visualmente em9,13/10** na auditoria independente, para o perfil estático de Enzo. Gate>9,0 atingido; meta9,5 permanece. Evidências e diferenças menores em AUDITORIA.md.

## Referência e composição

Referência oficial: MODEL_assets_v1/referencias/referencia-tela-03.png,203×404, recorte[420,0,623,404] do mockup geral. O retrato continua sendo Enzo,26, sem geração de pessoa/pele ou troca de pose.

A fotografia de runtime é assets/enzo-mockup-foto-com-lacunas-precisas2.png,203×404. Pixels visíveis idênticos à fonte; UI removida com alpha0 e RGB oculto zerado. Nome/localização são camadas de UI separadas, recortadas por contornos, com franja contextual conhecida de1px. Não há screenshot intacto usado como fundo. Manifestos e método em ASSETS.md e assets/ui/reference-type-manifest.json.

- Unidade de projeção: altura/404; foto object-fit:cover e object-position:8%50%, escala uniforme. O recorte horizontal decorre da razão das viewports.
- Nome: Enzo,26, selo SVG azul; localização São Paulo,SP·1,84m (espaçamento real nos textos HTML). Camadas visuais específicas do perfil, H1/P nativos acessíveis e fonte semântica.
- Ativação das duas legendas é atômica: ambas carregadas e textos exatos. Falha, opt-out data-native-text=true ou mudança textual usa fallback nativo; não apresenta raster de outro perfil.
- Categorias nativas: Fashion, Editorial, Comercial. Posição e dimensões proporcionais à referência.
- Status9:41 e cinco segmentos; voltar/opções com alvos44px. Status/gesto simulados ocultáveis via data-native-status=true.
- Ações centradas: ignorar, favoritar, curtir; círculos42unidades fonte e ícones SVG locais. Favoritar/curtir alternam aria-pressed. Ignorar permite desfazer sem inventar outro perfil.
- Informações e navegação ainda são painéis locais; nenhuma API ou persistência/backend alegada.
- Topo e base recebem fades de alpha restritos para integrar céu/status e rodapé sem apagar torso relevante; fotografia preservada entre as faixas.
- Foco visível, redução de movimento, safe areas consideradas, sem overflow nas três viewports.

## Evidências de aceite

Capturas reais375×812,390×844,430×932, DPR1, Chromium156.0.8078.79; comparacao-390.png com alturas normalizadas e proporções preservadas. render.py executa testes e registra hashes/console/rede/escala/interações/fallbacks. Auditoria independente abriu as três capturas, referência e comparação; soma ponderada9,125, arredondada9,13.

Limites: fonte original e fotografia integral limpa não foram fornecidas; não se afirma recuperação dessas fontes. UI de nome/localização raster é específica do Enzo da referência, não tipografia genérica. Safe areas em aparelho físico e VoiceOver não certificados. RefinamentosP2 listados na auditoria. Histórico de especificação em evidencias/design-spec-historico.md.
