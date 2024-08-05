import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def identify_objects(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(text=["a photo of a cat", "a photo of a dog", "a photo of a bird"], images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    return probs

if __name__ == "__main__":
    object_image_path = "../data/segmented_objects/object_0.png"
    probs = identify_objects(object_image_path)
    print(probs)
