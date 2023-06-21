import Apriori as AP1
from utils import *
from AssociationRules import *

MIN_SUPPORT = 0.3
MIN_CONFIDENCE = 0.5
MIN_LIFT = 1.0


def test_apriori():
    transactions = [
        {'D', 'H', 'B', 'J', 'I'},
        {'J', 'F', 'A'},
        {'A', 'G', 'E', 'J'},
        {'B', 'A', 'H', 'J'},
        {'B', 'J', 'G'},
        {'F'},
        {'J'},
        {'I', 'E'},
        {'F'},
        {'C', 'D'},
        {'A', 'G', 'D'},
        {'H', 'F', 'A'},
        {'A', 'I', 'C'},
        {'A', 'I', 'G', 'C'},
        {'B', 'J', 'I', 'G'},
        {'C'},
        {'B', 'A', 'E', 'F'},
        {'G', 'C', 'F'},
        {'J', 'I', 'E'},
        {'H', 'I'},
        {'H', 'I', 'J'},
        {'A', 'D'},
        {'H', 'D'},
        {'A', 'C', 'E', 'F'},
        {'H', 'C', 'A'},
        {'B', 'H', 'I', 'C'},
        {'B', 'A', 'F'},
        {'H', 'E'},
        {'B', 'H', 'G', 'F'},
        {'H', 'J', 'G', 'A'},
        {'E'},
        {'D'},
        {'H', 'G', 'J'},
        {'G', 'H', 'C', 'B', 'I'},
        {'E', 'D', 'A', 'C', 'B'},
        {'I'},
        {'H', 'E'},
        {'H', 'G'},
        {'A', 'I', 'G'},
        {'A'},
        {'B', 'J', 'C', 'F'},
        {'C'},
        {'A', 'J'},
        {'F', 'H', 'C', 'B', 'J'},
        {'I'},
        {'B', 'I', 'C'},
        {'H', 'G', 'J'},
        {'C'},
        {'A', 'G', 'F', 'D'},
        {'A', 'I', 'F'},
        {'A', 'I', 'G', 'C'},
        {'G', 'E', 'A', 'C', 'B'},
        {'A', 'I', 'J'},
        {'A', 'D'},
        {'G', 'E', 'C', 'B', 'J'},
        {'E'},
        {'J', 'C', 'E', 'F'},
        {'I', 'G'},
        {'A'},
        {'H', 'G', 'E'},
        {'B', 'E'},
        {'B', 'J', 'G'},
        {'H', 'G'},
        {'H'},
        {'I'},
        {'A', 'G', 'D'},
        {'B'},
        {'H'},
        {'I', 'G'},
        {'A', 'J', 'F', 'H'},
        {'A', 'D', 'F'},
        {'B', 'J', 'E'},
        {'H', 'E'},
        {'B'},
        {'B'},
        {'E', 'C', 'D'},
        {'E'},
        {'A'},
        {'J', 'G'},
        {'H'},
        {'J', 'E', 'G', 'D'},
        {'I', 'D', 'F'},
        {'B', 'F'},
        {'B'},
        {'I', 'C', 'D'},
        {'J', 'F', 'D'},
        {'F', 'A', 'B', 'J', 'I'},
        {'H', 'D', 'A'},
        {'B', 'I'},
        {'A', 'C', 'E', 'F'},
        {'G', 'C'},
        {'A', 'G'},
        {'H', 'I'},
        {'J', 'I', 'F'},
        {'G'},
        {'H'},
        {'B', 'C', 'F'},
        {'H'},
        {'B', 'C'},
        {'E', 'A', 'H', 'C', 'I'},
    ]
    print("======================Support=====================")
    support = get_support_item(transactions)
    print(support)
    print("=====================Apriori===================")
    frequent_itemsets, itemsets_by_length = AP1.apriori(transactions, MIN_SUPPORT)
    rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    print_rules(rules)
    # print("=================AprioriPruning================")
    # frequent_itemsets, itemsets_by_length = AP1.apriori(transactions, MIN_SUPPORT)
    # rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    # print_rules(rules)


if __name__ == "__main__":
    test_apriori()
