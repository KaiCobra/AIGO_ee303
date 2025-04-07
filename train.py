import torch
from torch.utils.data import DataLoader, TensorDataset
from Model.model import SimpleNN
from data_preprocessing import X_train, y_train, X_val, y_val

def main():
    # 轉換為 Tensor
    X_train_tensor = torch.FloatTensor(X_train)
    y_train_tensor = torch.FloatTensor(y_train.values).view(-1, 1)
    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

    # 初始化模型
    input_dim = X_train.shape[1]
    model = SimpleNN(input_dim)

    # 定義損失函數和優化器
    criterion = torch.nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # 訓練循環
    num_epochs = 5
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss/len(train_loader):.4f}")

    # 保存模型
    torch.save(model.state_dict(), "Checkpoints/basic_model.pth")

if __name__ == "__main__":
    main()