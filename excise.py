#csv文件的简单的读写操作
import pandas as pd

a = [1,2,3]
b = [4,5,6]

dataFrame = pd.DataFrame({"col1":a,"col2":b})

dataFrame.to_csv("excise.csv",index = False)


data = pd.read_csv('excise.csv')
print(data)

#json文件的读写
json_str = '{"country":"Netherlands"}'
js = pd.read_json("excise.json")
print(js)