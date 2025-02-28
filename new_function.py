import os
import numpy as np
import matplotlib.pyplot as plt
import CaculateHistogram as cacu
from scipy.interpolate import interp1d
from CaculateHistogram import single_1d_his, calculate_his, chose_cluster
from PIL import Image
import matplotlib.mlab as mlab
from scipy.fftpack import fft


def devide_cluster(conductance, object_data=None, n_clusters=4, clusters_way=0):
    plt.close('all')
    conductance_normalized = object_data
    labels = chose_cluster(conductance_normalized, clusters_way=clusters_way, n_clusters=n_clusters)

    class_conductance = []  # 用于存储各个分类的conductance

    for i in range(n_clusters):
        class_i_indices = np.where(labels == i)[0]
        class_i_conductance = conductance[class_i_indices]
        # 存储每次循环的结果
        class_conductance.append(class_i_conductance)
    # 一次性计算所有结果,创建图表

    return class_conductance


def divide(conductance, distance, length, bins_1Dcon=200, low_cut_1Dcon=-6, high_cut_1Dcon=1, cacu_num=500):
    hist = []
    data = []
    hist_2d = []
    cacu_time = len(conductance) // cacu_num  # 每500个数据计算一次 整除，不算最后一组
    if cacu_time == 0:
        cacu.signal_window('Data is not enough!')
    else:
        for j in range(cacu_time):
            bin_edges_con, histogram_con, con_his_list = calculate_his(conductance[j * cacu_num:(j + 1) * cacu_num],
                                                                       bins_1Dcon=bins_1Dcon,
                                                                       low_cut_1Dcon=low_cut_1Dcon,
                                                                       high_cut_1Dcon=high_cut_1Dcon)
            conductance_array = conductance[j * cacu_num:(j + 1) * cacu_num]
            distance_array = distance[j * cacu_num:(j + 1) * cacu_num]
            length_array = length[j * cacu_num:(j + 1) * cacu_num]
            hist_2d.append(histogram_con)
            hist.append([bin_edges_con, histogram_con, con_his_list])
            # 'distance_array', 'conductance_array', 'length_array', 'additional_length'
            data.append([distance_array, conductance_array, length_array, len(distance_array)])
    return data, hist, cacu_time, hist_2d


def divide_merge(judgment_list, conductance, distance, length, cacu_num=500):
    cacu_time = len(conductance) // cacu_num + 1  # 每500个数据计算一次
    # Assuming conductance, distance, and length are already defined
    conductance_array = None
    distance_array = None
    length_array = None

    for j in range(cacu_time):
        if judgment_list[j] and distance_array is not None:
            if (j + 1) * cacu_num < len(conductance):
                conductance_array = np.concatenate((conductance_array, conductance[j * cacu_num:(j + 1) * cacu_num]))
                distance_array = np.concatenate((distance_array, distance[j * cacu_num:(j + 1) * cacu_num]))
                length_array = np.concatenate((length_array, length[j * cacu_num:(j + 1) * cacu_num]))
            else:
                conductance_array = np.concatenate((conductance_array, conductance[j * cacu_num:]))
                distance_array = np.concatenate((distance_array, distance[j * cacu_num:]))
                length_array = np.concatenate((length_array, length[j * cacu_num:]))
        elif judgment_list[j]:
            if (j + 1) * cacu_num < len(conductance):
                conductance_array = conductance[j * cacu_num:(j + 1) * cacu_num]
                distance_array = distance[j * cacu_num:(j + 1) * cacu_num]
                length_array = length[j * cacu_num:(j + 1) * cacu_num]
            else:
                conductance_array = conductance[j * cacu_num:]
                distance_array = distance[j * cacu_num:]
                length_array = length[j * cacu_num:]

    # 'distance_array', 'conductance_array', 'length_array', 'additional_length'
    data = [distance_array, conductance_array, length_array, distance_array.shape[0]]
    return data


