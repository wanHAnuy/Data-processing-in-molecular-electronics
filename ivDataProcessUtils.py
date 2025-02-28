# -*- coding: utf-8 -*-
# @Time   : 2023/12/12 22:21
# @Author : Gang/wang
# @File   : ivDataProcessUtils.py
import copy
import os
import matplotlib.pyplot as plt
from nptdms import TdmsFile
import numpy as np
import CaculateHistogram as cacu
import statsmodels.api as sm


def cacu_3fig(V_data, logI_data, logG, I_data, butter_parameter=1, sample_point=1000, label='data', bin_1dhis=400,
              bin_2dhis=200, threshold=255, logI_min_max=None, logdI_min_max=None, logG_min_max=None, I_min_max=None,
              color_2d='jet'):
    if logI_min_max is None:
        logI_min_max = [-3, 3]
    if logdI_min_max is None:
        logdI_min_max = [-3, 3]
    if logG_min_max is None:
        logG_min_max = [-6, -1]
    if I_min_max is None:
        I_min_max = [-1e-6, 1e-6]
    V_data_sample = cacu.sample_data(V_data, sample_point)
    I_data_sample = cacu.sample_data(I_data, sample_point)
    logI_data_sample = cacu.sample_data(logI_data, sample_point)
    logG_sample = cacu.sample_data(logG, sample_point)

    I_data_sample_derivative_list = []

    for i in range(len(I_data_sample)):
        # 使用滤波器过滤信号
        x = V_data_sample[i]
        y = I_data_sample[i]

        # 使用加权线性最小二乘法和二次多项式模型进行局部回归
        lowess = sm.nonparametric.lowess
        y_smoothed = lowess(y, x, frac=0.01 * butter_parameter, it=0, delta=0.0, is_sorted=False, missing='drop',
                            return_sorted=True)

        # 提取平滑后的数据
        smoothed_x, smoothed_y = zip(*y_smoothed)

        I_data_sample_derivative = np.log10(np.abs(np.gradient(smoothed_y, smoothed_x)))
        I_data_sample_derivative_list.append(I_data_sample_derivative)

    I_data_sample_derivative_list = np.array(I_data_sample_derivative_list)

    hist_logI, extent_logI, edg_logI = cacu.plt_2dIV(V_data_sample, logI_data_sample, bin_1dhis=bin_1dhis,
                                                     bin_2dhis=bin_2dhis,
                                                     threshold=threshold, range_y=[logI_min_max[0], logI_min_max[1]])

    hist_logDI, extent_logDI, edg_logDI = cacu.plt_2dIV(V_data_sample, I_data_sample_derivative_list,
                                                        bin_1dhis=bin_1dhis,
                                                        bin_2dhis=bin_2dhis, threshold=threshold,
                                                        range_y=[logdI_min_max[0], logdI_min_max[1]])

    hist_logG, extent_logG, edg_logG = cacu.plt_2dIV(V_data_sample, logG_sample, bin_2dhis=bin_2dhis,
                                                     bin_1dhis=bin_1dhis,
                                                     threshold=threshold, range_y=[logG_min_max[0], logG_min_max[1]])

    hist_I, extent_I, edg_I = cacu.plt_2dIV(V_data_sample, I_data_sample, bin_2dhis=bin_2dhis, bin_1dhis=bin_1dhis,
                                            threshold=threshold, range_y=[I_min_max[0], I_min_max[1]])

    fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(20, 3.7))
    im0 = ax[0].imshow(hist_logI.T, origin='lower', extent=extent_logI, aspect='auto', cmap=color_2d)
    ax[0].set_title(f'log(I(nA)) 2D histogram({label})')
    ax[0].set_xlabel('V(V)')
    ax[0].set_ylabel('log(I(nA))')
    im1 = ax[1].imshow(hist_logDI.T, origin='lower', extent=extent_logDI, aspect='auto', cmap=color_2d)
    ax[1].set_title(f'log(dI/dV) 2D histogram({label})')
    ax[1].set_xlabel('V(V)')
    ax[1].set_ylabel('log(dI/dV)')
    im2 = ax[2].imshow(hist_logG.T, origin='lower', extent=extent_logG, aspect='auto', cmap=color_2d)
    ax[2].set_title(f'log(G/G0) 2D histogram({label})')
    ax[2].set_xlabel('V(V)')
    ax[2].set_ylabel('log(G/G0)')

    im3 = ax[3].imshow(hist_I.T, origin='lower', extent=extent_I, aspect='auto', cmap=color_2d)
    ax[3].set_title(f'I 2D histogram({label})')
    ax[3].set_xlabel('V(V)')
    ax[3].set_ylabel('I(mA)')

    plt.colorbar(im0, ax=ax[0])
    plt.colorbar(im1, ax=ax[1])
    plt.colorbar(im2, ax=ax[2])
    plt.colorbar(im3, ax=ax[3])

    plt.tight_layout()
    folder_name = "png_images"
    # 返回 :
    # 1. 图像地址
    image_path0 = os.path.join(folder_name, f'IVfig{label}.png')

    plt.savefig(image_path0, dpi=100)

    # image_path2 = os.path.join(folder_name, f'IVfig{label}.eps')
    # plt.savefig(image_path2, format='eps', dpi=100)


    # 2. 图像数据
    his_data = (hist_logI, hist_logDI, hist_logG, hist_I, edg_logI, edg_logDI, edg_logG, edg_I)
    # 3.处理后数据
    data = (V_data_sample, logI_data_sample, I_data_sample_derivative_list, logG_sample, I_data_sample)
    return his_data, data


