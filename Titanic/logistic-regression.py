from sklearn import metrics
import numpy
from sklearn.linear_model import LogisticRegressionCV
from Titanic import features

if __name__ == '__main__':
    train, test = features.wash_features()
    y = train['Survived']
    x = train.drop(['Survived'], axis=1)
    x_test = test
    passenger_id = test['PassengerId']
    cs = numpy.logspace(-3, 4, 8)
    clf = LogisticRegressionCV(Cs=cs, cv=5)
    clf.fit(x, y)
    print(clf.C_)
    y_hat = clf.predict(x)
    print('训练集精确度：', metrics.accuracy_score(y, y_hat))
    # y_test_hat = clf.predict(x_test)
    # print('测试集精确度：', metrics.accuracy_score(y_test, y_test_hat))