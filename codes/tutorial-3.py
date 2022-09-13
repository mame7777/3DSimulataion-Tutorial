# 滞空時間:19.2 s
# 最高高度:450.1 m
# 落下位置(N,E):(96.9, -648.5)

# 3*1行列で表現

# ライブラリのインポート
from math import sin, cos
import numpy as np

# パラメータ
height_start = 0.0       # 初期高度[m]
height_finish = 0.0      # 演算終了高度[m]
angle_elevation = 70     # 地面に対する仰角[deg]
angle_direction = 278.5  # 方位角[deg]
velocity_start = 100.0   # 初速度[m/s]
time_delta = 0.01        # 時間刻み幅[s]
gravity = np.array([[-9.8], [0.0], [0.0]], dtype=np.float64)  # 重力加速度

# 計算時の変数
time = 0.0      # 時間[s]
position = np.array([[height_start], [0.0], [0.0]], dtype=np.float64)
velocity = np.array([[velocity_start*sin(angle_elevation*np.pi/180)],
                    [velocity_start*cos(angle_elevation*np.pi/180)*cos(angle_direction*np.pi/180)],
                    [velocity_start*cos(angle_elevation*np.pi/180)*sin(angle_direction*np.pi/180)]],
                    dtype=np.float64)

# 出力用変数
height_max = 0.0  # 最高高度[m]


# 計算部分
while (position[0,0] >= height_finish):
    velocity += gravity * time_delta
    position += velocity * time_delta
    time += time_delta

    # 最高高度の更新
    if (position[0,0] > height_max):
        height_max = position[0, 0]


# 出力
print("計算終了")
print("滞空時間:"+str(time))
print("最高高度:"+str(height_max))
print("落下位置(N,E):("+str(position[1,0])+", "+str(position[2,0])+")")
