def facility_engine(row):
    facilities = []

    if row["Teachers"] <= 3:
        facilities.append("👨‍🍳 Mid-Day Meal Support Staff")

    if row["Students"] > 800:
        facilities.append("👨‍🏫 Additional Classrooms / Teachers")

    if row["Accessibility"] < 50:
        facilities.append("🛡️ Watchman / Security Staff")

    if row["Growth"] < 5:
        facilities.append("🌱 Gardener / Maintenance Staff")

    if len(facilities) == 0:
        facilities.append("✔ Basic Infrastructure OK")

    return ", ".join(facilities)


def apply_facility(df):
    df["Facility_Need"] = df.apply(facility_engine, axis=1)
    return df