# <center><font color="Blue">空力班Pythonシミュ　チュートリアル</font></center>

～目次～
<!-- vscode-markdown-toc -->
* [本ドキュメントについて](#)
* [1.直線上の鉛直投げ上げ](#-1)
* [2.二次元平面での投げ上げ](#-1)
* [3.三次元での投げ上げ](#-1)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

<!-- TOC depthFrom:2 -->

## <a name=''></a>本ドキュメントについて
- 対象
  - pythonシミュに興味がある方
  - pythonの基礎的な文法を把握している初心者
        ※四則演算，if文，while文程度が書ける読める段階からスタートします
- 目的
  - pythonに親しむ
  - シミュの雰囲気を掴む
- その他
  - 質問・記載内容の誤り等があればご連絡下さい
<br>
すぐに本番のコードを読むのは大変に感じたので，pythonに慣れながらシミュレータの実装の雰囲気を掴んで欲しいとの思いで作成しました．  
実際に手を動かしながら読み進めていくと効果的かと思います．  
各自のスキルに合わせて適宜飛ばしながら利用して下さい．  

## <a name='-1'></a>1.直線上の鉛直投げ上げ
早速鉛直投げ上げ運動の実装を試してみましょう．  
初めは直線上での動きから考えていきます．  
実装方法は例は以下の通りです．(鉛直上向きを正としています)
1. 速度 = 速度 + -1 * 重力加速度 * 時間刻み幅
2. 高度 = 高度 + 速度 * 時間刻み幅
3. 時間 = 時間 + 時間刻み幅
4. もし高度が演算終了高度以上なら1.へ戻る
5. 結果の出力

以下の条件で実行して滞空時間を求めてみましょう．
```python
# 初期高度[m]:0
# 演算終了高度[m]:0
# 初速度[m/s]:100.0
# 時間刻み幅[s]:0.01
# 重力加速度[m/s^2]:9.8
```
コードの実装例・答え(コード1行目に記載)は[こちら](https://github.com/mame7777/3DSimulataion-Tutorial/blob/main/codes/tutorial-1.py)

## <a name='-1'></a>2.二次元平面での投げ上げ
次は投射角を付けた運動をシミュレートしてみようと思います．  
また，ここからは位置や速度の情報を行列で扱っていきます．  

ライブラリでnumpyを使います．  
インストールされていない人はコマンドプロンプト等で`pip install numpy`と入力し実行して下さい．  
※エラーが出る場合は調べるか，質問して下さい．  
※これからいくつかライブラリを使いますが，必要に応じて各自インストールして下さい．  

numpyで行列を表現する時は以下のように書きます．
```python
import numpy as np
matrix = np.array([data0, data1, data2])
```
ここで，`np.array([data0, data1, data2], dtype=np.float64)`とすると，要素がnumpy.float64型に揃えられます．  
その他，行列の扱い方については[こちら](https://qiita.com/tseno/items/3b7ef7e36eab64d42753)等を参照して下さい．  

以下の条件で実行して滞空時間・最高高度・水平方向の落下距離を求めてみましょう．
```python
# 初期高度[m]:0
# 演算終了高度[m]:0
# 地面に対する投射角[deg]:70
# 初速度[m/s]:100.0
# 時間刻み幅[s]:0.01
# 重力加速度[m/s^2]:9.8
```
コードの実装例・答え(コード1行目に記載)は[こちら](https://github.com/mame7777/3DSimulataion-Tutorial/blob/main/codes/tutorial-2.py)  
※小数点以下1桁までとして正解を記載  

## <a name='-1'></a>3.三次元での投げ上げ
いよいよ三次元空間での投げ上げをシミュレートしたいと思います．  
今回は以下のように空間を表現します．
```math
position = 
\begin{pmatrix}
鉛直 　\leftarrow 上が正 \\
南北 　\leftarrow 北が正 \\
東西 　\leftarrow 東が正 \\
\end{pmatrix}
```

また，方位は北を0[deg]として，時計周りに360[deg]表記で表しています．  

以下の条件で実行して滞空時間・最高高度・距離位置を求めてみましょう．
```python
# 初期高度[m]:0
# 演算終了高度[m]:0
# 地面に対する仰角[deg]:70
# 方位角[deg]:278.5
# 初速度[m/s]:100.0
# 時間刻み幅[s]:0.01
# 重力加速度[m/s^2]:9.8
```
コードの実装例・答え(コード1行目に記載)は[こちら](https://github.com/mame7777/3DSimulataion-Tutorial/blob/main/codes/tutorial-3.py)  
※小数点以下1桁までとして正解を記載  
  
コードの[実装例2](https://github.com/mame7777/3DSimulataion-Tutorial/blob/main/codes/tutorial-3_sub.py)  
classを使った例です．  
資料作成者もあまり使い慣れていないため，汚い実装となっています．　　
