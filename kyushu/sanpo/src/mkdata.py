import json
exec(open('src/spots.py',encoding='utf-8').read())
cats='''var CATS={
  bridge:{l:"橋梁",v:"--c-bridge"},
  rail:{l:"鉄道・道路・地下",v:"--c-rail"},
  water:{l:"治水・利水",v:"--c-water"},
  port:{l:"港湾・空港・城郭",v:"--c-port"},
  tower:{l:"塔",v:"--c-tower"},
  modern:{l:"近代建築（〜1945）",v:"--c-modern"},
  post:{l:"戦後・現代建築",v:"--c-post"}
};
var D=[
'''
rows=",\n".join(" "+json.dumps(r[:9],ensure_ascii=False) for r in R)
tail='''
].map((r,i)=>({id:"s"+i,name:r[0],cat:r[1],year:r[2],yl:r[3],area:r[4],by:r[5],spec:r[6],note:r[7],badge:r[8]}));
// 緯度・経度（概算を含む。現地で確かめて直す）
var COORDS=%s;
D.forEach(d=>{d.ll=COORDS[d.name]||null});
''' % json.dumps({r[0]:[r[9],r[10]] for r in R},ensure_ascii=False)
open('data.js','w',encoding='utf-8').write("// 九州 土木建築散歩 — 名所データ（src/spots.py から src/mkdata.py で作る）\n"+cats+rows+tail)
