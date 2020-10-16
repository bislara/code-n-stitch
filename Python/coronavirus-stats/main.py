import requests
from datetime import date, timedelta

country = input("Country or region: ")
yesterday = date.today() - timedelta(days=1)

response = requests.get("https://covid-api.com/api/reports?date=" +
                        str(yesterday) + "&q=" + country)

if response and response.json()['data']:
    confirmed = 0
    deaths = 0
    recovered = 0
    confirmed_diff = 0
    deaths_diff = 0
    recovered_diff = 0
    active = 0
    active_diff = 0
    for region in response.json()['data']:
        confirmed += region['confirmed']
        deaths += region['deaths']
        recovered += region['recovered']
        confirmed_diff += region['confirmed_diff']
        deaths_diff += region['deaths_diff']
        recovered_diff += region['recovered_diff']
        active += region['active']
        active_diff += region['active_diff']

    print(yesterday)
    print(f"Confirmed: {confirmed:,}" +
          f"\nDeaths: {deaths:,}" +
          f"\nRecovered: {recovered:,}" +
          f"\nConfirmed_diff: {confirmed_diff:,}" +
          f"\nDeaths diff: {deaths_diff:,}" +
          f"\nRecovered diff: {recovered_diff:,}" +
          f"\nActive: {active:,}" +
          f"\nActive diff: {active_diff:,}")
else:
    print("Country/region " + country + " not valid.")
