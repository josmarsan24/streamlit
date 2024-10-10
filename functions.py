import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import pi
import streamlit as st

team_colors = {
    'MIA': 'red',
    'WAS': 'red',
    'TOR': 'green',
    'PHI': 'blue',
    'ORL': 'blue',
    'NYK': 'orange',
    'MIL': 'green',
    'ATL': 'red',
    'IND': 'yellow',
    'CLE': 'red',
    'BOS': 'green',
    'BRK': 'black',
    'CHI': 'red',
    'CHO': 'blue',
    'DET': 'blue',
    'MEM': 'blue',
    'DEN': 'yellow',
    'DAL': 'blue',
    'MIN': 'blue',
    'NOP': 'yellow',
    'GSW': 'yellow',
    'OKC': 'blue',
    'LAL': 'purple',
    'LAC': 'blue',
    'PHO': 'orange',
    'POR': 'red',
    'SAC': 'purple',
    'SAS': 'black',
    'UTA': 'purple',
    'HOU': 'red',
    '2TM': 'grey',
    '3TM': 'grey'
}

def menu():
    with st.sidebar:
        st.page_link('streamlit_main.py', label='Home')
        st.page_link('pages/compare.py', label='Compare players')
        st.page_link('pages/plot.py', label='Plot metrics')

def read_df():
    df = pd.read_csv('nba2024.csv')
    df = df.drop('Rk', axis=1)
    df = df.loc[(df['Player'] != 'League Average') & (df['Team'] != '2TM') & (df['Team'] != '3TM')]
    return df

def filter_df(df, team, pos, games, minutes):
    if team is not None:
        df = df.loc[df.Team == team]
    if pos is not None:
        df = df.loc[df.Pos == pos]
    if games is not None:
        df = df.loc[df.G >= games]
    if minutes is not None:
        df = df.loc[df.MP >= minutes]
    return df

def scatter_plot(df, x, y, ax):
    try:
        valid_df = df[np.isfinite(df[x]) & np.isfinite(df[y])].dropna(subset=[x, y, 'Player'])

        colors = valid_df['Team'].map(team_colors)
        ax.scatter(valid_df[x], valid_df[y], c=colors)
        ax.set_xlabel(x)
        ax.set_ylabel(y)

        if len(valid_df) < 50:
            for i in range(len(valid_df)):
                ax.text(valid_df[x].iloc[i], valid_df[y].iloc[i], valid_df['Player'].iloc[i], fontsize=9)
        else:
            mean_x = valid_df[x].mean()
            mean_y = valid_df[y].mean()
            for i in range(len(valid_df)):
                if valid_df[x].iloc[i] > mean_x or valid_df[y].iloc[i] > mean_y:
                    ax.text(valid_df[x].iloc[i], valid_df[y].iloc[i], valid_df['Player'].iloc[i], fontsize=9)
    except:
        pass
    return ax

def radar_plot(player1, player2, df, fig, ax):
    try:
        cols = ['PTS', 'TRB', 'AST', 'BLK', 'STL', 'FG%']
        
        df_normalized = df[cols].apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)

        player1_stats = df_normalized[df['Player'] == player1].iloc[0].values
        player2_stats = df_normalized[df['Player'] == player2].iloc[0].values

        player1_stats = np.concatenate((player1_stats, [player1_stats[0]]))
        player2_stats = np.concatenate((player2_stats, [player2_stats[0]]))

        angles = [n / float(len(cols)) * 2 * pi for n in range(len(cols))]
        angles += angles[:1]

        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        ax.set_yticklabels([])

        plt.xticks(angles[:-1], cols)

        ax.plot(angles, player1_stats, linewidth=1, linestyle='solid', label=player1)
        ax.fill(angles, player1_stats, 'b', alpha=0.1)

        ax.plot(angles, player2_stats, linewidth=1, linestyle='solid', label=player2)
        ax.fill(angles, player2_stats, 'r', alpha=0.1)

        ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    except Exception as e:
        print(f"Error: {e}")
    return fig, ax

def df_compare(df, player1, player2):
    cols = ['Player','Team','Pos','PTS', 'TRB', 'AST', 'BLK', 'STL', 'FG%']
    df_table = df.loc[(df.Player == player1) | (df.Player == player2)][cols]
    df_table[df_table.select_dtypes(include=['number']).columns] = df_table.select_dtypes(include=['number']).apply(lambda col: col.round(3).astype(str))
    return df_table
    
    