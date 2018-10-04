
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.lcb.wa.gov", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata(data.lcb.wa.gov,
                 'hTbHgZowMsN6SuOjSXztZhMm3',
                 userame="Jawaun.Brown95@gmail.com",
                 password="CannabisPassword$")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("bhbp-x4eb", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df)

if __name__ == "__main__":
