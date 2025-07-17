import pytest
import pandas as pd
#from great_expectations.dataset import PandasDataset

@pytest.fixture(scope = "session")
def event_df():
    df = pd.read_csv("data/events_large.csv", parse_dates = ["timestamp"])
    return df

#@pytest.fixture(scope = "session")
#def ge_df(event_df):
#    return PandasDataset(event_df)