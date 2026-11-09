'use strict';

const screen = document.querySelector('.screen');
const announcement = document.querySelector('#announcement');
const details = document.querySelector('.details');
const actions = document.querySelector('.actions');
const emptyState = document.querySelector('.empty-state');
const undo = document.querySelector('.undo');
const dismiss = document.querySelector('.dismiss');
const dialog = document.querySelector('dialog');
const portrait = document.querySelector('.portrait');

for (const [selector, selected, cleared] of [
  ['.favorite', 'Enzo adicionado aos favoritos desta sessão.', 'Enzo removido dos favoritos desta sessão.'],
  ['.like', 'Curtida registrada nesta sessão.', 'Curtida desfeita nesta sessão.'],
]) {
  const button = document.querySelector(selector);
  button.addEventListener('click', () => {
    const next = button.getAttribute('aria-pressed') !== 'true';
    button.setAttribute('aria-pressed', String(next));
    announcement.textContent = next ? selected : cleared;
  });
}

dismiss.addEventListener('click', () => {
  details.hidden = true;
  actions.hidden = true;
  emptyState.hidden = false;
  screen.dataset.dismissed = 'true';
  announcement.textContent = 'Perfil ignorado nesta sessão. Desfazer disponível.';
  undo.focus();
});
undo.addEventListener('click', () => {
  details.hidden = false;
  actions.hidden = false;
  emptyState.hidden = true;
  delete screen.dataset.dismissed;
  announcement.textContent = 'Perfil de Enzo restaurado.';
  dismiss.focus();
});

const panels = {
  back: ['Descobrir', 'Esta versão apresenta o perfil de Enzo. A navegação para a grade será conectada na integração ao aplicativo.'],
  options: ['Mais opções', 'As ações disponíveis neste protótipo são ignorar, favoritar e curtir. As escolhas ficam apenas nesta sessão.'],
  info: ['Enzo, 26', 'São Paulo, SP · 1,84 m. Fashion, Editorial, Comercial. Perfil verificado.'],
};
for (const button of document.querySelectorAll('[data-panel]')) {
  button.addEventListener('click', () => {
    const [title, copy] = panels[button.dataset.panel];
    document.querySelector('#dialog-title').textContent = title;
    document.querySelector('#dialog-copy').textContent = copy;
    dialog.showModal();
  });
}
document.querySelector('.close-dialog').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => {
  if (event.target !== dialog) return;
  const bounds = dialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
});

function showImageError() {
  document.querySelector('.image-error').hidden = false;
  for (const button of actions.querySelectorAll('button')) button.disabled = true;
}
portrait.addEventListener('error', showImageError);
if (portrait.complete && portrait.naturalWidth === 0) showImageError();
