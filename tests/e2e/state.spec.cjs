const { test, expect } = require('@playwright/test');
test('casting salvo aparece nos salvos', async ({page}) => {
  await page.goto('/MODEL_tela_07_V1/');
  await page.getByRole('button',{name:'Salvar Campanha Inverno 2025'}).click();
  await page.goto('/MODEL_tela_09_V1/');
  await page.getByRole('tab',{name:'Castings'}).click();
  await expect(page.getByRole('heading',{name:'Campanha Inverno 2025'})).toBeVisible();
});
test('favorito de Enzo é compartilhado entre descoberta, perfil e salvos', async ({page}) => {
  await page.goto('/MODEL_tela_03_V2/');
  await expect(page.locator('.favorite')).toHaveAttribute('aria-pressed','true');
  await page.locator('.favorite').click();
  await page.goto('/MODEL_tela_04_V1/');
  await expect(page.locator('#save')).toHaveAttribute('aria-pressed','false');
  await page.goto('/MODEL_tela_09_V1/');
  await expect(page.getByText('Enzo, 26')).toHaveCount(0);
  await page.goto('/MODEL_tela_04_V1/');
  await page.locator('#save').click();
  await page.goto('/MODEL_tela_09_V1/');
  await expect(page.getByText('Enzo, 26')).toBeVisible();
});

