from ucimlrepo import fetch_ucirepo

# fetch dataset 
gender_by_name = fetch_ucirepo(id=591)

unique_counts = gender_by_name.data.features.groupby('Name')['Gender'].nunique()

def find_gender2(X):
    # 'Name'列がXに一致する行を取得する
    match = gender_by_name.data.features[gender_by_name.data.features['Name'] == X]
    
    # 一致する行がある場合は対応する'Gender'を返す
    if not match.empty:
        return match['Gender'].iloc[0]
    else:
        return None

# csvファイルのName列に対して実行する
i

X = "Johnw"
y = find_gender2(X)
print(y)

def check_unique_gender(gender_by_name):
    # 'Name'列をキーとして、'Gender'列のユニークな値の数を数える
    unique_counts = gender_by_name.data.features.groupby('Name')['Gender'].nunique()
    
    # ユニークな値の数が2以上（複数のGenderが指定されている）の名前を取得する
    duplicate_names = unique_counts[unique_counts > 1].index.tolist()
    
    if len(duplicate_names) == 0:
        print("すべての名前に対してユニークなGenderが指定されています。")
    else:
        print("以下の名前に対して複数のGenderが指定されています:")
        print(len(duplicate_names))

# 使用例
check_unique_gender(gender_by_name)

unique_counts = gender_by_name.data.features.groupby('Name')['Gender'].nunique()
len(unique_counts[unique_counts == 0].index.tolist())

def find_gender3(X):
    # 'Name'列がXに一致する行を取得する
    match = gender_by_name.data.features[gender_by_name.data.features['Name'] == X]
    
    # 一致する行がある場合
    if not match.empty:
        unique_genders = match['Gender'].unique()
        if len(unique_genders) == 1:
            return unique_genders[0]  # 一意のGenderを返す
        else:
            return None  # 複数のGenderがある場合はNoneを返す
    else:
        return None  # 一致する行がない場合はNoneを返す

# 使用例
X = "John"
y = find_gender(X, gender_by_name)
print(y)
