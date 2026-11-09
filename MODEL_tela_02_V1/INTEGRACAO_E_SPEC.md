# Tela 02 — Descobrir (V1)

## Objetivo
Grade editorial minimalista de modelos masculinos adultos, com acesso ao perfil aberto, favoritos e manifestação de interesse. O modelo poderá consultar interessados e compartilhar álbuns privados mediante autorização individual.

## Layout
- Mobile: 2 colunas de cards com fotografia 3:4, nome, idade, categorias e ação de favoritar; desktop: grade responsiva.
- Topo: marca MODEL, notificações e acesso ao perfil.
- Abas: Descobrir, Favoritos, Interesses. Navegação principal: Descobrir, Mensagens, Projetos, Perfil.
- Filtros: categoria (Editorial/Fitness/Comercial/Fashion), biotipo (Atlético/Musculoso e peludo/Jovem adulto), idade mínima/máxima (21+), disponibilidade.
- Perfil aberto: hero fotográfico, informações profissionais, medidas, portfólio, interesse, favoritos, mensagens e álbuns privados.
- Design: preto #171717, branco, bege #EAE5DE; tipografia editorial e ícones SVG independentes.

## Regras
- Interesse não libera automaticamente álbum privado nem abre conversa.
- Modelo aprova compartilhamento, com possibilidade de revogação e controle de acesso.
- Evitar expor dados de clientes sem autenticação e consentimento.
- Fotos originais devem permanecer independentes de screenshots/mockups.

## Estado da integração
O pacote local MODEL-tela-02-prototipo.zip foi inspecionado: contém index.html, styles.css, app.js, quatro retratos PNG, 32 SVGs e a especificação. Este documento foi publicado no GitHub como primeiro passo de integração.

**Pendente:** transferir o código e as imagens binárias do pacote ao repositório. Não considerar a Tela 02 publicada ou funcional no GitHub até os arquivos estarem presentes.

## Validação
Tentativas de executar Chromium com servidor local e arquivo file:// foram bloqueadas pelo ambiente (ERR_BLOCKED_BY_ADMINISTRATOR). Capturas reais, comparação visual e testes de interação não foram realizados; não atribuir nota de aprovação.

## Próximos gates
1. Publicar HTML/CSS/JS, SVGs e PNGs originais na branch.
2. Rodar Chromium nas larguras 375, 390, 430 e 1440 px e capturar perfil aberto.
3. Comparar com o mockup aprovado, registrar diferenças e corrigir.
4. Executar testes de filtros, favoritos, interesse, álbum privado e navegação.
5. Revisão e merge somente após auditoria.
