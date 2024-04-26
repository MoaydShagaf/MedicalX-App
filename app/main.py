from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND
from .services.medical_predictor import prediction_service, mark_image
import uvicorn

app = FastAPI(title="MedicalX-App")

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs', status_code=HTTP_302_FOUND)

@app.post("/get_predictions")
async def get_predictions(image: UploadFile = File(...)):
    if not image.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Invalid file format.")
    # Assuming prediction_service is a function that takes an image file and returns predictions
    predictions = await prediction_service(image)
    return {"filename": image.filename, "predictions": predictions}

@app.post("/get_predicted_image")
async def get_predicted_image(image: UploadFile = File(...)):
    if not image.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Invalid file format.")
    # Assuming mark_image is a function that processes the image and returns a new image with marks
    marked_image = await mark_image(image)
    return {"filename": image.filename, "marked_image": marked_image}

# Functions like prediction_service and mark_image need to be implemented
# They should handle the AI processing and image marking, respectively

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
