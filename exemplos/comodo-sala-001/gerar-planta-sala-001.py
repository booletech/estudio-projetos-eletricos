"""Gerar planta didatica DXF/SVG/PNG e tabela a partir de pontos-001.json.
Usar o Python isolado em .venv, com Pillow ja disponivel neste ambiente.
Nao especifica condutores, protecoes, cargas ou conformidade normativa.
"""
from pathlib import Path
import json, hashlib, csv, math, html, struct
from PIL import Image, ImageDraw, ImageFont

root=Path(__file__).resolve().parent
config_path=root/'pontos-001.json'
cfg=json.loads(config_path.read_text(encoding='utf-8'))
number=1
while (root/f'planta-{number:03d}').exists(): number+=1
out=root/f'planta-{number:03d}'
out.mkdir()
items=[]
colors={'ARQUITETURA':'#727d86','ILUMINACAO':'#da6b17','TOMADAS':'#1268c4','PENDENCIAS':'#c63245','TEXTOS':'#243749','COTAS':'#667888'}
def line(a,b,layer):
    if a!=b: items.append(('LINE',layer,tuple(a),tuple(b)))
def path(vertices,layer):
    for a,b in zip(vertices,vertices[1:]):line(a,b,layer)
def rect(x,y,w,h,layer):path([(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)],layer)
def text(x,y,s,layer='TEXTOS',size=95,angle=0):items.append(('TEXT',layer,(x,y),s,size,angle))
def circle(x,y,r,layer):items.append(('CIRCLE',layer,(x,y),r))

# Geometria arquitetonica em mm; porta e janela preservam as posicoes do 3D.
rect(-150,0,150,4000,'ARQUITETURA');rect(5000,0,150,4000,'ARQUITETURA')
rect(-150,-150,850,150,'ARQUITETURA');rect(1600,-150,3550,150,'ARQUITETURA')
rect(-150,4000,1650,150,'ARQUITETURA');rect(2700,4000,2450,150,'ARQUITETURA')
rect(1500,4040,1200,70,'ARQUITETURA');line((2100,4040),(2100,4110),'ARQUITETURA')
line((740,-75),(740,745),'ARQUITETURA')
path([(740+820*math.cos(t*math.pi/60),-75+820*math.sin(t*math.pi/60)) for t in range(31)],'ARQUITETURA')

segments=set()
for r in cfg['rotas']:
    layer='PENDENCIAS' if r['grupo']=='origem_pendente' else 'TOMADAS' if r['grupo']=='tomadas' else 'ILUMINACAO'
    v=[p[:2] for p in r['vertices_mm']]
    for a,b in zip(v,v[1:]):
        key=(layer,tuple(sorted([tuple(a),tuple(b)])))
        if key not in segments:
            line(a,b,layer);segments.add(key)

label_positions={'L1':(2710,1870),'S1':(1720,260),'T1':(4220,260),'T2':(4570,2270),'T3':(3500,3650),'T4':(230,1770),'D1':(4370,1970),'A0':(5180,2220)}
for p in cfg['pontos']:
    x,y,z=p['centro_mm'];ident=p['id'];kind=p['tipo']
    if kind=='lampada':
        circle(x,y,110,'ILUMINACAO');line((x-80,y-80),(x+80,y+80),'ILUMINACAO');line((x-80,y+80),(x+80,y-80),'ILUMINACAO')
    elif kind=='interruptor':
        circle(x,y,65,'ILUMINACAO');line((x,y),(x+110,y+100),'ILUMINACAO')
    elif kind=='tomada':
        rect(x-55,y-55,110,110,'TOMADAS');line((x-22,y-30),(x-22,y+30),'TOMADAS');line((x+22,y-30),(x+22,y+30),'TOMADAS')
    elif kind=='caixa_grafica':rect(x-60,y-60,120,120,'PENDENCIAS')
    else:
        line((x,y),(x-90,y+55),'PENDENCIAS');line((x,y),(x-90,y-55),'PENDENCIAS')
    text(*label_positions[ident],ident,size=105)

