"""
A script for plotting 2D cell tracking data produced by 
IJM Epidermal Cell Tracking Module

MIT License
Copyright (c) 2020 Kota Miura
"""
import pandas as pd
import bokeh.io
import bokeh.plotting
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

def execute( csvfilepath ):
    #df = pd.read_csv('Dataset/desktop_tracks.csv')
    df = pd.read_csv( csvfilepath )
    print( max(df['Mean']) )
    tracks = [ df.loc[df['Mean'] == x, ['Slice', 'X', 'Y', 'Mean']] for x in range(1, int(max(df['Mean']))) ]
    print( "Number of Tracks:", len(tracks))
    tracklists = [ list(zip(tracks[x]['X'], tracks[x]['Y'], tracks[x]['Slice'])) for x in range( len(tracks) ) ]
    tracklists[0:3]
    trackplot = hv.Path(tracklists, vdims='time')
    trackplot.opts(cmap='Inferno', color='time', line_width=2 )
    
    outfilename = "trackplot.html"
    hv.save( trackplot , outfilename, fmt='html')

    #file_name = "hello_world.txt"
    #copyfile(input, file_name)
    #f = open(file_name, "w")
    #f.write("Hello, World!")
    #f.close()

    return {'Output': outfilename}
