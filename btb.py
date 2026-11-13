# Beyond The Box
# pip install nba_api
# pip install pandas

import pandas as pd
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats
import random as r

players_df = pd.DataFrame(players.get_players())
random_player_id = r.choice(players_df['id'])
players.find_player_by_id(random_player_id)
print(players.find_player_by_id(random_player_id))

career = playercareerstats.PlayerCareerStats(player_id=random_player_id)  # sends the request

df = career.season_totals_regular_season.get_data_frame()
print(df)