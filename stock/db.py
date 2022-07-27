import sqlite3


connection = sqlite3.connect('investment_pred.db')
cursor = connection.cursor()

yaml_config_path = r'C:\Users\arunk\OneDrive\Documents\GitHub\investment_prediction\Config\config.yaml'
yaml_schema_path = r'C:\Users\arunk\OneDrive\Documents\GitHub\investment_prediction\Config\schema.yaml'
yaml_model_path = r'C:\Users\arunk\OneDrive\Documents\GitHub\investment_prediction\Config\model.yaml'

log_folder = r'C:\Users\arunk\OneDrive\Documents\GitHub\investment_prediction\logs'
saved_models_path = r'C:\Users\arunk\OneDrive\Documents\GitHub\investment_prediction\saved_models'
artifact_path =r'C:\Users\arunk\OneDrive\Documents\GitHub\investment_prediction\stock\artifact'