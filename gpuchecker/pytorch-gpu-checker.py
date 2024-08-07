# Pytorchを入れる
import torch

# GPUを認識するかの簡易テスト
if torch.cuda.is_available():
    print("GPUが認識されています！")

else:
    print("GPUが認識されていません...")