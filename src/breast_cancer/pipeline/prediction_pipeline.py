from breast_cancer.components.predictor  import Predictor
from breast_cancer.config.configuration import ConfigurationManager
import pandas as pd


input_data = pd.DataFrame([{
    'radius_mean': 14.2,
    'texture_mean': 20.3,
    'perimeter_mean': 90.5,
    'area_mean': 580.0,
    'smoothness_mean': 0.08,
    'compactness_mean': 0.05,
    'concavity_mean': 0.03,
    'concave points_mean': 0.02,
    'symmetry_mean': 0.18,
    'fractal_dimension_mean': 0.06,

    'radius_se': 0.5,
    'texture_se': 1.0,
    'perimeter_se': 3.5,
    'area_se': 40.0,
    'smoothness_se': 0.005,
    'compactness_se': 0.015,
    'concavity_se': 0.02,
    'concave points_se': 0.01,
    'symmetry_se': 0.02,
    'fractal_dimension_se': 0.003,

    'radius_worst': 15.5,
    'texture_worst': 25.0,
    'perimeter_worst': 105.0,
    'area_worst': 700.0,
    'smoothness_worst': 0.12,
    'compactness_worst': 0.15,
    'concavity_worst': 0.2,
    'concave points_worst': 0.1,
    'symmetry_worst': 0.25,
    'fractal_dimension_worst': 0.08
}])

class PredictionPipeline:
    def __init__(self):
        pass
    def main(self,input):
        config = ConfigurationManager()
        prediction_config = config.prediction_config()
        predictor = Predictor(config=prediction_config)
        return predictor.predict(input_data=input)


if __name__ == "__main__":
    try :
        obj = PredictionPipeline()
        result = obj.main(input=input_data)
        print(result)
    except Exception as e:
        raise e
    