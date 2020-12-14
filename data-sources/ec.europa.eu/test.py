#!/usr/bin/env python3

import numpy as np
import pandas as pd

d = pd.read_csv("demo_r_mwk3_t.tsv",
                sep="[ p]?\t",
                na_values=":",
                #names=True,
                #dtype=np.int32,
                engine='python',
                skipinitialspace=True,
                index_col=0
                )

print(d.head())

