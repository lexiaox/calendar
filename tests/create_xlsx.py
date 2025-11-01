import pandas as pd
from datetime import time

# 创建课程表数据
data = {
    '时间/星期': ['周一', '周二', '周三', '周四', '周五'],
    '8:00-9:40': ['高等数学', '大学英语', 'C语言程序设计', '高等数学', '体育'],
    '10:00-11:40': ['大学物理', '思想政治', '大学英语', '实验课', 'C语言程序设计'],
    '14:00-15:40': ['体育', '高等数学', '社团活动', '大学物理', '自习'],
    '16:00-17:40': ['自习', '实验课', '自习', '社团活动', '大学英语']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 设置第一列为索引，让显示更美观
df.set_index('时间/星期', inplace=True)

# 创建Excel文件
with pd.ExcelWriter('课程表.xlsx', engine='openpyxl') as writer:
    # 写入课程表
    df.to_excel(writer, sheet_name='课程表')
    
    # 获取工作表并进行格式调整
    workbook = writer.book
    worksheet = writer.sheets['课程表']
    
    # 调整列宽
    worksheet.column_dimensions['A'].width = 12
    for col in ['B', 'C', 'D', 'E']:
        worksheet.column_dimensions[col].width = 15

print("课程表已生成并保存为 '课程表.xlsx'")
print("\n课程表内容：")
print(df)