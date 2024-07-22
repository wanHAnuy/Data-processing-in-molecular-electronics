import os
import numpy as np
import matplotlib.pyplot as plt
from CaculateHistogram import single_1d_his


# 定义计算 delta_conductance 的函数，应只计算下降沿
def cacu_delta(data_load, bins=300, low_cut_1Dcon=-6, conductance_high_cut=0.5):
    conductance = data_load['conductance_array']
    conductance_1d = single_1d_his(conductance, bins=bins, conductance_low_cut=low_cut_1Dcon,
                                   conductance_high_cut=conductance_high_cut)
    mean_conductance_1d = np.mean(conductance_1d, axis=0)
    return conductance_1d - mean_conductance_1d


def cacu_cov(data, color_2d='coolwarm', vmin=-0.1, vmax=0.1, bins=300, low_cut_1Dcon=-6, conductance_high_cut=0.5,file_path2=None):
    # 计算 delta_conductance
    plt.close('all')
    delta_conductance = cacu_delta(data, bins=bins, low_cut_1Dcon=low_cut_1Dcon,
                                   conductance_high_cut=conductance_high_cut)

    # 截取长度
    len_num = min(len(delta_conductance), len(delta_conductance)) - 1
    delta_conductance = delta_conductance[:len_num]

    # 计算协方差
    H_cov = np.einsum('ij,ik->ijk', delta_conductance, delta_conductance)
    H_cov = np.mean(H_cov, axis=0)

    mean_delta_conductance_square = np.mean(np.square(delta_conductance), axis=0)

    # # 计算相关系数
    result = H_cov / np.sqrt(np.outer(mean_delta_conductance_square, mean_delta_conductance_square))
    # 上下翻转矩阵
    result = result[::-1]
    extent = [low_cut_1Dcon, conductance_high_cut, low_cut_1Dcon, conductance_high_cut]
    plt.imshow(result, cmap=color_2d, extent=extent, vmin=vmin, vmax=vmax)
    # 显示坐标轴# 计算方差
    # 设置 X 轴和 Y 轴的坐标轴范围
    extent = np.arange(low_cut_1Dcon, conductance_high_cut, (conductance_high_cut - low_cut_1Dcon) / bins).tolist()
    result = result[::-1]
    plt.axis('on')
    plt.colorbar()
    plt.title('Correlation coefficient analysis')
    folder_name = "png_images"
    image_path = os.path.join(folder_name, 'cacu_cov.png')
    parent_folder = os.path.dirname(file_path2)
    image_path2 = os.path.join(parent_folder, f'cacu_cov.eps')
    plt.savefig(image_path2, format='eps', dpi=400)
    # zip转换回去
    plt.savefig(image_path)
    return result, extent, image_path

