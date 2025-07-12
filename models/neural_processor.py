import torch
from torchvision import transforms
from PIL import Image
from Transformer import Generator

class AnimeGANProcessor:
    def __init__(self, model_paths: dict):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.models = {}

        for style_name, pth_path in model_paths.items():
            model = Generator().to(self.device)
            model.load_state_dict(torch.load(pth_path, map_location=self.device))
            model.eval()
            self.models[style_name] = model

        self.transform = transforms.Compose([
            transforms.Resize((512, 512)),
            transforms.ToTensor(),
        ])
        self.inv_transform = transforms.ToPILImage()

    def process(self, input_path: str, output_path: str, style: str):
        img = Image.open(input_path).convert('RGB')
        input_tensor = self.transform(img).unsqueeze(0).to(self.device)

        model = self.models[style]

        with torch.no_grad():
            output_tensor = model(input_tensor).cpu().squeeze(0)

        output_img = self.inv_transform(output_tensor.clamp(0, 1))
        output_img.save(output_path)
