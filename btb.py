# Beyond The Box
# pip install nba_api
# pip install pandas

import pandas as pd
import random as r


# Raw data without any querying
raw_stats = pd.read_csv('downloads/btb.csv')
#'season', 'lg', 'player', 'player_id', 'age', 'team', 'pos', 'g', 'gs','mp', 'fg', 'fga', 'fg_percent', 'x3p', 'x3pa', 'x3p_percent', 'x2p','x2pa', 'x2p_percent', 'e_fg_percent', 'ft', 'fta', 'ft_percent', 'orb','drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'trp_dbl'
raw_advanced_stats = pd.read_csv('downloads/btb_advanced.csv')
#'season', 'lg', 'player', 'player_id', 'age', 'team', 'pos', 'g', 'gs','mp', 'per', 'ts_percent', 'x3p_ar', 'f_tr', 'orb_percent','drb_percent', 'trb_percent', 'ast_percent', 'stl_percent','blk_percent', 'tov_percent', 'usg_percent', 'ows', 'dws', 'ws','ws_48', 'obpm', 'dbpm', 'bpm', 'vorp'

# query for if a player at any moment played for 50 games and averaged 15 or more points
def query_for_selected_attributes():
    raw_stats = pd.read_csv('downloads/btb.csv')
    btb = raw_stats
    btb['ppg'] = btb['pts']/btb['g']
    btb = btb[btb['g']>50]
    btb = btb[btb['ppg']>15]
    return btb

# Randomly selects a player id and returns the players carrer stats
def random_selection():
    btb = query_for_selected_attributes()
    random_player_id = r.choice(btb['player_id'])
    random_player = btb[btb['player_id'] == random_player_id]
    return random_player

print(query_for_selected_attributes())
print(raw_advanced_stats.columns)
