import fs from 'node:fs';
const source = fs.readFileSync(new URL('generate.py', import.meta.url), 'utf8');
const data = {};
for (const key of ['policies','trial','other','ages','schedule','pricing','dress','locations']) {
  const raw = source.match(new RegExp(`^${key} = (\\[.*\\])$`, 'm'))[1];
  data[key] = Function(`return ${raw}`)();
}
const section = (title, facts, id) => `<section class="info" id="${id}"><h2>${title}</h2><div>${facts.map(f=>`<p>${f}</p>`).join('')}</div></section>`;
const template = source.match(/return f'''([\s\S]*?)'''/)[1];
const page = (name,title,subtitle,content) => {
 const nav = [['Home','index.html'],['Programs','programs.html'],['Contact Us','contact.html']].map(([label,url])=>`<a href="${url}"${label===name?' aria-current="page"':''}>${label}</a>`).join('');
 return template.replace(/\{(name|title|subtitle|content|nav)\}/g,(_,key)=>({name,title,subtitle,content,nav})[key]);
};
let home = source.match(/home = '''([\s\S]*?)'''/)[1];
home += section('Your first class is on us',data.trial,'trial-policy') + section('General policies',data.policies,'general-policies') + section('Beyond the classroom',data.other,'other');
home += '<aside class="reference-note"><h2>What families can be told today</h2><p>Reference screenshot note: 10 FAQs · 2 documents are counted separately under Knowledge sources above; Ready facts only counts approved fact answers.</p></aside>';
let programs = '<div class="program-grid">';
for (const [num,style,age,price,days] of [['01','Ballet','3–18','$200','Monday & Wednesday · 4–5 PM'],['02','Jazz','6–18','$180','Friday · 4–5 PM'],['03','Hip-hop','6–18','$150','Tuesday & Thursday · 5–6 PM'],['04','Contemporary','8–18','$190','Saturday · 10–11 AM']]) programs += `<article class="program"><span class="program-number">${num} / DANCE</span><h2>${style}</h2><p>Ages ${age}</p><p>${days}</p><div class="price">${price}<small> / month</small></div></article>`;
programs += '</div>' + section('Programs & ages',data.ages,'programs-ages') + section('Schedule',data.schedule,'schedule') + section('Pricing',data.pricing,'pricing') + section('Dress code',data.dress,'dress-code');
const contact = source.match(/contact = '(<section[\s\S]*?)' \+ section/)[1] + section('Locations',data.locations,'locations') + section('Studio hours',data.schedule.slice(0,3),'hours') + section('Plan your trial',data.trial,'trial-policy');
const pages = [['index.html','Home','Every dancer starts<br>with a <em>first step.</em>','A welcoming place for young dancers to move, discover, and grow.',home],['programs.html','Programs','Find your kind<br>of <em>movement.</em>','Four dance styles. A world of possibility. Explore your next step.',programs],['contact.html','Contact Us','Let’s get<br><em>moving.</em>','Visit our Springfield studio and start your dance journey.',contact]];
const all = pages.map(([file,...args])=>{const html=page(...args);fs.writeFileSync(new URL(`dist/${file}`,import.meta.url),html);return html;}).join('');
for (const fact of Object.values(data).flat()) if(!all.includes(fact)) throw Error(`Missing fact: ${fact}`);
for (const [file] of pages) {
 const html=fs.readFileSync(new URL(`dist/${file}`,import.meta.url),'utf8');
 for (const [,href] of html.matchAll(/href="([^"#]+)(?:#[^"]*)?"/g)) if(!fs.existsSync(new URL(`dist/${href}`,import.meta.url))) throw Error(`Broken link ${href}`);
}
console.log(`Verified 3 pages, navigation, and all ${Object.values(data).flat().length} supplied studio facts.`);
