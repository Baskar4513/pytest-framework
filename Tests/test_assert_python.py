def test_timesatamps_sorted(event_df):
    df_sorted = event_df.sort_values(["match_id","timestamp"])
    for match_id, group in df_sorted.groupby("match_id"):
        assert group["timestamp"].is_monotonic_increasing, f"Timestamps not ordered in match {match_id}"


def test_goal_streak(event_df):
    df = event_df.copy()
    df["is_goal"] = (df["event_type"]=="goal").astype(int)
    df["goal_streak"] = df.groupby("player_id")["is_goal"].rolling(3).sum().reset_index(level=0, drop = True)
    assert not (df["goal_streak"]>2).any(), "goal streak >2 dedected"