import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt
import sys
import glob

def parse_arguments():
    """Description of what the fxn does, what arguments it requires, what it returns
    Parses user's command line arguments, returns appropriate list of files
    Input: Nothing
    Return: file_list, which is a list of filenames (strings)"""
    if len(sys.argv) == 1:
        #If no argument has been supplied
        print("Not enough arguments have been provided")
        print("Usage: python gdp_plots.py <filenames>")
        print("Options: -a: plot all gdp data in current directory")
        exit()

    if sys.argv[1] == '-a':
        file_list = glob.glob("*gdp*.csv")
        if len(file_list) == 0:
            print("No files found in current directory")
            exit()

    else:
        file_list = sys.argv[1:]

    return file_list

def create_plots(file_list):
    """Plot all files in file_list using pandas and matplotlib.
    Each data file is its own plot.

    Input: file_list: list of files to plot, filenames are strings
    Return: Nothing"""
    for filename in file_list:
    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows

    # read data into a pandas dataframe and transpose    
        data = pandas.read_csv(filename, index_col = 'country').T

        # create a plot the transposed data
        ax = data.plot(title=filename)

        # axes labels
        ax.set_xlabel('Year')
        ax.set_ylabel('GDP per capita')

        # set axes ticks
        ax.set_xticks(range(len(data.index)))
        ax.set_xticklabels(data.index, rotation=45)

        # display the plot
        plt.show()

def main():
    file_list = parse_arguments()
    create_plots(file_list)

main()
