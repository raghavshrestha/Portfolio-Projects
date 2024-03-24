import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    

    # Create scatter plot
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']
    fig,ax = plt.subplots()
    plt.scatter(x,y)
    # Create first line of best fit
    res = linregress(x, y)
    x1 = pd.Series([i for i in range (1880,2051)])
    y1 = res.slope * x1 + res.intercept
    plt.plot(x1, y1, 'red')

    # Create second line of best fit
    df_1 = df.loc[ df['Year'] >= 2000]
    x2 = df_1['Year']
    y2 = df_1['CSIRO Adjusted Sea Level']

    res_2 = linregress(x2, y2)
    x2_predict = pd.Series( [i for i in range(2000,2051)] )
    y2_predict = res_2.slope * x2_predict + res_2.intercept

    plt.plot ( x2_predict, y2_predict, 'green')

    # Add labels and title
    ax.set_title('Rise in Sea level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea level (inches)' )
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()