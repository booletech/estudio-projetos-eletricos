"""Confere cópias CAD sintéticas; não valida conformidade elétrica."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
sample = root / 'exemplos/residencial-001'
manifest = json.loads((sample / 'manifesto-001.json').read_text(encoding='utf-8'))
if manifest['pronto_para_publicar'] or manifest['pronto_para_execucao']:
    raise SystemExit('A amostra pendente não pode estar marcada como aprovada.')
for record in manifest['arquivos']:
    path = sample / record['arquivo']
    if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
        raise SystemExit(f'Integridade divergente: {path.name}; criar revisão numerada.')
dxf = (sample / 'planta-residencial-001.dxf').read_text(encoding='ascii').splitlines()
if len(dxf) % 2:
    raise SystemExit('DXF com quantidade ímpar de linhas.')
pairs = list(zip(dxf[::2], dxf[1::2]))
if pairs[-1] != ('0', 'EOF'):
    raise SystemExit('DXF incompleto.')
counts = {kind: pairs.count(('0', kind)) for kind in ['LINE', 'TEXT', 'CIRCLE']}
if counts['CIRCLE'] != 18 or sum(counts.values()) != 114:
    raise SystemExit(f'Contagem inesperada no DXF: {counts}')
qet = ET.parse(sample / 'quadro-residencial-001.qet').getroot()
elements = qet.findall('diagram/elements/element')
conductors = qet.findall('diagram/conductors/conductor')
terminals = {x.get('id') for e in elements for x in e.findall('terminals/terminal')}
if len(elements) != 9 or len(conductors) != 8:
    raise SystemExit('Contagem inesperada no QET.')
for conductor in conductors:
    if any(conductor.get(name) not in terminals for name in ['terminal1', 'terminal2']):
        raise SystemExit('Referência de terminal ausente no QET.')
print(f'OK: hashes preservados; DXF {counts}; QET 9 elementos e 8 condutores.')
print('Esta verificação não comprova renderização ou conformidade elétrica.')
