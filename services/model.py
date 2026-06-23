from xgboost import XGBRegressor

def train_model(df):
    X = df[["Students", "Teachers", "Vacancy", "Growth", "Accessibility"]]
    y = df["TDI"]

    model = XGBRegressor(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1
    )

    model.fit(X, y)

    df["AI_Prediction"] = model.predict(X)

    return model, df