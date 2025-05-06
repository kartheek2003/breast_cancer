import seaborn as sns
import matplotlib.pyplot as plt
from breast_cancer import logger
from breast_cancer.entity.config_entity import EDAconfig
import os
from pathlib import Path
import pandas as pd

class EDA :
    def __init__(self,config:EDAconfig):
        self.config = config
    
    def load_data(self):
        return pd.read_csv(self.config.df_clean_path)
    
    def perform_eda(self):
        try:
            df = self.load_data()
            logger.info("df_cleaned loaded as df")

            # os.makedirs(self.config.report_path,exist_ok=True)

            #basic_info
            with open(os.path.join(self.config.report_path,"basic_info.txt"),"w") as f:
                df.info(buf=f)
                f.write("\n\n")
                f.write(str(df.describe()))

            logger.info("basic info written")

            #class distribution or count plot
            sns.countplot(data=df,x = "diagnosis")
            plt.title("class distribution")
            plt.savefig(os.path.join(self.config.report_path,"countplot.png"))
            plt.clf()
            
            logger.info("class distribution graphs")


            #correlation
            plt.figure(figsize=(12,10))
            sns.heatmap(df.drop("diagnosis",axis=1).corr(),cmap="coolwarm",annot=False)
            plt.title("collinearity between features")
            plt.savefig(os.path.join(self.config.report_path,"correlation.png"))
            plt.clf()

            logger.info("correlation")

            #histograms / distribution plots
            df.drop("diagnosis",axis=1).hist(figsize=(16,12))
            plt.title("distribution plots")
            plt.savefig(os.path.join(self.config.report_path,"distribution_plots.png"))
            plt.clf()

            logger.info("histograms")

            #Boxplots
            plt.figure(figsize=(10,6))
            sns.boxplot(data=df,orient="h")
            plt.title("Box Plots")
            plt.savefig(os.path.join(self.config.report_path,"boxplots.png"))
            plt.clf() 

            logger.info("Boxplots")

            #pairplot
            sns.pairplot(df,hue="diagnosis")   
            # plt.title("Pair Plots")
            plt.savefig(os.path.join(self.config.report_path,"pairplot.png"))
            plt.clf()
            
            logger.info("pairplot")

            #violin plots
            for col in df.columns:
                if col=="diagnosis":
                    continue
                sns.violinplot(data=df,x="diagnosis",y=col)
                plt.title(f"violinplot-{col}")
                plt.savefig(os.path.join(self.config.report_path,f"violin_{col}.png"))
                plt.clf()

            logger.info("violin plots")

            #feature vs target bar plots

            df.groupby("diagnosis").mean().T.plot(kind="bar",figsize=(12,6))
            plt.title("feature vs target bar plot")
            plt.savefig(os.path.join(self.config.report_path,"feature_vs_target_barplot.png"))
            plt.clf()

            logger.info("done with EDA...loaded the entire analysis to report folder in artifacts")

        except Exception as e:
            raise e