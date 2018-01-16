### Definition of domain

The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.

One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

In this challenge, we ask you to complete the analysis of what sorts of people were likely to survive. In particular, we ask you to apply the tools of machine learning to predict which passengers survived the tragedy.

This is a classification issue. The output 1 is for survive, 0 is for not.

### Data Set
The data has been split into two groups:
* training set (train.csv)
* test set (test.csv)
The training set should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class. You can also use feature engineering to create new features.

The test set should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.

We also include gender_submission.csv, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.

#### Data Dictionary
<table>
  <tr>
    <th>Variable</th>
    <th>Definition</th>
    <th>Key</th>
  </tr>
  <tr>
    <th>survival</th>
    <th>Survival</th>
    <th>0 = No, 1 = Yes</th>
  </tr>
  <tr>
    <th>pclass</th>
    <th>Ticket class</th>
    <th>1 = 1st, 2 = 2nd, 3 = 3rd</th>
  </tr>
  <tr>
    <th>sex</th>
    <th>Sex</th>
    <th></th>
  </tr>
  <tr>
    <th>Age</th>
    <th>Age in years</th>
    <th></th>
  </tr>
  <tr>
    <th>sibsp</th>
    <th># of siblings / spouses aboard the Titanic</th>
    <th></th>
  </tr>
  <tr>
    <th>parch</th>
    <th># of parents / children aboard the Titanic</th>
    <th></th>
  </tr>
  <tr>
    <th>ticket</th>
    <th>Ticket number</th>
    <th></th>
  </tr>
  <tr>
    <th>fare</th>
    <th>Passenger fare</th>
    <th></th>
  </tr>
  <tr>
    <th>cabin</th>
    <th>Cabin number</th>
    <th></th>
  </tr>
  <tr>
    <th>embarked</th>
    <th>Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton</th>
    <th></th>
  </tr>
</table>

#### Variable Notes
__pclass__: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

__age__: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

__sibsp__: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

__parch__: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.

