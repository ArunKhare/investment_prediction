from stock.entity.config_entity import DataIngestionConfig

from stock.exception import StockException
from stock.logger import logging

import sys, os
from nsepy import get_history
from datetime import date
import pandas as pd
import shutil
from stock.entity.artifact_entity import DataIngestionArtifact
from datetime import datetime

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info("{=*20} Data ingestion start{=*20}")
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise StockException(e, sys) from e

    """"
    def download_symbol (self,)-> str:
        try:
            download_symbol_url = self.data_ingestion_config.symbol_download_url

            os.makedirs(raw_download_dir,exist_ok=True)

            symbol_file_name = os.path.basename(download_symbol_url)

            raw_file_path = os.path.join(raw_download_dir,symbol_file_name)

            if not os.path.exists(raw_file_path.symbol_file_name):
                urllib.request.urlretrieve(download_symbol_url, raw_file_path)
                logging.info(f"Download file from :[{download_symbol_url}] into [{raw_file_path}]")
            else:
                logging.info(f"symbols file already exist")
                
            return raw_file_path
            
           
        except Exception as e:
            raise StockException(e, sys) from e """


    def downloading_stock_data(self,)-> str:
        try:

            # extraction remote url to download dataset
                        
            raw_download_dir = self.data_ingestion_config.raw_data_dir
            start_date =self.data_ingestion_config.start_date
            end_date = self.data_ingestion_config.end_date
            stock_symbol = self.data_ingestion_config.stock_symbol

            os.makedirs(raw_download_dir,exist_ok=True)
            
            # stock_data_df = get_history(symbol= stock_symbol,start=datetime.strptime(start_date,"%Y,%m,%d"), end=datetime.strptime(end_date,"%Y,%m,%d"))
            
            
            raw_file_path = os.path.join(raw_download_dir,stock_symbol)
                
            # logging.info(f"Download file from :[{stock_data_df}] into [{raw_file_path}]")
            # stock_data_df.to_csv(raw_file_path)
            file_path= r"C:\Users\arunk\OneDrive\Documents\GitHub\investment_prediction\stock\artifact\data_ingestion\2022-07-26-16-18-27\raw_data\SBIN"
            shutil.copy(file_path,raw_file_path)

            return raw_file_path

        except Exception as e:
            raise StockException(e, sys) from e
          
    
    def split_data_as_train_test(self,tqz_file_path:str) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            stock_file_path = os.path.join(raw_data_dir,file_name)
            
            
            logging.info(f"Reading csv file: [{stock_file_path}]")
            stock_data_frame = pd.read_csv(stock_file_path,index_col=None)
            # stock_data_frame.reset_index(inplace=True)

             # convert date column to Datetime and convert date to numeric
            stock_data_frame["Date"] = pd.to_datetime(stock_data_frame['Date'])
            stock_data_frame['Date'] = pd.to_numeric(stock_data_frame["Date"])

            # filter the columns required
            # filtered_stock_df =stock_data_frame.filter(['Date', 'Close', 'Prev Close','Open','High','Low', 'VWAP', 'Volume'])
            
            filtered_stock_df = stock_data_frame.drop(['Symbol', 'Series', 'Last','Turnover', 'Trades', 'Deliverable Volume','%Deliverble'],axis=1)

            filtered_stock_df.rename(columns = {'Prev Close':'Prev_Close'}, inplace = True)
            logging.info(f"Splitting data into train and test")
           
            sliced_train_set = filtered_stock_df.iloc[:987,:]
            sliced_test_set = filtered_stock_df.iloc[987:,:]


            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)
            
            if sliced_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                sliced_train_set.to_csv(train_file_path,index=False)

            if sliced_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                sliced_test_set.to_csv(test_file_path,index=False)
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise StockException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            raw_file_path =  self.downloading_stock_data()

            return self.split_data_as_train_test(raw_file_path)

        except Exception as e:
           raise StockException(e,sys) from e
    


    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")

