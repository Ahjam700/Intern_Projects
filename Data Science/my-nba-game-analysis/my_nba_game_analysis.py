def analyse_nba_game(play_by_play_moves):
    # Initialize dictionaries for home and away team statistics
    home_team_stats = {}
    away_team_stats = {}

    # Helper function to initialize player stats structure
    def init_player_stats(player_name):
        return {
            "player_name": player_name,
            "FG": 0, "FGA": 0, "FG%": 0,
            "3P": 0, "3PA": 0, "3P%": 0,
            "FT": 0, "FTA": 0, "FT%": 0,
            "ORB": 0, "DRB": 0, "TRB": 0,
            "AST": 0, "STL": 0, "BLK": 0,
            "TOV": 0, "PF": 0, "PTS": 0
        }

    # Helper function to fetch or initialize player stats
    def get_player_stats(team_stats, player_name):
        if player_name not in team_stats:
            team_stats[player_name] = init_player_stats(player_name)
        return team_stats[player_name]

    # Process each play to update player statistics
    for play in play_by_play_moves:
        period, remaining_sec, relevant_team, away_team, home_team, away_score, home_score, description = play.split('|')
        
        # Determine which team's stats to update based on relevant_team
        team_stats = home_team_stats if relevant_team == home_team else away_team_stats
        
        # Convert description to lowercase to handle actions uniformly
        description = description.lower()

        # Handle scoring actions (2P, 3P, FT)
        if 'makes' in description:
            player_name = description.split('makes')[1].split('(')[0].strip()
            player_data = get_player_stats(team_stats, player_name)

            if '3-pt' in description:
                player_data["3P"] += 1
                player_data["3PA"] += 1
                player_data["PTS"] += 3
            elif 'free throw' in description:
                player_data["FT"] += 1
                player_data["FTA"] += 1
                player_data["PTS"] += 1
            else:
                player_data["FG"] += 1
                player_data["FGA"] += 1
                player_data["PTS"] += 2

        # Handle missed shots
        elif 'misses' in description:
            player_name = description.split('misses')[1].split('(')[0].strip()
            player_data = get_player_stats(team_stats, player_name)

            if '3-pt' in description:
                player_data["3PA"] += 1
            else:
                player_data["FGA"] += 1

        # Handle rebounds
        elif 'offensive rebound' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_player_stats(team_stats, player_name)
            player_data["ORB"] += 1
        elif 'defensive rebound' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_player_stats(team_stats, player_name)
            player_data["DRB"] += 1

        # Handle assists
        elif 'assist' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_player_stats(team_stats, player_name)
            player_data["AST"] += 1

        # Handle steals
        elif 'steal' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_player_stats(team_stats, player_name)
            player_data["STL"] += 1

        # Handle blocks
        elif 'block' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_player_stats(team_stats, player_name)
            player_data["BLK"] += 1

        # Handle turnovers
        elif 'turnover' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_player_stats(team_stats, player_name)
            player_data["TOV"] += 1

        # Handle personal fouls
        elif 'foul' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_player_stats(team_stats, player_name)
            player_data["PF"] += 1

    # Helper function to calculate shooting percentages
    def compute_percentages(player_stats):
        if player_stats["FGA"] > 0:
            player_stats["FG%"] = round(player_stats["FG"] / player_stats["FGA"] * 100, 2)
        if player_stats["3PA"] > 0:
            player_stats["3P%"] = round(player_stats["3P"] / player_stats["3PA"] * 100, 2)
        if player_stats["FTA"] > 0:
            player_stats["FT%"] = round(player_stats["FT"] / player_stats["FTA"] * 100, 2)

    # Convert stats into a list format
    def format_player_data(team_stats):
        players_data = []
        for player_name, stats in team_stats.items():
            compute_percentages(stats)
            players_data.append(stats)
        return players_data

    # Return the game summary with player data
    return {
        "home_team": {
            "name": home_team,
            "players_data": format_player_data(home_team_stats)
        },
        "away_team": {
            "name": away_team,
            "players_data": format_player_data(away_team_stats)
        }
    }