def draw_divide(conductance, distance, length, bins_1Dcon=400, low_cut_1Dcon=-6, high_cut_1Dcon=1,
                cacu_num=600, color_1d='blue', color_2d='jet', red=1000, file_path2=None):
    data, hist, cacu_time, hist_2d = divide(conductance, distance, length, bins_1Dcon=bins_1Dcon,
                                            low_cut_1Dcon=low_cut_1Dcon,
                                            high_cut_1Dcon=high_cut_1Dcon,
                                            cacu_num=cacu_num)
    fig, axes = plt.subplots(1, int(cacu_time + 2), figsize=((cacu_time + 2) * 3, 2.5))
    row_variances = []
    for j in range(cacu_time + 2):
        if j > 1:
            bin_edges_con, histogram_con, con_his_list = hist[j - 2]
            axes[j].bar(bin_edges_con[:-1], histogram_con, width=np.diff(bin_edges_con), align='edge', color=color_1d)
            axes[j].set_title(f'batch {j - 1}')
            axes[j].set_xlabel('conductance')
            axes[j].grid(True)  # 显示网格线
        elif j == 0:
            im0 = axes[0].imshow(np.array(hist_2d), cmap=color_2d, aspect='auto', origin='lower',
                                 extent=[low_cut_1Dcon, high_cut_1Dcon, 1, cacu_time], vmax=red)

            axes[0].set_title('Time Histogram')
            axes[0].set_xlabel('Conductance(logG)')
            axes[0].set_ylabel('batch')
            plt.colorbar(im0, ax=axes[0])
        else:
            row_variances = np.var(hist_2d, axis=1) / len(hist_2d[0])  # 方差曲线
            var_variances = np.var(row_variances) / cacu_time
            axes[1].plot(row_variances, range(cacu_time))
            axes[1].set_title(f'var_variances={round(var_variances, 1)}')
            axes[1].set_ylabel('batch')
            axes[1].set_xlabel('variances')
            axes[1].grid(True)  # 显示网格线

    plt.tight_layout()
    folder_name = "png_images"
    image_path = os.path.join(folder_name, 'draw_divide.png')
    plt.savefig(image_path, dpi=200)

    # # 保存方差曲线为 EPS 文件
    # axes[0].set_visible(True)  # 仅显示方差曲线子图
    # axes[0].set_frame_on(True)  # 显示框架
    # parent_folder = os.path.dirname(file_path2)
    # eps_path = os.path.join(parent_folder, 'Time Histogram.eps')
    # plt.savefig(eps_path, format='eps')  # 保存为 EPS 文件
    # plt.close()

    hist_2d_data = [np.array(hist_2d), row_variances]
    return data, image_path, hist_2d_data


def peak_divide(conductance, distance, bins_1Dcon=50, his_1d_dis_0=1,
                his_1d_dis_1=2, cacu_num=500, peak=-3.5):
    bin_edges = []
    hist_2d = []
    cacu_time = len(conductance) // cacu_num  # 每500个数据计算一次
    if cacu_time == 0:
        cacu.signal_window("Data is not enough!")

    for j in range(cacu_time):
        his = research_peak_length_his(distance[j * cacu_num:(j + 1) * cacu_num],
                                       conductance[j * cacu_num:(j + 1) * cacu_num], peak=peak)
        histogram_con, bin_edges_con = np.histogram(his, bins=bins_1Dcon, range=(his_1d_dis_0, his_1d_dis_1))

        hist_2d.append(histogram_con)
        bin_edges.append(bin_edges_con)
    return cacu_time, hist_2d, bin_edges


def peak_draw_divide(conductance, distance, bins_1Dlen=50, his_1d_dis_0=0, his_1d_dis_1=2,
                     cacu_num=600, color_1d='blue', color_2d='jet', peak=-3.5, red=1000, file_path2=None):
    cacu_time, hist_2d, bin_edges = peak_divide(conductance, distance, bins_1Dcon=bins_1Dlen,
                                                his_1d_dis_0=his_1d_dis_0,
                                                his_1d_dis_1=his_1d_dis_1,
                                                cacu_num=cacu_num, peak=peak)
    hist_2d_data = np.array(hist_2d)
    fig, axes = plt.subplots(1, int(cacu_time + 1), figsize=((cacu_time + 1) * 3, 3))

    for j in range(cacu_time):
        if j == 0:
            cax = axes[0].imshow(np.array(hist_2d), cmap=color_2d, aspect='auto', origin='lower',
                                 extent=[his_1d_dis_0, his_1d_dis_1, 1, cacu_time], vmax=red)
            axes[0].set_ylabel('batch')
            axes[0].set_xlabel('distance (nm)')
            plt.colorbar(cax, ax=axes[0], label='Counts')  # 绘制颜色条并设置标签

        else:
            axes[j].bar(bin_edges[j - 1][:-1], hist_2d[j - 1], width=np.diff(bin_edges[j - 1]), align='edge',
                        color=color_1d)
            axes[j].set_title(f'batch {j}')
            axes[j].set_xlabel('distance (nm)')
            axes[j].grid(True)  # 显示网格线

    plt.tight_layout()
    folder_name = "png_images"
    image_path = os.path.join(folder_name, 'draw_divide_peak.png')
    plt.savefig(image_path, dpi=200)
    plt.close()

    return image_path, hist_2d_data


