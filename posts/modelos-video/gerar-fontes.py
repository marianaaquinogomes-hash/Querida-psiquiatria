# uso: python3 fontes.py saida.png "linha|r" "linha|i" ...
import sys,numpy as np
from PIL import Image,ImageDraw,ImageFont
S='/tmp/claude-0/-home-user-Querida-psiquiatria/dd765379-9e4a-53e2-ba7e-a1a50ea79544/scratchpad/'
im=np.asarray(Image.open(S+'vf4.png').convert('RGB')).astype(float)
old=np.array([216,170,171.]);target=np.array([0xF4,0xC3,0xBE],float)
dist=np.sqrt(((im-old)**2).sum(2));w=np.clip((48-dist)/20,0,1)
out=im*(1-w[...,None])+np.clip(im+(target-old),0,255)*w[...,None]
r,g=im[...,0],im[...,1];tt=np.zeros(dist.shape,bool);tt[415:485,415:655]=True
tw=np.clip(((r-g)-55)/15,0,1)*tt;out=out*(1-tw[...,None])+np.array([0x9B,0x50,0x6E])*tw[...,None]
base=Image.fromarray(out.astype(np.uint8));d=ImageDraw.Draw(base)
reg='/usr/share/fonts/opentype/inter/Inter-Regular.otf';ita='/usr/share/fonts/opentype/inter/Inter-Italic.otf'
f=ImageFont.truetype(reg,20);d.rectangle((447,1015,668,1040),fill=(252,250,242));asc=f.getbbox('D')[1];d.text((452,1020-asc),'Dra. Mariana Aquino •',font=f,fill=(50,50,48))
lines=[a.rsplit('|',1) for a in sys.argv[2:]]
fr=ImageFont.truetype(reg,56);fi=ImageFont.truetype(ita,52)
y=510;col=(0x4a,0x1c,0x2e);prev=None
for t,k in lines:
  if prev=='r' and k=='i': y+=16
  ff=fr if k=='r' else fi;wd=ff.getlength(t);d.text((540-wd/2,y),t,font=ff,fill=col);y+=66 if k=='r' else 62;prev=k
assert y<920,y
base.save(sys.argv[1])
