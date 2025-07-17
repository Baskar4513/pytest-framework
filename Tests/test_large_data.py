import pytest

@pytest.mark.dataquality
def test_event_id_not_null(ge_df):
    ge_df.expect_column_values_to_not_be_null("event_id")

@pytest.mark.dataquality
def test_event_id_unique(ge_df):
    ge_df.expect_column_values_to_be_unique("event_id")

@pytest.mark.dataquality
def test_event_type_valid(ge_df):
    ge_df.expect_column_values_to_be_in_set("event_type",["pass", "shot","goal","tackle"])


@pytest.mark.dataquality
@pytest.mark.parametrize("col",["x_coord","y_coord"])
def test_coordinates_within_bounds(ge_df, col):
    ge_df.expect_column_values_to_be_between(col, 0, 100)