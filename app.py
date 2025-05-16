from flask import Flask, render_template, request
import pandas as pd
from breast_cancer.components.predictor import Predictor
from breast_cancer.config.configuration import ConfigurationManager

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Collect all 30 feature inputs from the form
            features = [
                float(request.form.get("radius_mean")),
                float(request.form.get("texture_mean")),
                float(request.form.get("perimeter_mean")),
                float(request.form.get("area_mean")),
                float(request.form.get("smoothness_mean")),
                float(request.form.get("compactness_mean")),
                float(request.form.get("concavity_mean")),
                float(request.form.get("concave points_mean")),
                float(request.form.get("symmetry_mean")),
                float(request.form.get("fractal_dimension_mean")),

                float(request.form.get("radius_se")),
                float(request.form.get("texture_se")),
                float(request.form.get("perimeter_se")),
                float(request.form.get("area_se")),
                float(request.form.get("smoothness_se")),
                float(request.form.get("compactness_se")),
                float(request.form.get("concavity_se")),
                float(request.form.get("concave points_se")),
                float(request.form.get("symmetry_se")),
                float(request.form.get("fractal_dimension_se")),

                float(request.form.get("radius_worst")),
                float(request.form.get("texture_worst")),
                float(request.form.get("perimeter_worst")),
                float(request.form.get("area_worst")),
                float(request.form.get("smoothness_worst")),
                float(request.form.get("compactness_worst")),
                float(request.form.get("concavity_worst")),
                float(request.form.get("concave points_worst")),
                float(request.form.get("symmetry_worst")),
                float(request.form.get("fractal_dimension_worst"))
            ]

            columns = [
                'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
                'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean',
                'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
                'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
                'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst',
                'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
                'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst',
                'fractal_dimension_worst'
            ]

            input_data = pd.DataFrame([features], columns=columns)

            config = ConfigurationManager().prediction_config()
            predictor = Predictor(config=config)
            result = predictor.predict(input_data=input_data)

            return render_template('index.html', prediction=result)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
