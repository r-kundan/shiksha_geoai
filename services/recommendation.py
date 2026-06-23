def teacher_need(score):
    return max(1, int(score / 10))


def apply_teacher_need(df):
    df["Teachers_Required"] = df["AI_Prediction"].apply(teacher_need)
    return df