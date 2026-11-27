import base64
S='/tmp/claude-0/-home-user-Querida-psiquiatria/dd765379-9e4a-53e2-ba7e-a1a50ea79544/scratchpad/'
O='../originais/'
f={n:'data:font/woff2;base64,'+base64.b64encode(open(S+'woff/%s.woff2'%n,'rb').read()).decode() for n in ['Roca','Cretina','PoppinsR','PoppinsB']}
CSS=f'''@font-face{{font-family:R;src:url({f['Roca']})}}@font-face{{font-family:C;src:url({f['Cretina']})}}
@font-face{{font-family:P;src:url({f['PoppinsR']});font-weight:400}}@font-face{{font-family:P;src:url({f['PoppinsB']});font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
#post{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P;color:#4a1c2e}}
.a{{position:absolute}}.bg{{position:absolute;inset:0;width:1080px;height:1350px}}
.R{{font-family:R;line-height:1;letter-spacing:-.005em;-webkit-text-stroke:1.6px currentColor}}
.C{{font-family:C;line-height:1;-webkit-text-stroke:1.4px currentColor;color:#9B506E}}
.grao{{position:absolute;inset:0;z-index:50;pointer-events:none;mix-blend-mode:soft-light;opacity:.7;background:radial-gradient(circle,rgba(0,0,0,.16) 0 1px,transparent 1.4px) 0 0/5px 5px}}
.tom{{position:absolute;inset:0;z-index:49;pointer-events:none;background:#F4C3BE;mix-blend-mode:soft-light;opacity:.18}}
.selo{{position:absolute;background:radial-gradient(ellipse 70% 60% at 40% 35%,#fbd6d1,transparent 70%),#F4C3BE;
 -webkit-mask:radial-gradient(circle 13px at 50% 50%,transparent 98%,#000) -20px -20px/40px 40px,linear-gradient(#000,#000) center/calc(100% - 28px) calc(100% - 28px) no-repeat}}
.bal{{position:absolute;left:38px;right:16px;top:872px;height:465px;background:#F8EFEC;border-radius:200px/150px;border-top:7px solid #F4C3BE;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 70px;font-size:66px;line-height:1.22;letter-spacing:-.01em}}
.bal b{{font-weight:700}}
'''
pg=lambda n,body:f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post"><img class="bg" src="{O}{n}.png">{body}<div class="tom"></div><div class="grao"></div></div></body></html>'
P={}
P[1]=pg('01','''<div class="selo" style="left:555px;top:225px;width:440px;height:800px"></div>
<div class="a" style="left:555px;top:225px;width:440px;height:800px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
<div class="R" style="font-size:76px;line-height:1.05">Como<br>fazer a<br>médica<br>do seu<br>filho</div>
<div class="C" style="font-size:104px;margin:8px 0">surtar</div>
<div class="R" style="font-size:76px;line-height:1.05">em<br>10 dias?</div></div>''')
txt={2:'Dar um celular próprio aos 6 anos <b>“porque todos os amiguinhos têm”</b>',
     3:'Dar o remédio só na véspera da prova e jurar que <b>“não funciona”</b>',
     4:'Parar o remédio sozinho porque ele <b>“já está bem”</b>',
     5:'<b>“Lá em casa todo mundo dorme tarde, é o ritmo da família”</b>'}
for i,t in txt.items(): P[i]=pg('%02d'%i,f'<div class="bal"><div>{t}</div></div>')
P[6]=pg('06','''<div class="a" style="left:425px;top:500px;width:650px;height:345px;background:#FCEAC6;border-radius:60px;box-shadow:0 0 40px 34px #FCEAC6"></div>
<div class="a" style="left:445px;top:505px;display:flex;flex-direction:column;align-items:flex-start;gap:12px">
<div class="R" style="background:#F4C3BE;border-radius:40px;padding:6px 34px 16px;font-size:76px">Quantas dessas</div>
<div class="R" style="background:#F4C3BE;border-radius:40px;padding:6px 34px 16px;font-size:76px;margin-left:10px">você já <span class="C" style="font-size:92px">fez?</span></div>
<div style="font-size:38px;font-weight:700;margin:8px 0 0 30px">me conta nos comentários</div>
<div style="font-size:32px;margin-left:44px">(prometo tentar não surtar)</div></div>''')
for k,v in P.items(): open(S+'sutil/s%d.html'%k,'w').write(v)