class IVDataProcessUtils:
    # logger = MyLog("IVDataProcessUtils", BASEDIR)

    @classmethod
    def loadTMDSFile(cls, filePath):
        """
        加载tdms文件（单个）
        :param filePath:
        :param file_path:tdms文件路径
        :return:采样电压（numpy）
        """
        with TdmsFile.open(filePath) as tdmsFile:
            biasVolt = tdmsFile.groups()[0].channels()[0][:]  # 此处读完数据就是numpy数组了
            current = tdmsFile.groups()[0].channels()[1][:]
            cond = tdmsFile.groups()[0].channels()[2][:]
        return [biasVolt, current, cond]

    @classmethod
    # def hysteresis(cls, filePath, keyPara):
    def hysteresis(cls, filePath, bias_base=0.1, peakStart=-2.5, peakEnd=-5.5):

        biasVolt, current, cond = cls.loadTMDSFile(filePath)
        # bias_base = keyPara['le_Bias']
        biasVTrace, currentTrace, condTrace = [], [], []
        diffBiasV = np.concatenate((np.diff(biasVolt), np.array([10.0])))
        # 偏压从0.1到0.2阶跃中0.2v处的索引
        start_candi = \
            np.where((np.isclose(biasVolt, bias_base, 0.0001)) & (np.isclose(diffBiasV, bias_base, 0.0001)))[0] + 1

        # 从0.2到0.1的阶跃中0.2处的索引
        end_candi = \
            np.where((np.isclose(biasVolt, bias_base * 2, 0.0001)) & (np.isclose(diffBiasV, -bias_base, 0.0001)))[0]
        # 确保每个对应位置上结束点索引大于起始点索引
        startIdx = []
        endIdx = []
        for i in range(len(start_candi)):
            end_i = end_candi[end_candi > start_candi[i]]
            if len(end_i) > 0:
                startIdx.append(start_candi[i])
                endIdx.append(end_i[0])
        startIdx = np.array(startIdx)
        endIdx = np.array(endIdx)

        # 确保扫描区间没有超过总长度，同时保证结束点的电压是0.1
        # strat是第一个为0.2的index  end是最后一个为0.2的点！！
        endIdx = endIdx + 200
        trueIdx = endIdx < biasVolt.shape[0]
        endIdx = endIdx[trueIdx]  # 这里直接使用了布尔索引！！
        if trueIdx.shape[0] != 0:
            startIdx = startIdx[trueIdx]
            biasVoltEnd = biasVolt[endIdx]
            tempIdx = np.where(np.isclose(biasVoltEnd, bias_base, 0.0001))[0]
            endIdx = endIdx[tempIdx]
            startIdx = startIdx[tempIdx]

        # 得到扫面区间，接下来就是把中间的切开！！
        for i in range(startIdx.shape[0]):
            biasVTrace.append(biasVolt[startIdx[i]:endIdx[i]])
            currentTrace.append(current[startIdx[i]:endIdx[i]])
            condTrace.append(cond[startIdx[i]:endIdx[i]])
        biasVTrace = np.array(biasVTrace, dtype='object')
        currentTrace = np.array(currentTrace, dtype='object')
        condTrace = np.array(condTrace, dtype='object')

        if biasVTrace.shape[0] == 0:
            return None, None, None

        # 寻找电压是0v的起始和终点
        cutStart, cutEnd = np.ones(biasVTrace.shape[0], dtype=int), np.ones(biasVTrace.shape[0], dtype=int)
        for i in range(biasVTrace.shape[0]):
            zero_idx = np.where(np.isclose(biasVTrace[i], 0, 0.0001))[0]
            # TODO 起点处可以也有波动，起点可以按照开始阶段的最后一个0来算，但终点需要根据最后一个peak来计算，从peak开始遍历找到第一个变号的地方
            for j in range(zero_idx.shape[0] - 1):  # 找到正式扫描的起点
                if (zero_idx[j + 1] - zero_idx[j] > 1) and (biasVTrace[i][zero_idx[j] + 1] != 0):
                    cutStart[i] = zero_idx[j]
                    break
            if cutStart[i] == 1:
                continue
            # 寻找可能的终点
            zero_end = 1
            for j in range(zero_idx.shape[0] - 1, 0, -1):
                if zero_idx[j] - zero_idx[j - 1] > 1:
                    zero_end = zero_idx[j]
                    break
            if zero_end == 1:
                continue
            trace = biasVTrace[i]
            peak_index = np.where((trace == trace.min()) | (trace == trace.max()))[0]
            first_peak = peak_index[0]
            if biasVTrace[i][first_peak] > 0 and biasVTrace[i][zero_end - 1] > 0:  # 从0到1，结尾必须从-1到0
                for j in range(zero_end - 1, 0, -1):
                    if biasVTrace[i][j] <= 0 and biasVTrace[i][j + 1] > 0:
                        zero_end = j
                        break
            elif biasVTrace[i][first_peak] < 0 and biasVTrace[i][zero_end - 1] < 0:  # 从0到-1，结尾必须从1到0
                for j in range(zero_end - 1, 0, -1):
                    if biasVTrace[i][j] >= 0 and biasVTrace[i][j + 1] < 0:
                        zero_end = j
                        break
            cutEnd[i] = zero_end

        # 删除bad boys
        trueIndex = np.where((cutStart == 1) | (cutEnd == 1), False, True)
        biasVTrace = biasVTrace[trueIndex]
        currentTrace = currentTrace[trueIndex]
        condTrace = condTrace[trueIndex]
        cutStart = cutStart[trueIndex]
        cutEnd = cutEnd[trueIndex]

        # 再次检查！！！
        if biasVTrace.shape[0] == 0:
            return None, None, None

        max_len = np.max([len(i) for i in biasVTrace])
        biasVTrace_same_len = [np.pad(trace, (0, max_len - len(trace)), 'edge') for trace in biasVTrace]
        biasVTrace_same_len = np.array(biasVTrace_same_len)
        diffBiasTrace = np.concatenate(
            (np.diff(biasVTrace_same_len),
             np.array([10.0] * biasVTrace_same_len.shape[0]).reshape(biasVTrace_same_len.shape[0], -1)), axis=1)
        frontCheckBIdx = np.where(
            np.isclose(biasVTrace_same_len, bias_base * 2, 0.001) & np.isclose(diffBiasTrace, -bias_base * 2, 0.001),
            True,
            False)  # 从0.2 下降到0/0.2的位置的值
        backCheckFIdx = np.where(
            np.isclose(biasVTrace_same_len, 0, 0.001) & np.isclose(diffBiasTrace, bias_base * 2, 0.001),
            True,
            False)  # 从 0 上升到0.2/0.2的位置的值
        backCheckBIdx = np.where(
            np.isclose(biasVTrace_same_len, bias_base * 2, 0.001) & np.isclose(diffBiasTrace, -bias_base, 0.001),
            True,
            False)  # 从0.2下降到0.1/0.2的位置的值

        # 此处对原来的程序做改动，此处应该应该对这三个check中的异常值进行删除(同时满足三个检测点)
        trueIdx = np.apply_along_axis(np.any, 1, frontCheckBIdx) & np.apply_along_axis(np.any, 1,
                                                                                       backCheckFIdx) & np.apply_along_axis(
            np.any, 1, backCheckBIdx)
        """
        上面的写法，还可以这样写：
        eg:
        b=array([[1., 2., 3., 4.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.]])
        
        np.any(b,axis=1)
        Out[61]: array([ True, False, False])
        
        即np.any  np.all 都是可以指定axis这个轴参数的
        """
        biasVTrace = biasVTrace[trueIdx]
        currentTrace = currentTrace[trueIdx]
        condTrace = condTrace[trueIdx]
        cutStart = cutStart[trueIdx]
        cutEnd = cutEnd[trueIdx]
        frontCheckBIdx = frontCheckBIdx[trueIdx]
        backCheckFIdx = backCheckFIdx[trueIdx]
        backCheckBIdx = backCheckBIdx[trueIdx]

        # 再次检查！！！
        if biasVTrace.shape[0] == 0:
            return None, None, None

        frontCheckB = np.array([np.where(temp)[0][0] for temp in frontCheckBIdx])
        backCheckF = np.array([np.where(temp)[0][0] for temp in backCheckFIdx])
        backCheckB = np.array([np.where(temp)[0][0] for temp in backCheckBIdx])

        # 其实这里我担心是有问题的，因为万一frontCheckB[i]-100比100 还小呢。。。。就离谱了
        condCheckF = np.array([np.mean(condTrace[i][100:frontCheckB[i] - 100]) for i in range(biasVTrace.shape[0])])
        condCheckB = np.array(
            [np.mean(condTrace[i][backCheckF[i] + 100:backCheckB[i] - 100]) for i in range(biasVTrace.shape[0])])

        # 通过偏压把电导曲线切出来
        # 注意这里的这几个data其中每一行的数据维度都是不一致的！
        biasVData = np.empty(biasVTrace.shape[0], dtype=object)
        currentData = np.empty(biasVTrace.shape[0], dtype=object)
        condData = np.empty(biasVTrace.shape[0], dtype=object)

        for i in range(biasVTrace.shape[0]):
            biasVData[i] = biasVTrace[i][cutStart[i]:cutEnd[i] + 1]
            currentData[i] = currentTrace[i][cutStart[i]:cutEnd[i] + 1]
            condData[i] = condTrace[i][cutStart[i]:cutEnd[i] + 1]

        # 删除超过scanRange的数据
        # scanRange = keyPara["le_ScanRange"]
        scanRange = 3000

        trueIdx = [(data <= scanRange).all() for data in biasVData]
        biasVData = biasVData[trueIdx]
        currentData = currentData[trueIdx]
        condData = condData[trueIdx]
        condCheckB = condCheckB[trueIdx]
        condCheckF = condCheckF[trueIdx]

        meanCond = (condCheckB + condCheckF) / 2
        # 再次检查！！！
        if biasVData.shape[0] == 0:
            return None, None, None

        # # 整流判定  这个一般是不用开启的！！！
        # selectRetificate = int(keyPara["le_SelectRetificate"])
        # if selectRetificate == 0:
        #     retificationCheckGF = np.zeros(biasVData.shape[0])
        #     retificationCheckGB = np.zeros(biasVData.shape[0])
        #     quarterBiasV = round(0.35 * len(biasVTrace[0]))
        #     if biasVTrace[0][quarterBiasV] < 0:
        #         for i in range(biasVData.shape[0]):
        #             retificationCheckGF = np.mean(
        #                 condData[i][(biasVData >= -scanRange - 0.001) & (biasVData <= -scanRange + 0.001)])
        #             retificationCheckGB = np.mean(
        #                 condData[i][(biasVData >= scanRange - 0.001) & (biasVData <= scanRange + 0.001)])
        #     else:
        #         for i in range(biasVData.shape[0]):
        #             retificationCheckGB = np.mean(
        #                 condData[i][(biasVData >= -scanRange - 0.001) & (biasVData <= -scanRange + 0.001)])
        #             retificationCheckGF = np.mean(
        #                 condData[i][(biasVData >= scanRange - 0.001) & (biasVData <= scanRange + 0.001)])

        #     biasVData = np.where(retificationCheckGF >= retificationCheckGB, -biasVData, biasVData)
        # # 完成整流判定
        currentData_so = copy.deepcopy(currentData)
        # 对电流进行处理
        for i in range(currentData.shape[0]):
            currentData[i] = np.log10(np.abs(currentData[i])) + 6  # 原本mA 放大了e6倍数，单位变为nA
            currentData[i] = np.where(currentData[i] == -np.inf, -3, currentData[i])

        # 判断是否处于悬停状态
        # peakStart = keyPara["le_PeakStart"]
        # peakEnd = keyPara["le_PeakEnd"]

        trueIdx = np.where(
            (condCheckB >= peakEnd) & (condCheckB <= peakStart) & (condCheckF >= peakEnd) & (
                    condCheckF <= peakStart),
            True, False)
        currentData = currentData[trueIdx]
        condData = condData[trueIdx]
        biasVData = biasVData[trueIdx]
        currentData_so = currentData_so[trueIdx]

        # 再次检查！！！
        if biasVData.shape[0] == 0:
            return None, None, None
        else:
            return currentData, condData, biasVData, currentData_so, meanCond

    @classmethod
    def getPartitionData(cls, currentData, condData, biasVData, currentData_source, meanCond, de_capicity=False):

        """
        在matlab的版本里面还要将数据叠加成矩阵然后再绘图这里我认为不再需要这样操作直接hisd2d绘图就可以了
        另外此处应该将数据扁平化处理
        """
        # 这里的数据已经经过所需处理，这里只是负责拆分， 至少有一组数据
        biasVDataFor = []
        currentDataFor = []
        condDataFor = []
        currentData_sourceFor = []
        meanCond_sourceFor = []

        biasVDataReve = []
        currentDataReve = []
        condDataReve = []
        currentData_sourceReve = []
        meanCond_sourceReve = []

        for i in range(biasVData.shape[0]):
            trace = biasVData[i]
            peak_idx = np.where((trace == trace.max()) | (trace == trace.min()))[0]
            forward_scan = []
            reverse_scan = []
            if trace[peak_idx[0]] == trace.max():  # 起始是从0 到 1正扫
                forward_scan.append((0, peak_idx[0]))
                forward_scan.append((peak_idx[-1], len(trace) - 1))
            if trace[peak_idx[0]] == trace.min():  # 起始是从0到-1 反扫
                reverse_scan.append((0, peak_idx[0]))
                reverse_scan.append((peak_idx[-1], len(trace) - 1))
            for j in range(len(peak_idx) - 1):
                cur_idx = peak_idx[j]
                next_idx = peak_idx[j + 1]
                if trace[cur_idx] < trace[next_idx]:  # 正扫
                    forward_scan.append((cur_idx, next_idx))
                elif trace[cur_idx] > trace[next_idx]:  # 反扫
                    reverse_scan.append((cur_idx, next_idx))
            # 正向数据提取
            for v in forward_scan:
                biasVDataFor.append(biasVData[i][v[0]:v[1] + 1])
                currentDataFor.append(currentData[i][v[0]:v[1] + 1])
                condDataFor.append(condData[i][v[0]:v[1] + 1])
                currentData_sourceFor.append(currentData_source[i][v[0]:v[1] + 1])
                meanCond_sourceFor.append(meanCond[i])
            # 反向数据提取
            # 如果需要去电容效应if :
            # 1. 求currentData[i][v[0]:v[1] + 1]的abs的min的index
            # 2. 索引位置移动这么多 就行
            log_g0 = np.log10(77.6e-6)

            if de_capicity:
                for v in reverse_scan:
                    biasVDataReve.append(biasVData[i][v[0]:v[1] + 1])
                    # condDataReve.append(condData[i][v[0]:v[1] + 1])  # 可以改成计算logG

                    min_index = np.argmin(currentData[i][v[0]:v[1] + 1])
                    a = min_index - len(currentData[i][v[0]:v[1] + 1]) // 2  # 偏移量
                    currentData_sourceReve.append(currentData_source[i][v[0] + a:v[1] + 1 + a])
                    currentDataReve.append(currentData[i][v[0] + a:v[1] + 1 + a])

                    condData_i = (currentData[i][v[0] + a:v[1] + 1 + a] -
                                  np.log10(np.abs(biasVData[i][v[0]:v[1] + 1])) + log_g0 - 1)
                    condDataReve.append(condData_i)
                    meanCond_sourceReve.append(meanCond[i])
            else:
                for v in reverse_scan:
                    biasVDataReve.append(biasVData[i][v[0]:v[1] + 1])
                    currentDataReve.append(currentData[i][v[0]:v[1] + 1])
                    condDataReve.append(condData[i][v[0]:v[1] + 1])
                    currentData_sourceReve.append(currentData_source[i][v[0]:v[1] + 1])
                    meanCond_sourceReve.append(meanCond[i])

        #  如果0到0.1加反扫之后接受到了-0.1到0，则将两者拼接到一起作为正扫
        biasVDataFor_new = []
        currentDataFor_new = []
        condDataFor_new = []
        currentData_sourceFor_new = []
        meanCond_sourceFor_new = []

        for i in range(len(biasVDataFor)):
            if biasVDataFor[i][1] > 0 > biasVDataFor[i + 1][1]:
                biasVDataFor_new.append(np.concatenate((biasVDataFor[i + 1], biasVDataFor[i])))
                currentDataFor_new.append(np.concatenate((currentDataFor[i + 1], currentDataFor[i])))
                condDataFor_new.append(np.concatenate((condDataFor[i + 1], condDataFor[i])))
                currentData_sourceFor_new.append(
                    np.concatenate((currentData_sourceFor[i + 1], currentData_sourceFor[i])))
                meanCond_sourceFor_new.append(meanCond_sourceFor[i])

        return (biasVDataFor_new, currentDataFor_new, condDataFor_new, biasVDataReve,
                currentDataReve, condDataReve, currentData_sourceFor_new, currentData_sourceReve,
                meanCond_sourceFor_new, meanCond_sourceReve)

    @classmethod
    def iv_process(cls, tdms_file, bias_base, peakStart, peakEnd, de_capicity):
        """
        Process IV curve data.

        Args:
            tdms_file (str): Path to the TDMS file.
            bias_base (float): Bias base value.
            peakStart (float): Peak start value.
            peakEnd (float): Peak end value.
            de_capicity (int): De-capacity value.

        Returns:
            Tuple: A tuple containing processed biasVDataFor, currentDataFor, condDataFor,
            biasVDataReve, currentDataReve, condDataReve, currentData_sourceFor,
            currentData_sourceReve.
        """
        try:
            currentData, condData, biasVData, currentData_source, meanCond = IVDataProcessUtils.hysteresis(tdms_file,
                                                                                                           bias_base=bias_base,
                                                                                                           peakStart=peakStart,
                                                                                                           peakEnd=peakEnd)

            biasVDataFor, currentDataFor, condDataFor, biasVDataReve, currentDataReve, condDataReve, currentData_sourceFor, currentData_sourceReve, meanCond_sourceFor_new, meanCond_sourceReve = IVDataProcessUtils.getPartitionData(
                currentData, condData, biasVData, currentData_source, meanCond, de_capicity=bool(de_capicity))

            return (biasVDataFor, currentDataFor, condDataFor, biasVDataReve, currentDataReve,
                    condDataReve, currentData_sourceFor, currentData_sourceReve, meanCond_sourceFor_new, meanCond_sourceReve)
        except Exception as e:
            # Log the error or handle it in a more appropriate way
            print(f"Function execution failed: {str(e)}")
            return []