# 0. 进行批次聚类处理
# 1. 选择分类方式并进行分类,返回数据
# 2. 计算His并进行绘图，绘制所有批次
# 3. 点击保存时将在原始文件夹中保存，仅保存single_trance数据以及大图像（在页面{一}中可以保存其他类型数据）

def cacu_mix_his(source_con, cacu_time, all_object_data, bins_1Dcon=200, low_cut_1Dcon=-6, high_cut_1Dcon=1,
                 n_clusters=2,
                 clusters_way=0, cacu_num=600, len_conductance=2000):
    file_path = []
    for j in range(cacu_time):
        _, con, _, _ = source_con[j]

        if (j + 1) * cacu_num < len_conductance:
            object_data = all_object_data[j * cacu_num:(j + 1) * cacu_num]

        else:
            object_data = all_object_data[j * cacu_num:]

        cluster_con = devide_cluster(con, object_data=object_data, n_clusters=n_clusters, clusters_way=clusters_way)
        for i in range(len(cluster_con) + 1):
            if i == 0:
                bin_edges_con, histogram_con, _ = calculate_his(con,
                                                                bins_1Dcon=bins_1Dcon,
                                                                low_cut_1Dcon=low_cut_1Dcon,
                                                                high_cut_1Dcon=high_cut_1Dcon)

            else:
                bin_edges_con, histogram_con, _ = calculate_his(cluster_con[i - 1],
                                                                bins_1Dcon=bins_1Dcon,
                                                                low_cut_1Dcon=low_cut_1Dcon,
                                                                high_cut_1Dcon=high_cut_1Dcon)

            plt.bar(bin_edges_con[:-1], histogram_con, width=np.diff(bin_edges_con), align='edge', alpha=0.65)
            folder_name = "png_images"
            Source_data_file_path = os.path.join(folder_name, f'combined_hist_{j}.png')
            plt.savefig(Source_data_file_path)
            file_path.append(Source_data_file_path)
    plt.tight_layout(pad=0)
    plt.close('all')

    fig, axes = plt.subplots(1, int(cacu_time), figsize=(4 * cacu_time, 3))
    for j in range(cacu_time):
        img = Image.open(file_path[j])
        if cacu_time == 1:
            ax = axes
        else:
            ax = axes[j]

        ax.imshow(img)
        ax.axis('off')  # 隐藏坐标轴
        ax.set_title(f'batch {j + 1} cluster', fontsize=10, y=-0.02)
    plt.tight_layout(pad=0)
    folder_name = "png_images"
    image_path = os.path.join(folder_name, 'cluster_divide.png')
    plt.savefig(image_path, dpi=188)
    plt.close()

    return image_path


#  采样函数
def sample(data, number):
    # 期望的采样点数量
    desired_sample_points = number
    x = np.arange(len(data))
    f = interp1d(x, data, kind='linear')  # 使用线性插值
    x_new = np.linspace(0, len(data) - 1, desired_sample_points)  # 生成新的采样点
    interpolated_curve = f(x_new)

    return interpolated_curve


