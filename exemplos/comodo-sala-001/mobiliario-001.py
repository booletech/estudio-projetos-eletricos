# -*- coding: utf-8 -*-
"""Executado somente pela macro da sala, no Python nativo do FreeCAD.
Geometria sintetica; pecas simplificadas sem marcas nem imagens de terceiros.
"""
doc.Piso.Length=5300;doc.Piso.Width=4300
doc.BaseFrente.Length=5300
doc.BaseFundo.Length=5300;doc.BaseFundo.Placement.Base=App.Vector(-150,4000,0)
doc.ParedeEsquerda.Width=4000
doc.ParedeDireita.Width=4000;doc.ParedeDireita.Placement.Base=App.Vector(5000,0,0)
doc.VaoJanela.Placement.Base=App.Vector(1500,3990,1000)
for name in ['JanelaLateralE','JanelaLateralD','JanelaInferior','JanelaSuperior','JanelaMontante','Vidro1','Vidro2']:
    obj=doc.getObject(name);p=obj.Placement.Base;obj.Placement.Base=App.Vector(p.x,p.y+1000,p.z)

furn=doc.addObject('App::DocumentObjectGroup','Mobiliario')
furn.Label='Sala - sofa, TV 43 polegadas, estante'
decor=doc.addObject('App::DocumentObjectGroup','Decoracao')
decor.Label='Decoracao - quadros, livros, vasos e planta'
sofa_color=(0.19,0.35,0.43)
oak=(0.55,0.36,0.20)
cream=(0.88,0.83,0.72)

def piece(name,size,pos,color,group=furn):
    obj=doc.addObject('Part::Box',name)
    obj.Label=name.replace('_',' ')
    obj.Length,obj.Width,obj.Height=size;obj.Placement.Base=App.Vector(*pos)
    obj.ViewObject.ShapeColor=color;obj.ViewObject.LineColor=(0.25,0.27,0.29)
    group.addObject(obj)
    return obj

# Sofa voltado para a TV na parede posterior. Dimensoes ilustrativas.
piece('Sofa_base_2200_mm',(2200,1000,180),(2450,650,150),sofa_color)
piece('Sofa_encosto',(2200,150,650),(2450,650,330),sofa_color)
piece('Sofa_braco_esquerdo',(150,850,450),(2450,800,330),sofa_color)
piece('Sofa_braco_direito',(150,850,450),(4500,800,330),sofa_color)
for n in range(3):
    piece('Sofa_assento_%d'%(n+1),(620,710,160),(2610+n*630,830,330),(0.29,0.45,0.52))
    piece('Sofa_almofada_encosto_%d'%(n+1),(620,90,390),(2610+n*630,805,500),(0.25,0.40,0.48))
for x in (2560,4500):
    for y in (740,1490):piece('Pe_sofa',(55,55,150),(x,y,0),(0.20,0.19,0.17))
piece('Tapete_sala',(2500,1300,8),(2300,1670,0),(0.73,0.62,0.47),decor)
piece('Almofada_decorativa',(260,120,260),(2770,970,510),(0.85,0.59,0.24),decor)
piece('Almofada_decorativa',(260,120,260),(4110,970,510),(0.78,0.76,0.65),decor)

piece('Rack_TV',(1100,350,420),(3050,3610,120),oak)
for x in (3080,4060):piece('Pe_rack',(40,260,120),(x,3650,0),(0.20,0.19,0.17))
for x in (3070,3595):piece('Porta_rack',(495,12,370),(x,3597,145),(0.63,0.46,0.29))

