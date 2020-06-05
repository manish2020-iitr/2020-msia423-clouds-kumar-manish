import logging
# For modeling
import sklearn
from sklearn import model_selection
from sklearn import linear_model
from sklearn import metrics
import numpy as np
import pandas as pd
logger = logging.getLogger(__name__)

def build_models(df):
    """ This function builds the model on the dataframe """

    features = df.drop('class', 1)
    target = df["class"]

    X_train, X_test, y_train, y_test = model_selection.train_test_split(features, target, test_size=0.4, random_state=123)
    initial_features = [
        'visible_norm_range', 'log_entropy', 'IR_mean',
        'entropy_x_contrast', 'IR_norm_range', 'visible_mean']
    lr = linear_model.LogisticRegression(fit_intercept=False, penalty='l2',random_state=123)
    lr_fit = lr.fit(X_train[initial_features], y_train)
    ypred_proba_test = lr.predict_proba(X_test[initial_features])[:, 1]
    ypred_bin_test = lr.predict(X_test[initial_features])
    auc = sklearn.metrics.roc_auc_score(y_test, ypred_proba_test)
    confusion = sklearn.metrics.confusion_matrix(y_test, ypred_bin_test)
    accuracy = sklearn.metrics.accuracy_score(y_test, ypred_bin_test)
    classification_report = sklearn.metrics.classification_report(y_test, ypred_bin_test)
    fitted = pd.DataFrame(index=initial_features)
    fitted['coefs'] = lr.coef_[0]
    fitted['odds_ratio'] = fitted.coefs.apply(np.exp)
    fitted = fitted.sort_values(by='odds_ratio', ascending=False)

    return fitted
