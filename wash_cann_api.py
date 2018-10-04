import pandas as pd

from sodapy import Socrata


def connect(limiter):
    # Initiate connection using api token, username and pw
    client = Socrata('data.lcb.wa.gov',
                     'hTbHgZowMsN6SuOjSXztZhMm3',
                     username='Jawaun.Brown95@gmail.com',
                     password='CannabisPassword$')

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get('bhbp-x4eb', limit=limiter)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    cols = results_df.columns
    types = results_df.dtypes
    descriptions = results_df.describe()
    bycounty = results_df.sort_values(by='county')
    print(cols)
    print(types)
    print(descriptions)
    print(bycounty)

    return results_df


# def get_schema(df):
#     pd.build_table_schema(df)


if __name__ == "__main__":
    d = connect(2000)
    d.to_csv('projects/cannadata/cannadata.csv')
