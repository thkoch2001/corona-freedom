#!/usr/bin/env python3

import numpy as np
import pandas as pd

d = pd.read_csv("demo_r_mwk_ts.tsv",
                sep="[ p]*\t",
                na_values=":",
                engine='python',
                skipinitialspace=True,
                index_col=0
                )

# Throw away individual sexes, keep only totals
d = d.truncate(before='T,NR,AD', axis='index', copy=True)
d.index.name=''
d.columns = pd.MultiIndex.from_tuples([(c[0:4], c[5:7]) for c in d.columns])
d.index = [c[5:] for c in d.index]

def get_years_for_country(country):
    years = d.columns.levels[0]
    result = {}
    for y in years:
        result[y] = d[y].loc[country].fillna(0).astype('int').sum()
    return pd.DataFrame(result, index=[0])
