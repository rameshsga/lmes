import pandas as pd
import numpy as np

df = pd.DataFrame({"f1":[1,2,3,4,5],
                    "f2":[2,4,6,8,10],
                    "f3":[10,8,6,4,2],
                    "output":[10,20,5,30,40]})
print(df)

correlation_finder = df.corr()
print(correlation_finder)

threshold_value = 0.5

target_correlation = correlation_finder['output'].drop('output')
print(target_correlation)
print(type(target_correlation))

#
# selected_feature = target_correlation[(target_correlation)>threshold_value]
# print("------------------")
# print(selected_feature)


selected_feature = target_correlation[target_correlation > threshold_value].index.tolist()
print("------------------")
print(selected_feature)
print(type(selected_feature))
final_df = df[selected_feature + ['output']]
print(final_df)
"""============================================================="""
# import pandas as pd


