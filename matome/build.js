// 地方版（東京・関西・北陸・九州）の名所をまとめて matome/data.js を作る： node matome/build.js
const fs=require("fs"),vm=require("vm"),path=require("path");const R=path.join(__dirname,"..");
const REG=[["tokyo","東京","tokyo/sanpo",["tokyo-data.js","tokyo-maps.js","tokyo-maps-gsi.js","tokyo-mapdraw.js"]],
 ["kansai","関西","kansai/sanpo",["data.js","maps.js","mapdraw.js"]],["hokuriku","北陸","hokuriku/sanpo",["data.js","maps.js","mapdraw.js"]],["kyushu","九州","kyushu/sanpo",["data.js","maps.js","mapdraw.js"]]];
const out={regions:[],spots:[]};let cats=null;
for(const [key,title,dir,files] of REG){const c={};c.window=c;vm.createContext(c);
  vm.runInContext(files.map(f=>fs.readFileSync(path.join(R,dir,f),"utf8")).join("\n;\n")+";this.D=D;this.CATS=CATS;this.T=TOKYO_MAPS;",c);
  if(!cats){cats={};for(const k in c.CATS)cats[k]=c.CATS[k].l}
  const TM=c.window.TokyoMap,ov=c.T.overview;let n=0;
  const areas=TM.AREA_KEYS.map(k=>({key:k,title:c.T[k].title.replace(/（.*）/,""),bbox:c.T[k].bbox}));
  c.D.forEach(d=>{if(!d.ll)return;const a=TM.areaOf?TM.areaOf(d):null;n++;
    out.spots.push([key,d.id,d.name,d.cat,d.yl,d.area,+d.ll[0].toFixed(5),+d.ll[1].toFixed(5),a?c.T[a].title.replace(/（.*）/,""):""])});
  out.regions.push({key,title,url:"../"+dir+"/",bbox:ov.bbox,count:n,total:c.D.length,areas});
}
cats.tower="塔・古建築";out.cats=cats;
fs.writeFileSync(path.join(__dirname,"data.js"),"// 自動生成（matome/build.js）\nvar MATOME="+JSON.stringify(out)+";\n");
console.log(out.regions.map(r=>r.title+r.count+"/"+r.total).join(" "),out.spots.length);
