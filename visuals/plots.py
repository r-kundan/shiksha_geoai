import plotly.express as px

def create_geo_plot(df):
    fig = px.scatter(
        df,
        x="Accessibility",
        y="AI_Prediction",
        size="Students",
        color="Risk",
        hover_name="School",
        title="GeoAI School Risk Map"
    )

    return fig