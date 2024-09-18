from fastapi import FastAPI, Depends, Security, HTTPException

# import pickle
import mlflow

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin, BaseEstimator

app = FastAPI()


@app.on_event("startup")
def load_model():

    global loaded_model

    # with open("../../model/model.pickle", "rb") as openfile:
    #     model1 = pickle.load(openfile)
    model_uri = ""
    loaded_model = mlflow.pyfunc.load_model(model_uri)


@app.get("/health")
async def root():
    return {"message": "Hello World"}


# @app.get("/predict")
# async def predict():
#     X_test, y_test = get_test_data()
#     predictions = loaded_model.predict(X_test)

#     return {"actual_class": y_test[:4], "predicted_class": predictions[:4]}
