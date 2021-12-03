import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_curve
from sklearn import ensemble
from sklearn import metrics
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score,auc, accuracy_score


df = pd.read_csv("C:\\Users\\fawmain\\Desktop\\kredi kartı\\CreditCardFraud\\creditcard.csv")
df.drop('Time',axis=1,inplace=True)

class Learning:
    def __init__(self):
        pass

    def superVectorMachine(self):
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(df.drop('Class',axis=1))
        principalDf = pd.DataFrame(data = principalComponents, 
                           columns = ['principal component 1', 'principal component 2'])
        final_df = pd.concat([df['Class'], principalDf],axis=1)
        X_train,X_test, y_train,y_test = train_test_split(final_df.drop('Class',axis=1), 
                                                  final_df['Class'],
                                                  test_size=0.2,
                                                  random_state=100)
        under = RandomUnderSampler(sampling_strategy=0.002)
        over = SMOTE(sampling_strategy=0.01)
        X_train_smote, y_train_smote = under.fit_resample(X_train, y_train)
        X_train_both, y_train_both = over.fit_resample(X_train_smote, y_train_smote)
        model = SGDClassifier()
        model.fit(X_train_both, y_train_both)
        prediction = model.predict(X_test)
        print('classification report:', classification_report(prediction, y_test))
        print('accuracy_score : ',accuracy_score(prediction, y_test))
    
    def RandomForest(self):
        X = df.drop(['Class'], axis=1)
        y = df.Class
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
        rf = ensemble.RandomForestClassifier()
        rf.fit(X_train, y_train)
        y_rf = rf.predict(X_test)
        cm = confusion_matrix(y_test, y_rf)
        print(cm)

    def over_sampling(self):
        X = df.drop(['Class'], axis=1)
        y = df.Class
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
        smote = SMOTE()
        X_train, y_train = smote.fit_resample(X_train, y_train)
        y_train.value_counts()
        rf = ensemble.RandomForestClassifier()
        rf.fit(X_train, y_train)
        y_rf = rf.predict(X_test)
        print(classification_report(y_test, y_rf))
        cm = confusion_matrix(y_test, y_rf)
        print(cm)



Learn = Learning()
# Learn.superVectorMachine()
# Learn.RandomForest()
Learn.over_sampling()