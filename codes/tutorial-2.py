# 滞空時間:19.2 s
# 最高高度:450.1 m
# 水平方向落下距離:655.7 m

# 位置や速度を[水平方向, 垂直方向]の行列で表現する

# ライブラリのインポート
from math import sin, cos
from turtle import position  # mathというライブラリからsinとcosを使います，という意味．
import numpy as np         # numpyというライブラリをnpという名前で使います，という意味

# パラメータ
height_start = 0.0      # 初期高度[m]
height_finish = 0.0     # 演算終了高度[m]
angle = 70              # 地面に対する投射角[deg]
velocity_start = 100.0  # 初速度[m/s]
time_delta = 0.01       # 時間刻み幅[s]
gravity = np.array([0.0, 9.8], dtype=np.float64)  # 重力加速度

# 計算時の変数
time = 0.0      # 時間[s]
position = np.array([height_start*cos(angle*np.pi/180),
                    height_start*sin(angle*np.pi/180)], dtype=np.float64)
velocity = np.array([velocity_start*cos(angle*np.pi/180),
                    velocity_start*sin(angle*np.pi/180)], dtype=np.float64)

# 出力用変数
height_max = 0.0  # 最高高度[m]


# 計算部分
while (position[1] >= height_finish):
    velocity += ((-1) * gravity) * time_delta
    position += velocity * time_delta
    time += time_delta

    # 最高高度の更新
    if (position[1] > height_max):
        height_max = position[1]


# 出力
print("計算終了")
print("滞空時間:"+str(time))
print("最高高度:"+str(height_max))
print("水平方向落下距離:"+str(position[0]))
