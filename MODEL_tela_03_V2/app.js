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

function syncActions() {
  const state = ModelStore.getState();
  document.querySelector('.favorite').setAttribute('aria-pressed', state.savedProfileIds.includes('enzo'));
  document.querySelector('.like').setAttribute('aria-pressed', state.likedProfileIds.includes('enzo'));
  const ignored=state.dismissedProfileIds.includes('enzo');
  details.hidden=ignored; actions.hidden=ignored; emptyState.hidden=!ignored;
  if(ignored) screen.dataset.dismissed='true'; else delete screen.dataset.dismissed;
}
for (const [selector, field] of [['.favorite','savedProfileIds'], ['.like','likedProfileIds']]) {
  document.querySelector(selector).addEventListener('click', () => {
    const result = ModelStore.dispatch({type:'toggle',field,id:'enzo'});
    announcement.textContent = result.persistent ? 'Alteração salva neste dispositivo.' : 'Armazenamento indisponível: a alteração pode se perder ao sair desta página.';
  });
}
ModelStore.subscribe(syncActions); syncActions();

dismiss.addEventListener('click', () => {
  const result=ModelStore.dispatch({type:'toggle',field:'dismissedProfileIds',id:'enzo'});
  announcement.textContent = result.persistent?'Perfil ignorado neste dispositivo. Desfazer disponível.':'Armazenamento indisponível: a alteração pode se perder ao sair desta página.';
  undo.focus();
});
undo.addEventListener('click', () => {
  ModelStore.dispatch({type:'toggle',field:'dismissedProfileIds',id:'enzo'});
  announcement.textContent = 'Perfil de Enzo restaurado.';
  dismiss.focus();
});

const panels = {
  back: ['Descobrir', 'Esta versão apresenta o perfil de Enzo. A navegação para a grade será conectada na integração ao aplicativo.'],
  options: ['Mais opções', 'As ações disponíveis neste protótipo são ignorar, favoritar e curtir. As escolhas ficam neste dispositivo.'],
  info: ['Enzo, 26', 'São Paulo, SP · 1,84 m. Fashion, Editorial, Comercial. Perfil verificado.'],
};
for (const button of document.querySelectorAll('[data-panel]')) {
  button.addEventListener('click', () => {
    if (button.dataset.panel === 'back') return ModelNavigation.goTo('descobrir');
    if (button.dataset.panel === 'info') return ModelNavigation.goTo('perfil-modelo');
    const [title, copy] = panels[button.dataset.panel];
    document.querySelector('#dialog-title').textContent = title;
    document.querySelector('#dialog-copy').textContent = copy;
    let link = dialog.querySelector('.saved-link'); if (!link) { link = document.createElement('a'); link.className = 'saved-link'; link.href = '../MODEL_tela_09_V1/'; link.textContent = 'Salvos'; dialog.append(link); }
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


// These foreground glyph contours represent only the fixed reference data.
// Native text remains the accessible source of truth and the atomic fallback.
const referenceTextLayers = [
  { native: document.querySelector('.name h1'), visual: document.querySelector('.label-name'), expected: 'Enzo, 26' },
  { native: document.querySelector('.location-row p'), visual: document.querySelector('.label-location'), expected: 'São Paulo, SP · 1,84 m' },
];
function syncReferenceText() {
  const ready = screen.dataset.nativeText !== 'true' && referenceTextLayers.every(({ native, visual, expected }) =>
    native.textContent.trim() === expected && visual.complete && visual.naturalWidth > 0
  );
  for (const { native, visual } of referenceTextLayers) {
    native.classList.toggle('sr-only', ready);
    visual.hidden = !ready;
  }
}
for (const { visual } of referenceTextLayers) {
  visual.addEventListener('load', syncReferenceText);
  visual.addEventListener('error', syncReferenceText);
}
new MutationObserver(syncReferenceText).observe(screen, {
  subtree: true, childList: true, characterData: true,
  attributes: true, attributeFilter: ['data-native-text'],
});
syncReferenceText();