# 峰值查找
def research_peak_length_his(distance, conductance, peak):
    peak_range = [peak - 0.1, peak + 0.1]
    stage = []
    for i in range(len(conductance)):
        # 每曲线降维至1D电导直方图
        bin_counts2, bin_edges_con = np.histogram(conductance[i], bins=20, range=peak_range)
        # 寻找局域峰值
        con = bin_edges_con[np.argmax(bin_counts2)]
        # # 寻找该con值邻域内的所有点的坐标索引
        index = np.where(np.abs(conductance[i] - con) <= 0.1)[0]
        # # 寻找该索引的最大值作为峰值
        if len(index) != 0:
            stage.append(distance[i][max(index)])
    return stage


def class_for_one(distance, conductance, length, low_cut_1Dcon=-5.5, similar=0.2, bins=100, conductance_high_cut=-0.5,
                  p=2,
                  i=0, distance_2=None, conductance_2=None, correlation=False):
    conductance_1d = single_1d_his(conductance, bins=bins, conductance_low_cut=low_cut_1Dcon,
                                   conductance_high_cut=conductance_high_cut)  # 投影至1dhis

    mean_conductance_1d = np.mean(conductance_1d, axis=0)
    std_conductance_1d = np.std(conductance_1d, axis=0)

    # 标准化 x
    normalized_x = (conductance_1d - mean_conductance_1d) / std_conductance_1d

    if distance_2 is not None:  # 如果进行异类查找
        conductance_1d_2 = single_1d_his(conductance_2, bins=bins, conductance_low_cut=low_cut_1Dcon,
                                         conductance_high_cut=conductance_high_cut)  # 投影至1dhis

        mean_conductance_1d_2 = np.mean(conductance_1d_2, axis=0)
        std_conductance_1d_2 = np.std(conductance_1d_2, axis=0)

        # 标准化 x
        normalized_x_2 = (conductance_1d_2 - mean_conductance_1d_2) / std_conductance_1d_2
        x1 = normalized_x_2[i]
    else:
        x1 = normalized_x[i]

    sorted_conductance_cut = []
    sorted_distance_cut = []
    sorted_length = []

    if correlation is False:
        minkowski_distance = []
        # 计算闵氏距离，例如 p=2 对应欧氏距离
        for j in range(len(normalized_x)):
            minkowski_distance_single = np.linalg.norm(normalized_x[j] - x1, ord=p)
            minkowski_distance.append(minkowski_distance_single)

        sorted_indices = np.argsort(minkowski_distance)

    else:
        correlation = []
        # 计算相关距离
        for j in range(len(normalized_x)):
            correlation_single = np.corrcoef(normalized_x[j] - x1)
            correlation.append(correlation_single)

        sorted_indices = np.argsort(correlation)

    # 使用排序后的索引对其他数组进行排序
    for j in range(len(normalized_x)):
        sorted_conductance_cut.append(conductance[sorted_indices[j]])
        sorted_distance_cut.append(distance[sorted_indices[j]])
        sorted_length.append(length[sorted_indices[j]])

    # 绘图
    split_index = int(len(sorted_conductance_cut) * similar)
    class_1_conductance = np.array(sorted_conductance_cut[:split_index])
    class_1_distance = np.array(sorted_distance_cut[:split_index])
    class_1_length = sorted_length[:split_index]

    class_2_conductance = np.array(sorted_conductance_cut[split_index:])
    class_2_distance = np.array(sorted_distance_cut[split_index:])
    class_2_length = sorted_length[split_index:]

    datas = [[class_1_distance, class_2_distance],
             [class_1_conductance, class_2_conductance], [class_1_length, class_2_length]]
    return datas


def Denoising_preprocessing(data):
    conductance = []
    tran_X = []
    if len(data['conductance_array'][0]) == 1000:  # !!!!!!!!!!!!
        conductance.append(data['conductance_array'])

    else:
        alfa = int(len(data['conductance_array'][0]) / 1000)
        conductance_array = data['conductance_array']
        for i in range(len(data['conductance_array'])):
            conductance.append(conductance_array[i][::alfa])

    for i in range(len(conductance)):
        mole_array = np.array(conductance[i][::2])  # 1000/12 = 84 个点为输入大小
        tran_X.append(mole_array)
    tran_X = (tran_X - np.min(tran_X)) / (np.max(tran_X) - np.min(tran_X))  # 归一化
    tran_X = np.array(tran_X)
    return tran_X


