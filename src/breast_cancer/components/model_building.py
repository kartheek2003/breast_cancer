from breast_cancer import logger
from breast_cancer.pipeline.stage04_data_transformation import data_transformation_pipeline
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
import joblib
import os 
from breast_cancer.entity.config_entity import ModelBuilding

class ModelBuildingComponent :
    def __init__(self,config:ModelBuilding):
        self.config = config

    def load_data(self):
        data = data_transformation_pipeline()
        return data.main()
    def model(self):
        x_train, x_test, y_train, y_test = self.load_data()
        logger.info("data load complete")
        rf = RandomForestClassifier(random_state=self.config.random_state)
        gb = GradientBoostingClassifier(random_state=self.config.random_state)

        rf_params = {
            'n_estimators': [50, 100, 150],
            'max_depth': [3, 5, 10, None]
        }

        gb_params = {
            'n_estimators': [50, 100, 150],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7]
        }

        #random search for rf
        rf_search = RandomizedSearchCV(rf,rf_params,n_iter=self.config.n_iter, cv= self.config.cv, n_jobs= self.config.n_jobs)
        rf_search.fit(x_train,y_train)
        rf_best = rf_search.best_estimator_

        logger.info("rf_best")

        #random search for gradien boost
        gb_search = RandomizedSearchCV(gb,gb_params,n_iter=self.config.n_iter, cv= self.config.cv, n_jobs= self.config.n_jobs)
        gb_search.fit(x_train,y_train)
        gb_best = gb_search.best_estimator_

        logger.info("gb_best")

        #ensemble

        ensemble = VotingClassifier(estimators=[
            ("rf",rf_best),
            ("gb",gb_best)
        ],voting="soft")

        ensemble.fit(x_train,y_train)

        logger.info("ensemble model trained")

        #eval

        y_pred = ensemble.predict(x_test)

        logger.info("prediction done")

        acc = accuracy_score(y_true = y_test , y_pred=y_pred)

        print(f"Ensemble Test Accuracy: {acc:.4f}")

        joblib.dump(ensemble,os.path.join(self.config.model_save_path, "ensemble.pkl"))

        logger.info("model saved")

        return ensemble