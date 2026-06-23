def risk_level(score):
    if score > 45:
        return "🔴 HIGH RISK"
    elif score > 25:
        return "🟡 MEDIUM RISK"
    else:
        return "🟢 LOW RISK"


def apply_risk(df):
    df["Risk"] = df["AI_Prediction"].apply(risk_level)
    return df