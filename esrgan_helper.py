import torch
import torchvision.transforms as transforms
import numpy as np
import cv2

class ESRGAN:
    def __init__(self, model_path=r"C:\Users\Default\models\RRDB_ESRGAN_x4.pth"):
        print(model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.load_model(model_path)
    
    def load_model(self, model_path):
        model = torch.load(model_path, map_location=self.device)
        model.eval()
        return model

    def upscale(self, image):
        # Convert image to tensor
        transform = transforms.ToTensor()
        tensor_image = transform(image).unsqueeze(0).to(self.device)
        
        # Perform super-resolution
        with torch.no_grad():
            output = self.model(tensor_image)
        
        # Convert tensor back to image
        output_image = output.squeeze().cpu().clamp(0, 1).numpy()
        output_image = (output_image * 255).astype(np.uint8)
        output_image = np.transpose(output_image, (1, 2, 0))
        return output_image
