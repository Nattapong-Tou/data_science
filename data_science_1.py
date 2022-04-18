import pandas as pd
import random
import numpy as np



# rang (strat, stop, step)
'''
a = range(0, 10, 2)

for x in a:
    print(x)

# ตรวจสอบค่า start, stop, step
print('------ ตรวจสอบค่า start, stop, step -------')
start = a.start
stop = a.stop
step = a.step
print('Start = ', start)
print('Stop = ', stop)
print('Step = ', step)
'''

# รายการข้อมูลแบบ list
'''
# สร้าง list โดยใช้ function
a = list() # list ว่างเปล่า
b = list([1, 2, 3, 4, 5]) # list ที่มีสมาชิก 1, 2, 3, 4, 5
c = list(['one', 'two', 'tree']) # list แบบ string
d = list(range(1, 5)) # สร้าง list โดยใช้ rang()

# สร้าง list โดยใช้ []
e = [1, 2, 3, 4, 5]
f = ['one', 'two', 'tree']
g = [range(1, 5)]
'''

# functoin built in ที่สามารถใช้งานร่วมกับ list
'''
e = [1, 2, 3, 4, 5]
print('จำนวนสมาชิกทั้งหมดใน list = ', len(e)) # len = จำนวนสมาชิกทั้งหมดใน list
print('ผลรวมทั้งหมดใน list = ', sum(e)) # ผลรวมทั้งหมดใน list
print('ค่ามากสุดใน list = ', max(e)) # ค่ามากสุดใน list
print('ค่าน้อยสุดใน list = ', min(e))
'''
# 29 / 08 / 2020

'''
#การกำหนดข้อมูลให้กับ Series
data1 = [70, 85, 50, 75] # >> list
sr1 = pd.Series(data=data1)

data2 = (10, 20, 30, 40) # >> tuple
sr2 = pd.Series(data2)

sr3 = pd.Series([20, 40, 60, 80])

print(sr1)

# กำหนด index ลงไปด้วย
index = ['A', 'B', 'C', 'D']
sr4 = pd.Series(data1, index=index)
print(sr4)

# values and index
data3 = {'T-Shirt': 499, 'shoe': 2000, 'Bag': 40000}
sr5 = pd.Series(data3)
print(sr5.index, sr5.values, sep='\n\n')
'''

# 25 / 9 / 2020
# function ที่น่าสนใจของ series
'''
data = [1,2,4,6,8,16]
sr = pd.Series(data)
print('count = ', sr.count()) # นับจำนวนของสมาชิก
print('mean = ', sr.mean()) # ค่าเฉลี่ยของสมาชิก
print('std = ', sr.std()) # ค่าเบี่ยงเบนมาตรฐานของสมาชิก
print('max = ', sr.max()) # ค่ามากสุดของสมาชิก
print('min = ', sr.min()) # ค่าน้อยสุดของสมาชิก
print(sr.describe()) # แสดงค่าพื้นฐานทางสถิติ
'''

# การกำหนด dataframe จากข้อมูลที่มีอยู่แล้ว
'''
data = (
    [10,50,80,100],
    [50,30,20,10],
    [15,30,45,55],
    [100,200,300,400]
)

df = pd.DataFrame(data, index=list('ABCD'), columns=['one','two','tree','four'])
print(df)
'''
# กำหนด dataframe โดยใช้ numpy
data1 = np.array([
    [10,20,30,40],
    [55,66,77,88],
    [100,105,1000,17]

])
df1 = pd.DataFrame(data1, index=list('ABC'), columns=list('ABCD'))

data2 = np.random.uniform(1,11,(4,5))
df2 = pd.DataFrame(data2, columns=['Mon','Tue','wed','thu','fri'])

print(df1)
print(df2)

# 25 / 09 / 2020
# การกำหนดข้อมูลแบบดิกชันนารี
'''
syntax
data = {
    'columns 1' : [row1, row2, row3],
    '.....' : [..., ..., ...],
    ...
}
'''

data3 = {
    'column1' : [110, 111, 113, 115],
    'column2' : [200, 300, 400, 500],
    'column3' : [10, 20, 30, 40],
}

df3 = pd.DataFrame(data3, index=['p1', 'p2', 'p3', 'p4'])
print('การกำหนดข้อมูลแบบดิกชันนารี')
print(df3)


data4 = {
    'Mon' : np.arange(10, 14),
    'Tue' : np.random.randint(10, 100, 4),
    'Web' : np.full(4, 10)
}
df4 = pd.DataFrame(data4, index=['p1', 'p2', 'p3', 'p4'])
print('การกำหนดข้อมูลแบบดิกชันนารี โดยใช้ numpy')
print(df4)


### การ join dataframe คือการนำ  dataframe / dataframe มาต่อกัน
data5 = {
    'col 1' : [10, 20, 30],
    'col 2' : [40, 50, 60],
    'col 3' : [70, 80, 90]
}
df5 = pd.DataFrame(data5, index=list('ABC'))

data6 = {
    'col 4' : [100, 200, 300],
    'col 5' : [400, 500, 600]

}
df6 = pd.DataFrame(data6, index=list('ABC'))

# join dataframe
df_5_6 = df5.join(df6)

print('Dataframe5')
print(df5)
print('Dataframe6')
print(df6)
print('Dataframe5 - 6')
print(df_5_6)

# ในกรณีที่ชื่อ coulmn ซ้ำกันหากเรา join dataframe ต้องเพิ่มคำสั่ง lsuffix/rsuffix
data7 = {
    'col 1' : [1, 2, 3],
    'col 2' : [4, 5, 6]

}
df7 = pd.DataFrame(data7, index=list('ABC'))
df_5_7 = df5.join(df7, lsuffix='_old', rsuffix='_new')

print(df_5_7)
