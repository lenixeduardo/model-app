const {chromium}=require('playwright');
const fs=require('fs');
const out=__dirname, base='http://127.0.0.1:8877';
const axe='/tmp/model-audit-deps/node_modules/axe-core/axe.min.js';
const routes=Array.from({length:9},(_,i)=>({n:String(i+3).padStart(2,'0'),folder:i===0?'MODEL_tela_03_V2':`MODEL_tela_${String(i+3).padStart(2,'0')}_V1`}));
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const report={date:new Date().toISOString(),browser:browser.version(),base,dpr:1,screens:[],root:null};
 for(const route of routes){
  const context=await browser.newContext({viewport:{width:390,height:844},deviceScaleFactor:1});
  const page=await context.newPage(); const result={...route,viewports:[],errors:[],requestsFailed:[],httpErrors:[],buttons:[],links:[],axe:null};
  page.on('pageerror',e=>result.errors.push(String(e)));
  page.on('console',m=>{if(m.type()==='error')result.errors.push(m.text())});
  page.on('requestfailed',r=>result.requestsFailed.push({url:r.url(),failure:r.failure()}));
  page.on('response',r=>{if(r.status()>=400)result.httpErrors.push({url:r.url(),status:r.status()})});
  const url=`${base}/${route.folder}/`;
  for(const [w,h] of [[375,812],[390,844],[430,932],[320,568],[768,1024],[1440,900]]){
   await page.setViewportSize({width:w,height:h});await page.goto(url,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
   const geometry=await page.evaluate(()=>{
    const bounds=e=>{const r=e.getBoundingClientRect();return{x:r.x,y:r.y,w:r.width,h:r.height}};
    const shown=e=>!!(e.getClientRects().length)&&getComputedStyle(e).visibility!=='hidden';
    const targets=[...document.querySelectorAll('button,a,input,select,[role=button],[role=tab],[role=radio]')].filter(shown).map(e=>({name:e.getAttribute('aria-label')||e.textContent.trim().slice(0,80)||e.id,tag:e.tagName,...bounds(e)}));
    const overlaps=[];for(let i=0;i<targets.length;i++)for(let j=i+1;j<targets.length;j++){const a=targets[i],b=targets[j];if(Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)>.5&&Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)>.5)overlaps.push([a.name,b.name])}
    return{document:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],horizontalOverflow:document.documentElement.scrollWidth>innerWidth,verticalOverflow:document.documentElement.scrollHeight>innerHeight,fonts:document.fonts.status,images:[...document.images].filter(shown).map(e=>({src:e.getAttribute('src'),loaded:e.complete&&e.naturalWidth>0,natural:[e.naturalWidth,e.naturalHeight],...bounds(e)})),smallTargets:targets.filter(e=>e.w<43.9||e.h<43.9),targetOverlaps:overlaps,headings:[...document.querySelectorAll('h1')].map(e=>e.textContent.trim())};
   });
   if([375,390,430].includes(w))await page.screenshot({path:`${out}/capturas/tela-${route.n}-${w}.png`,fullPage:true});
   result.viewports.push({viewport:[w,h],target:[375,390,430].includes(w),...geometry});
  }
  await page.setViewportSize({width:390,height:844});await page.goto(url,{waitUntil:'networkidle'});
  await page.addScriptTag({path:axe});const a=await page.evaluate(async()=>await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}}));
  result.axe={version:a.testEngine.version,violations:a.violations.map(v=>({id:v.id,impact:v.impact,description:v.description,help:v.help,nodes:v.nodes.map(n=>({html:n.html,target:n.target,failureSummary:n.failureSummary}))})),incomplete:a.incomplete.map(v=>({id:v.id,nodes:v.nodes.length})),passes:a.passes.length};
  const links=await page.locator('a[href]').evaluateAll(es=>es.map(e=>({label:e.getAttribute('aria-label')||e.textContent.trim(),href:e.href})));
  for(const link of links){if(link.href.startsWith(base)){const r=await page.request.get(link.href);result.links.push({...link,status:r.status()})}else result.links.push({...link,status:'external/not requested'})}
  const count=await page.locator('button').count();
  for(let i=0;i<count;i++){
   await page.goto(url,{waitUntil:'networkidle'});const b=page.locator('button').nth(i);if(!await b.isVisible()||!await b.isEnabled())continue;
   const name=await b.getAttribute('aria-label')||await b.innerText();
   try{
    await b.click({timeout:3000});await page.waitForTimeout(70);
    const state=await page.evaluate(()=>({dialog:[...document.querySelectorAll('dialog[open]')].map(e=>e.textContent.trim().slice(0,250)),pressed:[...document.querySelectorAll('[aria-pressed=true],[aria-selected=true]')].map(e=>e.getAttribute('aria-label')||e.textContent.trim()),active:document.activeElement?.outerHTML.slice(0,180)}));
    let dialogCheck=null;if(state.dialog.length){await page.keyboard.press('Escape');dialogCheck={escapeClosed:await page.locator('dialog[open]').count()===0,focusReturned:await b.evaluate(e=>e===document.activeElement).catch(()=>false)}}
    result.buttons.push({index:i,name,click:'ok',state,dialogCheck});
   }catch(e){result.buttons.push({index:i,name,click:'failed',error:String(e)})}
  }
  report.screens.push(result);await context.close();fs.writeFileSync(`${out}/browser.json`,JSON.stringify(report,null,2));
  console.log(route.n,JSON.stringify({errors:result.errors.length,http:result.httpErrors.length,axe:result.axe.violations.length,buttons:result.buttons.length,targetOverflow:result.viewports.filter(v=>v.target&&(v.horizontalOverflow||v.verticalOverflow)).length}));
 }
 const p=await browser.newPage();await p.goto(base);report.root={title:await p.title(),directoryListing:await p.locator('h1').innerText(),url:p.url()};await browser.close();fs.writeFileSync(`${out}/browser.json`,JSON.stringify(report,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