# 43 polegadas e diagonal da tela, nao largura. Proporcao 16:9 ilustrativa.
diag=43*25.4
screen_w=diag*16/math.sqrt(16*16+9*9)
screen_h=diag*9/math.sqrt(16*16+9*9)
frame=piece('TV_43_polegadas_moldura',(screen_w+40,50,screen_h+40),(3600-screen_w/2-20,3920,1500-screen_h/2-20),(0.08,0.09,0.10))
frame.addProperty('App::PropertyLength','DiagonalTela','Referencia').DiagonalTela=diag
frame.addProperty('App::PropertyString','ProporcaoTela','Referencia').ProporcaoTela='16:9 - hipotese grafica'
piece('TV_tela_43_polegadas',(screen_w,4,screen_h),(3600-screen_w/2,3916,1500-screen_h/2),(0.10,0.21,0.27))
# Composicao abstrata geometrica na tela, sem conteudo externo.
piece('TV_imagem_geometrica',(screen_w*.46,2,screen_h*.25),(3600-screen_w*.33,3914,1500-screen_h*.20),(0.17,0.35,0.41),decor)
piece('TV_imagem_geometrica',(screen_w*.24,2,screen_h*.40),(3600+screen_w*.10,3914,1500-screen_h*.20),(0.39,0.51,0.52),decor)

# Estante na parede esquerda, longe da porta.
piece('Estante_fundo',(25,900,1800),(40,2550,100),oak)
for y in (2550,3415):piece('Estante_lateral',(350,35,1800),(40,y,100),oak)
for z in (100,550,1000,1450,1865):piece('Estante_prateleira',(350,900,35),(40,2550,z),oak)
palette=[(0.32,0.42,0.48),(0.72,0.46,0.26),(0.80,0.74,0.57),(0.36,0.48,0.35)]
for row,z in enumerate((135,585,1035)):
    for n in range(6):piece('Livro_%d_%d'%(row+1,n+1),(220,40+5*(n%3),220+20*(n%4)),(85,2620+n*65,z),palette[(row+n)%4],decor)

def cylinder(name,r,h,pos,color,group=decor):
    obj=doc.addObject('Part::Cylinder',name);obj.Label=name.replace('_',' ')
    obj.Radius=r;obj.Height=h;obj.Placement.Base=App.Vector(*pos);obj.ViewObject.ShapeColor=color;group.addObject(obj);return obj
cylinder('Vaso_rack',65,140,(4080,3780,540),(0.84,0.76,0.62))
cylinder('Vaso_rack_bocal',40,45,(4080,3780,680),(0.84,0.76,0.62))
cylinder('Enfeite_estante',45,130,(230,3230,1035),(0.85,0.56,0.18))
cylinder('Vaso_planta',100,230,(900,3500,0),(0.63,0.41,0.28))
cylinder('Caule_planta',14,850,(900,3500,230),(0.26,0.33,0.17))
for n,(x,y,z,r) in enumerate([(900,3500,1040,200),(1050,3500,900,150),(750,3480,850,170),(900,3650,900,170)]):
    obj=doc.addObject('Part::Sphere','Folhagem_%d'%n);obj.Radius=r;obj.Placement.Base=App.Vector(x,y,z);obj.ViewObject.ShapeColor=(0.19,0.36+0.025*n,0.21);decor.addObject(obj)

# Quadros geometricos proprios nas paredes laterais.
for n,y in enumerate((1800,2500,3200)):
    piece('Quadro_moldura_%d'%n,(35,440,600),(4955,y-220,1220),(0.31,0.23,0.16),decor)
    piece('Quadro_fundo_%d'%n,(4,400,560),(4950,y-200,1240),cream,decor)
    piece('Quadro_arte_geometrica_%d'%n,(3,200,280),(4947,y-100,1340),palette[n],decor)
piece('Quadro_parede_esquerda',(35,520,650),(10,1030,1280),(0.31,0.23,0.16),decor)
piece('Quadro_fundo_esquerda',(4,480,610),(45,1050,1300),cream,decor)
piece('Quadro_arte_esquerda',(3,210,340),(49,1180,1420),(0.72,0.46,0.26),decor)
doc.recompute()
assert math.isclose(math.hypot(screen_w,screen_h),diag,abs_tol=.001)
assert doc.Piso.Length.Value==5300 and doc.Piso.Width.Value==4300
for group in (furn,decor):
    for obj in group.Group:
        assert obj.Shape.isValid() and obj.Shape.Volume>0 and len(obj.Shape.Solids)==1,obj.Name
