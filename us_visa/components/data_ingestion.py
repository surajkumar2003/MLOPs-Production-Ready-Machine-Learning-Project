import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.exception import USVisaException
from us_visa.logger import logging
from us_visa.data_access.usvisa_data import USVisaData

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig()):
        """
        param data_ingestion_config: configuration for data ingestion
        """

        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise USVisaException(e, sys)   


    def export_data_into_feature_store(self) -> DataFrame:
        """
        Method Name: export_data_into_feature_store
        Description: This method exports the dataframe from mongodb to csv file
        Output: data is returned as artifact of data ingestion components
        On Failure: write an exception lof and then raise an exceotion
        """

        try:
            logging.info(f"Exporting data from mongodb")
            usvisa_data = USVisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}") 
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe    
        except Exception as e:
            raise USVisaException(e, sys)
        
    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        """
        Method Name: split_data_as_train_test
        Description: This method splits the data into train and test file
        Output: folder is created in artifact directory and train and test file is saved in that folder
        On Failure: write an exception log and then raise an exception
        """    
        logging.info(f"Entered split_data_as_train_test method of DataIngestion class")

        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe ")
            logging.info("Exited split_data_as_train_test method of DataIngestion class")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Exporting train and test file to path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info(f"Exported train and test file to path successfully.")

        except Exception as e:
            raise USVisaException(e, sys)  


    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Method Name: initiate_data_ingestion
        Description: This method initiates the data ingestion and returns the artifact

        output: train set and test set are returned as artifact of data ingestion component
        on failure: write an exception log and then raise an exception
        """      
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Got the data from mongodb")

            self.split_data_as_train_test(dataframe=dataframe)

            logging.info("Performed train test split on the dataset")

            logging.info("Exited initiate_data_ingestion method of DataIngestion class")
            data_ingestion_artifact = DataIngestionArtifact(training_file_path=self.data_ingestion_config.training_file_path,
                                                            testing_file_path=self.data_ingestion_config.testing_file_path)
            
            logging.info(f"Data Ingestion artifact: {data_ingestion_artifact}"
                         )
            return data_ingestion_artifact
        
        except Exception as e:
            raise USVisaException(e, sys)

            