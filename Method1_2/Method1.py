# This file is used to fit different type od classifiers on the featureset generated through tf and tfidf.
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from UnigramTfFeatureGeneration import create_feature_set_and_labels
from UnigramTfifdFeaturesetGeneration import get_features


def begin_test(train_x, test_x, train_y, test_y):
    x = train_x + test_x
    y = train_y + test_y

    clf1 = LinearRegression()
    clf2 = LogisticRegression()
    clf3 = SGDClassifier()
    clf4 = SVC()
    clf5 = KNeighborsClassifier()
    clf6 = MLPClassifier()
    clf7 = DecisionTreeClassifier()
    clf8 = MultinomialNB()
    
    eclf = VotingClassifier(
        estimators=[('logr', clf2), ('sgd', clf3), ('svm', clf4), ('kn', clf5), ('nn', clf6), ('dt', clf7)],
        voting='hard')

    for label, clf in zip(
            ['### LogisticRegressionClassifier', '### SGDClassifierClassifier', '### SVCClassifier',
             '### NearestNeighbourClassifier', '### NeuralNetworkClassifier', '### DecisionTreeClassifier',
             '### MultinomialNB', '### EnsembleClassifier'],
            [clf2, clf3, clf4, clf5, clf6, clf7, clf8, eclf]):
        scores = cross_val_score(clf, x, y, cv=10, scoring='accuracy')
        f_measure = cross_val_score(clf, x, y, cv=10, scoring='f1')
        
        print(label, "Accuracy ::  ", scores.mean(), "+/- ", scores.std())
        print(label, "F-measure ::  ", f_measure.mean())


def test_by_tf():
    train_x, train_y, test_x, test_y = create_feature_set_and_labels \
        ('pos_hindi.txt', 'neg_hindi.txt')
    begin_test(train_x, test_x, train_y, test_y)


def test_by_tfidf():
    train_x, train_y, test_x, test_y = get_features()
    begin_test(train_x, test_x, train_y, test_y)


if __name__ == '__main__':
    print("###### METHOD 1 :: SA using In Language Classification")
    print("\n")
    print("###### Unigram+Tf Accuracies")
    test_by_tf()
    # print("\n")
    # print("###### Unigram+Tfidf Accuracies")
    # test_by_tfidf()