def print_game_stats(team_dict):
    # Print the header for the stats table
    print("Players\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tORB\tDRB\tTRB\tAST\tSTL\tBLK\tTOV\tPF\tPTS")
    
    # Initialize total stats accumulator
    total_stats = {
        "FG": 0, "FGA": 0, "3P": 0, "3PA": 0, "FT": 0, "FTA": 0,
        "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0,
        "TOV": 0, "PF": 0, "PTS": 0
    }

    for player in team_dict["players_data"]:
        # Print individual player stats
        print(f"{player['player_name']}\t{player['FG']}\t{player['FGA']}\t{player['FG%']}\t{player['3P']}\t{player['3PA']}\t{player['3P%']}\t{player['FT']}\t{player['FTA']}\t{player['FT%']}\t{player['ORB']}\t{player['DRB']}\t{player['TRB']}\t{player['AST']}\t{player['STL']}\t{player['BLK']}\t{player['TOV']}\t{player['PF']}\t{player['PTS']}")

        # Accumulate total stats
        for stat in total_stats:
            total_stats[stat] += player[stat]

    # Helper function for safely calculating percentages
    def safe_percent(numerator, denominator):
        return round(numerator / denominator * 100, 2) if denominator > 0 else 0.0

    # Print team totals with percentage calculations
    print(f"Totals\t{total_stats['FG']}\t{total_stats['FGA']}\t{safe_percent(total_stats['FG'], total_stats['FGA'])}\t{total_stats['3P']}\t{total_stats['3PA']}\t{safe_percent(total_stats['3P'], total_stats['3PA'])}\t{total_stats['FT']}\t{total_stats['FTA']}\t{safe_percent(total_stats['FT'], total_stats['FTA'])}\t{total_stats['ORB']}\t{total_stats['DRB']}\t{total_stats['TRB']}\t{total_stats['AST']}\t{total_stats['STL']}\t{total_stats['BLK']}\t{total_stats['TOV']}\t{total_stats['PF']}\t{total_stats['PTS']}")

# Example play-by-play data for testing
play_by_play_moves = [
    "1|566.0|PORTLAND_TRAIL_BLAZERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|6|2|C. McCollum misses 2-pt layup from 2 ft",
    "1|566.0|PORTLAND_TRAIL_BLAZERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|6|2|Offensive rebound by Team",
    "1|563.0|PORTLAND_TRAIL_BLAZERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|6|2|Turnover by J. Layman (bad pass; steal by L. James)",
    "1|451.0|PORTLAND_TRAIL_BLAZERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|12|11|D. Lillard makes 2-pt jump shot from 15 ft",
    "1|430.0|LOS_ANGELES_LAKERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|12|11|K. Kuzma enters the game for J. McGee",
    "1|430.0|PORTLAND_TRAIL_BLAZERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|12|11|M. Harkless enters the game for A. Aminu",
    "1|416.0|LOS_ANGELES_LAKERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|14|11|K. Kuzma makes 2-pt layup from 2 ft (assist by R. Rondo)",
    "1|401.0|PORTLAND_TRAIL_BLAZERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|14|11|J. NurkiÄ‡ misses 2-pt jump shot from 2 ft",
    "1|400.0|LOS_ANGELES_LAKERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|14|11|Defensive rebound by L. James",
    "1|397.0|LOS_ANGELES_LAKERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|16|11|L. James makes 2-pt layup from 1 ft",
    "1|397.0|LOS_ANGELES_LAKERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|16|11|Shooting foul by C. McCollum (drawn by L. James)",
    "1|397.0|LOS_ANGELES_LAKERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|17|11|L. James makes free throw 1 of 1",
    "1|388.0|PORTLAND_TRAIL_BLAZERS|LOS_ANGELES_LAKERS|PORTLAND_TRAIL_BLAZERS|17|11|D. Lillard misses 3-pt jump shot from 25 ft",

]

# Analyse the game
game_summary = analyse_nba_game(play_by_play_moves)

# Print statistics for the home and away teams
print_game_stats(game_summary["home_team"])
print_game_stats(game_summary["away_team"])