def save_data_iv(listX=None, list_pathX=None, histX=None, hist_pathX=None):
    # 保存列表
    if listX is not None and len(listX) > 0:
        with open(list_pathX, 'w') as file:
            for item in listX:
                formatted_values = ['%.2f' % val for val in item]  # 将元素保留两位小数
                line = '\t'.join(formatted_values)  # 使用制表符分隔格式化后的元素
                file.write(line + '\n')  # 写入每个子列表，并添加换行符
                file.write('\n\n')  # 添加两个换行符
    if histX is not None and len(histX) > 0:
        # 保存直方图
        with open(hist_pathX, 'w') as file:
            for row in histX:
                formatted_row = [f'{int(element):<6}' for element in row]  # 使用格式化字符串对齐每个元素的整数部分
                line = ' '.join(formatted_row) + '\n'
                file.write(line)


def set_progressbar_style(progressbar, height):
    progressbar.setStyleSheet(f"""
        QProgressBar {{
            border: 1px solid rgb(33, 37, 43);
            background-color: rgb(33, 37, 43);
            height: {height}px;
        }}

        QProgressBar::chunk {{
            background-color: rgb(201, 157, 229);
            width: 20px;
        }}
    """)


def make_forder():  # 定义要创建的文件夹名称
    folder_name = "png_images"
    # 创建文件夹（如果不存在）
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def getMinNInterval(gMean, integPSD):
    """

    :param gMean:
    :param integPSD:
    :return:
    """
    if gMean.shape[0] == 0:
        cacu.signal_window('window size is too big!!!please change it!!!')
        return 0
    exponentIdx = np.arange(0.5, 2.5, 0.005)
    minNIdx = [getMinHelper(gMean, integPSD, k) for k in exponentIdx]
    # print(minNIdx)

    # plt.plot(exponentIdx, [i[0] for i in minNIdx])
    # plt.xlabel("n")
    # plt.ylabel("corrcoef")
    return sorted(minNIdx)[0][1], exponentIdx, [i[0] for i in minNIdx]


def getMinHelper(gMean, integPSD, exponent):
    try:
        gMeanPower = np.power(gMean, exponent)
        scaledPSD = integPSD / gMeanPower
        coef = np.corrcoef(scaledPSD, gMean)[0, 1]
    except Exception as e:
        errMsg = f"minNIdx计算异常：{e}"
        # cls.logger.error(errMsg)
        return np.inf, exponent
    else:
        return np.abs(coef), exponent


