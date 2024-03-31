import pandas as pd

features = pd.read_csv('features.csv')

list_ex = []

def extract_probability_difference_data(output_csv_path, threshold=0.1):
    # ユニークでない名前を抽出する
    non_unique_names = features['Name'][features.duplicated(subset='Name', keep=False)]
    
    # 名前ごとに確率の差を計算し、閾値よりも大きい行を抽出する
    result_rows = []
    for name in non_unique_names:
        data = features[features['Name'] == name]
        diff = (data[data['Gender'] == 'M']['Probability'].mean()) - (data[data['Gender'] == 'F']['Probability'].mean())
        list_ex.append(diff)

# 使用例
extract_probability_difference_data("probability_difference_data.csv", threshold=1e-3)

list_ex = [abs(x) for x in list_ex]

print(min(list_ex))
print(max(list_ex))
print(len(list_ex))
print(len([i for i in list_ex if i > 1e-3]))
# 中間値
print(sorted(list_ex)[len(list_ex) // 2])
# 平均値
print(sum(list_ex) / len(list_ex))
# 分散
print(sum([(i - sum(list_ex) / len(list_ex)) ** 2 for i in list_ex]) / len(list_ex))
# 標準偏差
print((sum([(i - sum(list_ex) / len(list_ex)) ** 2 for i in list_ex]) / len(list_ex)) ** 0.5)

# ヒストグラム
import matplotlib.pyplot as plt
plt.hist(list_ex, bins=len(list_ex)//10)
plt.show()
