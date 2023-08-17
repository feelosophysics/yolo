import torch

# CUDA 버전 확인
print("CUDA version:", torch.version.cuda)

# cuDNN 버전 확인
print("cuDNN version:", torch.backends.cudnn.version())

# PyTorch 버전 확인
print("PyTorch version:", torch.__version__)