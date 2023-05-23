import Apriori as AP1
import AprioriFix as AP2
from utils import *

MIN_SUPPORT = 0.3
MIN_CONFIDENCE = 0.5


def main():
    transactions = [
        {"A", "B", "C"},
        {"A", "B"},
        {"A", "C", },
        {"A", },
        {"B", "C"},
        {"B"},
        {"C"},
    ]
    print("======================Support=====================")
    support = get_support_item(transactions)
    print(support)
    print("======================Apriori=====================")
    rules = AP1.association_rules(transactions, MIN_SUPPORT, MIN_CONFIDENCE)
    rules = sorted(rules, key=lambda x: x[1])
    print_rules(rules)
    print("====================AprioriFix====================")
    rules = AP2.association_rules(transactions, MIN_SUPPORT, MIN_CONFIDENCE)
    print_rules(rules)



if __name__ == "__main__":
    main()