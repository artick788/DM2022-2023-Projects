import pandas as pd
from sklearn.naive_bayes import GaussianNB


def read_excel(excel_file_path: str) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_excel(excel_file_path, index_col=0)

    # postprocess the data
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


if __name__ == '__main__':
    customers = read_excel('data/existing-customers.xlsx')
    salary, _ = pd.factorize(customers['class'])
    customers['class'] = salary

    potential_customers = read_excel('data/potential-customers.xlsx')

    # Create a Gaussian Naive Bayes classifier
    classifier = GaussianNB()
    # Train the classifier on the customers dataset using all columns except the last one which is salary
    classifier.fit(customers.iloc[:, :-1], customers.iloc[:, -1])
    # Predict the potential customers salary
    predictions = classifier.predict(potential_customers.iloc[:, :])

    potential_customers['pred_class'] = predictions
    ids = potential_customers.loc[potential_customers['pred_class'] == 1].index

    with open("RowIDs.txt", "w") as f:
        for id in ids:
            f.write(str(id) + "\n")
