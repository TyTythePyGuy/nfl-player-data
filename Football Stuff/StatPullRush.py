import pandas as pd
#All of the actual data needs to be changed for rushing stats

class StatPullRush:
    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)
        self.pullstats(self.data)


    def pullstats(self, data):
        self.psdata = self.data[["Player", "Tm", "Pos", "G", "Rec", "Yds", "TD"]]
        self.df_1000_yards = self.psdata[self.psdata["Yds"] >= 1000]
        self.df_10_touchdowns = self.psdata[self.psdata["TD"] >= 10]
        self.df_elite_rec = self.psdata[(self.psdata["Yds"] >= 1000) | (self.psdata["TD"] >= 10)]
        self.df_them_rec = self.psdata[(self.psdata["Yds"] >= 1000) & (self.psdata["TD"] >= 10)]

    def send_to_csv(self, year):
        self.df_elite_rec.to_csv(f"{year} top receivers.csv")