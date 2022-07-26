from stock.pipeline.pipeline import Pipeline
from stock.exception import StockException
from stock.logger import logging
from stock.config.configuration import Configuartion
from stock.component.data_transformation import DataTransformation
from stock.component.data_ingestion import DataIngestion 
from stock.constant import get_current_time_stamp

def main():
    try:
        pipeline = Pipeline(config=Configuartion(current_time_stamp=get_current_time_stamp()))
        if not Pipeline.experiment.running_status:
            message = "Training started."
            pipeline.start()
        else:
            message = "Training is already in progress."
        context = {
            "experiment": pipeline.get_experiments_status().to_html(classes='table table-striped col-12'),
            "message": message
        }
        
        pipeline.run_pipeline()
        logging.info("main function execution completed.")
        # # data_validation_config = Configuartion().get_data_transformation_config()
        # # print(data_validation_config)
        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\stock\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\stock.csv"

        # df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()