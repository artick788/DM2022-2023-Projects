from DatasetPreprocessor import DataPreprocessor
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import ClassifierMixin
import copy
import threading


class Classifier:
    def __init__(self, dataProc: DataPreprocessor):
        self.dataProc: DataPreprocessor = dataProc

        self.ids_nb: list = []
        self.ids_dt: list = []
        self.ids_knn: list = []

    def run_classifier(self, classifier):
        customers = copy.deepcopy(self.dataProc.customers)
        potential_customers = copy.deepcopy(self.dataProc.potential_customers)

        # Train the classifier on the customers dataset using all columns except the last one which is salary
        classifier.fit(customers.iloc[:, :-1], customers.iloc[:, -1])
        # Predict the potential customers salary
        predictions = classifier.predict(potential_customers.iloc[:, :])

        potential_customers['pred_class'] = predictions
        ids = potential_customers.loc[potential_customers['pred_class'] == 1].index

        return list(ids)

    def run_gaussian_naive_bayes(self):
        self.ids_nb = self.run_classifier(GaussianNB())

    def run_decision_tree(self):
        self.ids_dt = self.run_classifier(DecisionTreeClassifier())

    def run_knn(self):
        self.ids_knn = self.run_classifier(KNeighborsClassifier())

    def run_all(self):
        t1 = threading.Thread(target=self.run_gaussian_naive_bayes)
        t2 = threading.Thread(target=self.run_decision_tree)
        t3 = threading.Thread(target=self.run_knn)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

    def get_intersection(self) -> list:
        # get the intersection of the three lists but keep the order
        set_dt = frozenset(self.ids_dt)
        set_knn = frozenset(self.ids_knn)
        intersection = [x for x in self.ids_nb if x in set_dt and x in set_knn]
        return intersection


if __name__ == '__main__':
    dataProcessor = DataPreprocessor('data/existing-customers.xlsx', 'data/potential-customers.xlsx')
    c: Classifier = Classifier(dataProcessor)
    c.run_decision_tree()

    ids = c.ids_dt

    with open("RowIDs.txt", "w") as f:
        for id in ids:
            f.write(str(id) + "\n")
