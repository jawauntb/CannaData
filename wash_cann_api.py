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
    df = pd.DataFrame.from_records(results)

    # cols = df.columns
    # types = df.dtypes
    # descriptions = df.describe()
    # county = df.county.unique()
    # print(cols)
    # print(types)
    # print(descriptions)
    # print(county)
    # print(ndf)

    return df


if __name__ == "__main__":
    d = connect(2000)
    d.to_csv('/Users/Juan/projects/cannadata/cannadata.csv')
    max_type = d.groupby('county').type.max()
    max_type.to_csv('/Users/Juan/projects/cannadata/most_common_biz_type_per_county.csv')