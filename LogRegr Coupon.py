import os
import pandas as pd
import numpy as np
import pymysql
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import average_precision_score

class Get_Price_Rate(BaseEstimator, TransformerMixin):

    def get_feature_names(self):

        return [self.__class__.__name__]

    def fit(self, date_frame, y=None):

        return self

    def transform(self, date_frame):

        return date_frame["price_rate"].as_matrix()[None].T.astype(np.float)


class Get_Match_Pref(BaseEstimator, TransformerMixin):

    def get_feature_names(self):

        return [self.__class__.__name__]

    def fit(self, date_frame, y=None):

        return self

    def transform(self, date_frame):
        res_sr = date_frame["pref_name"] == date_frame["ken_name"]

        return res_sr.as_matrix()[None].T.astype(np.float)


def top_merge(df, n=10, column="predict", merge_column="coupon_id_hash"):

    return " ".join(df.sort_index(by=column)[-n:][merge_column])

feature_list = [
    ('PRICE_RATE', Get_Price_Rate()),
    ('MATCH_PREF', Get_Match_Pref()),
]

HOST = 'couponsmall.c58qgcdaakud.us-west-2.rds.amazonaws.com'
USER = 'alumno'
PASSWORD = 'proyecto2017'
DB = 'coupon_reduce'

connection = pymysql.connect(host=HOST,
                             port=3306,
                             user=USER,
                             password=PASSWORD,
                             database=DB,
                             local_infile=True,
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

# data
train_visit_df = pd.read_sql('select * from visit', con=connection)
user_df = pd.read_sql('select * from user', con=connection)
train_coupon_df = pd.read_sql('select * from list', con=connection)
    #test_coupon_df = pd.read_csv("C:\Users\eduar_000\Downloads\coupon_list_test.csv")
connection.close()

if __name__ == '__main__':
    train_df = pd.merge(train_visit_df, train_coupon_df,
                        left_on="VIEW_COUPON_ID_hash", right_on="coupon_id_hash")
    train_df = pd.merge(train_df, user_df,
                        left_on="USER_ID_hash", right_on="user_id_hash")

    fu_obj = FeatureUnion(transformer_list=feature_list)
    X_train = fu_obj.fit_transform(train_df)
    y_train = train_df["PURCHASE_FLG", "user_id_hash"]
    assert X_train.shape[0] == y_train.size
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    train_coupon_df["cross"] = 1
    user_df["cross"] = 1
    test_df = pd.merge(train_coupon_df, user_df, on="cross")
    X_test = fu_obj.transform(test_df)
    predict_proba = clf.predict_proba(X_test)
    pos_idx = np.where(clf.classes_ == True)[0][0]
    test_df["predict"] = predict_proba[:, pos_idx]
    top10_coupon = test_df.groupby("USER_ID_hash").apply(top_merge)
    top10_coupon.name = "PURCHASED_COUPONS"
    top10_coupon.to_csv("submission.csv", header=True)
    pur = train_df["PURCHASE_FLG"] == 1
    y = train_df[pur][["coupon_id_hash", "USER_ID_hash"]]
    y = y.groupby("USER_ID_hash")["coupon_id_hash"].apply(list)
    average_precision_score(y, top10_coupon)
