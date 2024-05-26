import torch

# CUDA 사용 가능 여부 확인
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

# 사용 가능한 GPU 장치 수 확인
if cuda_available:
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    print(f"Current GPU: {torch.cuda.current_device()}")
    print(f"GPU Name: {torch.cuda.get_device_name(torch.cuda.current_device())}")

# CPU 사용 여부 확인
cpu_available = torch.device('cpu')
print(f"CPU available: {cpu_available}")
