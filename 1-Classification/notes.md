# Classification
## Approach 1: Predict income
1. We have an existing customers table, and we have a potential customers table. Of all given features in the existing customers 
table, we want to predict the income of all the potential customers. We will use Naive Bayes to predict the income of the
potential customers.
2. Then, we will calculate the expected profit for each existing customer who attracted new customers, taking into account the 
likelihood of positive reaction to the special promotion and the average return of a new customer based on their income level. 

## Approach 2: Predict reaction to promotion
1. We have an existing customers table, and we have a potential customers table. Of all given features in the existing customers
table, we want to predict the reaction of all the potential customers to the special promotion. We will use Naive Bayes to predict

## Approach 3: Confusion matrix
1. Split the existing customers table into training and test sets.
2. Train a Naive Bayes model on the training set.
3. create confusion matrix and user the TP and TN to calculate the accuracy of the model.