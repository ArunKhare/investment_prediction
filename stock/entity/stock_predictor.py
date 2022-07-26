import os
import sys
import pandas as pd
from stock.exception import StockException
from stock.util.util import load_object
from datetime import datetime



class StockData:

    def __init__(self,
                 Date,
                 Prev_Close:float,
                 Open:float,
                 High:float,
                 Low:float,
                 VWAP:float,
                 Volume:int,
                 Close: float=None
                ):
               
        try:
           
            self.Date = Date
            self.Close = Close
            self.Prev_Close = Prev_Close
            self.Open = Open
            self.High = High
            self.Low = Low
            self.VWAP = VWAP
            self.Volume = Volume
        except Exception as e:
            raise StockException(e, sys) from e

    def get_stock_input_data_frame(self):

        try:
            stock_input_dict = self.get_stock_data_as_dict()
            df = pd.DataFrame(stock_input_dict)
            df['Date'] = pd.to_numeric(df['Date'])
            return df
        except Exception as e:
            raise StockException(e, sys) from e

    def get_stock_data_as_dict(self):
        try:
            
            input_data = {
                "Date": [self.Date],
                "Prev_Close": [self.Prev_Close],
                "Open": [self.Open],
                "High": [self.High],
                "Low":  [self.Low],
                "VWAP": [self.VWAP],
                "Volume": [self.Volume]
            }
            return input_data
        except Exception as e:
            raise StockException(e, sys)


class StockPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise StockException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
           
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
           
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
           
            return latest_model_path
        except Exception as e:
            raise StockException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            print('model_path', model_path)
            model = load_object(file_path=model_path)
            Close = model.predict(X)
            return Close
        except Exception as e:
            raise StockException(e, sys) from e