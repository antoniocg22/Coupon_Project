import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

coupon_visit = pd.read_csv("C:\Users\eduar_000\Documents\coupon_visit_train.csv")
user_list = pd.read_csv("C:\Users\eduar_000\Documents\user_list.csv")
coupon_list = pd.read_csv("C:\Users\eduar_000\Documents\coupon_list_train.csv")

coupon_visit_b= coupon_visit[coupon_visit.purchased == 1]
coupon_visit_nb= coupon_visit[coupon_visit.purchased == 0]

count_VCI_b = coupon_visit_b.VIEW_COUPON_ID_hash.value_counts()[0:1000].index
count_UI_b = coupon_visit_b.USER_ID_hash.value_counts()[0:1000].index
count_REF_b = coupon_visit_b.REFERRER_hash.value_counts()[0:1000].index
count_PUR_b = coupon_visit_b.PURCHASEID_hash.value_counts()[0:1000].index
count_SI_b = coupon_visit_b.SESSION_ID_hash.value_counts()[0:1000].index
count_VCI_nb = coupon_visit_nb.VIEW_COUPON_ID_hash.value_counts()[0:1000].index
count_UI_nb = coupon_visit_nb.USER_ID_hash.value_counts()[0:1000].index
count_REF_nb = coupon_visit_nb.REFERRER_hash.value_counts()[0:1000].index
count_PUR_nb = coupon_visit_nb.PURCHASEID_hash.value_counts()[0:1000].index
count_SI_nb = coupon_visit_nb.SESSION_ID_hash.value_counts()[0:1000].index

coupon_list_b = coupon_list[coupon_list['COUPON_ID_hash'].isin(count_VCI_b)]
user_list_b = user_list[user_list['USER_ID_hash'].isin(count_UI_b)]
coupon_list_nb = coupon_list[coupon_list['COUPON_ID_hash'].isin(count_VCI_nb)]
user_list_nb = user_list[user_list['USER_ID_hash'].isin(count_UI_nb)]

plt.hist(coupon_visit_b.PAGE_SERIAL)
plt.xlabel("coupon_visit_b.PAGE_SERIAL")
plt.show()
plt.hist(coupon_visit_nb.PAGE_SERIAL)
plt.xlabel("coupon_visit_nb.PAGE_SERIAL")
plt.show()
plt.hist(coupon_list_b.PRICE_RATE)
plt.xlabel("coupon_list_b.PRICE_RATE")
plt.show()
plt.hist(coupon_list_nb.PRICE_RATE)
plt.xlabel("coupon_list_nb.PRICE_RATE")
plt.show()
plt.hist(coupon_list_b.CATALOG_PRICE)
plt.xlabel("coupon_list_b.CATALOG_PRICE")
plt.show()
plt.hist(coupon_list_nb.CATALOG_PRICE)
plt.xlabel("coupon_list_nb.CATALOG_PRICE")
plt.show()
plt.hist(coupon_list_b.DISCOUNT_PRICE)
plt.xlabel("coupon_list_b.DISCOUNT_PRICE")
plt.show()
plt.hist(coupon_list_nb.DISCOUNT_PRICE)
plt.xlabel("coupon_list_nb.DISCOUNT_PRICE")
plt.show()
plt.pie(user_list_b.SEX_ID.value_counts(),labels=["f","m"], autopct='%1.1f%%',shadow=True, startangle=90)
plt.xlabel("user_list_b.SEX_ID")
plt.show()
plt.pie(user_list_nb.SEX_ID.value_counts(),labels=["f","m"], autopct='%1.1f%%',shadow=True, startangle=90)
plt.xlabel("user_list_nb.SEX_ID")
plt.show()
plt.hist(user_list_b.AGE)
plt.xlabel("user_list_b.AGE")
plt.show()
plt.hist(user_list_nb.AGE)
plt.xlabel("user_list_nb.AGE")
plt.show()

