define black_white_matrix = Matrix([
  1, 0, 0, 0,
  0.33, 0.33, 0.33, 0,
  0.33, 0.33, 0.33, 0,
  0, 0, 0, 1
])


init python:
  class BloodGreyRedtMatrix(ColorMatrix):
    def __init__(self, color):

        # Store the color given as a parameter.
        print(self, color)
        self.color = Color(color)

    def __call__(self, other, done):

        if type(other) is not type(self) and self.color is not None:

        # 没有原来的颜色，我们从self.color获取自身rgba数值
        # r, g, b = self.color.rgb
          print(self)
          r, g, b = self.color.rgb
          maxgb = g > b and g or b
          if(maxgb == 0 or self.color.rgb[0] / maxgb >= 1.5):
            return Matrix([
              1.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 1.0,
            ])
          else:
            return Matrix([
              1.0, 0.0, 0.0, 0.0,
              0.0, 1.0, 0.0, 0.0,
              0.0, 0.0, 1.0, 0.0,
              0.0, 0.0, 0.0, 1.0,
            ])

        else:
          return Matrix([
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0,
          ])

        # else:

        #     # 否则，我们从self.color和other.color分别获取rgba并进行计算结果
        #     oldr, oldg, oldb = other.color.rgb
        #     olda = other.color.alpha
        #     r, g, b = self.color.rgb
        #     a = self.color.alpha

        #     r = oldr + (r - oldr) * done
        #     g = oldg + (g - oldg) * done
        #     b = oldb + (b - oldb) * done
        #     a = olda + (a - olda) * done

        # # alpha预乘
        # r *= a
        # g *= a
        # b *= a

        # # 返回一个矩阵对象
        # return Matrix([ r, 0, 0, 0,
        #                 0, g, 0, 0,
        #                 0, 0, b, 0,
        #                 0, 0, 0, a ])

# 使用Transform类
transform blood_gray_red:
    # matrixcolor BloodGreyRedtMatrix("#f00")
    matrixcolor SepiaMatrix(tint='#ffeec2', desat=(0.2126, 0.7152, 0.0722))
    # matrixcolor SaturationMatrix(0.0).add(TintMatrix(Color(rgb=(1.0, 0.0, 0.0))))
    # matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
#     matrixcolor Matrix([
#   1, 0, 0, 0,
#   # 0.33, 0.33, 0.33, 0,
#   0,0,0,0,
#   0,0,0,0,
#   # 0.33, 0.33, 0.33, 0,
#   0, 0, 0, 1
# ])

    # matrixcolor gray_red_matrix # 使用之前定义的矩阵
    # 或者直接使用预定义的函数
# image blood_gray_red = "blood.png"

# 使用ATL
# image blood_gray_red = "blood.png":
#     matrixcolor gray_red_matrix # 使用之前定义的矩阵
    # 或者直接使用预定义的函数
    # matrixcolor SaturationMatrix(0.0) + TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))

# transform black_white_blood:
#   matrixcolor Matrix([
#     0.33, 0.33, 0.33, 0,
#     0.33, 0.33, 0.33, 0,
#     0.33, 0.33, 0.33, 0,
#     0, 0, 0, 1
#     ])