import torch
import torchvision
from PIL import Image
import numpy as np
import matplotlib.pylot as plt

model=torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

def segment_image(image_path):
    image=Image.open(image_path).convert("RGB")
    transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
    image_tensor=transform(image)
    with torch.no_grad():  
	    prediction=model([image_tensor]) 
    return image,prediction[0]

def plot_segmented_image(image, prediction):
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    for mask in prediction['masks']:
        mask = mask[0].mul(255).byte().cpu().numpy()
        plt.contour(mask, levels=[0.5], colors=['r'])
    plt.show()

if __name__ == "__main__":
    image_path = "../data/input_images/sample.jpg"
    image, prediction = segment_image(image_path)
    plot_segmented_image(image, prediction)