from IPython.display import clear_output, HTML
from ipywidgets import widgets
import numpy as np

import plotly.graph_objects as go

# Class for the visualization of the DataFrame with 3 dropdowns
class Change:
    """
    class Change to define what happens when the action "change" is applied to the dropdown widgets for the DataFrame visualization.
    The aim of this class and functions is to create an interactive visualization of the restaurants DataFrame, with one dropdown
    to filter on boroughs, one dropdown to filter on "restaurant type 1" and a dropdown to filter on "restaurant type 2".
    This Class allows applying and disapplying more than one filter at the same time.

    Attributes:
    1) restaurant1 : string
        The restaurant type 1 for applying the filter. If None, no filter is applied
    2) restaurant2 : string
        The restaurant type 2 for applying the filter. If None, no filter is applied
    3) borough : string
        The borough for applying the filter. If None, no filter is applied
    4) df : pandas.DataFrame
        The dataframe which the user wants to apply the filter on
    5) out: widgets.Output()
        the jupyter display where the user wants to show the results
    """
    restaurant1 = None
    restaurant2 = None
    borough = None
    
    def __init__(self, df, out):
        self.df = df
        self.out = out

    def on_change1(self, change):
        """
        Function to apply filter on borough
        Inputs:
        1) change
           The notification that an action was applied to the dropdown
        """
        if change['type'] == 'change' and change['name'] == 'value':
            if not change['new'] == "Choose Borough" :
                self.borough = change['new']
            else:
                self.borough = None
            with self.out:
                clear_output(wait=True)
                self.set_masks()

    def on_change2(self, change):
        """
        Function to apply filter on restaurant type 1
        Inputs:
        1) change
           The notification that an action was applied to the dropdown
        """
        if change['type'] == 'change' and change['name'] == 'value':
            if not change['new'] == "Choose restaurant type 1" :
                self.restaurant1 = change['new']
            else:
                self.restaurant1 = None

            with self.out:
                clear_output(wait=True)
                self.set_masks()

    def on_change3(self, change):
        """
        Function to apply filter on restaurant type 2
        Inputs:
        1) change
           The notification that an action was applied to the dropdown
        """
        if change['type'] == 'change' and change['name'] == 'value':
            if not change['new'] == "Choose restaurant type 2" :
                self.restaurant2 = change['new']
            else:
                self.restaurant2 = None
            with self.out:
                clear_output(wait=True)
                self.set_masks()

    def set_masks(self):
        """
        Apply all the the filters to the dataframe
        """
        if self.borough!=None:
            mask1 = self.df["Boroughs"]== self.borough
        else:
            mask1 = np.logical_not(self.df["Boroughs"]== self.borough) #A mask with all true!!
        if self.restaurant1!=None:
            mask2 = self.df["Restaurant type 1"]== self.restaurant1
        else: #in this case self.restaurant1 = None and the mask will be all False
            mask2 = np.logical_not(self.df["Restaurant type 1"]== self.restaurant1) #A mask with all true!!
        if self.restaurant2!=None:
            mask3 = self.df["Restaurant type 2"]== self.restaurant2
        else:
            mask3 = np.logical_not(self.df["Restaurant type 2"]== self.restaurant2) #A mask with all true!!
        datos = self.df[(mask1) & (mask2) & (mask3)]
        display(datos)


def display_df_dropdowns(df):

    """
    This function creates the widgets.Output() structure with the 3 dropdowns and instantiates an object Change, to apply the 
    changes to the DataFrame, when the user clicks on the dropdowns

    Inputs:
    1) df : pandas.DataFrame
        The DataFrame the user wants to filter
    """

    dropdown_boroughs = widgets.Dropdown(
        options=["Choose Borough"] + list(df["Boroughs"].dropna().unique()) ,
        value="Choose Borough",
        description='Borough:',
        disabled=False,
    )

    dropdown_restaurantType1 = widgets.Dropdown(
        options=["Choose restaurant type 1"] + list(df["Restaurant type 1"].dropna().unique()) ,
        value="Choose restaurant type 1",
        description='Type 1:',
        disabled=False,
    )

    dropdown_restaurantType2 = widgets.Dropdown(
        options=["Choose restaurant type 2"] + list(df["Restaurant type 2"].dropna().unique()) ,
        value="Choose restaurant type 2",
        description='Type 2:',
        disabled=False,
    )

    out = widgets.Output()
    with out:
        display(HTML("<h3>Filter the dataset with the dropdown options"))

    myChange = Change(df, out)
    dropdown_boroughs.observe(myChange.on_change1, type='change')
    dropdown_restaurantType1.observe(myChange.on_change2, type='change')
    dropdown_restaurantType2.observe(myChange.on_change3, type='change')


    display(widgets.VBox([widgets.HBox([dropdown_boroughs, dropdown_restaurantType1, dropdown_restaurantType2]), out]))


#Class for the bar plots with 3 dropdowns

