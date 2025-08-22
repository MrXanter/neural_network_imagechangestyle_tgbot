import torch
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from models.Transformer import Transformer
from io import BytesIO
import torchvision.utils as vutils

class AnimeStyleTransfer:
    def __init__(self, model_paths: dict):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.load_size = 450
        self.models = {}
        
        # Load all models
        for style_name, model_path in model_paths.items():
            model = Transformer()
            model.load_state_dict(torch.load(model_path, map_location=self.device))
            model.eval()
            if self.device.type == 'cuda':
                model.cuda()
            else:
                model.float()
            self.models[style_name] = model

    def process_image(self, input_bytes: BytesIO, output_buffer: BytesIO, style: str):
        model = self.models[style]
        
        # Load and preprocess image
        input_image = Image.open(input_bytes).convert("RGB")
        
        # Resize image, keep aspect ratio
        h = input_image.size[0]
        w = input_image.size[1]
        ratio = h * 1.0 / w
        if ratio > 1:
            h = self.load_size
            w = int(h * 1.0 / ratio)
        else:
            w = self.load_size
            h = int(w * ratio)
        input_image = input_image.resize((h, w), Image.BICUBIC)
        input_image = np.asarray(input_image)
        
        # RGB -> BGR
        input_image = input_image[:, :, [2, 1, 0]]
        input_image = transforms.ToTensor()(input_image).unsqueeze(0)
        # Preprocess to [-1, 1]
        input_image = -1 + 2 * input_image
        input_image = input_image.to(self.device)

        # Forward pass with selected model
        with torch.no_grad():
            output_image = model(input_image)
            output_image = output_image[0]
            # BGR -> RGB
            output_image = output_image[[2, 1, 0], :, :]
            # Deprocess to [0, 1]
            output_image = output_image.data.cpu().float() * 0.5 + 0.5

        # Save to buffer
        vutils.save_image(output_image, output_buffer, format='jpeg')
        output_buffer.seek(0)
