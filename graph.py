import plotly.express as px

def graph(data):
    """
    Skapar en linjediagram för temperaturdata för de kommande 24 timmarna.
    """
    df = data
    fig = px.line(
        df,
        x="tid",       # uppdaterad kolumn från 'time' till 'tid'
        y="grad",      # uppdaterad kolumn från 'degree' till 'grad'
        title="Vädret för de kommande 24 timmarna"
    )

    fig.update_layout(
        title={
            "text": "Vädret för de kommande 24 timmarna",
            "x": 0.5,
            "xanchor": "center"
        },
        xaxis_title="Tid (hh:mm)",
        yaxis_title="Temperatur (°C)",
        template="plotly_white"
    )
    
    return fig
