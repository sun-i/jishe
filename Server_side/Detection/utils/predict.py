import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from Detection.nets.u_net import U_Net

if __name__ == '__main__':
    unet = U_Net()
    img = input('Input image filename:')
    prob, pred = unet.predict(img)
    # 输出预测结果
    print('prob:', prob)
    # 显示拼接后的图片
    plt.imshow(pred)
    plt.show()






