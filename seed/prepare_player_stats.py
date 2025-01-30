def prepare_player_stats(player_stats_general):
  stats = {"Gols": 0, "Assistências": 0, "Cartões Amarelos": 0, "Cartões Vermelhos": 0, "Jogos": 0, "Minutos Jogados": 0}
  for x in range(0,len(player_stats_general["stats"])):
    if "goals" in player_stats_general["stats"][x]:
      stats["Gols"] += player_stats_general["stats"][x]["goals"]
    if "assists" in player_stats_general["stats"][x]:
      stats["Assistências"] += player_stats_general["stats"][x]["assists"]
    if "yellowCards" in player_stats_general["stats"][x]:
      stats["Cartões Amarelos"] += player_stats_general["stats"][x]["yellowCards"]
    if "redCards" in player_stats_general["stats"][x]:
      stats["Cartões Vermelhos"] += player_stats_general["stats"][x]["redCards"]
    if "appearances" in player_stats_general["stats"][x]:
      stats["Jogos"] += player_stats_general["stats"][x]["appearances"]
    if "minutesPlayed" in player_stats_general["stats"][x]:
      stats["Minutos Jogados"] += player_stats_general["stats"][x]["minutesPlayed"]
  return stats