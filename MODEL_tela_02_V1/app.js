const dialog=document.querySelector('dialog'), title=document.querySelector('#dialog-title'),copy=document.querySelector('#dialog-copy'),actions=document.querySelector('#dialog-actions');let opener;
function show(t,p){opener=document.activeElement;title.textContent=t;copy.textContent=p;actions.replaceChildren();dialog.showModal()}
document.querySelector('#close').onclick=()=>dialog.close();dialog.onclose=()=>opener?.focus();document.querySelector('#options').onclick=()=>{show('Mais opções','Demonstração local.');const a=document.createElement('a');a.href='../MODEL_tela_09_V1/';a.textContent='Salvos';actions.append(a)};
document.querySelectorAll('[data-person]').forEach(b=>b.onclick=()=>show(b.dataset.person,'Prévia local da fotografia original. Perfil completo indisponível nesta demonstração.'));
function renderDiscovery() {
 const state=ModelStore.getState(), f=state.filters;
 for(const profile of ModelData.profiles){
  const card=document.querySelector('.card.'+profile.id);
  let show=true;
  if(f.applied&&f.origin==='descobrir') {
   if(f.city&&!profile.city.toLocaleLowerCase('pt-BR').includes(f.city.toLocaleLowerCase('pt-BR')))show=false;
   if(profile.age<f.age[0]||profile.age>f.age[1])show=false;
   if(profile.height!==undefined&&(profile.height<f.height[0]||profile.height>f.height[1]))show=false;
   if(f.categories.length&&profile.categories.length&&!f.categories.some(c=>profile.categories.includes(c)))show=false;
  }
  card.hidden=!show;
  const bookmark=document.querySelector('.bookmark-'+profile.id);if(bookmark){bookmark.hidden=!show;bookmark.setAttribute('aria-pressed',state.savedProfileIds.includes(profile.id))}
 }
 let status=document.querySelector('#filter-status');if(!status){status=document.createElement('p');status.id='filter-status';status.setAttribute('role','status');document.querySelector('.grid').after(status)}
 status.replaceChildren();if(f.applied&&f.origin==='descobrir'){status.append(document.createTextNode('Filtros ativos. Dados ausentes não são presumidos. '));const clear=document.createElement('button');clear.textContent='Limpar filtros';clear.onclick=()=>ModelStore.dispatch({type:'filters',value:{applied:false}});status.append(clear);if(![...document.querySelectorAll('.grid .card')].some(x=>!x.hidden))status.prepend(document.createTextNode('Nenhum modelo encontrado. '))}
}
for(const b of document.querySelectorAll('.bookmark'))b.onclick=()=>{const id=b.classList.contains('bookmark-enzo')?'enzo':'rafael';const result=ModelStore.dispatch({type:'toggle',field:'savedProfileIds',id});if(!result.persistent)show('Salvos','Armazenamento indisponível: a alteração pode se perder ao sair desta página.')};
document.querySelectorAll('.categories button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.categories button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));ModelStore.dispatch({type:'filters',value:{origin:'descobrir',applied:b.textContent!=='Todos',city:'',age:[18,100],height:[1,2.5],categories:b.textContent==='Todos'?[]:[b.textContent]}})});
ModelStore.subscribe(renderDiscovery);renderDiscovery();
