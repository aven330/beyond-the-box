# Beyond The Box
# pip install nba_api
# pip install pandas

import pandas as pd
import random as r
import matplotlib.pyplot as plt

\
# Raw data without any querying

#'season', 'lg', 'player', 'player_id', 'age', 'team', 'pos', 'g', 'gs','mp', 'fg', 'fga', 'fg_percent', 'x3p', 'x3pa', 'x3p_percent', 'x2p','x2pa', 'x2p_percent', 'e_fg_percent', 'ft', 'fta', 'ft_percent', 'orb','drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'trp_dbl'
raw_stats = pd.read_csv('downloads/BTB/raw_stats.csv')

#'season', 'lg', 'player', 'player_id', 'age', 'team', 'pos', 'g', 'gs','mp', 'per', 'ts_percent', 'x3p_ar', 'f_tr', 'orb_percent','drb_percent', 'trb_percent', 'ast_percent', 'stl_percent','blk_percent', 'tov_percent', 'usg_percent', 'ows', 'dws', 'ws','ws_48', 'obpm', 'dbpm', 'bpm', 'vorp'
raw_stats_advanced = pd.read_csv('downloads/BTB/raw_stats_advanced.csv')

#'season', 'lg', 'player', 'player_id', 'age', 'team', 'pos', 'g', 'gs','mp', 'fg', 'fga', 'fg_percent', 'x3p', 'x3pa', 'x3p_percent', 'x2p','x2pa', 'x2p_percent', 'e_fg_percent', 'ft', 'fta', 'ft_percent', 'orb','drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'trp_dbl', 'ppg', 'apg', 'rpg', 'bpg', 'spg', 'tpg'
btb = pd.read_csv('downloads/BTB/btb.csv')

# querying new dataframe and turns it into a new csv
# function no longer in use since the csv file has been constructed
# kept simply for understanding how the csv file was created
def query_for_selected_attributes():
    # create new dataframe
    raw_stats = pd.read_csv('downloads/BTB/raw_stats.csv')
    raw_stats_per_game = raw_stats
    btb = pd.DataFrame()
    qualified_players = raw_stats
    
    # convert totals to per game stats
    raw_stats_per_game['ppg'] = raw_stats['pts']/raw_stats['g']
    raw_stats_per_game['apg'] = raw_stats['ast']/raw_stats['g']
    raw_stats_per_game['rpg'] = raw_stats['trb']/raw_stats['g']
    raw_stats_per_game['bpg'] = raw_stats['blk']/raw_stats['g']
    raw_stats_per_game['spg'] = raw_stats['stl']/raw_stats['g']
    raw_stats_per_game['tpg'] = raw_stats['tov']/raw_stats['g']
    
    
    # query for if a player at any moment played for 50 games and averaged 10 or more points
    qualified_players = qualified_players[qualified_players['g']>50]
    qualified_players = qualified_players[qualified_players['ppg']>10]
    for i in list(set(qualified_players['player_id'])):
        btb =  btb._append(raw_stats_per_game[raw_stats_per_game['player_id'] == i])
    # creates csv file so we don't have to query for our stats every time the program runs
    # commented out incase new csv file becomes problem and requires the funciton to be run every time
    btb.to_csv('downloads/BTB/btb.csv', index=True)

    return btb

# Randomly selects a player id and returns the players carrer stats
def random_selection():
    # dataframe containing qualified candidates (created by query_for_selected_attributes() into a csv) 
    random = pd.read_csv('downloads/BTB/btb.csv')
    # dataframe containing qualified candidates (created by query_for_selected_attributes())
    # random = query_for_selected_attributes()
    # NBA positions
    positions = ['PG', 'SG', 'SF', 'PF', 'C']
    # Dictionary containing difficulty modes and how many options you are given in each mode
    difficulty = {'easy':2, 'medium':3, 'hard':5}
    # Tested difficulty
    selected_difficulty = 'hard'
    # overarching dictionary with all the players of each position
    random_players_stats_position = {}
    # iterates through each position
    for position in positions:
        # dictionary full of all the players in a given position
        random_player_stats = {}
        # generates a new player as many times as the difficulty requires 
        for i in range(difficulty[selected_difficulty]):
            # queries by position
            random_by_postion = random[random['pos'] == position]
            # randomly selects a player id
            random_player_id = r.randint(0,random_by_postion.shape[0])
            # gets the box score of random player
            random_player = random_by_postion.iloc[random_player_id]
            # drops player as to not randomly select them again
            random_by_postion = random_by_postion.drop(random_by_postion[random_by_postion.player_id == random_player_id].index)
            # change later to get rid of player and season to remove all context
            displayed_stats = ['player', 'season', 'pos','ppg', 'fg_percent', 'x3p_percent','ft_percent', 'apg', 'rpg', 'bpg', 'spg', 'tpg']
            # only player name so we can see how it works (just for testing)
            test_stats = ['ppg', 'fg_percent', 'x3p_percent','ft_percent', 'apg', 'rpg']
            # puts the player in the position dictionary with an assigned number
            random_player_stats[i+1] = random_player[displayed_stats]
        # puts the postion dictionary in the overarching dictionary
        random_players_stats_position[position] = random_player_stats
    # returns overarching dictionary
    return random_players_stats_position

# checks if a player object contains an all star
# not sure what to do yet if there isn't an all star so currently function is not in use
def is_allstar(player):
    # csv filled with players who have been allstars 
    # 'player', 'player_id', 'team', 'season', 'lg', 'replaced'
    all_star = pd.read_csv('downloads/BTB/all_star.csv')
    all_star_list = list(set(all_star['player_id']))
    if player.player_id in all_star_list:
        return True
    return False

#print(raw_stats[raw_stats['player_id'] == 'abdulka01'])
print(random_selection())
