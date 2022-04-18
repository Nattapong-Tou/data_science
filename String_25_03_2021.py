import pandas as pd
import numpy as np

# การดำเนินการกับข้อมูลที่เป็น String
data = {'title':['Data Science', 'Database', 'Big Data', 'Python Data Analysis'],
    'price':['400', '500', '600', '700']
}

df = pd.DataFrame(data)

print('Show data from Dataframe')
print(df, '\n\n')

df1 = df[df.title.str.startswith('Data')] # หากต้องการค้าหาคำที่ขึ้นต้นด้วย Data ใช้ startswith ตัวอักษรตัวเล็กตัวใหญ่สำคัญ
print('Search word start with Data')
print(df1, '\n\n')

df2 = df[df['title'].str.endswith('sis')] # หากต้องการค้าหาคำที่ลงท้าย ใช้ endswith ตัวอักษรตัวเล็กตัวใหญ่สำคัญ
print('Search word end with Data')
print(df2, '\n\n')

df3 = df[df['title'].str.find('Data') != -1] #ค้นหา title ที่มีคำว่า Data อยู่
print(df3, '\n\n')

df_upper = pd.DataFrame(data)
df_upper.title = df_upper['title'].str.upper() #เปลี่ยน title เป็ฯตัวใหญ่ทั้งหมด
print(df_upper, '\n\n')

df_replace = pd.DataFrame(data)
df_replace.title = df_replace['title'].str.replace('Data', 'Info')
print(df_replace, '\n\n')