rect(2450,650,2200,1000,'ARQUITETURA')
rect(2450,650,2200,150,'ARQUITETURA')
for x in (2600,4500):rect(x,800,150,850,'ARQUITETURA')
text(3150,1100,'SOFA 2,20 m',size=90)
rect(40,2550,350,900,'ARQUITETURA')
text(500,2970,'ESTANTE',size=85)
rect(3050,3610,1100,350,'ARQUITETURA')
rect(3104,3920,992,50,'ARQUITETURA')
text(3070,3410,'TV 43 / RACK',size=85)
circle(900,3500,150,'ARQUITETURA')
text(720,3170,'PLANTA',size=75)
# Cotas de referencia internas, sem escala de impressao fixada.
line((0,-260),(0,-500),'COTAS');line((5000,-260),(5000,-500),'COTAS')
line((0,-430),(2250,-430),'COTAS');line((2750,-430),(5000,-430),'COTAS')
text(2280,-470,'5000','COTAS',105)
for x in (0,5000):line((x-50,-480),(x+50,-380),'COTAS')
line((-260,0),(-550,0),'COTAS');line((-260,4000),(-550,4000),'COTAS')
line((-480,0),(-480,4000),'COTAS');text(-650,1230,'4000','COTAS',105,90)
for y in (0,4000):line((-530,y-50),(-430,y+50),'COTAS')

text(5900,3770,'LEGENDA / ESTUDO',size=110)
legend=[('L1  1 lampada central','ILUMINACAO'),('S1  1 interruptor: controla L1','ILUMINACAO'),('T1-T4  4 tomadas genericas','TOMADAS'),('Laranja: luz e comando','ILUMINACAO'),('Azul: trajetos das tomadas','TOMADAS'),('D1: distribuicao conceitual','PENDENCIAS'),('A0: origem a definir','PENDENCIAS'),('Simbolos didaticos','TEXTOS'),('Dimensoes em mm','TEXTOS'),('Alturas ilustrativas:','TEXTOS'),('S1: 1100 / T1-T4: 300','TEXTOS'),('L1: plano do teto a 2700','TEXTOS')]
for n,(s,layer) in enumerate(legend):text(5900,3500-n*190,s,layer,78)
text(-450,4400,'SALA 5 x 4 m | MOBILIARIO E ELETRICA 001',size=150)
text(-450,-780,'DISPOSICAO E TRAJETOS CONCEITUAIS - NAO LIBERADO PARA EXECUCAO',size=85)
text(-450,-960,'Tensao, potencias, circuitos, condutores e protecoes: pendentes de projeto e revisao.',size=75)

# DXF ASCII R12, sem dependencia externa nem simbolos de terceiros.
pairs=[]
def add(code,value):pairs.extend((str(code),str(value)))
add(0,'SECTION');add(2,'HEADER');add(9,'$ACADVER');add(1,'AC1009');add(0,'ENDSEC')
add(0,'SECTION');add(2,'TABLES');add(0,'TABLE');add(2,'LAYER');add(70,len(colors))
aci={'ARQUITETURA':8,'ILUMINACAO':30,'TOMADAS':5,'PENDENCIAS':1,'TEXTOS':7,'COTAS':8}
for layer in colors:add(0,'LAYER');add(2,layer);add(70,0);add(62,aci[layer]);add(6,'CONTINUOUS')
add(0,'ENDTAB');add(0,'ENDSEC');add(0,'SECTION');add(2,'ENTITIES')
for item in items:
    kind,layer,*values=item;add(0,kind);add(8,layer)
    if kind=='LINE':
        a,b=values;add(10,a[0]);add(20,a[1]);add(30,0);add(11,b[0]);add(21,b[1]);add(31,0)
    elif kind=='CIRCLE':a,r=values;add(10,a[0]);add(20,a[1]);add(30,0);add(40,r)
    else:
        a,s,h,angle=values;add(10,a[0]);add(20,a[1]);add(30,0);add(40,h);add(1,s);add(50,angle)
