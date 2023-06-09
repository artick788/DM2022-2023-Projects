import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


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


def create_confusion_matrix(classifier, train, validation):
    classifier.fit(train.iloc[:, :-1], train.iloc[:, -1])
    predictions = classifier.predict(validation.iloc[:, :-1])
    actual = validation.iloc[:, -1]

    # cm = pd.crosstab(actual, predictions, rownames=['Actual'], colnames=['Predicted'])
    cm = confusion_matrix(actual, predictions, labels=[1, 0], normalize='all')
    tn, fp, fn, tp = cm.ravel()
    return tn, fp, fn, tp


def main():
    # split the existing customers into train and validation sets
    customers: pd.DataFrame = read_excel('data/existing-customers.xlsx')
    customers['class'], _ = pd.factorize(customers['class'])
    potential_customers: pd.DataFrame = read_excel('data/potential-customers.xlsx')
    train, validation = train_test_split(customers, test_size=0.2, random_state=42)

    # train and validate the classifiers
    classifier = DecisionTreeClassifier()
    tn, fp, fn, tp = create_confusion_matrix(classifier, train, validation)
    print(f'GaussianNB: tn={tn}, fp={fp}, fn={fn}, tp={tp}')

    # predict the potential customers
    predictions = classifier.predict(potential_customers.iloc[:, :])
    potential_customers['pred_class'] = predictions
    ids = potential_customers.loc[potential_customers['pred_class'] == 1].index

    with open("RowIDs.txt", "w") as f:
        for id in ids:
            f.write(str(id) + "\n")

    # calculate estimated revenue
    sent_packages = len(ids)
    positive_revenue = (sent_packages * tp) * ((0.1 * 980) - 10)
    negative_revenue = (sent_packages * fp) * ((0.05 * -310) - 10)
    estimated_revenue = positive_revenue + negative_revenue
    print(f'Estimated revenue: {estimated_revenue}')
    print(f'Total packages sent: {sent_packages}')
    print(f'TP packages: {tp * sent_packages}')
    print(f'FP packages: {fp * sent_packages}')


if __name__ == "__main__":
    main()

