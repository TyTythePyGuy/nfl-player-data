import pandas as pd
from StatPullRec import StatPullRec

# * Next to name indicates the player was selected to a Pro Bowl that year
# + Next to name indicates the player was First Team All-Pro that year
year_1980 = StatPullRec("1980receivingstats.csv")
year_1981 = StatPullRec("1981receivingstats.csv")
year_1982 = StatPullRec("1982receivingstats.csv")
year_1983 = StatPullRec("1983receivingstats.csv")
year_1984 = StatPullRec("1984receivingstats.csv")
year_1985 = StatPullRec("1985receivingstats.csv")
year_1986 = StatPullRec("1986receivingstats.csv")
year_1987 = StatPullRec("1987receivingstats.csv")
year_1988 = StatPullRec("1988receivingstats.csv")
year_1989 = StatPullRec("1989receivingstats.csv")

# Shows me every player that had 10 or more touchdowns for the year
#print(year_1980.df_10_touchdowns)

# Shows me every player that had 1000 or more yards for the year
#print(year_1981.df_1000_yards)

# Shows me every player that had 1000 or more yards OR 10 or more touchdowns for the year
#print(year_1983.df_elite_rec)

# Shows me every player that had 1000 or more yards AND 10 or more touchdowns for the year
#print(year_1984.df_them_rec)

# Allows me to pull the entire raw data for the year
#print(year_1984.data)

# Allows me to pull just the Name, Team, Position, Games Played, Receptions, Yards, and Touchdowns of every player that year
#print(year_1985.psdata)

# Allows me to send just the players identified with .df_elite_rec to a csv so I can look at that elsewhere, if needed
# The year input allows the csv to read as {year} top receivers
#year_1986.send_to_csv(1986)

# Concatenating all of the top receivers from the decade into a single dataframe
top = [year_1980.df_elite_rec, year_1981.df_elite_rec, year_1982.df_elite_rec, year_1983.df_elite_rec, year_1984.df_elite_rec,
       year_1985.df_elite_rec, year_1986.df_elite_rec, year_1987.df_elite_rec, year_1988.df_elite_rec, year_1989.df_elite_rec]
top_of_80s = pd.concat(top)

# Concatenating all of the unique (.df_them_rec) receivers into a single dataframe
hof = [year_1980.df_them_rec, year_1981.df_them_rec, year_1982.df_them_rec, year_1983.df_them_rec, year_1984.df_them_rec,
       year_1985.df_them_rec, year_1986.df_them_rec, year_1987.df_them_rec, year_1988.df_them_rec, year_1989.df_them_rec]
hof_of_80s = pd.concat(hof)
print(hof_of_80s)

# Looking at how many players from a specific team hit the 10 TDs or 1000 yards qualifier
#chargers_80s = top_of_80s[top_of_80s["Tm"] == "SDG"]
#print(chargers_80s)

# Looking at how many players from a specific team hit the 10 TDs and 1000 yards qualifier
#san_fran = hof_of_80s[hof_of_80s["Tm"] == "SFO"]
#print(san_fran)