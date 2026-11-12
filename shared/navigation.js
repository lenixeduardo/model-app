(function(root){
  const routes={login:'MODEL_tela_01_V1/',descobrir:'MODEL_tela_02_V1/',swipe:'MODEL_tela_03_V2/','perfil-modelo':'MODEL_tela_04_V1/',portfolio:'MODEL_tela_05_V1/',chat:'MODEL_tela_06_V1/',castings:'MODEL_tela_07_V1/',filtros:'MODEL_tela_08_V1/',salvos:'MODEL_tela_09_V1/','meu-perfil':'MODEL_tela_10_V1/',notificacoes:'MODEL_tela_11_V1/'};
  const current=typeof document==='undefined'?null:document.currentScript;
  const base=current?new URL('../',current.src):null;
  function getRoutePath(route){if(!Object.hasOwn(routes,route))throw new Error('Rota desconhecida: '+route);return base?new URL(routes[route],base).pathname:routes[route]}
  function goTo(route,options={}){const url=new URL(getRoutePath(route),location.origin);if(options.returnTo){getRoutePath(options.returnTo);url.searchParams.set('returnTo',options.returnTo)}location.assign(url.href)}
  function goBack(fallback,allowed){const target=new URLSearchParams(location.search).get('returnTo');goTo(target&&allowed.includes(target)?target:fallback)}
  const api={getRoutePath,goTo,goBack};if(typeof module!=='undefined')module.exports=api;root.ModelNavigation=api;
})(typeof window==='undefined'?globalThis:window);
