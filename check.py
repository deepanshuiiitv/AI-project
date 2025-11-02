# import torch
# print("CUDA available:", torch.cuda.is_available())
# print("Device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU only")

import os

result_dir = r"A:\college\Clg_project\AI_project\Non-Uniform_Illumination\TinyImageNet\results"
print("Exists:", os.path.exists(result_dir))
