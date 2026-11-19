import json
exec(open('src/spots.py',encoding='utf-8').read())
ALL=[('bridge','橋梁','--c-bridge'),('rail','鉄道・道路・地下','--c-rail'),('water','治水・利水','--c-water'),('port','港湾・空港・城郭','--c-port'),('tower','塔','--c-tower'),('modern','近代建築（〜1945）','--c-modern'),('post','戦後・現代建築','--c-post')]
used={r[1] for r in R}
cats='var CATS={\n'+',\n'.join('  %s:{l:"%s",v:"%s"}'%(k,l,v) for k,l,v in ALL if k in used)+'\n};\nvar D=[\n'
rows=",\n".join(" "+json.dumps(r[:9],ensure_ascii=False) for r in R)
tail='''
].map((r,i)=>({id:"s"+i,name:r[0],cat:r[1],year:r[2],yl:r[3],area:r[4],by:r[5],spec:r[6],note:r[7],badge:r[8]}));
// 緯度・経度（概算を含む。現地で確かめて直す）
var COORDS=%s;
D.forEach(d=>{d.ll=COORDS[d.name]||null});
''' % json.dumps({r[0]:[r[9],r[10]] for r in R},ensure_ascii=False)
open('data.js','w',encoding='utf-8').write("// 北陸 土木建築散歩 — 名所データ（src/spots.py から src/mkdata.py で作る）\n"+cats+rows+tail)
