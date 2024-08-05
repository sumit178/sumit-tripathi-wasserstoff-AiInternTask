import os
import cv2
import numpy as np

def extract_objects(image, prediction, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    masks = prediction['masks'].detach().numpy()
    unique_id = 0
    for mask in masks:
        mask = mask[0]
        _, binary_mask = cv2.threshold(mask, 0.5, 1, cv2.THRESH_BINARY)
        binary_mask = binary_mask.astype(np.uint8)
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            object_image = image[y:y+h, x:x+w]
            object_path = os.path.join(output_dir, f"object_{unique_id}.png")
            cv2.imwrite(object_path, cv2.cvtColor(object_image, cv2.COLOR_RGB2BGR))
            unique_id += 1

if __name__ == "__main__":
    image_path = "../data/input_images/sample.jpg"
    output_dir = "../data/segmented_objects/"
    image, prediction = segment_image(image_path)
    image_np = np.array(image)
    extract_objects(image_np, prediction, output_dir)
