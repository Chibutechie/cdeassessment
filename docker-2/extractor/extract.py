import kaggle
import pandas as pd

kaggle.api.authenticate()


kaggle.api.dataset_download_files('carrie1/ecommerce-data', path='.', unzip=True)


kaggle.api.dataset_metadata('carrie1/ecommerce-data', path='.')


try:
    data = pd.read_csv('data.csv', encoding='ISO-8859-1') 
    
    print(data.head(10))

    
except Exception as e:
    print(f"An error occurred: {str(e)}")