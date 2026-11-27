import base64
S='/tmp/claude-0/-home-user-Querida-psiquiatria/dd765379-9e4a-53e2-ba7e-a1a50ea79544/scratchpad/'
U='../originais/'
f={n:'data:font/woff2;base64,'+base64.b64encode(open(S+'woff/%s.woff2'%n,'rb').read()).decode() for n in ['Roca','Cretina','PoppinsR','PoppinsB']}
ORD={'61742049':'01','56d32a89':'02','fa5b56d3':'03','c81c5614':'04','473a1c4e':'05','edccca27':'06'}
img=lambda k:U+ORD[k]+'.png'
CSS=f'''@font-face{{font-family:R;src:url({f['Roca']})}}@font-face{{font-family:C;src:url({f['Cretina']})}}
@font-face{{font-family:P;src:url({f['PoppinsR']});font-weight:400}}@font-face{{font-family:P;src:url({f['PoppinsB']});font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
#post{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P;color:#4a1c2e;background:#F7E6B6}}
.a{{position:absolute}}
.R{{font-family:R;line-height:.98;letter-spacing:-.008em;-webkit-text-stroke:2px currentColor}}
.C{{font-family:C;line-height:1;-webkit-text-stroke:1.5px currentColor}}
.ph{{position:absolute;overflow:hidden}}.ph img{{position:absolute;display:block;filter:sepia(.18) saturate(.9) contrast(.95) brightness(1.03)}}
.ph::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,214,150,.18),rgba(244,195,190,.18));mix-blend-mode:soft-light}}
.selo{{position:absolute;background:radial-gradient(ellipse 70% 60% at 40% 35%,#fbd6d1,transparent 70%),#F4C3BE;
 -webkit-mask:radial-gradient(circle 17px at 50% 50%,transparent 98%,#000) -26px -26px/52px 52px,linear-gradient(#000,#000) center/calc(100% - 36px) calc(100% - 36px) no-repeat;
 filter:drop-shadow(0 10px 18px rgba(120,70,20,.25))}}
.ouro{{background:radial-gradient(ellipse 60% 50% at 25% 20%,#fbefc4,transparent 70%),radial-gradient(ellipse 60% 55% at 85% 90%,#efcf7c,transparent 70%),#F5DE9C}}
.pil{{background:#F4C3BE;color:#4a1c2e;border-radius:40px;padding:8px 30px 12px;font-size:32px;display:inline-block}}
.rod{{position:absolute;left:0;right:0;bottom:46px;text-align:center;font-size:20px;letter-spacing:.03em;text-transform:uppercase;z-index:40;color:#4a1c2e}}
.rod b{{font-weight:700}}
.tex{{position:absolute;inset:0;z-index:50;pointer-events:none;opacity:.45;mix-blend-mode:multiply;background:repeating-linear-gradient(0deg,rgba(0,0,0,.035) 0 1px,transparent 1px 4px),repeating-linear-gradient(90deg,rgba(0,0,0,.03) 0 1px,transparent 1px 4px)}}
.grao{{position:absolute;inset:0;z-index:51;pointer-events:none;mix-blend-mode:soft-light;background:radial-gradient(circle,rgba(0,0,0,.18) 0 1.1px,transparent 1.5px) 0 0/5px 5px}}
.faixa{{position:absolute;left:0;right:0;bottom:0;height:240px;z-index:30;background:#F7E6B6;clip-path:polygon(0 22%,8% 16%,18% 19%,30% 11%,42% 16%,55% 8%,68% 14%,80% 6%,91% 12%,100% 8%,100% 100%,0 100%)}}
'''
def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post">{body}<div class="rod">Dra Mariana Aquino | <b>Psiquiatria Infantil</b></div><div class="tex"></div><div class="grao"></div></div></body></html>'
glow=lambda pos,col:f'<div class="a" style="inset:0;z-index:2;background:radial-gradient(ellipse 110px 70px at 300px 0,{col} 0 60%,rgba(0,0,0,0) 100%),radial-gradient(ellipse 360px 300px at 0 0,{col} 0 75%,rgba(0,0,0,0) 100%),radial-gradient(ellipse 260px 260px at 100% 88%,{col} 0 60%,rgba(0,0,0,0) 100%)"></div>'
P={}
# 1 capa
P[1]=page(f'''<div class="ph" style="inset:0"><img src="{img('61742049')}" style="left:0;top:0;width:1080px"></div>
{glow("0 0","#FDECC0")}
<div class="selo" style="left:555px;top:200px;width:468px;height:832px;z-index:5"></div>
<div class="a" style="left:555px;top:200px;width:468px;height:832px;z-index:6;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 40px">
 <div class="R" style="font-size:66px">Como fazer<br>a médica<br>do seu filho</div>
 <div class="C" style="font-size:118px;color:#9B506E;-webkit-text-stroke:2px #9B506E;margin:10px 0 6px">surtar</div>
 <div class="R" style="font-size:72px">em <span style="font-size:110px">10</span><br>dias?</div>
</div>
<div class="a pil" style="right:70px;top:1050px;z-index:31;transform:rotate(-3deg);background:#4a1c2e;color:#FCC8BF;font-size:28px">arrasta pro lado →</div>
<div class="faixa"></div>''')
# 2-5 erros
erros=[('56d32a89','Dar um celular próprio<br>aos <span style="font-size:1.15em">6</span> anos',"“porque todos os amiguinhos têm”","50% 40%"),
       ('fa5b56d3','Dar o remédio só na<br>véspera da prova',"e jurar que “não funciona”","50% 35%"),
       ('c81c5614','Parar o remédio sozinho',"porque ele “já está bem”","50% 30%"),
       ('473a1c4e','“Lá em casa todo mundo<br>dorme tarde,',"é o ritmo da família”","50% 35%")]
for i,(k,t1,t2,pos) in enumerate(erros):
    P[i+2]=page(f'''<div class="ph" style="left:0;right:0;top:0;height:900px"><img src="../fotos-limpas/0{i+2}.png" style="left:-12px;top:-8px;width:1104px"></div>
<div class="a ouro" style="left:0;right:0;top:860px;bottom:0;z-index:3;clip-path:polygon(0 5%,10% 2%,22% 6%,35% 1%,48% 5%,60% 0,74% 5%,86% 1%,100% 4%,100% 100%,0 100%)"></div>
<div class="a" style="left:70px;right:70px;top:925px;z-index:6;text-align:center">
 <div class="R" style="font-size:66px;line-height:1.02">{t1}</div>
 <div class="C" style="font-size:62px;color:#9B506E;-webkit-text-stroke:1.3px #9B506E;margin-top:16px;line-height:1.1">{t2}</div></div>''')
# 6 final
P[6]=page(f'''<div class="ph" style="inset:0"><img src="{img('edccca27')}" style="left:0;top:0;width:1080px"></div>
{glow("0 0","#F2D9A6")}
<div class="selo" style="left:436px;top:420px;width:624px;height:520px;z-index:5"></div>
<div class="a" style="left:436px;top:420px;width:624px;height:520px;z-index:6;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 40px">
 <div class="R" style="font-size:74px">Quantas dessas<br>você já <span class="C" style="color:#9B506E;-webkit-text-stroke:1.8px #9B506E;font-size:96px">fez?</span></div>
 <div class="P" style="font-size:32px;margin-top:26px;font-weight:700">me conta nos comentários</div>
 <div class="P" style="font-size:28px;margin-top:4px">(prometo tentar não surtar)</div></div>
<div class="faixa"></div>''')
for k,v in P.items(): open(S+'filme/s%d.html'%k,'w').write(v)
