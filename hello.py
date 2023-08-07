import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./shinri.csv')
print("This is a dataframe.")
print(df)
result = df.result
original = df.original

#各列の平均
mean_result = result.mean()
mean_original = original.mean()
print("\n")
print("This is mean of result and original.")
print(f"mean_result: {mean_result}, mean_original: {mean_original}")

#各列の最大値
max_result = result.max()
max_original = original.max()
print("\n")
print("This is max of result and original.")
print(f"max_result: {max_result}, max_original: {max_original}")

#各列の最小値
min_result = result.min()
min_original = original.min()
print("\n")
print("This is min of result and original.")
print(f"min_result: {min_result}, min_original: {min_original}")

#各列の標準偏差
std_result = result.std()
std_original = original.std()
print("\n")
print("This is std of result and original.")
print(f"std_result: {std_result}, std_original: {std_original}")

#行数
print("\n")
print(f"Line count: {df.shape[0]}")

#ピアソン相関係数
print("\n")
print("Pearson`s Factor")
print(df.corr())