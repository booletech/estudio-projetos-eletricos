"""Conferir a revisao publicada: preservacao, hashes, pontos e arquivos reais.
Nao confere calculos, conformidade eletrica ou o conteudo visual integral.
"""
from pathlib import Path
import hashlib, json, csv, zipfile, struct
import xml.etree.ElementTree as ET

root=Path(__file__).resolve().parent
config=json.loads((root/'pontos-001.json').read_text(encoding='utf-8'))
source=root.parent/'comodo-3d-001/saida-002/comodo-001.FCStd'
expected='81a0be19aa58bcb56289ed640e3e1360ae255ff5802be3cbbdf37c13a7cfc7d5'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected,'Fonte alterada'
file_count=0
for output,manifest_name in [('saida-002','manifesto-3d-001.json'),('planta-002','manifesto-planta-001.json')]:
    folder=root/output
    manifest=json.loads((folder/manifest_name).read_text(encoding='utf-8'))
    assert not manifest['pronto_para_execucao'] and not manifest['pronto_para_publicar']
    for rec in manifest['arquivos']:
        local=root/rec['nome']
        if not local.exists(): local=folder/rec['nome']
        data=local.read_bytes()
        assert len(data)==rec['bytes'] and hashlib.sha256(data).hexdigest()==rec['sha256'],rec['nome']
        file_count+=1
    assert manifest['pendencias']==config['pendencias']

assert hashlib.sha256((root/'saida-002/fonte-comodo-001.FCStd').read_bytes()).hexdigest()==expected
for p in (root/'saida-002').glob('*.FCStd'):
    with zipfile.ZipFile(p) as z:
        assert z.testzip() is None,p.name
        ET.fromstring(z.read('Document.xml'))
with zipfile.ZipFile(root/'saida-002/comodo-eletrico-001.FCStd') as z:
    xml=ET.fromstring(z.read('Document.xml'))
    objects={x.get('name') for x in xml.findall('./Objects/Object')}
    assert {'L1','S1','T1','T2','T3','T4','D1','A0'}<=objects

idx={p['id']:p for p in config['pontos']}
assert len(idx)==8 and idx['S1']['controla']=='L1'
for route in config['rotas']:
    assert route['vertices_mm'][0]==idx[route['de']]['centro_mm']
    assert route['vertices_mm'][-1]==idx[route['para']]['centro_mm']
with (root/'planta-002/lista-pontos-001.csv').open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
assert {r['id'] for r in rows}==set(idx)
for row in rows:
    assert [int(row[k]) for k in ('x_mm','y_mm','z_mm')]==idx[row['id']]['centro_mm']

lines=(root/'planta-002/planta-eletrica-001.dxf').read_text(encoding='ascii').splitlines()
assert len(lines)%2==0
pairs=list(zip(lines[::2],lines[1::2]));assert pairs[-1]==('0','EOF')
counts={k:pairs.count(('0',k)) for k in ('LINE','CIRCLE','TEXT')}
assert counts=={'LINE':116,'CIRCLE':2,'TEXT':26}
assert set(idx)<={v for c,v in pairs if c=='1'}
for name,size in [('saida-002/comodo-eletrico-isometrico-001.png',(1600,1100)),('planta-002/planta-eletrica-001.png',(1650,1120))]:
    data=(root/name).read_bytes();assert data[:8]==b'\x89PNG\r\n\x1a\n'
    assert struct.unpack('>II',data[16:24])==size
ET.parse(root/'planta-002/planta-eletrica-001.svg')
print(json.dumps({'arquivos_com_hash_conferido':file_count,'fonte_preservada':True,'pontos_de_uso':6,'contagens_dxf':counts,'csv_svg_png_fcstd_lidos':True}))
