import plotly.express as px
import plotly.graph_objs as go

import pandas as pd
from plotly.io import templates

templates.default = "plotly_dark"


def Scatter(df: pd.DataFrame, **kwargs) -> go.Figure:
    fig = px.scatter(df, **kwargs)
    fig.update_layout(
        font=dict(size=14),
        height=800,
        width=1000,
    )
    fig.update_traces(
        marker_size=12,
        marker_line=dict(width=2),
        selector=dict(mode="markers"),
    )
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    return fig


def Box(df: pd.DataFrame, **kwargs) -> go.Figure:
    fig = px.box(df, **kwargs)
    fig.update_xaxes(dtick=10)
    fig.update_layout(
        font=dict(size=14),
        height=30 * len(df[kwargs.get("y")].unique()),
        width=1000,
        showlegend=False,
    )
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    return fig
