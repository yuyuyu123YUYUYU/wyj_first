import numpy as np
from scipy.signal import medfilt
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# 加载Excel数据
file_path = 'data.xlsx'  # 修复文件路径名中的空格问题
df = pd.read_excel(file_path)

# 假设数据集中有一列名为'signal_data'的列，需要进行去噪、归一化和滑动窗口处理
signal_data = df['signal_data'].values  # 获取信号数据列

# 数据去噪
window_length = 5
filtered_signal = medfilt(signal_data, window_length)

# 数据归一化
scaler = MinMaxScaler(feature_range=(0, 1))
normalized_signal = scaler.fit_transform(filtered_signal.reshape(-1, 1)).flatten()

# 滑动窗口取样
window_size = 20  # 滑动窗口大小
stride = 1  # 步长（窗口移动的距离）

windows = []
for i in range(0, len(normalized_signal) - window_size + 1, stride):
    window = normalized_signal[i:i+window_size]
    windows.append(window)
