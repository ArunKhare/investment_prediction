from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
["start_date","end_date","stock_symbol", "raw_data_dir","ingested_train_dir","ingested_test_dir"]) 

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path","report_file_path","report_page_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","model_config_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])


ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])