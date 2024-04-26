# medical_predictor.py
import asyncio

async def prediction_service(image_path: str) -> dict:
    await asyncio.sleep(1)
    return {
        "image": image_path,
        "prediction": "Pneumonia",
        "confidence": 95.5
    }

async def mark_image(image_data: bytes, marks: list) -> bytes:
    await asyncio.sleep(1)
    return image_data

async def main():
    prediction = await prediction_service("path/to/xray_image.jpg")
    print("Prediction:", prediction)
    
    image_data = b'original_image_data'
    marks = [{"shape": "circle", "coordinates": (100, 150), "radius": 10}]
    marked_image = await mark_image(image_data, marks)
    print("Image Processed:", marked_image)

if __name__ == "__main__":
    asyncio.run(main())
