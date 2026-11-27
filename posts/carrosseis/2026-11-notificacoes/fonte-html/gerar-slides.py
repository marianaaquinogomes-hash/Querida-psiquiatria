import json,base64
S='/tmp/claude-0/-home-user-Querida-psiquiatria/dd765379-9e4a-53e2-ba7e-a1a50ea79544/scratchpad/'
M=json.load(open(S+'memes.json'))
m=lambda i:M[i]['d']
f={n:'data:font/woff2;base64,'+base64.b64encode(open(S+'woff/%s.woff2'%n,'rb').read()).decode() for n in ['Roca','Cretina','PoppinsR','PoppinsB']}
CSS=f'''@font-face{{font-family:R;src:url({f['Roca']})}}@font-face{{font-family:C;src:url({f['Cretina']})}}
@font-face{{font-family:P;src:url({f['PoppinsR']});font-weight:400}}@font-face{{font-family:P;src:url({f['PoppinsB']});font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
#post{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P;color:#4a1c2e}}
.rosa{{background:radial-gradient(ellipse 55% 40% at 25% 20%,#fbd8d2,transparent 70%),radial-gradient(ellipse 55% 45% at 80% 85%,#f3b8b0,transparent 70%),#F6C6BF}}
.creme{{background:radial-gradient(ellipse 60% 45% at 30% 25%,#fbf9f2,transparent 70%),radial-gradient(ellipse 60% 45% at 75% 80%,#ebe5d6,transparent 70%),#F3EFE4}}
#post.vinho{{color:#FCC8BF;background:radial-gradient(ellipse 55% 40% at 22% 25%,#6e3048,transparent 70%),radial-gradient(ellipse 55% 45% at 80% 78%,#3d1526,transparent 70%),#55223a}}
.tex{{position:absolute;inset:0;z-index:30;pointer-events:none;opacity:.5;mix-blend-mode:multiply;background:repeating-linear-gradient(0deg,rgba(0,0,0,.035) 0 1px,transparent 1px 4px),repeating-linear-gradient(90deg,rgba(0,0,0,.03) 0 1px,transparent 1px 4px)}}
.tex2{{position:absolute;inset:0;z-index:31;pointer-events:none;opacity:.3;mix-blend-mode:overlay;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E")}}
.grao{{position:absolute;inset:0;z-index:32;pointer-events:none;mix-blend-mode:soft-light;background:radial-gradient(circle,rgba(0,0,0,.18) 0 1.1px,transparent 1.5px) 0 0/5px 5px}}
.a{{position:absolute}}
.R{{font-family:R;line-height:.96;letter-spacing:-.01em;-webkit-text-stroke:2px currentColor}}
.C{{font-family:C;line-height:1;-webkit-text-stroke:1.5px currentColor;letter-spacing:0}}
.P{{font-family:P;letter-spacing:-.02em;line-height:1.28}}
.c{{text-align:center}}
.ph{{overflow:hidden;position:absolute}}.ph img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.8) sepia(.12) contrast(.95) brightness(1.04)}}
.ph::after{{content:"";position:absolute;inset:0;background:#f2b3ad;mix-blend-mode:multiply;opacity:.22}}
.rod{{position:absolute;left:0;right:0;bottom:52px;text-align:center;font-size:20px;letter-spacing:.03em;text-transform:uppercase;z-index:25}}
.rod b{{font-weight:700}}
.pil{{background:#5a2538;color:#FCC8BF;border-radius:44px;font-size:38px;padding:14px 40px 18px;text-align:center;letter-spacing:-.02em}}
'''
def page(cls,body,rodcor='#4a1c2e'):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post" class="{cls}">{body}<div class="rod" style="color:{rodcor}">Dra Mariana Aquino | <b>Psiquiatria Infantil</b></div><div class="tex"></div><div class="tex2"></div><div class="grao"></div></div></body></html>'
P={}
# 2 — faixa de foto entre o texto e o título gigante (ref. Priscila 2)
P[2]=page('rosa',f'''
<div class="a P" style="left:90px;top:150px;width:900px;font-size:44px">180 jovens, um teste de atenção e</div>
<div class="ph" style="left:0;right:0;top:290px;height:330px"><img src="{m(3)}" style="object-position:50% 45%;transform:scale(1.35);transform-origin:78% 55%"></div>
<div class="a R" style="left:80px;top:650px;font-size:122px;line-height:.92">notificações<br><span class="C" style="font-size:112px;color:#9B506E;-webkit-text-stroke:1.5px #9B506E">pipocando</span> na tela.</div>
<div class="a P" style="left:90px;top:1010px;width:900px;font-size:34px">Eles achavam que os alertas vinham do próprio celular. Os pesquisadores mediram a velocidade das respostas e até <b>a dilatação da pupila.</b></div>
<div class="a P" style="left:90px;top:1170px;font-size:26px;font-style:italic;opacity:.8">Fournier et al., Computers in Human Behavior, 2026</div>''')
# 3 — três quadros + caixa alta + cursiva (ref. Priscila 5)
fr=''.join(f'<div class="ph" style="left:{60+i*325}px;top:330px;width:310px;height:230px;outline:5px solid #3a2a2e"><img src="{m(13)}" style="object-position:{40+i*10}% {30+i*6}%;transform:scale({1+i*.06})"></div>' for i in range(3))
P[3]=page('creme',f'''
<div class="a c R" style="left:0;right:0;top:220px;font-size:50px;color:#B36978;-webkit-text-stroke:0;letter-spacing:.02em">A CADA NOTIFICAÇÃO, O CÉREBRO</div>{fr}
<div class="a c R" style="left:0;right:0;top:610px;font-size:150px;line-height:.92">FICA MAIS<br>LENTO POR</div>
<div class="a c C" style="left:0;right:0;top:850px;font-size:170px;color:#B36978;-webkit-text-stroke:2px #B36978">~7 segundos.</div>
<div class="a c P" style="left:120px;right:120px;top:1080px;font-size:36px">E isso sem nem abrir a mensagem:<br><b>bastou ver o ícone do app aparecer.</b></div>''')
# 4 — título cursivo + recortes ovais + texto sublinhado (ref. Camila 2)
ov=lambda i,css,pos: f'<div class="ph" style="{css};border-radius:48% 52% 45% 55%/55% 45% 55% 45%;z-index:5"><img src="{m(i)}" style="object-position:{pos}"></div>'
P[4]=page('vinho',f'''
<div class="a c C" style="left:60px;right:60px;top:200px;font-size:104px;line-height:1.1;color:#FCC8BF;-webkit-text-stroke:2px #FCC8BF;transform:rotate(-3deg)">Nem precisa ser<br>o seu celular.</div>
{ov(16,"left:45px;top:560px;width:220px;height:280px;transform:rotate(-8deg)","40% 40%")}
{ov(17,"right:55px;top:870px;width:210px;height:260px;transform:rotate(7deg)","50% 40%")}
<div class="a P" style="left:300px;right:90px;top:600px;font-size:40px;color:#F7EFEA">Notificações que não eram dos participantes também atrapalharam.</div>
<div class="a P" style="left:110px;right:300px;top:860px;font-size:40px;color:#F7EFEA;font-weight:700;text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:8px">O cérebro aprendeu que aquele “plim” importa e reage no automático.</div>''','#F7EFEA')
# 5 — foto inteira + título com palavra destacada + linhas (ref. Priscila 4)
P[5]=page('vinho',f'''
<div class="ph" style="inset:0"><img src="{m(9)}" style="object-position:50% 30%;filter:saturate(.7) brightness(.72) contrast(.95)"></div>
<div class="a P" style="left:100px;top:300px;font-size:40px;color:#F7EFEA;width:700px">Quanto mais a gente espera aquela notificação,</div>
<div class="a R" style="left:90px;top:430px;font-size:170px;color:#F7EFEA;-webkit-text-stroke:2px #F7EFEA;line-height:.9">mais ela<br><span class="C" style="color:#FCC8BF;-webkit-text-stroke:2px #FCC8BF;font-size:170px">distrai</span> <span style="display:inline-block;width:200px;height:3px;background:#F7EFEA;vertical-align:middle"></span></div>
<div class="a" style="left:100px;top:880px;width:330px;height:3px;background:#FCC8BF"></div>
<div class="a P" style="left:470px;right:80px;top:850px;font-size:36px;color:#F7EFEA">Alertas vistos como mais importantes ou agradáveis deixaram o cérebro <b>ainda mais lento.</b></div>
<div class="a P" style="left:100px;top:1100px;background:#FCC8BF;color:#4a1c2e;font-size:32px;padding:6px 22px 10px;transform:rotate(-2deg)">tipo a curtida da foto que você acabou de postar</div>''','#F7EFEA')
# 6 — tabela de duas colunas com fita (ref. Camila 1)
fita=lambda t: f'<div class="P c" style="background:#F3EFE4;color:#4a1c2e;font-size:40px;line-height:1.15;padding:16px 20px;clip-path:polygon(0 4%,97% 0,100% 18%,96% 36%,100% 55%,97% 75%,100% 100%,2% 97%)">{t}</div>'
P[6]=page('rosa',f'''
<div class="a c R" style="left:60px;right:60px;top:160px;font-size:86px">Não é só o tempo de tela.<br>É quantas vezes a tela <span class="C" style="color:#9B506E;-webkit-text-stroke:2px #9B506E;font-size:110px">chama.</span></div>
<div class="a" style="left:120px;right:120px;top:520px;display:grid;grid-template-columns:1fr 1fr;column-gap:70px">
 <div>{fita("O que mais<br>distraiu")}<div class="P c" style="font-size:42px;padding:34px 0 30px;border-bottom:2px solid #4a1c2e">Receber mais<br>notificações</div><div class="P c" style="font-size:42px;padding:30px 0">Checar mais<br>o celular</div></div>
 <div>{fita("Quase não fez<br>diferença")}<div class="P c" style="font-size:42px;padding:34px 0 30px">Total de horas<br>no aparelho</div></div>
</div>
<div class="a" style="left:539px;top:520px;width:2px;height:560px;background:#4a1c2e"></div>''')
# 7 — pílulas empilhadas (designer)
P[7]=page('creme',f'''
<div class="a c P" style="left:0;right:0;top:220px;font-size:40px">Num dia comum, em média:</div>
<div class="a" style="left:160px;right:160px;top:310px;display:flex;flex-direction:column;gap:6px">
 <div class="pil" style="font-size:46px">~7h no celular</div><div class="pil" style="font-size:46px">+150 notificações</div><div class="pil" style="font-size:46px">+100 checadas no celular</div></div>
<div class="a c R" style="left:0;right:0;top:670px;font-size:120px">Faz a <span class="C" style="color:#9B506E;-webkit-text-stroke:2px #9B506E">conta:</span></div>
<div class="a c P" style="left:110px;right:110px;top:830px;font-size:40px">150 notificações × 7 segundos dá uns <b>17 minutos por dia</b> com a atenção em câmera lenta.</div>
<div class="a c P" style="left:110px;right:110px;top:1060px;font-size:28px;font-style:italic;opacity:.75">(conta ilustrativa, não é um resultado do estudo)</div>''')
# 8 — foto em cima, bloco colorido embaixo com linha (ref. Priscila 3)
P[8]=page('creme',f'''
<div class="ph" style="left:0;right:0;top:0;height:560px"><img src="{m(22)}" style="object-position:50% 25%"></div>
<div class="a" style="left:0;right:0;top:560px;bottom:0;background:radial-gradient(ellipse 60% 50% at 30% 30%,#c27d8a,transparent 70%),#B36978"></div>
<div class="a" style="left:240px;right:240px;top:650px;height:3px;background:#F7EFEA"></div>
<div class="a c P" style="left:0;right:0;top:690px;font-size:38px;color:#F7EFEA">O estudo foi com adultos jovens,<br>de uns 20 anos.</div>
<div class="a c R" style="left:0;right:0;top:810px;font-size:160px;color:#F7EFEA;-webkit-text-stroke:2px #F7EFEA">E as <span class="C" style="font-size:170px">crianças?</span></div>
<div class="a c P" style="left:110px;right:110px;top:1000px;font-size:34px;color:#F7EFEA">Os próprios autores alertam: quem ainda está com a atenção em desenvolvimento <b>pode ser ainda mais sensível a interrupções repetidas.</b></div>''','#F7EFEA')
# 9 — foto inteira + pílulas inclinadas (designer)
dicas=["Desligue as notificações que não são<br>essenciais (as suas e as dos filhos).","Celular longe na hora da lição de casa,<br>das refeições e do sono.","Combine horários da casa<br>sem notificação.","Olhe o celular em blocos,<br>não a cada apito.","Lembre: as crianças copiam<br>o que a gente faz."]
pp=''.join(f'<div class="pil" style="align-self:{"flex-start" if i%2==0 else "flex-end"};transform:rotate({[-2,2,-1.5,2.5,-2][i]}deg);font-size:33px;line-height:1.2;padding:16px 36px 20px">{d}</div>' for i,d in enumerate(dicas))
P[9]=page('vinho',f'''
<div class="ph" style="inset:0"><img src="{m(21)}" style="object-position:45% 40%;filter:saturate(.55) brightness(.95)"></div>
<div class="a" style="inset:0;background:#b98a97;mix-blend-mode:multiply;opacity:.55"></div>
<div class="a c R" style="left:0;right:0;top:120px;font-size:110px;color:#FCC8BF;-webkit-text-stroke:2px #FCC8BF">Menos “plim”,<br>mais <span class="C" style="font-size:120px">foco:</span></div>
<div class="a" style="left:50px;right:50px;top:420px;display:flex;flex-direction:column;gap:26px">{pp}</div>''','#F7EFEA')
# 10 — balões só com contorno (designer)
def bal(t,css,flip=False):
    tr='transform:scaleX(-1);' if flip else ''
    return f'<div class="a" style="{css};width:470px;height:290px"><svg viewBox="0 0 360 250" style="position:absolute;inset:0;width:100%;height:100%;{tr}overflow:visible"><path d="M95,196.6 A170,100 0 1 0 49.8,174.3 L12,238 Z" fill="#55223a" stroke="#FCC8BF" stroke-width="4"/></svg><div class="P c" style="position:absolute;left:30px;right:30px;top:0;height:245px;display:flex;align-items:center;justify-content:center;font-size:38px;line-height:1.15;color:#FCC8BF">{t}</div></div>'
