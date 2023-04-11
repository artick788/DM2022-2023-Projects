import pandas as pd
import copy
import threading
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from DatasetPreprocessor import read_excel
from sklearn.metrics import confusion_matrix


def create_confusion_matrix(classifier, train, validation):
    classifier.fit(train.iloc[:, :-1], train.iloc[:, -1])
    predictions = classifier.predict(validation.iloc[:, :-1])
    actual = validation.iloc[:, -1]

    # cm = pd.crosstab(actual, predictions, rownames=['Actual'], colnames=['Predicted'])
    cm = confusion_matrix(actual, predictions, labels=[1, 0])
    tn, fp, fn, tp = cm.ravel()
    return tn, fp, fn, tp


def main():
    # split the existing customers into train and validation sets
    customers: pd.DataFrame = read_excel('data/existing-customers.xlsx')
    customers['class'], _ = pd.factorize(customers['class'])
    train, validation = train_test_split(customers, test_size=0.2, random_state=42)

    # train and validate the classifiers
    classifier: GaussianNB = GaussianNB()
    create_confusion_matrix(classifier, train, validation)


if __name__ == "__main__":
    main()