class Figure_change:
    """
    class Figure_change to define what happens when the action "change" is applied to the dropdown widgets for the Bar plots visualization.
    The aim of this class and functions is to create an interactive visualization of bar plots of number of restaurants by type and
    neighbourhood. We will have 3 different dropdowns where the user can select up to 3 different restaurant types

    Attributes:
    1) restaurant1 : string
        The first restaurant type to be visualized in the bar plot. If None, nothing is showed
    2) restaurant2 : string
        The second restaurant type to be visualized in the bar plot. If None, nothing is showed
    2) restaurant3 : string
        The third restaurant type to be visualized in the bar plot. If None, nothing is showed
    4) df : pandas.DataFrame
        The dataframe which the user wants to visualize
    5) out: widgets.Output()
        the jupyter display where the user wants to show the results
    """
    restaurant1 = None
    restaurant2 = None
    restaurant3 = None

    layout = go.Layout( width=1100, height=700,
    title='Number of Restaurants by Type and Neighborhood',
    xaxis=dict(title='Restaurant Type'),
    yaxis=dict(title='Number of Restaurants'))
    fig = go.Figure(layout=layout)

    def __init__(self, df, out):
        self.df = df
        self.out = out

    def on_change1(self, change):
        """
        Function to show the bar-plot of the 1st restaurant
        Inputs:
        1) change
           The notification that an action was applied to the dropdown
        """
        #delete all previous traces
        self.fig.data = []
        if change['type'] == 'change' and change['name'] == 'value':
            if not change['new'] == "Choose 1st type of restaurant" :
                self.restaurant1 = change['new']
            else:
                self.restaurant1 = None
            with self.out:
                clear_output(wait = True) 
                self.show_plot()

    def on_change2(self, change):
        """
        Function to show the bar-plot of the 2nd restaurant
        Inputs:
        1) change
           The notification that an action was applied to the dropdown
        """
        #delete all previous traces 
        self.fig.data = []
        if change['type'] == 'change' and change['name'] == 'value':
            if not change['new'] == "Choose 2nd type of restaurant" :
                self.restaurant2 = change['new']
            else:
                self.restaurant2 = None
            with self.out:
                clear_output(wait = True) 
                self.show_plot()

    def on_change3(self, change):
        """
        Function to show the bar-plot of the 3rd restaurant
        Inputs:
        1) change
           The notification that an action was applied to the dropdown
        """
        #delete all previous traces
        self.fig.data = []
        if change['type'] == 'change' and change['name'] == 'value':
            if not change['new'] == "Choose 3rd type of restaurant" :
                self.restaurant3 = change['new']
            else:
                self.restaurant3 = None
            with self.out:
                clear_output(wait=True) 
                self.show_plot()

    def show_plot(self):
        """
        Function to add the traces to the plot
        """
        df_bors_rests = self.df.groupby(["Boroughs", "Restaurant type"])["Restaurant name"].count().reset_index()
        df_bors_rests = df_bors_rests.rename({"Restaurant name" : "count"}, axis=1)
        restaurant_types = [self.restaurant1, self.restaurant2, self.restaurant3]
        for neighborhood in self.df["Boroughs"].unique():
            df_tmp2 = df_bors_rests[df_bors_rests["Boroughs"] == neighborhood]
            df_tmp2 = df_tmp2[df_tmp2["Restaurant type"].isin(restaurant_types)]
            self.fig.add_trace( go.Bar(
                    x=restaurant_types,
                    y=df_tmp2["count"],
                    name=neighborhood,
                    marker = dict(
                            line = dict(color='rgb(0,0,0)', width = 1.5)),
                    text = neighborhood
                    ))
        display(self.fig)


def display_barPlot_dropdowns(df):

    """
    This function creates the widgets.Output() structure with the 3 dropdowns and instantiates an object Figure_change, to apply the 
    changes to the plotly bar plot, when the user clicks on the dropdowns

    Inputs:
    1) df : pandas.DataFrame
        The DataFrame the user wants to filter
    """

    dropdown_rest1 = widgets.Dropdown(
    options=["Choose 1st type of restaurant"] + list(df["Restaurant type"].unique()) ,
    value="Choose 1st type of restaurant",
    description='1st restaurant:',
    disabled=False,
    )

    dropdown_rest2 = widgets.Dropdown(
    options=["Choose 2nd type of restaurant"] + list(df["Restaurant type"].unique()) ,
    value="Choose 2nd type of restaurant",
    description='2nd restaurant:',
    disabled=False,
    )

    dropdown_rest3 = widgets.Dropdown(
    options=["Choose 3rd type of restaurant"] + list(df["Restaurant type"].unique()) ,
    value="Choose 3rd type of restaurant",
    description='3rd restaurant:',
    disabled=False,
    )

    out = widgets.Output()
    with out:
        display(HTML("<h3>Plot total number of restaurants of a certain type for each neighbourhood"))

    myFigure = Figure_change(df, out)
    dropdown_rest1.observe(myFigure.on_change1, type='change')
    dropdown_rest2.observe(myFigure.on_change2, type='change')
    dropdown_rest3.observe(myFigure.on_change3, type='change')


    display(widgets.VBox([widgets.HBox([dropdown_rest1, dropdown_rest2, dropdown_rest3]), out]))