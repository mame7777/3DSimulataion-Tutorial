# 鉛直上方向を正とする

# パラメータ
height_start = 0.0      # 初期高度[m]
height_finish = 0.0     # 演算終了高度[m]
velocity_start = 100.0  # 初速度[m/s]
time_delta = 0.01     # 時間刻み幅[s]
gravity = 9.8         # 重力加速度

# 計算時の変数
time = 0.0      # 時間[s]
height = 0.0    # 高度[m]
velocity = 0.0  # 速度[m/s]

# 値の初期化
height = height_start
velocity = velocity_start


# 計算部分
while (height >= height_finish):
    velocity += ((-1) * gravity) * time_delta
    height +=  velocity * time_delta
    time += time_delta


# 出力
print("計算終了\n滞空時間:"+str(time))
