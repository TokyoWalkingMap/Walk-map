# 関西 土木建築散歩 — 名所の一覧（このファイルから data.js を作る）
# s(名前, 分類, 年, 市区, 設計・施工, 規模・特徴, 解説, 緯度, 経度, バッジ="", 年の表記=None)
R = []
def s(n,c,y,city,by,spec,note,la,lo,b="",yl=None):
    R.append([n,c,y,yl or str(y),city,by,spec,note,b,la,lo])
