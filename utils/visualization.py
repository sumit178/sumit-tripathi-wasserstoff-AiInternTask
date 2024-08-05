import matplotlib.pyplot as plt
import cv2
import json

def visualize_output(image_path, mapping_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with open(mapping_path, "r") as f:
        mapping = json.load(f)

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    for obj in mapping["objects"]:
        x, y, w, h = obj["bbox"]
        plt.gca().add_patch(plt.Rectangle((x, y), w, h, linewidth=2, edgecolor='r', facecolor='none'))
        plt.text(x, y, f'ID: {obj["object_id"]}\n{obj["description"]}', bbox=dict(facecolor='white', alpha=0.5))

    plt.show()

if __name__ == "__main__":
    image_path = "../data/input_images/sample.jpg"
    mapping_path = "../data/output/mapping_1.json"
    visualize_output(image_path, mapping_path)