test('último salvo pode ser removido e desfeito após reload', async ({page}) => {
 await page.goto('/MODEL_tela_09_V1/');
 for(const name of ['Gabriel','Rafael','Theo']) await page.getByRole('button',{name:new RegExp('Remover '+name)}).click();
 await page.reload(); await page.getByRole('button',{name:/Remover Enzo/}).click();
 await expect(page.getByText('Nenhum modelo salvo.')).toBeVisible();
 await page.getByRole('button',{name:'Desfazer'}).click(); await expect(page.getByText('Enzo, 26')).toBeVisible();
});
test('filtro de cidade e limpeza retornam à origem', async ({page}) => {
 await page.goto('/MODEL_tela_08_V1/?returnTo=castings'); await page.locator('#city').fill('cidade inexistente');
 await page.getByRole('button',{name:'Aplicar filtros'}).click(); await page.getByRole('link',{name:'Voltar aos castings'}).click();
 await expect(page.getByText('Nenhum casting encontrado.',{exact:false})).toBeVisible(); await page.getByRole('button',{name:'Limpar filtros'}).click(); await expect(page.getByRole('button',{name:'Detalhes: Marca Esportiva'})).toBeVisible();
});
test('mensagem local usa texto seguro e persiste',async({page})=>{
 await page.goto('/MODEL_tela_06_V1/'); await page.locator('#message').fill('<img src=x onerror=alert(1)>'); await page.locator('#composer').evaluate(form=>form.requestSubmit()); await page.reload(); await expect(page.getByText('<img src=x onerror=alert(1)>')).toBeVisible();
});
test('estado inválido recupera defaults e IDs estranhos são removidos',async({page})=>{
 await page.goto('/MODEL_tela_09_V1/'); await page.evaluate(()=>localStorage.setItem('model:state:v1','{')); await page.reload(); await expect(page.getByText('Enzo, 26')).toBeVisible();
 await page.evaluate(()=>localStorage.setItem('model:state:v1',JSON.stringify({schemaVersion:1,savedProfileIds:['inexistente'],filters:{age:[-5,500],height:[3,4],fee:[-1,999999],distance:'999'}}))); await page.reload();
 const state=await page.evaluate(()=>ModelStore.getState()); expect(state.savedProfileIds).toEqual([]); expect(state.filters.age).toEqual([18,35]); expect(state.filters.distance).toBe('50');
});
test('filtro de modelos preserva origem e não presume metadados ausentes',async({page})=>{
 await page.goto('/MODEL_tela_08_V1/?returnTo=descobrir'); await page.locator('#city').fill('Rio de Janeiro');
 await page.getByRole('button',{name:'Aplicar filtros'}).click(); await page.getByRole('link',{name:'Voltar à descoberta'}).click();
 await expect(page.locator('.card.gabriel')).toBeVisible(); await expect(page.locator('.card.enzo')).toBeHidden();
 await page.reload(); await expect(page.locator('.card.enzo')).toBeHidden(); await page.getByRole('button',{name:'Limpar filtros'}).click(); await expect(page.locator('.card.enzo')).toBeVisible();
});
test('armazenamento bloqueado mantém ação na página e informa limitação',async({page})=>{
 await page.addInitScript(()=>{Object.defineProperty(window,'localStorage',{get(){throw new Error('bloqueado')}})});
 await page.goto('/MODEL_tela_04_V1/'); await page.locator('#save').click(); await expect(page.locator('#save')).toHaveAttribute('aria-pressed','false'); await expect(page.locator('#announcement')).toContainText('Armazenamento indisponível');
});
test('edição e leitura persistem no dispositivo',async({page})=>{
 await page.goto('/MODEL_tela_10_V1/'); await page.locator('#edit').click(); await page.locator('input[name=name]').fill('Nome local'); await page.getByRole('button',{name:'Salvar localmente'}).click(); await page.reload(); await expect(page.locator('#identity-name')).toContainText('Nome local');
 await page.goto('/MODEL_tela_11_V1/'); await page.locator('.notification').first().click(); await page.getByRole('button',{name:'Marcar como lida',exact:true}).click(); await page.reload(); await expect(page.locator('.notification').first()).toHaveAttribute('data-read','lida');
});
test('storage event atualiza assinantes em outra aba',async({context,page})=>{
 await page.goto('/MODEL_tela_04_V1/'); const second=await context.newPage(); await second.goto('/MODEL_tela_03_V2/'); await second.locator('.favorite').click(); await expect(page.locator('#save')).toHaveAttribute('aria-pressed','false');
});
test('perfil ignorado permanece ignorado ao recarregar e pode ser restaurado',async({page})=>{
 await page.goto('/MODEL_tela_03_V2/'); await page.locator('.dismiss').click(); await page.reload(); await expect(page.locator('.empty-state')).toBeVisible(); await page.locator('.undo').click(); await expect(page.locator('.details')).toBeVisible(); await page.reload(); await expect(page.locator('.details')).toBeVisible();
});
test('edição de nome preserva disponibilidade local',async({page})=>{
 await page.goto('/MODEL_tela_10_V1/'); await page.getByRole('button',{name:'Disponibilidade',exact:false}).click(); await page.getByLabel('Disponibilidade local').selectOption('Disponível'); await page.getByRole('button',{name:'Salvar localmente'}).click();
 await page.locator('#edit').click(); await page.locator('input[name=name]').fill('Novo nome'); await page.getByRole('button',{name:'Salvar localmente'}).click(); expect(await page.evaluate(()=>ModelStore.getState().profile.availability)).toBe('Disponível');
});
test('notificações em duas abas preservam leituras e atualizam lista',async({context,page})=>{
 await page.goto('/MODEL_tela_11_V1/'); const second=await context.newPage(); await second.goto('/MODEL_tela_11_V1/');
 await page.locator('.notification').nth(0).click(); await page.getByRole('button',{name:'Marcar como lida',exact:true}).click();
 await expect(second.locator('.notification').nth(0)).toHaveAttribute('data-read','lida'); await second.locator('.notification').nth(1).click(); await second.getByRole('button',{name:'Marcar como lida',exact:true}).click();
 await expect(page.locator('.notification').nth(1)).toHaveAttribute('data-read','lida'); expect((await second.evaluate(()=>ModelStore.getState())).notificationReadStates.slice(0,2)).toEqual(['lida','lida']);
});
test('salvos, chat, castings e perfil refletem atualizações de outra aba',async({context,page})=>{
 await page.goto('/MODEL_tela_09_V1/'); const second=await context.newPage(); await second.goto('/MODEL_tela_04_V1/'); await second.locator('#save').click(); await expect(page.getByText('Enzo, 26')).toHaveCount(0);
 await page.goto('/MODEL_tela_06_V1/'); await second.goto('/MODEL_tela_06_V1/'); await second.locator('#message').fill('Mensagem de outra aba'); await second.locator('#composer').evaluate(f=>f.requestSubmit()); await expect(page.getByText('Mensagem de outra aba')).toBeVisible();
 await page.goto('/MODEL_tela_07_V1/'); await second.goto('/MODEL_tela_07_V1/'); await second.getByRole('button',{name:'Salvar Marca Esportiva'}).click(); await expect(page.getByRole('button',{name:'Salvar Marca Esportiva'})).toHaveAttribute('aria-pressed','true');
 await page.goto('/MODEL_tela_10_V1/'); await second.goto('/MODEL_tela_10_V1/'); await second.locator('#edit').click(); await second.locator('input[name=name]').fill('Perfil de outra aba'); await second.getByRole('button',{name:'Salvar localmente'}).click(); await expect(page.locator('#identity-name')).toContainText('Perfil de outra aba');
});
test('desfazer retorna foco ao item restaurado',async({page})=>{
 await page.goto('/MODEL_tela_09_V1/'); await page.getByRole('button',{name:/Remover Enzo/}).click(); await page.getByRole('button',{name:'Desfazer'}).click(); await expect(page.getByRole('button',{name:/Remover Enzo/})).toBeFocused();
});
test('ações em lote informam bloqueio do armazenamento e política de reload',async({page})=>{
 await page.addInitScript(()=>Object.defineProperty(window,'localStorage',{get(){throw Error('bloqueado')}})); await page.goto('/MODEL_tela_11_V1/'); await page.locator('.manage').first().click(); await expect(page.locator('dialog')).not.toContainText('restauradas ao recarregar');
 await page.getByRole('button',{name:'Marcar todas como lidas'}).click(); await expect(page.locator('#read-state')).toContainText('Armazenamento indisponível'); await page.getByRole('button',{name:'Restaurar estado inicial'}).click(); await expect(page.locator('#read-state')).toContainText('Armazenamento indisponível');
});
