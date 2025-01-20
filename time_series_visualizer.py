import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# import data
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# clean data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
df = df[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]

# ------------------------------------------------------------------------------------------------------
#  draw_line_plot function
def draw_line_plot():
    fig = df.plot.line(figsize=(15, 5), color='red', legend=False)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.xticks(rotation=0)
    plt.ylabel('Page Views')
    fig = fig.figure

    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig

draw_line_plot()
plt.show()

# ------------------------------------------------------------------------------------------------------
# draw_bar_plot function
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month_name()

    # grouping and organizing the df
    df_bar_group = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar_group = df_bar_group.unstack(level='month')
    df_bar_group = df_bar_group[['January', 'February', 'March', 'April', 'May',
                                'June', 'July', 'August', 'September', 'October', 'November', 'December']]


    fig = df_bar_group.plot.bar(figsize=(7,7)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

draw_bar_plot()
plt.show()

# ------------------------------------------------------------------------------------------------------
# draw_box_plot function
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    mon_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    ax1 = sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax2 = sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=mon_order)
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Year')
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()
plt.show()