add(0,'ENDSEC');add(0,'EOF')
dxf=out/'planta-eletrica-001.dxf';dxf.write_text('\n'.join(pairs)+'\n',encoding='ascii')

# SVG e PNG usam exatamente as mesmas primitivas do DXF.
scale=.18;origin=(170,140);width,height=1650,1120
def xy(p):return origin[0]+p[0]*scale,origin[1]+(4000-p[1])*scale
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">','<rect width="100%" height="100%" fill="white"/>']
image=Image.new('RGB',(width,height),'white');draw=ImageDraw.Draw(image)
font_path=Path('C:/Windows/Fonts/arial.ttf')
for item in items:
    kind,layer,*values=item;color=colors[layer];stroke=3 if layer in ('TOMADAS','ILUMINACAO') else 2
    if kind=='LINE':
        a,b=map(xy,values);draw.line([a,b],fill=color,width=stroke)
        svg.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{color}" stroke-width="{stroke}"/>')
    elif kind=='CIRCLE':
        a,r=values;x,y=xy(a);r*=scale;draw.ellipse((x-r,y-r,x+r,y+r),outline=color,width=stroke)
        svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="white" stroke="{color}" stroke-width="{stroke}"/>')
    else:
        a,s,h,angle=values;x,y=xy(a);font_size=max(12,round(h*scale));font=ImageFont.truetype(str(font_path),font_size)
        if not angle:draw.text((x,y),s,font=font,fill=color,anchor='ls')
        else:
            box=font.getbbox(s);stamp=Image.new('RGBA',(box[2]-box[0]+8,font_size+10));sd=ImageDraw.Draw(stamp);sd.text((4,-box[1]),s,font=font,fill=color);stamp=stamp.rotate(angle,expand=True);image.paste(stamp,(round(x),round(y-stamp.height)),stamp)
        svg.append(f'<text x="{x:.2f}" y="{y:.2f}" fill="{color}" font-family="Arial,sans-serif" font-size="{font_size}" transform="rotate({-angle} {x:.2f} {y:.2f})">{html.escape(s)}</text>')
svg.append('</svg>');vector=out/'planta-eletrica-001.svg';vector.write_text('\n'.join(svg),encoding='utf-8')
png=out/'planta-eletrica-001.png';image.save(png)
table=out/'lista-pontos-001.csv'
with table.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['id','tipo','x_mm','y_mm','z_mm','controla','observacao'])
    for p in cfg['pontos']:w.writerow([p['id'],p['tipo'],*p['centro_mm'],p.get('controla',''),p.get('nota','Hipotese didatica')])

assert len({p['id'] for p in cfg['pontos']})==len(cfg['pontos'])
idx={p['id']:p for p in cfg['pontos']}
for r in cfg['rotas']:
    assert r['vertices_mm'][0]==idx[r['de']]['centro_mm']
    assert r['vertices_mm'][-1]==idx[r['para']]['centro_mm']
assert list(zip(pairs[::2],pairs[1::2]))[-1]==('0','EOF')
assert struct.unpack('>II',png.read_bytes()[16:24])==(width,height)
manifest={'tipo':'planta_eletrica_didatica','unidade_geometria':'mm','impressao':'Escala de impressao nao configurada; geometria 1:1 em mm','camadas':list(colors),'entidades_dxf':{k:sum(i[0]==k for i in items) for k in ('LINE','CIRCLE','TEXT')},'quantidades':{'lampada':1,'interruptor':1,'tomadas':4},'rotas_com_extremos_conferidos':len(cfg['rotas']),'hipoteses':cfg['hipoteses'],'pendencias':cfg['pendencias'],'pronto_para_publicar':False,'pronto_para_execucao':False,'arquivos':[{'nome':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (Path(__file__),config_path,dxf,vector,png,table)]}
(out/'manifesto-planta-001.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'saida':str(out),'entidades':manifest['entidades_dxf'],'dimensoes_png':[width,height]},ensure_ascii=False))
