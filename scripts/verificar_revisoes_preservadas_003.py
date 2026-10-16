"""Integridade das copias 003; nao valida dimensionamento ou revisao visual."""
from pathlib import Path
from collections import Counter
import hashlib, json, zipfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
FOLDERS=['exemplos/comodo-eletrico-001/planta-003','exemplos/comodo-sala-001/saida-003']

def entities(path):
    lines=path.read_text(encoding='cp1252').splitlines()
    assert len(lines)%2==0, 'DXF com pares incompletos'
    pairs=[(int(lines[i].strip()),lines[i+1].strip()) for i in range(0,len(lines),2)]
    assert pairs[-1]==(0,'EOF'), 'DXF sem EOF'
    result=[];active=False;current=None
    for i,(code,value) in enumerate(pairs):
        if (code,value)==(2,'ENTITIES') and i and pairs[i-1]==(0,'SECTION'):
            active=True;continue
        if active and (code,value)==(0,'ENDSEC'):
            if current: result.append(current)
            active=False;current=None
        elif active and code==0:
            if current: result.append(current)
            current=[(code,value)]
        elif active and current is not None: current.append((code,value))
    assert result, 'DXF sem entidades'
    return result

def main():
    results=[]
    for folder in FOLDERS:
        base=ROOT/folder
        m=json.loads((base/'manifesto-preservacao-003.json').read_text(encoding='utf-8'))
        p=base/m['file'];old=ROOT/m['original_path'];data=p.read_bytes()
        assert hashlib.sha256(data).hexdigest()==m['sha256']==m['source_sha256']
        assert len(data)==m['bytes']
        assert hashlib.sha256(old.read_bytes()).hexdigest()==m['original_sha256']
        assert not m['pronto_para_publicar'] and not m['pronto_para_execucao']
        r={'file':p.relative_to(ROOT).as_posix(),'hashes_ok':True}
        if p.suffix.lower()=='.dxf':
            a,b=entities(old),entities(p)
            r['original_entity_counts']=dict(Counter(e[0][1] for e in a))
            r['revision_entity_counts']=dict(Counter(e[0][1] for e in b))
            texts=lambda es: sorted(v for e in es for k,v in e if k==1)
            r['texts_equal']=texts(a)==texts(b)
            r['revision_texts']=texts(b)
            def geometry(es):
                values=[]
                for entity in es:
                    fields=dict(entity); kind=fields[0]
                    codes={'LINE':[10,20,30,11,21,31],
                           'CIRCLE':[10,20,30,40],
                           'TEXT':[10,20,30,11,21,31,40,50,72,73]}[kind]
                    values.append((kind,fields.get(8,'0'),fields.get(1,''),
                                   tuple(round(float(fields.get(c,0)),6) for c in codes)))
                return sorted(values)
            r['geometry_layer_text_fields_equal']=geometry(a)==geometry(b)
            assert r['texts_equal'] and r['geometry_layer_text_fields_equal']
        else:
            with zipfile.ZipFile(p) as z:
                assert z.testzip() is None
                doc=ET.fromstring(z.read('Document.xml'));ET.fromstring(z.read('GuiDocument.xml'))
                objects={o.get('name') for o in doc.findall('./Objects/Object')}
                assert {'L1','S1','T1','T2','T3','T4','Mobiliario','Decoracao','Sofa_base_2200_mm'}<=objects
                r['object_count']=len(objects);r['zip_xml_ok']=True
            with zipfile.ZipFile(old) as z:
                original={o.get('name') for o in ET.fromstring(z.read('Document.xml')).findall('./Objects/Object')}
            r['object_ids_equal']=objects==original
            assert r['object_ids_equal']
        results.append(r)
    print(json.dumps(results,ensure_ascii=True))

if __name__=='__main__': main()
