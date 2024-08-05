import json

def map_data(image_id, object_data):
    mapping = {
        "image_id": image_id,
        "objects": object_data
    }
    with open(f"../data/output/mapping_{image_id}.json", "w") as f:
        json.dump(mapping, f, indent=4)

if __name__ == "__main__":
    image_id = 1
    object_data = [
        {
            "object_id": 0,
            "description": "a photo of a cat",
            "text": "The cat is sitting on the mat.",
            "summary": "A happy cat sitting on the mat."
        }
    ]
    map_data(image_id, object_data)
