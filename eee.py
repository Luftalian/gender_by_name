import pandas as pd

input_csv_name = "name"

uniqgen = pd.read_csv('unique_gender_data.csv')
prodiff = pd.read_csv('probability_difference_data.csv')

data = pd.concat([uniqgen, prodiff], axis=0)

# print(data)
# exit()

def find_gender(X):
    # Xがgender_by_nameのNameに一致するかを確認し、一致する場合は対応するGenderを返す
    match = data[data['Name'] == X]
    if not match.empty:
        return match['Gender'].iloc[0]  # 一致した場合のGenderを返す
    else:
        return None  # 一致するものがない場合はNoneを返す


def process_csv(input_csv_path, output_csv_path):
    # CSVファイルを読み込む
    df = pd.read_csv(input_csv_path)
    
    # "input_csv_name"列があるかどうかを確認し、あれば性別を探索して新しい列を追加する
    if input_csv_name in df.columns:
        df['Gender'] = df[input_csv_name].apply(lambda x: find_gender(x))
    
    # 出力用のCSVファイルを保存する
    df.to_csv(output_csv_path, index=False)

# 使用例
process_csv("name.csv", "output.csv")
