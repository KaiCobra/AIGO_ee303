import torch.nn as nn

# 測試是否能使用 nn 定義模型
model = nn.Linear(10, 2)
print("測試成功！模型定義：", model)