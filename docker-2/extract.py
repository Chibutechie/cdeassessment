import kaggle
import pandas as pd

kaggle.api.authenticate()


kaggle.api.dataset_download_files('carrie1/ecommerce-data', path='.', unzip=True)


kaggle.api.dataset_metadata('carrie1/ecommerce-data', path='.')


try:
    df = pd.read_csv('data.csv', encoding='ISO-8859-1') 
    
    print("\nFirst 5 rows of the DataFrame:")
    print(df.head())

    
except FileNotFoundError:
    print("Error: The dataset file was not found. Please check the filename in the unzipped folder.")
except Exception as e:
    print(f"An error occurred: {str(e)}")