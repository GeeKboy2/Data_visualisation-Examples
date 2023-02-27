import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def simple_graph(type='simple'):
    # Reading the tips.csv file
    data = pd.read_csv('IQ_Rarity.csv')

    # initializing the data
    x = data['IQ']
    y = data['Rarety']

    if type == 'simple':
        plt.scatter(y, x)
        plt.title("Simple graph")
    elif type == 'upgrade':
        plt.scatter(y,x, y,c=x,cmap='jet', marker='D', alpha=0.5)
        plt.title("Simple graph")

    # Adding label on the y-axis
    plt.ylabel('Rarity')

    # Adding label on the x-axis
    plt.xlabel('IQ')

    plt.show()


def pie_graph(type='simple'):
    #data = pd.read_csv('')
 
    # initializing the data
    cars = ['AUDI', 'BMW', 'FORD',
            'TESLA', 'JAGUAR',]
    data = [23, 10, 35, 15, 12]
    
    if(type=='simple'):
        plt.pie(data, labels=cars)
    if(type=='upgrade'):
        explode = [0.1, 0.5, 0, 0, 0]
 
        colors = ( "orange", "cyan", "yellow",
                "grey", "green",)
        
        # plotting the data
        plt.pie(data, labels=cars, explode=explode, autopct='%1.2f%%',
                colors=colors, shadow=True)
    
    # Adding title to the plot
    plt.title("Car data")
    
    plt.show()



def zone_graph():
    plt.style.use('_mpl-gallery')

    # make data
    np.random.seed(1)
    x = np.linspace(0, 8, 16)
    y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
    y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))

    # plot
    fig, ax = plt.subplots()

    ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
    ax.plot(x, (y1 + y2)/2, linewidth=2)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()




#simple_graph()
#simple_graph('upgrade')
#pie_graph()
#pie_graph('upgrade')
#zone_graph()