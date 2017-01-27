# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 08:46:13 2017

@author: if682693
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#%%
coupon_area_file = "coupon_area_train_en.csv"
coupon_area = pd.read_csv(coupon_area_file)
#%%
user_list_file = "user_list.csv"
user_list = pd.read_csv(user_list_file)
#%%
coupon_visit_file = "coupon_visit_train.csv"
#%%
coupon_visit = pd.read_csv(coupon_visit_file)
#%%
coupon_visits_user_list = coupon_area.merge(coupon_visit, left_index=True, right_index=True)
coupon_visits_user_list2 = user_list.merge(coupon_visits_user_list, left_index=True, right_index=True)
#%%
columnas = pd.DataFrame(list(coupon_visits_user_list.columns.values), columns=["Columns Names"])
columnas
#%%
data_types = pd.DataFrame(coupon_visits_user_list.dtypes, columns=['Data Type'])
data_types
#%%
missing_data_counts = pd.DataFrame(coupon_visits_user_list.isnull().sum(), columns = ['Missing Values'])
missing_data_counts
#%%
present_data_counts = pd.DataFrame(coupon_visits_user_list.count(), columns = ['Present Values'])
present_data_counts
#%%
pref_counts = coupon_visits_user_list.groupby('en_pref').agg({'PURCHASE_FLG':np.sum})
small_counts = coupon_visits_user_list.groupby('en_small_area').agg({'PURCHASE_FLG':np.sum})
page_counts = coupon_visits_user_list.groupby('PAGE_SERIAL').agg({'PURCHASE_FLG':np.sum})
sex_counts = coupon_visits_user_list2.groupby('SEX_ID').agg({'PURCHASE_FLG':np.sum})
age_counts = coupon_visits_user_list2.groupby('AGE').agg({'PURCHASE_FLG':np.sum})

#%%
#%%         
