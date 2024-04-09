import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from mpl_toolkits.mplot3d import Axes3D

# pandasの設定
pd.options.display.max_rows = None
pd.options.display.max_columns = None
# CSVファイルを読み込む
df = pd.read_csv('FEH_00600350_240403120215.csv')

# 日付列をdatetime型に変換
df['月次'] = pd.to_datetime(df['月次'])

# 重複した日付を削除
df.drop_duplicates(subset='月次', inplace=True)

# 計の各々の行を削除
df.index = ['ＪＲ旅客会社', '新幹線', '民鉄（ＪＲ以外）', '大手', '中小', '公営', '計']
df.drop('計')

# 結果を新しいCSVファイルに保存
df.to_csv('unique_dates.csv', index=False)
# CSVファイルからデータを読み中小中小
# csv_file = r'C:\Users\frontier-Python\Desktop\teishutubutu\FEH_00600350_240403120215.csv'
csv_file = r'C:\Users\mercu\OneDrive\デスクトップ\submission\FEH_00600350_240403120215.csv'


# データフレームを読み込む
df = pd.read_csv(csv_file, header=0, index_col="月次", encoding="shift_jis")
data_list = df.values.tolist()

selected_columns = ['旅客数量【千人】', '前月比【%】', '前年同月比【%】']
df_selected = df[selected_columns]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 各社のデータをプロット
for i, company in enumerate(df_selected['前月比【%】'].unique()):
    company_data = df_selected[df_selected['前月比【%】'] == company]
    if company == 'JR':
        label = 'JR'
    elif company == '新幹線':
        label = '新幹線'
    elif company == '民鉄':
        label = '民鉄'
    elif company == '大手':
        label = '大手'
    elif company == '中小':
        label = '中小'
    elif company == '公営':
        label = '公営'
    else:
        label = 'その他'
    ax.plot(company_data['旅客数量【千人】'], company_data['前月比【%】'], company_data['前年同月比【%】'], label=label)

# グラフの設定
ax.set_xlabel('旅客数量【千人】')
ax.set_ylabel('前月比【%】')
ax.set_zlabel('前年同月比【%】')
ax.set_title('鉄道各社の輸送統計調査')
ax.legend(loc="upper right")

# グラフの表示
plt.show()
