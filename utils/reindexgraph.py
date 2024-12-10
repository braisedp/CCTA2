import csv
import os

graph = "dash"

# 读取 CSV 文件并收集所有唯一的数字
unique_numbers = set()
with open(f'./graphs/{graph}.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)  # 跳过标题行
    for row in reader:
        unique_numbers.update(row)

# 创建从原始数字到重新编码数字的映射
unique_numbers = sorted(unique_numbers)
number_mapping = {num: str(i) for i, num in enumerate(unique_numbers)}

# 重新编码 CSV 文件中的数字
with open(f'./graphs/{graph}.csv', 'r') as infile, open(f'./graphs/{graph}_temp.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(next(reader))  # 写入标题行
    for row in reader:
        reencoded_row = [number_mapping[num] for num in row]
        writer.writerow(reencoded_row)

# 删除原有文件并重命名临时文件
os.remove(f'./graphs/{graph}.csv')
os.rename(f'./graphs/{graph}_temp.csv', f'./graphs/{graph}.csv')