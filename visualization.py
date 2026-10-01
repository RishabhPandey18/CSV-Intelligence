import pandas as pd 
import matplotlib.pyplot as plt

def bar_graph(df,x_column,y_column,graph_title):
    fig, ax = plt.subplots()
    ax.bar(df[x_column] ,df[y_column])
    
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(graph_title)
    
    
    
    return fig


def pie_chart(df,column,graph_title,selected_component):
    filtered_df = df[df[column].isin(selected_component)]
    components =  filtered_df[column].value_counts()
   
    fig,ax = plt.subplots()
    ax.pie(components.values, labels=components.index)
   
    ax.set_title(graph_title)
   
   
    return fig