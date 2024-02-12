#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:32:45 2024

@author: mutua
"""

import pandas as pd
import matplotlib.pyplot as plt
sample_data = pd.read_csv("craigslist_vehicles.csv")

dd = sample_data.head(100)
dd.loc[:, 'posting_date'] = pd.to_datetime(dd['posting_date'])
dd.loc[:, 'removal_date'] = pd.to_datetime(dd['removal_date'])


dd.set_index('posting_date', inplace=True)

relevant_columns = ['region', 'price', 'year', 'manufacturer', 'model', 'condition', 'fuel', 'odometer', 'title_status', 'transmission', 'drive', 'type', 'paint_color']
dd = dd[relevant_columns]

# Example: Group by region and resample by month
region_monthly_counts = dd.groupby(['region', dd.index.month])['model'].count().unstack()
region_monthly_counts.plot(kind='line', title='Monthly Vehicle Listings by Region')
plt.show()