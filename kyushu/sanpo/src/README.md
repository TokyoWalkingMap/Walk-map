# 九州 土木建築散歩 — データと地図の作り方

- `spots.py` … 名所の一覧（名前・分類・年・解説・緯度経度）。座標には概算を含む
- `mkdata.py` … `spots.py` から `../data.js` を作る（`python3 src/mkdata.py`、`kyushu/sanpo` で実行）
- `areas.json` … 地図の定義（key, bbox=[南,西,北,東], z=タイルの縮尺, 題名, 説明, 地名ラベル）。`overview` は九州全体図
- `areas.mjs` … 国土地理院 最適化ベクトルタイル（optimal_bvmap-v1）から道路・鉄道・水面を取り、地図データにする

```
npm i @mapbox/vector-tile@1.3.1 pbf@3.2.1
NODE_USE_ENV_PROXY=1 node areas.mjs areas.json out.json
```

out.json を `Object.assign(TOKYO_MAPS, …)` で包んで `../maps.js` に置く（`TOKYO_MAPS` は東京版から引き継いだ地図データの入れ物の名前）。
エリアを足したら `../mapdraw.js` の `AREA_KEYS` にも key を加える（先に書いたエリアが優先で名所が割り当てられる）。
名所は `spots.py` の末尾に足す（id は配列の順番。途中に入れると撮った写真とずれる）。
