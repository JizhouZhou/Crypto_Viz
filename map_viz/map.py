import plotly.express as px
import pandas as pd
import pycountry
import plotly.io as pio

pio.renderers.default = "browser"

df = pd.read_csv('trading_vol_by_country.csv')

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

df['code'] = [countries.get(country, 'Unknown code') for country in df['Country']]

fig = px.scatter_geo(df,
                     locations="code",
                     hover_name="Country",
                     size="Volume",
                     scope = 'world')
fig.update_geos(fitbounds="locations", visible=True)

fig.show()
