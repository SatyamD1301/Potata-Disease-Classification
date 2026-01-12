from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- STEP 1: MODEL PATH CONFIGURATION ---

MODEL_PATH = r"C:\Users\AMBREESH\Desktop\jbooks\potato-disease\saved_models\8"


if not os.path.exists(MODEL_PATH):
    print(f" ERROR: Model folder '{MODEL_PATH}' nahi mila!")
    print("Kripya check karein ki folder ka sahi path kya hai.")
else:
    try:
        model_layer = tf.keras.layers.TFSMLayer(MODEL_PATH, call_endpoint='serving_default')
        MODEL = tf.keras.Sequential([model_layer])
        print(f"Model folder '8' se successfully load ho gaya!")
    except Exception as e:
        print(f" Model load karne mein error: {e}")

CLASS_NAMES = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]

@app.get("/ping")
async def ping():
    return "Server is running!"

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).convert("RGB").resize((256, 256))
    return np.array(image)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    predictions = MODEL(img_batch)
    
   
    if isinstance(predictions, dict):
        output_key = list(predictions.keys())[0]
        prediction_tensor = predictions[output_key][0]
    else:
        prediction_tensor = predictions[0]

    predicted_class = CLASS_NAMES[np.argmax(prediction_tensor)]
    confidence = float(np.max(prediction_tensor))

    return {
        'class': predicted_class,
        'confidence': confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)