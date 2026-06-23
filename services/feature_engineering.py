def add_features(df):
    df["STR"] = df["Students"] / df["Teachers"]

    df["TDI"] = (
        (df["Students"] / 100) +
        (df["Vacancy"] * 5) +
        (df["Growth"] * 2)
    )

    return df