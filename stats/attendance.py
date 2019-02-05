import pandas as pd
import matplotlib.pyplot as plt
from data import games

attendance = games.loc[(games['type']=='info') & (games['multi2'] ==
'attendance'), ['year', 'multi3']] 
