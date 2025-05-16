from breast_cancer.entity.config_entity import Prediction
import joblib
import numpy as np
import pandas as pd
class Predictor : 
    def __init__(self,config : Prediction):
        self.config = config
        self.model = joblib.load(self.config.model_path)
        self.scaler = joblib.load(self.config.scaler_path)
    def predict(self,input_data : pd.DataFrame):

        scaled_data = self.scaler.transform(input_data)

        prediction = self.model.predict(scaled_data)

        probability = self.model.predict_proba(scaled_data)

        label = "Malignant" if prediction[0] == 1 else "Benign"

        return {
            "prediction": label,
            "probability": f"{float(np.max(probability)) * 100:.2f}%"
        }


        # return prediction , probability

        
        