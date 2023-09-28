from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from pathlib import Path
import joblib

# Call constructor and assign to variable app
app = FastAPI()

# Load base_dir
BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load pre-trained model
with open(f"{BASE_DIR}/model.pkl", "rb") as file:
    model = joblib.load(file)


class request_body(BaseModel):
    YearsExperiences: float


# The root route
@app.get("/")
async def root():
    return {"message": "Welcome to Salary Prediction!"}


# Welcome page
@app.get("/welcome")
async def say_hello():
    return {"message": ""}


@app.post("/predict/")
def predict(data: request_body):
    feature = data.YearsExperiences
    test_data = [[feature]]
    prediction = model.predict(test_data)

    return {"prediction": prediction.tolist()}


# Run API
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