def getIntegPSD(GArray, freqLow, freqHigh, keyPara, mode="mlab", CUT_num=0, CUT_time=0):
    """
    使用mlab.psd()或幅度谱平方求psd；并返回电导均值
    :param keyPara: 界面配置参数
    :param condData: 对数电导单条曲线
    :param mode:计算模式
    :return: psd的积分, 平均电导
    """
    windowSize = int(keyPara["le_WindowSize"])

    a = windowSize // (CUT_num + 1)

    if np.count_nonzero(GArray) < windowSize:
        return 0.0, 0.0
    else:
        try:
            GArray_0 = GArray[GArray != 0][:windowSize]
            GArray = GArray_0[CUT_time * a: CUT_time * a + a]
            gMean = np.mean(GArray)
            N = len(GArray)
            sampFreq = keyPara["le_Frequence"]
            if mode == "mlab":
                psd, freqs = mlab.psd(GArray, NFFT=N, sides='onesided',
                                      Fs=sampFreq, window=mlab.window_hanning,
                                      pad_to=N, scale_by_freq=False)
                psd *= 2  # 与手算的相差系数2
            else:
                fftRes = fft(GArray)
                fftResAbs = np.abs(fftRes)
                resNorm = fftResAbs / (N / 2)
                resNorm[0] /= 2

                freqs = np.linspace(0, sampFreq // 2, N // 2)
                oneSideFFT = resNorm[:N // 2]
                psd = oneSideFFT ** 2

            integRangeIdx = np.where((freqs >= freqLow) & (freqs <= freqHigh))[0]
            # integPSD = integrate.trapz(psd[integRangeIdx], freqs[integRangeIdx])
            integPSD = np.trapz(psd[integRangeIdx], freqs[integRangeIdx])
        except Exception as e:

            return 0.0, 0.0
        else:
            return integPSD, gMean


def getminN(logGArray, keyPara, CUT_num=0, CUT_time=0):
    logGHigh, logGLow = keyPara["le_CondHigh"], keyPara["le_CondLow"]
    logGArraySelect = np.where((logGArray >= logGLow) & (logGArray <= logGHigh), logGArray, -np.inf)   # 为什么是 -np.inf？？？？？

    gArraySelect = np.power(10.0, logGArraySelect)  # 将对数尺度的导电率数据转换为线性尺度。

    # 计算psd  GArray,gMean, freqLow, freqHigh, keyPara, mode="mlab"
    resultTemp = np.apply_along_axis(getIntegPSD, 1, gArraySelect, 100, 1000, keyPara, CUT_num=CUT_num,
                                     CUT_time=CUT_time)
    integPSD, gMean = resultTemp[:, 0], resultTemp[:, 1]
    finalIdx = np.where(integPSD != 0.0)

    gMean = gMean[finalIdx]
    integPSD = integPSD[finalIdx]
    if getMinNInterval(gMean, integPSD)!=0:
        minN, exponentIdx, minNIdx = getMinNInterval(gMean, integPSD)

        return minN, gMean, integPSD, exponentIdx, minNIdx  # N值计算/直方图绘图元素/过程图绘图
    else: return 0

# def Denoising(tran_X, data, predict_val=0.5):
#     # 加载模型
#     loaded_model = tf.keras.models.load_model('noise_signal_model.keras')
#     predictions = loaded_model.predict(tran_X)
#     # 数据初始化
#     conductance_signal = []
#     conductance_noise = []
#     distance_signal = []
#     distance_noise = []
#     length_signal = []
#     length_noise = []
#
#     conductance_array = data['conductance_array']
#     distance_array = data['distance_array']
#     length_array = data['length_array']
#
#     for i in range(len(predictions)):
#         if predictions[i] > predict_val:
#             conductance_signal.append(conductance_array[i])
#             distance_signal.append(distance_array[i])
#             length_signal.append(length_array[i])
#         else:
#             conductance_noise.append(conductance_array[i])
#             distance_noise.append(distance_array[i])
#             length_noise.append(length_array[i])
#
#     distance_signal = np.array(distance_signal)
#     conductance_signal = np.array(conductance_signal)
#     length_signal = np.array(length_signal)
#
#     distance_noise = np.array(distance_noise)
#     conductance_noise = np.array(conductance_noise)
#     length_noise = np.array(length_noise)
#
#     datas = [[distance_signal, distance_noise],
#              [conductance_signal, conductance_noise], [length_signal, length_noise]]
#     return datas


# def extract_features_cwt(data):
#     # 假设您有一个名为data的数组，包含您的原始数据
#     widths = (2, 5, 10, 20)  # 您指定的宽度
#     coefficients_list = []
#     for width in widths:
#         for i in range(6, 15):  # 6到14是您提供的系数
#             coefficients, _ = pywt.cwt(data, np.arange(1, width), 'morl')  # 使用Morlet小波进行连续小波变换
#             # 这里，'morl'代表Morlet小波，您可以选择其他小波函数
#             # 如果您的数据不是随机生成的，请将data替换为您的实际数据
#
#             coeff_value = coefficients[i]  # 提取特定的系数
#             coefficients_list.append(coeff_value)
#     return coefficients_list
#     # 现在，coefficients_list包含了您所需的系数
#     # 您可以将其进一步处理，或者根据需要进行操作
#
#     # 对于您所提供的系数，您可以使用类似的方法来获取它们
#
#
# def TSCFE(conductance):
#     # Time Series Classification Feature Extraction (TSCFE)
#     # 时间序列分类特征提取（TSCFE）
#     CustomFeatures = []
#     object_data = single_1d_his(conductance, bins=100, conductance_low_cut=-5.5, conductance_high_cut=-1.5)
#     for data in object_data:
#         CustomFeatures.append(extract_features_cwt(data))
#     # 未添加归一化
#     selected_features = np.vstack(CustomFeatures)
#     selected_features = np.transpose(selected_features)
#
#     return selected_features
