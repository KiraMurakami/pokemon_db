import sqlite3

# モード選択
print('モードを選択してください＞1:データ追加/2:素早さ比較/3:準速最速計算')
x = int(input())

# データベース開く
db = sqlite3.connect("pokemon.db")

c = db.cursor()

# データ追加モード(レコード登録)
if x == 1:
  # テーブル作成
  c.execute('create table if not exists speed (name text, spd int)')
  print('所持ポケモンを追加します')
  print('ポケモン名を入力してください＞')
  poke_name = input()
  print('素早さを入力してください')
  poke_spd = int(input())
  sql = 'insert into speed (name, spd) values (?,?)'
  data = (poke_name,poke_spd)
  c.execute(sql, data)

# 素早さ比較モード
if x == 2:
  print('入力された素早さより速いポケモンを表示します')
  print('参照する素早さを入力してください＞')
  std_spd = int(input())
  c.execute("select * from speed where spd > %d"% std_spd)
  for row in c:
    print(str(row[0]) + "|" + str(row[1]))

# 実数値計算モード
if x == 3:
  print('素早さの準速、最速の実数値を計算します')
  print('素早さ種族値を入力してください＞')
  base_spd = int(input())
  second_spd = base_spd+52
  first_spd = second_spd + (second_spd//10)
  print('準速の値は：%dです'% second_spd)
  print('最速の値は：%dです'% first_spd)

# コミット
db.commit()

# クローズ
db.close()
