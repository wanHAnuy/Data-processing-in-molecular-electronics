# -*- coding: utf-8 -*-
# @Time   : 2025/3/27 23:21
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
    # def hysteresis(cls, filePath, bias_base=0.1, peakStart=-2.5, peakEnd=-5.5):
    #     # 1. 数据加载
    #     biasVolt, current, cond = cls.loadTMDSFile(filePath)
    #     if biasVolt is None or current is None or cond is None:
    #         return None, None, None
    #
    #     # 2. 提取电压阶跃的起始和结束索引
    #     diffBiasV = np.concatenate((np.diff(biasVolt), np.array([10.0])))
    #     # 找到从bias_base开始的上升阶跃（0.1 -> 0.2）
    #     start_candi = (np.where(
    #         np.isclose(biasVolt, bias_base, atol=1e-4) &
    #         np.isclose(diffBiasV, bias_base, atol=1e-4))[0] + 1)
    #     # 找到从bias_base*2下降的阶跃（0.2 -> 0.1）
    #     end_candi = np.where(
    #         np.isclose(biasVolt, bias_base * 2, atol=1e-4) &
    #         np.isclose(diffBiasV, -bias_base, atol=1e-4))[0]
    #
    #     startIdx, endIdx = [], []
    #     for s in start_candi:
    #         # 找到比s更大的第一个结束点
    #         ends = end_candi[end_candi > s]
    #         if len(ends) > 0:
    #             startIdx.append(s)
    #             endIdx.append(ends[0])
    #     startIdx = np.array(startIdx)
    #     endIdx = np.array(endIdx)
    #
    #     # 保证endIdx加上额外偏移后不超出范围
    #     endIdx += 200
    #     valid = endIdx < biasVolt.shape[0]
    #     startIdx = startIdx[valid]
    #     endIdx = endIdx[valid]
    #
    #     # 根据电压是否回到bias_base进行二次筛选
    #     if len(endIdx) > 0:
    #         biasVoltEnd = biasVolt[endIdx]
    #         temp = np.where(np.isclose(biasVoltEnd, bias_base, atol=1e-4))[0]
    #         startIdx = startIdx[temp]
    #         endIdx = endIdx[temp]
    #
    #     # 如果没有符合条件的区间则返回空
    #     if len(startIdx) == 0:
    #         return None, None, None
    #
    #     # 3. 分割各段轨迹
    #     biasVTrace, currentTrace, condTrace = [], [], []
    #     for s, e in zip(startIdx, endIdx):
    #         biasVTrace.append(biasVolt[s:e])
    #         currentTrace.append(current[s:e])
    #         condTrace.append(cond[s:e])
    #     biasVTrace = np.array(biasVTrace, dtype=object)
    #     currentTrace = np.array(currentTrace, dtype=object)
    #     condTrace = np.array(condTrace, dtype=object)
    #
    #     # 如果没有有效轨迹直接返回
    #     if biasVTrace.shape[0] == 0:
    #         return None, None, None
    #
    #     # 4. 根据轨迹内部的零点、峰值确定真正的扫描区域
    #     cutStart = np.ones(biasVTrace.shape[0], dtype=int)
    #     cutEnd = np.ones(biasVTrace.shape[0], dtype=int)
    #     for i in range(biasVTrace.shape[0]):
    #         trace = biasVTrace[i]
    #         zero_idx = np.where(np.isclose(trace, 0, atol=1e-4))[0]
    #         if zero_idx.size < 2:
    #             continue
    #         # 找到正式扫描起点：连续0结束的位置
    #         for j in range(len(zero_idx) - 1):
    #             if (zero_idx[j + 1] - zero_idx[j] > 1) and (trace[zero_idx[j] + 1] != 0):
    #                 cutStart[i] = zero_idx[j]
    #                 break
    #         # 如果cutStart未更新，则跳过
    #         if cutStart[i] == 1:
    #             continue
    #
    #         # 反向寻找终点
    #         zero_end = 1
    #         for j in range(len(zero_idx) - 1, 0, -1):
    #             if zero_idx[j] - zero_idx[j - 1] > 1:
    #                 zero_end = zero_idx[j]
    #                 break
    #         if zero_end == 1:
    #             continue
    #
    #         # 根据轨迹峰值进行进一步调整
    #         peak_index = np.where((trace == trace.min()) | (trace == trace.max()))[0]
    #         if peak_index.size == 0:
    #             continue
    #         first_peak = peak_index[0]
    #         # 针对正向情况：电压先正后负，终点应为从负变正的索引
    #         if trace[first_peak] > 0 and trace[zero_end - 1] > 0:
    #             for j in range(zero_end - 1, 0, -1):
    #                 if trace[j] <= 0 and trace[j + 1] > 0:
    #                     zero_end = j
    #                     break
    #         # 针对负向情况：电压先负后正
    #         elif trace[first_peak] < 0 and trace[zero_end - 1] < 0:
    #             for j in range(zero_end - 1, 0, -1):
    #                 if trace[j] >= 0 and trace[j + 1] < 0:
    #                     zero_end = j
    #                     break
    #         cutEnd[i] = zero_end
    #
    #     # 删除那些起点或终点未更新的轨迹
    #     valid_trace = (cutStart != 1) & (cutEnd != 1)
    #     biasVTrace = biasVTrace[valid_trace]
    #     currentTrace = currentTrace[valid_trace]
    #     condTrace = condTrace[valid_trace]
    #     cutStart = cutStart[valid_trace]
    #     cutEnd = cutEnd[valid_trace]
    #
    #     if biasVTrace.shape[0] == 0:
    #         return None, None, None
    #
    #     # 5. 利用统一长度和差分计算检测点
    #     max_len = np.max([len(x) for x in biasVTrace])
    #     biasVTrace_same_len = [np.pad(trace, (0, max_len - len(trace)), mode='edge') for trace in biasVTrace]
    #     biasVTrace_same_len = np.array(biasVTrace_same_len)
    #     diffBiasTrace = np.concatenate(
    #         (np.diff(biasVTrace_same_len), np.full((biasVTrace_same_len.shape[0], 1), 10.0)),
    #         axis=1)
    #
    #     frontCheckBIdx = np.isclose(biasVTrace_same_len, bias_base * 2, atol=1e-3) & \
    #                      np.isclose(diffBiasTrace, -bias_base * 2, atol=1e-3)
    #     backCheckFIdx = np.isclose(biasVTrace_same_len, 0, atol=1e-3) & \
    #                     np.isclose(diffBiasTrace, bias_base * 2, atol=1e-3)
    #     backCheckBIdx = np.isclose(biasVTrace_same_len, bias_base * 2, atol=1e-3) & \
    #                     np.isclose(diffBiasTrace, -bias_base, atol=1e-3)
    #
    #     # 筛选条件：只保留同时满足三个检测点的轨迹
    #     valid_idx = np.apply_along_axis(np.any, 1, frontCheckBIdx) & \
    #                 np.apply_along_axis(np.any, 1, backCheckFIdx) & \
    #                 np.apply_along_axis(np.any, 1, backCheckBIdx)
    #
    #     biasVTrace = biasVTrace[valid_idx]
    #     currentTrace = currentTrace[valid_idx]
    #     condTrace = condTrace[valid_idx]
    #     cutStart = cutStart[valid_idx]
    #     cutEnd = cutEnd[valid_idx]
    #     frontCheckBIdx = frontCheckBIdx[valid_idx]
    #     backCheckFIdx = backCheckFIdx[valid_idx]
    #     backCheckBIdx = backCheckBIdx[valid_idx]
    #
    #     if biasVTrace.shape[0] == 0:
    #         return None, None, None
    #
    #     # 6. 从检测点数组中提取第一个True索引
    #     frontCheckB = np.array([np.where(temp)[0][0] for temp in frontCheckBIdx])
    #     backCheckF = np.array([np.where(temp)[0][0] for temp in backCheckFIdx])
    #     backCheckB = np.array([np.where(temp)[0][0] for temp in backCheckBIdx])
    #
    #     # 计算电导的均值时避免索引越界：动态选择偏移量（取20%区间长度或固定100，取较小值）
    #     condCheckF = []
    #     condCheckB = []
    #     for i in range(biasVTrace.shape[0]):
    #         seg_len = len(condTrace[i])
    #         offset = min(100, seg_len // 5)
    #         # 若frontCheckB[i] - offset 小于offset，则从offset开始
    #         start_range = offset if frontCheckB[i] - offset < offset else frontCheckB[i] - offset
    #         # 若backCheckB[i] - offset 小于 backCheckF[i] + offset，则取 backCheckB[i]
    #         end_range = backCheckB[i] - offset if backCheckB[i] - offset > backCheckF[i] + offset else backCheckB[i]
    #         condCheckF.append(np.mean(condTrace[i][offset:start_range]))
    #         condCheckB.append(np.mean(condTrace[i][backCheckF[i] + offset:end_range]))
    #     condCheckF = np.array(condCheckF)
    #     condCheckB = np.array(condCheckB)
    #
    #     # 7. 根据扫描区间限制筛选数据，删除超出scanRange的轨迹
    #     scanRange = 3000
    #     valid_scan = np.array([np.all(biasVData <= scanRange) for biasVData in
    #                            [trace[cutS:cutE + 1] for trace, cutS, cutE in zip(biasVTrace, cutStart, cutEnd)]])
    #
    #     # 提取最终的轨迹数据
    #     biasVData = np.empty(biasVTrace.shape[0], dtype=object)
    #     currentData = np.empty(biasVTrace.shape[0], dtype=object)
    #     condData = np.empty(biasVTrace.shape[0], dtype=object)
    #     for i in range(biasVTrace.shape[0]):
    #         biasVData[i] = biasVTrace[i][cutStart[i]:cutEnd[i] + 1]
    #         currentData[i] = currentTrace[i][cutStart[i]:cutEnd[i] + 1]
    #         condData[i] = condTrace[i][cutStart[i]:cutEnd[i] + 1]
    #
    #     biasVData = biasVData[valid_scan]
    #     currentData = currentData[valid_scan]
    #     condData = condData[valid_scan]
    #     condCheckB = condCheckB[valid_scan]
    #     condCheckF = condCheckF[valid_scan]
    #
    #     meanCond = (condCheckB + condCheckF) / 2
    #     if biasVData.shape[0] == 0:
    #         return None, None, None
    #
    #     # 8. 对电流数据转换：保存原始数据备份，同时转换为对数尺度（单位转换：mA->nA）
    #     import copy
    #     currentData_so = copy.deepcopy(currentData)
    #     for i in range(currentData.shape[0]):
    #         # 为避免 log10(0) 问题，clip到一个极小正值
    #         abs_current = np.clip(np.abs(currentData[i]), 1e-12, None)
    #         currentData[i] = np.log10(abs_current) + 6  # mA放大e6转换为nA
    #         currentData[i] = np.where(np.isneginf(currentData[i]), -3, currentData[i])
    #
    #     # 9. 根据condCheck的范围筛选数据
    #     valid_final = (condCheckB >= peakEnd) & (condCheckB <= peakStart) & \
    #                   (condCheckF >= peakEnd) & (condCheckF <= peakStart)
    #
    #     currentData = currentData[valid_final]
    #     condData = condData[valid_final]
    #     biasVData = biasVData[valid_final]
    #     currentData_so = currentData_so[valid_final]
    #
    #     if biasVData.shape[0] == 0:
    #         return None, None, None
    #     else:
    #         return currentData, condData, biasVData, currentData_so, meanCond

    def hysteresis(cls, filePath, bias_base=0.1, peakStart=-2.5, peakEnd=-5.5):
        """返回偏压，电导，电流三个二维数组，每一条占用一行
        """
        biasVolt, current, cond = cls.loadTMDSFile(filePath)
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

        # 得到扫面区间，接下来就是把中间的切开！！
        for i in range(startIdx.shape[0]):
            biasVTrace.append(biasVolt[startIdx[i]:endIdx[i] + 1])
            currentTrace.append(current[startIdx[i]:endIdx[i] + 1])
            condTrace.append(cond[startIdx[i]:endIdx[i]])
        biasVTrace = np.array(biasVTrace, dtype='object')
        currentTrace = np.array(currentTrace, dtype='object')
        condTrace = np.array(condTrace, dtype='object')

        if biasVTrace.shape[0] == 0:
            return None, None, None

        condPeakStart = peakStart
        condPeakEnd = peakEnd
        # 寻找电压是0v的起始和终点
        cutStart, cutEnd = np.ones(biasVTrace.shape[0], dtype=int), np.ones(biasVTrace.shape[0], dtype=int)
        for i in range(biasVTrace.shape[0]):
            trace = biasVTrace[i]
            zero_idx = np.where(np.isclose(trace, 0, 0.0001))[0]

            # 条件1 至少3个零点
            # if (len(zero_idx) < 3):
            #     continue

            # 条件2 必须有从2*bias_base-> 0 和 从 0 -> 2*bias_base的跳跃
            if abs(trace[zero_idx[0] - 1] - 2 * bias_base) > 0.0001 and abs(
                    trace[zero_idx[-1] + 1] - 2 * bias_base) > 0.0001:
                continue

            # 条件3 偏压在2*bias_base时的平均电导必须在范围内
            cond_start = condTrace[i][:zero_idx[0] - 1]
            cond_end = condTrace[i][zero_idx[-1] + 1:]
            cond_start_mean = cond_start[np.isfinite(cond_start)].mean()
            cond_end_mean = cond_end[np.isfinite(cond_end)].mean()
            if cond_start_mean < condPeakEnd or cond_start_mean > condPeakStart or cond_end_mean < condPeakEnd or cond_end_mean > condPeakStart:
                continue

            for j in range(zero_idx.shape[0] - 1):  # 找到正式扫描的起点
                if (zero_idx[j + 1] - zero_idx[j] > 1) and (trace[zero_idx[j] + 1] != 0):
                    cutStart[i] = zero_idx[j]
                    break
            if cutStart[i] == 1:
                continue
            # 寻找可能的终点
            temp_end = 1
            for j in range(zero_idx.shape[0] - 1, 0, -1):
                if zero_idx[j] - zero_idx[j - 1] > 1:
                    temp_end = zero_idx[j]
                    break
            if temp_end == 1:
                continue
            # 此时cut_start[i] 和 temp_end 必然不是1
            peak_index = np.where((trace == trace.min()) | (trace == trace.max()))[0]
            first_peak = peak_index[0]
            if trace[first_peak] > 0 and trace[temp_end - 1] > 0:  # 从0到1，结尾必须从-1到0
                for j in range(temp_end - 1, 0, -1):
                    if trace[j] <= 0 and trace[j + 1] > 0:
                        temp_end = j
                        break
            elif trace[first_peak] < 0 and trace[temp_end - 1] < 0:  # 从0到-1，结尾必须从1到0
                for j in range(temp_end - 1, 0, -1):
                    if trace[j] >= 0 and trace[i][j + 1] < 0:
                        temp_end = j
                        break
            cutEnd[i] = temp_end

        # 删除不完整的
        trueIndex = np.where((cutStart == 1) | (cutEnd == 1), False, True)
        biasVTrace = biasVTrace[trueIndex]
        currentTrace = currentTrace[trueIndex]
        condTrace = condTrace[trueIndex]
        cutStart = cutStart[trueIndex]
        cutEnd = cutEnd[trueIndex]
        # 再次检查！！！
        if biasVTrace.shape[0] == 0:
            return None, None, None

        # 通过偏压把电导曲线切出来
        # 注意这里的这几个data其中每一行的数据维度都是不一致的！
        biasVData = np.empty(biasVTrace.shape[0], dtype=object)
        currentData = np.empty(biasVTrace.shape[0], dtype=object)
        condData = np.empty(biasVTrace.shape[0], dtype=object)

        for i in range(biasVTrace.shape[0]):
            biasVData[i] = biasVTrace[i][cutStart[i]:cutEnd[i] + 1]
            currentData[i] = currentTrace[i][cutStart[i]:cutEnd[i] + 1]
            condData[i] = condTrace[i][cutStart[i]:cutEnd[i] + 1]

        currentData_so = []
        # 对电流进行处理
        for i in range(currentData.shape[0]):
            currentData_so.append(currentData[i])
            currentData[i] = np.log10(np.abs(currentData[i])) + 6
            currentData[i] = np.where(currentData[i] == -np.inf, -3, currentData[i])
        # 删除超过scanRange的数据
        # scanRange = 0.8 + 0.0001
        # tureIdx = [(data <= scanRange).all() for data in biasVData]
        # biasVData = biasVData[tureIdx]
        # currentData = currentData[tureIdx]
        # condData = condData[tureIdx]
        meanCond = [data[0] for data in condData]
        # currentData_so = currentData_so[tureIdx]

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
                                  np.log10(np.abs(biasVData[i][v[0]:v[1] + 1]) + 1e-10) + log_g0 - 1)
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
                    condDataReve, currentData_sourceFor, currentData_sourceReve, meanCond_sourceFor_new,
                    meanCond_sourceReve)
        except Exception as e:
            # Log the error or handle it in a more appropriate way
            print(f"Function execution failed: {str(e)}")
            return []
