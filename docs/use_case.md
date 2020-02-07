---
layout: post
title: Use Case
nav_order: 2
---

# Use Case
## Usage

## use case name
- abstract
- purpose
- actor
- trigger
- previous condition
- event flow
- irregular event flow
- after condition
---
## ユーザが論文を検索する
- abstract
<br> システム利用者が，検索エリアに論文名を入力し，検索を実行することで，このユースケースは利用される．
- purpose
<br> システム利用者が論文を検索するため．
- actor
<br> システム利用者
- trigger
<br> 検索ボタンを押す．
- previous condition
<br> 検索バーに文字が入力されている．
- event flow
1. システム利用者が検索ボタンを押す．
2. フロントが，サーバに検索バーの文字列をサーバに送る．
3. フロントが，サーバから返却されたjson形式のデータを受け取る．
4. フロントが，グラフ(ref, citation, related)をシステム利用者に提示する．
- irregular event flow
1. 文字を入力しないで，ボタンを押された場合，何も画面が変化しないよう，分岐処理を行う．
2. サーバから返却されたjsonが空白の場合，検索に何も反応しなかった旨を表示する．
- after condition
<br> 検索された論文に対する関係性のグラフが表示される．
---
## サーバが論文を検索する．
- abstract
<br> サーバが，フロントから渡された文字列を検索し，その関連文献を全て集め，jsonにまとめる．
- purpose
<br> システムを正常に機能させるため．
- actor
<br> フロント
- trigger
<br> フロントから文字列を渡される．
- previous condition
<br> なし
- event flow
1. 受け取った文字列を，APIの検索にかける．
2. APIから帰ってきたデータをフロントに渡す形に変形する．
3. フロントに値を返却する．
- irregular event flow
1. 検索に失敗した際は，jsonを空白にする．
- after condition
フロントとのやりとりが終了している．
---
