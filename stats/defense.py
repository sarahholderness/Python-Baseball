import pandas as pd
import matplotlib.pyplot as plt

from frames import games, info, events

print('\ngames data frame:')
print(games.head())
print('\ninfo data frame:')
print(info.head())
print('\nevents data frame:')
print(events.head())

plays = games.query("type == 'play' & event != 'NP'")

plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches',
'event', 'game_id', 'year']

pa = plays.loc[plays['player'].shift() != plays['player'],
['year', 'game_id', 'inning', 'team', 'player']]

pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name='PA')

events = events.set_index(['year', 'game_id', 'team', 'event_type'])

events = events.unstack().fillna(0).reset_index()
events.columns = events.columns.droplevel()
events.columns = ['year', 'game_id', 'team', 'BB', 'E',
                  'H', 'HBP', 'HR', 'ROE', 'SO']
events = events.rename_axis(None, axis='columns')

events_plus_pa = pd.merge(events, pa, how='outer',
left_on=['year', 'game_id', 'team'],
right_on=['year', 'game_id', 'team'])

defense = pd.merge(events_plus_pa, info)



print('\nplays data frame:')
print(plays.head())
print('\npa data frame:')
print(pa.head())
print('\nevents data frame:')
print(events.head())
