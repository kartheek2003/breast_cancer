from breast_cancer import logger
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
# from sklearn.decomposition import PCA
import joblib
from breast_cancer.entity.config_entity import DataTransform

class DataTransformation:
    def __init__(self,config : DataTransform):
        self.config = config

    def load_data(self):
        return pd.read_csv(self.config.df_path)
    
    def get_data_transformation(self):
        try:
            df = self.load_data()
            x = df.drop(['diagnosis'],axis=1)
            y = df['diagnosis'].replace({'M':1,'B':0})
            #split
            logger.info("train test split")
            x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = self.config.test_size,random_state=self.config.random_state)
            
            #scaling

            logger.info("Standard Scaling")
            scaler = StandardScaler()
            x_train_scaled = scaler.fit_transform(x_train)
            joblib.dump(scaler , os.path.join(self.config.scaler_path,"scaler.pkl"))
            x_test_scaled = scaler.transform(x_test)

            #SMOTE
            logger.info("synthetic minority over sampling technique")
            smote = SMOTE(k_neighbors=self.config.smote_k_neighbours,random_state=self.config.random_state)
            x_res , y_res = smote.fit_resample(x_train_scaled,y_train)


            #pca 

            # logger.info("principal component analysis")

            # pca = PCA(n_components=self.config.n_pca_components,random_state=self.config.random_state)

            # x_train_pca = pca.fit_transform(x_res)
            # joblib.dump(pca,os.path.join(self.config.pca_model_path,"pca.pkl"))
            # x_test_pca = pca.transform(x_test)

            return x_res,x_test_scaled, y_res, y_test

        except Exception as e:
            raise e
            

        

