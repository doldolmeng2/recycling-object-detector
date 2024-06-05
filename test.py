import torch

def get_gpu_memory_info():
    if torch.cuda.is_available():
        print("GPU is available.")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
            print(f"  Total Memory: {torch.cuda.get_device_properties(i).total_memory / 1024**3:.2f} GB")
            print(f"  Allocated Memory: {torch.cuda.memory_allocated(i) / 1024**3:.2f} GB")
            print(f"  Reserved Memory: {torch.cuda.memory_reserved(i) / 1024**3:.2f} GB")
            print(f"  Free Memory: {(torch.cuda.get_device_properties(i).total_memory - torch.cuda.memory_reserved(i)) / 1024**3:.2f} GB")
    else:
        print("No GPU available.")

get_gpu_memory_info()
