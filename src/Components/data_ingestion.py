import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException 
from src.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    row_data_path:str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion_config(self):
        logging.info("Enter the Data Ingestion Component or Method")

        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the Dataset as DataFrame")
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.row_data_path,index=False,header=True)

            logging.info("Train Test Split Initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)    

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )    
        except Exception as e:
            raise CustomException(e,sys)
        
if(__name__)=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion_config()
            