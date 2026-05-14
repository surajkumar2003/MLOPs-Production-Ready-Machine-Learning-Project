import os
from datetime import date
from dotenv import load_dotenv

MONGODB_URL= os.getenv("MONGODB_URL")

DATABASE_NAME="US_VISA"

COLLECTION_NAME="visa_data"

MONGODB_URL_KEY="MONGODB_URL"

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "visa.csv"
MODEL_FILE_NAME="model.pkl"


TARGET_COLUMN: str = "CASE_STATUS"
CURRENT_YEAR= date.today().year
PREPROCESSING_OBJECT_FILE_NAME="preprocessing.pkl"
SCHEMA_FILE_PATH=os.path.join("config","schema.yaml")

"""
Data Ingestion related constants starts with DATA_INGESTION VARIBLES NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


""""
Data Validation related constants starts with DATA_VALIDATION VARIBLES NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"