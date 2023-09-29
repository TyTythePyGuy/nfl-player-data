import pandas as pd
from StatPullRec import StatPullRec
from tkinter import *
from tkinter import messagebox

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
#print(hof_of_80s)

# Looking at how many players from a specific team hit the 10 TDs or 1000 yards qualifier
#chargers_80s = top_of_80s[top_of_80s["Tm"] == "SDG"]
#print(chargers_80s)

# Looking at how many players from a specific team hit the 10 TDs and 1000 yards qualifier
#san_fran = hof_of_80s[hof_of_80s["Tm"] == "SFO"]
#print(san_fran)

#Finding the max value of a specific part of the DataFrame
#print(year_1980.df_elite_rec.loc[year_1980.df_elite_rec["Yds"].idxmax()])
most_yards = year_1980.df_elite_rec.Yds.max()
#print(year_1980.df_elite_rec[year_1980.df_elite_rec["Yds"] == most_yards])
#-----------------------------Making the functions-------------------------------#
def show_info():
       #8=First Name, 9=Last Name, 10=Team, 11=Position, 13=Receptions, 14=Yards, 15=TDs
       try:
              year_picked = year_choice.get()
              stat = category.curselection()
              these_stats = StatPullRec(f"{year_picked}receivingstats.csv")
       except FileNotFoundError:
              messagebox.showerror(title="Wrong Year", message="Please input the year in a 4 digit format.")
       else:
              max_yards = these_stats.df_elite_rec.Yds.max()
              max_tds = these_stats.df_elite_rec.TD.max()
              max_rec = these_stats.df_elite_rec.Rec.max()
              try:
                     if stat[0] == 0:
                            td_player = str(these_stats.df_elite_rec[these_stats.df_elite_rec["TD"] == max_tds]).split()
                            messagebox.showinfo(title=f"Most Touchdowns {year_picked}",
                                                message=f"The player with the most touchdowns in {year_picked} was {td_player[8]} {td_player[9]} "
                                                        f"with {td_player[15]}. He also had {td_player[14]} yards and {td_player[13]} receptions "
                                                        f"while playing for {td_player[10]}")
                     elif stat[0] == 1:
                            yd_player = str(these_stats.df_elite_rec[these_stats.df_elite_rec["Yds"] == max_yards]).split()
                            messagebox.showinfo(title=f"Most Yards {year_picked}",
                                                message=f"The player with the most yards in {year_picked} was {yd_player[8]} {yd_player[9]} "
                                                        f"with {yd_player[14]}. He also had {yd_player[13]} receptions and {yd_player[15]} touchdowns "
                                                        f"while playing for {yd_player[10]}")
                     elif stat[0] == 2:
                            rec_player = str(these_stats.df_elite_rec[these_stats.df_elite_rec["Rec"] == max_rec]).split()
                            messagebox.showinfo(title=f"Most Receptions {year_picked}", message=f"The player with the most receptions in {year_picked} was {rec_player[8]} {rec_player[9]} "
                                                                                                f"with {rec_player[13]}. He also had {rec_player[14]} yards and {rec_player[15]} touchdowns "
                                                                                                f"while playing for {rec_player[10]}")
              except IndexError:
                     messagebox.showerror(title="Which Stat?", message="Please choose which stat to sort by")

#-----------------------------Making the UI--------------------------------------#
window = Tk()
window.title("Top NFL Players of the Years")
window.minsize(width=500, height=500)

choices = ["Receiving Touchdowns", "Receiving Yards", "Receptions"]
choicesvar = StringVar(value=choices)
category = Listbox(height=3, listvariable=choicesvar)
category.grid(row=0, column=1)

first_part = Label(text="I want to find the player with the most ")
first_part.grid(row=0, column=0)

second_part = Label(text="in the year ")
second_part.grid(row=0, column=2)

year_choice = Entry()
year_choice.grid(row=0, column=3)

get_info = Button(text="Show me the info", width=25, command=show_info)
get_info.grid(row=1, column=1, columnspan=3)

window.mainloop()