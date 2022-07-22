from collections import namedtuple
from datetime import datetime
import uuid
from stock.config.configuration import Configuartion
from stock.logger import logging, get_log_file_name
from stock.exception import StockException
from threading import Thread
from typing import List
from multiprocessing import Process
import os, sys
import pandas as pd

from stock.entity.artifact_entity import  DataIngestionArtifact #ModelEvaluationArtifact,ModelPusherArtifact
from stock.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact #, ModelTrainerArtifact
from stock.entity.config_entity import DataIngestionConfig# ModelEvaluationConfig
from stock.component.data_ingestion import DataIngestion
from stock.component.data_validation import DataValidation
from stock.component.data_transformation import DataTransformation
# from stock.component.model_trainer import ModelTrainer
# from stock.component.model_evaluation import ModelEvaluation
# from stock.component.model_pusher import ModelPusher

# from stock.constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME

config = Configuartion()
os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)

class Pipeline(Thread):

    def __init__(self, config: Configuartion = config ) -> None:
        try:
            super().__init__(daemon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise StockException(e,sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise StockException(e, sys) from e
    
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) \
            -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise StockException(e, sys) from e

    def start_data_transformation(self,
                                  data_ingestion_artifact: DataIngestionArtifact,
                                  data_validation_artifact: DataValidationArtifact
                                  ) -> DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise StockException(e, sys)
    
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(model_trainer_config=self.config.get_model_trainer_config(),
                                         data_transformation_artifact=data_transformation_artifact
                                         )
            return model_trainer.initiate_model_trainer()
        except Exception as e:
            raise HousingException(e, sys) from e


    def run_pipeline(self):
        try:
            # self.start_data_ingestion()
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
        
        
        except Exception as e:
            raise StockException(e, sys)
