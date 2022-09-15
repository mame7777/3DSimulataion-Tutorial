# 滞空時間:19.2 s
# 最高高度:450.1 m
# 落下位置(N,E):(96.9, -648.5)

# 3*1行列で表現

# ライブラリのインポート
from math import sin, cos
import numpy as np


def main():
    Parameter = Param()
    calculation = calc(Parameter)
    calculation.calc(Parameter)

    # 出力
    print("計算終了")
    print("滞空時間:"+str(calculation.time))
    print("最高高度:"+str(calculation.height_max))
    print("落下位置(N,E):(" + \
        str(calculation.position[1, 0])+", "+str(calculation.position[2, 0])+")")

# パラメータ
class Param:
    def __init__(self):
        self.height_start = 0.0       # 初期高度[m]
        self.height_finish = 0.0      # 演算終了高度[m]
        self.angle_elevation = 70     # 地面に対する仰角[deg]
        self.angle_direction = 278.5  # 方位角[deg]
        self.velocity_start = 100.0   # 初速度[m/s]
        self.time_delta = 0.01        # 時間刻み幅[s]
        self.gravity = np.array([[-9.8], [0.0], [0.0]], dtype=np.float64)  # 重力加速度


class calc:
    def __init__(self, Param: Param):
        # 計算時の変数
        self.time = 0.0      # 時間[s]
        self.position = np.array([[Param.height_start], [0.0], [0.0]], dtype=np.float64)
        self.velocity = np.array([[Param.velocity_start*sin(Param.angle_elevation*np.pi/180)], \
                                [Param.velocity_start*cos(Param.angle_elevation*np.pi/180)*cos(Param.angle_direction*np.pi/180)], \
                                [Param.velocity_start*cos(Param.angle_elevation*np.pi/180)*sin(Param.angle_direction*np.pi/180)]], \
                                dtype=np.float64)

        # 出力用変数
        self.height_max = 0.0  # 最高高度[m]

    def calc(self, Param: Param) -> None:
        while (self.position[0, 0] >= Param.height_finish):
            self.velocity += Param.gravity * Param.time_delta
            self.position += self.velocity * Param.time_delta
            self.time += Param.time_delta

            # 最高高度の更新
            if (self.position[0, 0] > self.height_max):
                self.height_max = self.position[0, 0]


if __name__ == "__main__":
    main()
