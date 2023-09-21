from fastapi import FastAPI
import uvicorn
from basemodel import request_body
import joblib

# Call constructor and assign to variable app
app = FastAPI()

# Load pre-trained model
model = joblib.load("model.pkl")


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