P[10]=page('vinho',f'''
<div class="a c R" style="left:0;right:0;top:200px;font-size:120px">Quantas<br>notificações você<br>recebeu <span class="C" style="font-size:130px">hoje?</span></div>
{bal("Conta aqui nos<br>comentários!","left:200px;top:620px")}
{bal("E manda pra quem<br>vive com o celular<br>apitando.","left:420px;top:830px",True)}
<div class="a c C" style="left:0;right:0;top:1140px;font-size:60px;-webkit-text-stroke:.8px #FCC8BF">com carinho, Dra. Mariana</div>''','#F7EFEA')
for k,v in P.items(): open(S+'n2/s%02d.html'%k,'w').write(v)
# 1 — capa: foto à esquerda se dissolvendo no rosa, título à direita e subtítulo em marca-texto (ref. "Nem toda criança agitada")
P1=page('rosa',f'''
<div class="ph" style="left:-170px;top:150px;width:900px;height:1050px;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 14%,#000 82%,transparent 100%)"><img src="{m(15)}" style="object-position:50% 45%;filter:saturate(.7) sepia(.15) brightness(1.06) contrast(.92)"></div>
<div class="a" style="left:0;right:0;top:0;bottom:0;background:linear-gradient(90deg,rgba(246,198,191,0) 40%,rgba(246,198,191,.85) 54%,#F6C6BF 62%)"></div>
<div class="a" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(0deg,#F6C6BF,rgba(246,198,191,0))"></div>
<div class="a P" style="left:560px;right:60px;top:290px;font-size:38px;line-height:1.2">Cada notificação<br>rouba cerca de</div>
<div class="a R" style="left:550px;top:420px;line-height:.85"><div style="font-size:250px">7</div><div style="font-size:112px;margin-top:6px">segundos</div></div>
<div class="a C" style="left:560px;top:770px;font-size:92px;color:#9B506E;-webkit-text-stroke:1.5px #9B506E;line-height:1.05">da sua<br>atenção.</div>
<div class="a P" style="left:560px;right:40px;top:1030px;font-size:40px;line-height:1.5"><span style="background:#D6E5DA;padding:2px 14px 6px;box-decoration-break:clone;-webkit-box-decoration-break:clone">E você nem abriu<br>a mensagem.</span></div>
<div class="a P" style="left:560px;top:1190px;font-size:28px;background:#5a2538;color:#FCC8BF;border-radius:30px;padding:6px 26px 10px">arrasta pro lado →</div>''')
open(S+'n2/s01.html','w').write(P1)
# 1 (versão aprovada) — título no alto, foto retangular, pílula na borda, frase final
P1=page('rosa',f'''
<div class="a c P" style="left:0;right:0;top:215px;font-size:36px;letter-spacing:.05em">CADA NOTIFICAÇÃO ROUBA CERCA DE</div>
<div class="a c R" style="left:0;right:0;top:268px;font-size:150px">7 segundos</div>
<div class="a c C" style="left:0;right:0;top:405px;font-size:118px;-webkit-text-stroke:1.8px #4a1c2e">da sua atenção.</div>
<div class="ph" style="left:165px;right:165px;top:545px;height:520px"><img src="{m(15)}" style="object-position:50% 62%;filter:saturate(.75) sepia(.15) brightness(1.06) contrast(.92)"></div>
<div class="a P" style="right:135px;top:575px;font-size:30px;background:#FCC8BF;border:2px solid #4a1c2e;padding:2px 20px 6px;transform:rotate(4deg);z-index:5">arrasta pro lado</div>
<div class="a pil" style="left:50%;transform:translateX(-50%);top:1038px;white-space:nowrap;font-size:40px;padding:14px 46px 18px;box-shadow:0 0 0 4px #F6C6BF;z-index:5">E você nem abriu a mensagem.</div>
<div class="a c P" style="left:0;right:0;top:1158px;font-size:44px;color:#3f3536">Bastou o ícone aparecer.</div>''')
open(S+'n2/s01.html','w').write(P1)
