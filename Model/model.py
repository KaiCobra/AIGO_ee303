# model.py
import torch.nn as nn  # 明確導入 PyTorch 的 nn 模組
import torch.nn.functional as F  # 補充導入 functional 模組（若需要）

class SimpleNN(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, 64)  # 使用 nn.Linear
        self.fc2 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = F.relu(self.fc1(x))  # 改用 F.relu 或保留 nn.functional.relu
        x = self.fc2(x)
        return self.sigmoid(x)