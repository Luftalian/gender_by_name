from ucimlrepo import fetch_ucirepo
import pandas as pd

input_csv_name = "name"

# # fetch dataset 
# gender_by_name = fetch_ucirepo(id=591)

# features = gender_by_name.data.features

# # Convert features to a DataFrame
# # df_features = pd.DataFrame(features)

# # Save the DataFrame to an external file
# features.to_csv('features.csv', index=False)

features = pd.read_csv('features.csv')


# find_gender関数の定義
def find_gender(X):
    # 'Name'列がXに一致する行を取得する
    match = features[features['Name'] == X]
    
    # 一致する行がある場合
    if not match.empty:
        unique_genders = match['Gender'].unique()
        if len(unique_genders) == 1:
            return unique_genders[0]  # 一意のGenderを返す
        else:
            # MとFの確率の差を取得する
            diff_M = match[match['Gender'] == 'M']['Probability'].mean() - match[match['Gender'] == 'F']['Probability'].mean()
            diff_F = match[match['Gender'] == 'F']['Probability'].mean() - match[match['Gender'] == 'M']['Probability'].mean()
            
            # 確率の差が一定以上の場合、対応するGenderを返す
            if diff_M > 1e-3:
                return 'M'
            elif diff_F > 1e-3:
                return 'F'
            else:
                return None
    else:
        return None

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
