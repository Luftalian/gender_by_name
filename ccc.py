import pandas as pd

features = pd.read_csv('features.csv')

def extract_unique_gender_data(output_csv_path):
    # 'Gender'列がユニークな行のみを抽出する
    unique_gender_data = features.groupby('Name').filter(lambda x: x['Gender'].nunique() == 1)
    
    # 名前と性別のみを含むDataFrameを作成する
    result_df = unique_gender_data[['Name', 'Gender']].copy()
    
    # CSVファイルとして保存する
    result_df.to_csv(output_csv_path, index=False)

# 使用例
extract_unique_gender_data("unique_gender_data.csv")
