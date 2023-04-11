import pandas as pd
import copy
import threading


def read_excel(excel_path: str):
    df: pd.DataFrame = pd.read_excel(excel_path, index_col=0)

    # preprocess the data
    workclass, _ = pd.factorize(df['workclass'])
    education, _ = pd.factorize(df['education'])
    marital_status, _ = pd.factorize(df['marital-status'])
    occupation, _ = pd.factorize(df['occupation'])
    relationship, _ = pd.factorize(df['relationship'])
    race, _ = pd.factorize(df['race'])
    sex, _ = pd.factorize(df['sex'])
    native_country, _ = pd.factorize(df['native-country'])

    df['workclass'] = workclass
    df['education'] = education
    df['marital-status'] = marital_status
    df['occupation'] = occupation
    df['relationship'] = relationship
    df['race'] = race
    df['sex'] = sex
    df['native-country'] = native_country

    return df

class DataPreprocessor:
    def __init__(self, customers_file_path: str, potential_customers_file_path: str):
        self.customers_file_path: str = customers_file_path
        self.potential_customers_file_path: str = potential_customers_file_path

        self.customers: pd.DataFrame = None
        self.potential_customers: pd.DataFrame = None

        # this hugely improved the execution time
        t1 = threading.Thread(target=self.preprocess_customers)
        t2 = threading.Thread(target=self.preprocess_potential_customers)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    def preprocess_customers(self):
        self.customers = read_excel(self.customers_file_path)
        self.customers['class'], _ = pd.factorize(self.customers['class'])

    def preprocess_potential_customers(self):
        self.potential_customers = read_excel(self.potential_customers_file_path)
