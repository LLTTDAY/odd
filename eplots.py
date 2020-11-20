# plot settings
themes.theme_fivethirtyeight(fontsize=10)
plt.rcParams["figure.figsize"] = (16,8)
plt.rcParams['font.sans-serif'] = ['news gothic std']
sns.set_palette(themes.palettes.FiveThirtyEight.colors)
pd.options.display.float_format = '{:.7f}'.format
pd.options.display.max_rows, pd.options.display.max_columns = 200,200