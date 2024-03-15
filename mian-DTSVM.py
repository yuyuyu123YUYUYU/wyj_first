import numpy as np
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# 阈值判断函数
def threshold_judgement1(vector):
    temperature, humidity = vector[:2]
    temperature_threshold_min = 20.0 * (1 - 0.02)
    temperature_threshold_max = 20.0 * (1 + 0.02)
    humidity_threshold_min = 65.0 * (1 - 0.04)
    humidity_threshold_max = 65.0 * (1 + 0.04)

    if temperature_threshold_min <= temperature <= temperature_threshold_max and \
            humidity_threshold_min <= humidity <= humidity_threshold_max:
        return '1A'
    else:
        return '1B'

# 假设 threshold_judgement2 的实现（这里仅作占位，实际请提供具体内容）
def threshold_judgement2(data_point):
    # 实际逻辑取决于具体应用场景
    pass

# 加载测试数据集
file_path = 'data.xlsx'  # 修复文件路径名中的空格问题
df = pd.read_excel(file_path)

# 假设数据预处理后可以分割特征和标签，并分为训练集和测试集
features = df[['temperature', 'humidity', ...]]  # 其他所需特征列
labels = df['label']  # 假设有一个标签列
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# 初始化模型
svm_model1 = svm.SVC(kernel='linear')
svm_model2 = svm.SVC(kernel='linear')
dt_model = DecisionTreeClassifier()

# 假设模型已经用训练数据拟合好
svm_model1.fit(X_train, y_train)
svm_model2.fit(X_train, y_train)
dt_model.fit(X_train, y_train)

# 分类流程
results = []

for idx, data_point in enumerate(X_test):
    # 第一级阈值判断
    env_class = threshold_judgement1(data_point.values[:2])

    if env_class == '1A':
        # 这里假设threshold_judgement2有实际实现
        run_status = threshold_judgement2(data_point.values)

        if run_status == '2B':
            # 第三级分类（SVM）
            standby_status = svm_model1.predict([data_point.values])[0]

            if standby_status == '3A':  # 待机状态
                # 第五级分类（决策树）
                prep_status = dt_model.predict([data_point.values])[0]
                results.append(('4' + prep_status))
            else:  # 非待机状态
                # 第四级分类（SVM）
                stretch_status = svm_model2.predict([data_point.values])[0]
                results.append(('3' + stretch_status))

# 输出分类结果
for idx, result in enumerate(results):
    print(f"Sample {idx + 1} classified as: Class{result}")