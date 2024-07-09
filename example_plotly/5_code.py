import plotly.express as px

# Data
weeks = ['0-4 weeks', '5-8 weeks', '9-12 weeks', '13-16 weeks', '17-20 weeks', '21-26 weeks']
n_values = [194, 65, 44, 31, 24, 7]

# Create a bar chart
fig = px.bar(x=weeks, y=n_values)

# Add labels and title
fig.update_xaxes(title_text='Weeks')
fig.update_yaxes(title_text='Number of episodes mastitis / women\n breastfeeding - weeks * 1000')

# Place the values on top of the bars.
for i in range(len(n_values)):
    fig.add_annotation(x=weeks[i], y=n_values[i]+5, text=str(n_values[i]), showarrow=False)

fig.show()