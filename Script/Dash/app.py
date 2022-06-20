###
#Importing librairies
import pandas as pd
import datetime
from datetime import *
import numpy as np
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.signal import lfilter
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
###

###
#Excracting data from files
main_path = 'L:/TL_COMMUNS/30-Pilotage Projets/90-ENF/04_R&D_THEIA/THEIA 500Hz/Manips/Fichiers manips/2022_05/22_05_20'

path_Flowmeter = main_path + ''
path_Watlow = main_path + ''
path_Ulink = main_path + ''
path_P = main_path + ''
path_Picolog = main_path + ''
path_NearField = main_path + '/NF/Centroid_Position 05-20.csv' #add csv file name
path_FarField = main_path + '/FF/Centroid_Position 05-20.csv' #add csv file name

#Parameters
# dateformat = '%A, %B %d, %Y %H:%M:%S.%f'
dateformat = '%d-%m-%Y %H:%M:%S.%f'

coef_UV=1
coef_NF=4.27
sampling_rate=5

TGI = 'T0264735'
TGI_path = 'C:/Users/' + TGI + '/Documents/MyApp'
path_result = TGI_path + '/22_05_20.html'

#Filter parameters
n = 20  #the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1

#Rolling mean parameter
k=100
###

###
#function that returns default yaxis domain for each subplot and the additional yaxes positions
def xyaxes_dom_yaxes_pos(gap, rows):
    if rows < 2:
        raise ValueError('This function works for subplots with  rows>2 and cols=1')
    h_window=  (1-gap)/rows  #window height
    d = 3/10/2
    #xaxis{k} has the domain [w[2],w[-3]] k=1,...rows
    #w[1], w[-2] give the left, resp right yaxes position associated to the default yaxis of the plot window
    yd = []
    for k in range(rows):
        start = k*(h_window+gap)
        end = start+h_window
        yd.append([start, end])
    w  =  [0, d, 2*d, 1-2*d, 1-d, 1]
   
    return w, yd[::-1]  #yd[::-1] contains the domains of the default yaxes

#Select color
fig=px.colors.qualitative.swatches()
#fig.show()
###

###
###--------------------------------------------------------------------------------------------------------------------------------------------###
#Débit mètre

def extract_data_flowmeter_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Flowmeter.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Flowmeter.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path_Flowmeter + '/Flowmeter.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       usecols = ['Date', 'Time', 'TEMP_SMC1', 'FLOW_SMC1', 'TEMP_SMC2', 'FLOW_SMC2', 'TEMP_SMC3', 'FLOW_SMC3', 'valeur_HT'],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time', 'valeur_HT'], inplace = True)
    data.rename(columns = {'TEMP_SMC1' : 'Bench flowmeter',
                           'FLOW_SMC1' : 'Bench flow',
                           'TEMP_SMC2' : 'Oscillator flowmeter',
                           'FLOW_SMC2' : 'Oscillator flow',
                           'TEMP_SMC3' : 'Amplifier flowmeter',
                           'FLOW_SMC3' : 'Amplifier flow'
                          },
                inplace=True
               )
    
    # for i in range(data.shape[1]):
    #     data[data.columns[i]].rolling(k).mean()[::k]
    #     data[data.columns[i]] = lfilter(b, a, data[data.columns[i]])
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Watlow

def extract_data_watlow_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Watlow.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Watlow.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/Watlow.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                      # usecols = ['Date', 'Time',
                      #            'Temperature SHG', 'Temperature THG', 'Temperature Bench',
                      #            'Heat Power SHG', 'Heat Power THG', 'Heat Power Bench',
                      #            'Cool Power SHG', 'Cool Power THG', 'Cool Power Bench'
                      #           ],
                       usecols = ['Date', 'Time',
                                  'Temperature Doubleur', 'Temperature Tripleur', 'Temperature Banc',
                                  'Heat Power Doubleur', 'Heat Power Tripleur', 'Heat Power Banc',
                                  'Cool Power Doubleur', 'Cool Power Tripleur', 'Cool Power Banc'
                                 ],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time'], inplace = True)
    
    # data['Heat Power Doubleur'].rolling(k).mean()[::k]
    # data['Heat Power Doubleur'] = lfilter(b, a, data['Heat Power Doubleur'])
    data['Cool Power Doubleur'].rolling(k).mean()[::k]
    # data['Cool Power Doubleur'] = lfilter(b, a, data['Cool Power Doubleur'])
    
    # data['Heat Power Tripleur'].rolling(k).mean()[::k]
    # data['Heat Power Tripleur'] = lfilter(b, a, data['Heat Power Doubleur'])
    data['Cool Power Tripleur'].rolling(k).mean()[::k]
    # data['Cool Power Tripleur'] = lfilter(b, a, data['Cool Power Tripleur'])
    
    # data['Heat Power Banc'].rolling(k).mean()[::k]
    # data['Heat Power Banc'] = lfilter(b, a, data['Heat Power Banc'])
    data['Cool Power Banc'].rolling(k).mean()[::k]
    # data['Cool Power Banc'] = lfilter(b, a, data['Cool Power Banc'])
    
    data.drop(columns = ['Heat Power Doubleur', 'Heat Power Tripleur', 'Heat Power Banc'], inplace = True)
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Picolog

def extact_data_picolog_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier pico.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'pico.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    '''
    
    filename = path + '/picolog.csv'

    data = pd.read_csv(filename,
                       delimiter = ',',
                       decimal = ',',
                       dtype = float,
                       skiprows = 0,
                       index_col = 0,
                       # on_bad_lines = 'skip',
                       parse_dates = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format='%Y-%m-%dT%H:%M:%S%z')
                      )
    data.columns = data.columns.str.replace('[()]', '')
    data.columns = data.columns.str.replace('Dernier C', '')
    data.index = data.index.tz_localize(None)
    
    for i in range(data.shape[1]):
    #     data[data.columns[i]].rolling(k).mean()[::k]
        data[data.columns[i]] = lfilter(b, a, data[data.columns[i]])
    
    data.rename(columns = {data.columns[0] : 'mirror1',
                           data.columns[1] : 'mirror2',
                           data.columns[2] : 'amp water',
                           data.columns[3] : 'town water',
                           data.columns[4] : 'sensor',
                           data.columns[5] : 'second circuit water',
                           data.columns[6] : 'room air',
                           data.columns[7] : 'room conditionning',
                           data.columns[8] : 'bench resistor near field',
                           data.columns[9] : 'energy meter UV',
                           data.columns[10] : 'tank2',
                           data.columns[11] : 'bench Rmax osc',
                           data.columns[12] : 'dichro1',
                           data.columns[13] : 'dump NC'
                          },
                inplace=True
               )
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Puissance UV

def extract_data_P_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier P532.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'P532.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/P355.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       header = 16,
                       usecols = ['Index', 'Date', 'Second', 'Measurement'],
                       parse_dates = ['Date'],
                       # on_bad_lines = 'skip',
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format='%H:%M:%S, %A, %B %d, %Y')
                      )
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Index', 'Date', 'Second'], inplace = True)
    data.rename(columns = {'Measurement' : 'Power UV'},
                inplace=True
               )
    
    data['Power UV'] = data[data['Power UV'] < 500]
    data['Power UV'] = data[data['Power UV'] > 100]
    # data['Power UV'].rolling(k).mean()[::k]
    # data['Power UV'] = lfilter(b, a, data['Power UV'])
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie UV

def extract_data_UV_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Energie UV.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Energie UV.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/Energie UV.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       usecols = ['Date', 'Time', 'Energie UV'],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time'], inplace = True)
    data.rename(columns = {'Energie UV' : 'Energy UV'},
                inplace=True
               )
    
    data['Energy UV'] = data['Energy UV']*coef_UV
    
    data['Energy UV'] = data[data['Energy UV'] < 5]
    data['Energy UV'] = data[data['Energy UV'] > 1]
    # data['Energy UV'].rolling(k).mean()[::k]
    # data['Energy UV'] = lfilter(b, a, data['Energy UV'])
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie UV stat

def extract_data_UV_stat_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Energie UV stat.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Energie UV.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/Energie UV stat.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       usecols = ['Date', 'Time', 'Mean', 'Sigma', 'Max', 'Min', 'Rapport'],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time'], inplace = True)
    
    data['Mean'] = data[data['Mean'] < 5]
    data['Mean'] = data[data['Mean'] > 1]
    # data['Mean'].rolling(k).mean()[::k]
    # data['Mean'] = lfilter(b, a, data['Mean'])
    
    data['Max'] = data[data['Max'] < 5]
    data['Max'] = data[data['Max'] > 1]
    # data['Max'].rolling(k).mean()[::k]
    # data['Max'] = lfilter(b, a, data['Max'])
    
    data['Min'] = data[data['Min'] < 5]
    data['Min'] = data[data['Min'] > 1]
    # data['Min'].rolling(k).mean()[::k]
    # data['Min'] = lfilter(b, a, data['Min'])
    
    # data['Rapport'] = (data['Sigma'] / data['Mean'])*100
    data['Rapport'] = data[data['Rapport'] < 100]
    data['Rapport'] = data[data['Rapport'] > 0]
    # data['Rapport'].rolling(k).mean()[::k]
    # data['Rapport'] = lfilter(b, a, data['Rapport'])
    
    data.rename(columns = {'Mean' : 'Mean UV',
                           'Sigma' : 'Sigma UV',
                           'Max' : 'Maximum UV',
                           'Min' : 'Minimum UV',
                           'Rapport' : 'RMS UV'
                          },
                inplace=True
               )
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie IR

def extract_data_IR_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Energie IR.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Energie IR.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/Energie IR.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       usecols = ['Date', 'Time', 'Energie IR'],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time'], inplace = True)
    data.rename(columns = {'Energie IR' : 'Energy IR'},
                inplace=True
               )
    
    data['Energy IR'] = data[data['Energy IR'] < 1500]
    data['Energy IR'] = data[data['Energy IR'] > 1000]
    # data['Energy IR'].rolling(k).mean()[::k]
    # data['Energy IR'] = lfilter(b, a, data['Energy IR'])
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie IR stat

def extract_data_IR_stat_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Energie IR stat.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Energie IR.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/Energie IR stat.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       usecols = ['Date', 'Time', 'Mean', 'Sigma', 'Max', 'Min', 'Rapport'],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time'], inplace = True)
    
    data['Mean'] = data[data['Mean'] < 1500]
    data['Mean'] = data[data['Mean'] > 1000]
    # data['Mean'].rolling(k).mean()[::k]
    # data['Mean'] = lfilter(b, a, data['Mean'])
    
    data['Max'] = data[data['Max'] < 1500]
    data['Max'] = data[data['Max'] > 1000]
    # data['Max'].rolling(k).mean()[::k]
    # data['Max'] = lfilter(b, a, data['Max'])
    
    data['Min'] = data[data['Min'] < 1500]
    data['Min'] = data[data['Min'] > 1000]
    # data['Min'].rolling(k).mean()[::k]
    # data['Min'] = lfilter(b, a, data['Min'])
    
    # data['Rapport'] = (data['Sigma'] / data['Mean'])*100
    data['Rapport'] = data[data['Rapport'] < 100]
    data['Rapport'] = data[data['Rapport'] > 0]
    # data['Rapport'].rolling(k).mean()[::k]
    # data['Rapport'] = lfilter(b, a, data['Rapport'])
    
    data.rename(columns = {'Mean' : 'Mean IR',
                           'Sigma' : 'Sigma IR',
                           'Max' : 'Maximum IR',
                           'Min' : 'Minimum IR',
                           'Rapport' : 'RMS IR'
                          },
                inplace=True
               )
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie Puissance depolar

def extract_data_Puissance_depolar_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Puissance depolar.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Puissance depolar.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/Puissance depolar.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       usecols = ['Date', 'Time', 'Puissance depolar'],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time'], inplace = True)
    data.rename(columns = {'Puissance depolar' : 'Depolar power'},
                inplace=True
               )
    
    data['Depolar power'] = data[data['Depolar power'] < 50]
    data['Depolar power'] = data[data['Depolar power'] > 30]
    # data['Depolar power'].rolling(k).mean()[::k]
    # data['Depolar power'] = lfilter(b, a, data['Depolar power'])
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie Puissance depolar stat

def extract_data_Puissance_depolar_stat_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus du fichier Energie IR stat.csv à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data 'Energie IR.csv' ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    ''' 
    
    filename = path + '/Puissance depolar stat.csv'

    data = pd.read_csv(filename,
                       delimiter = '\t',
                       decimal = '.',
                       usecols = ['Date', 'Time', 'Mean', 'Sigma', 'Max', 'Min', 'Rapport'],
                       header = 2,
                       # on_bad_lines = 'skip',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format=dateformat)
                      )
    data.drop(labels = [data.shape[0]-1, data.shape[0]-2], axis = 0, inplace = True)
    data.set_index(data['Date'], inplace=True)
    data.drop(columns = ['Date', 'Time'], inplace = True)
    
#     data['Mean'] = data[data['Mean'] < 50]
#     data['Mean'] = data[data['Mean'] > 30]
#     # data['Mean'].rolling(k).mean()[::k]
#     data['Mean'] = lfilter(b, a, data['Mean'])

#     data['Max'] = data[data['Max'] < 50]
#     data['Max'] = data[data['Max'] > 30]
#     # data['Max'].rolling(k).mean()[::k]
#     data['Max'] = lfilter(b, a, data['Max'])

#     data['Min'] = data[data['Min'] < 50]
#     data['Min'] = data[data['Min'] > 30]
#     # data['Min'].rolling(k).mean()[::k]
#     data['Min'] = lfilter(b, a, data['Min'])

#     # data['Rapport'] = (data['Sigma'] / data['Mean'])*100
#     data['Rapport'] = data[data['Rapport'] < 100]
#     data['Rapport'] = data[data['Rapport'] > 0]
#     # data['Rapport'].rolling(k).mean()[::k]
#     data['Rapport'] = lfilter(b, a, data['Rapport'])
    
    data.rename(columns = {'Mean' : 'Mean Pd',
                           'Sigma' : 'Sigma Pd',
                           'Max' : 'Maximum Pd',
                           'Min' : 'Minimum Pd',
                           'Rapport' : 'RMS Pd'
                          },
                inplace=True
               )
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Caméra Far Field

def extract_data_cameraFF_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus d'un fichier caméra à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    '''
    
    data = pd.read_csv(path,
                       delimiter = '\t\t',
                       decimal = '.',
                       usecols = ['Time', 'Position x', 'Position y', 'Ray x', 'Ray y', '1/e^2 X width', '1/e^2 Y width', 'Fit Order X', 'Fit Order Y', 'Steepness REX', 'Steepness FEX', 'Steepness REY', 'Steepness FEY', 'Peak Energy Density', 'Ellipticity'],
                       # on_bad_lines = 'skip',
                       parse_dates = ['Time'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format='%d-%m-%Y\t%H:%M:%S.%f'),
                       engine='python'
                      )
    data.set_index(data['Time'], inplace=True)
    data.drop(columns = ['Time', 'Ray x', 'Ray y', 'Fit Order X', 'Fit Order Y', 'Steepness REX', 'Steepness FEX', 'Steepness REY', 'Steepness FEY', 'Peak Energy Density', 'Ellipticity'], inplace = True)
    
    data['Position x'] = data['Position x'] - data['Position x'].mean()
    data['Position y'] = data['Position y'] - data['Position y'].mean()
    
    data.rename(columns = {'Position x' : 'Position x FF',
                           'Position y' : 'Position y FF',
                           '1/e^2 X width' : '1/e^2 X width FF',
                           '1/e^2 Y width' : '1/e^2 Y width FF'
                          },
                inplace=True
               )
    
    data['Position x FF'] = data[data['Position x FF'] < 200]
    data['Position x FF'] = data[data['Position x FF'] > -200]
    # data['Position x FF'].rolling(k).mean()[::k]
    data['Position x FF'] = lfilter(b, a, data['Position x FF'])
    
    data['Position y FF'] = data[data['Position y FF'] < 200]
    data['Position y FF'] = data[data['Position y FF'] > -200]
    # data['Position y FF'].rolling(k).mean()[::k]
    data['Position y FF'] = lfilter(b, a, data['Position y FF'])
    
#     data['1/e^2 X width FF'] = data[data['1/e^2 X width FF'] < 700]
#     data['1/e^2 X width FF'] = data[data['1/e^2 X width FF'] > 500]
#     data['1/e^2 X width FF'].rolling(k).mean()[::k]
    data['1/e^2 X width FF'] = lfilter(b, a, data['1/e^2 X width FF'])
    
#     data['1/e^2 Y width FF'] = data[data['1/e^2 Y width FF'] < 700]
#     data['1/e^2 Y width FF'] = data[data['1/e^2 Y width FF'] > 500]
#     data['1/e^2 Y width FF'].rolling(k).mean()[::k]
    data['1/e^2 Y width FF'] = lfilter(b, a, data['1/e^2 Y width FF'])
    
    return data

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Caméra Near Field

def extract_data_cameraNF_Date(path):
    '''
    Fonction qui permet d\'extraire les données issus d'un fichier caméra à l'aide de la colonne 'Date'.
    * Entrée : path --> chemin d'accès au fichier data ;
    * Sortie : tableau pandas contenant les données de mesures et la date traitée.
    '''
    
    data = pd.read_csv(path,
                       delimiter = '\t\t',
                       decimal = '.',
                       usecols = ['Time', 'Position x', 'Position y', 'Ray x', 'Ray y', '1/e^2 X width', '1/e^2 Y width', 'Fit Order X', 'Fit Order Y', 'Steepness REX', 'Steepness FEX', 'Steepness REY', 'Steepness FEY', 'Peak Energy Density', 'Ellipticity'],
                       # on_bad_lines = 'skip',
                       parse_dates = ['Time'],
                       dayfirst = True,
                       infer_datetime_format = True,
                       date_parser = lambda date: pd.to_datetime(date, format='%d-%m-%Y\t%H:%M:%S.%f'),
                       engine='python'
                      )
    data.set_index(data['Time'], inplace=True)
    data.drop(columns = ['Time', 'Ray x', 'Ray y', 'Fit Order X', 'Fit Order Y', 'Steepness REX', 'Steepness FEX', 'Steepness REY', 'Steepness FEY', 'Peak Energy Density', 'Ellipticity'], inplace = True)
    
    data['Position x'] = data['Position x']*coef_NF
    data['Position y'] = data['Position y']*coef_NF
    data['1/e^2 X width'] = (data['1/e^2 X width']*coef_NF)/1000
    data['1/e^2 Y width'] = (data['1/e^2 Y width']*coef_NF)/1000
    
    data['Position x'] = data['Position x'] - data['Position x'].mean()
    data['Position y'] = data['Position y'] - data['Position y'].mean()
    
    data.rename(columns = {'Position x' : 'Position x NF',
                           'Position y' : 'Position y NF',
                           '1/e^2 X width' : '1/e^2 X width NF',
                           '1/e^2 Y width' : '1/e^2 Y width NF'
                          },
                inplace=True
               )
    
    data['Position x NF'] = data[data['Position x NF'] < 200]
    data['Position x NF'] = data[data['Position x NF'] > -200]
    # data['Position x NF'].rolling(k).mean()[::k]
    data['Position x NF'] = lfilter(b, a, data['Position x NF'])
    
    data['Position y NF'] = data[data['Position y NF'] < 200]
    data['Position y NF'] = data[data['Position y NF'] > -200]
    # data['Position y NF'].rolling(k).mean()[::k]
    data['Position y NF'] = lfilter(b, a, data['Position y NF'])
    
#     data['1/e^2 X width NF'] = data[data['1/e^2 X width NF'] < 12]
#     data['1/e^2 X width NF'] = data[data['1/e^2 X width NF'] > 7]
#     data['1/e^2 X width NF'].rolling(k).mean()[::k]
    data['1/e^2 X width NF'] = lfilter(b, a, data['1/e^2 X width NF'])
    
#     data['1/e^2 Y width NF'] = data[data['1/e^2 Y width NF'] < 12]
#     data['1/e^2 Y width NF'] = data[data['1/e^2 Y width NF'] > 7]
#     data['1/e^2 Y width NF'].rolling(k).mean()[::k]
    data['1/e^2 Y width NF'] = lfilter(b, a, data['1/e^2 Y width NF'])
    
    return data
###

###
###--------------------------------------------------------------------------------------------------------------------------------------------###
#Débit mètre (Températures) + Watlow + Picolog

def plot_temperature(df_flow_tmp, df_watlow, df_pico):
    '''
    Fonction qui permet d\'afficher les résultats des mesures en fonction de la date.
    * Entrée : dataframe -> tableau pandas contenant les données de mesures et la date traitée ;
    * Sortie : affiche directement un graphe avec les mesures en ordonnée et la date en abscisse.
    '''
    
    yd = [[0.86, 1],
          [0.66, 0.85],
          [0.5, 0.65],
          [0.33, 0.49],
          [0.16, 0.32],
          [0, 0.15]
         ]
    w = [0, 0.05, 0.3, 0.7, 0.95, 1]
    
    fig = go.Figure()
    
    fig.update_layout(title_x=0.5, 
                      title_text='Température', 
                      showlegend=True,
                      legend=dict(groupclick='toggleitem'),
                      legend_title_text='Legend',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Temperature (°C)')
                     )
    
    #Flowmeter
    for i in range(len(df_flow_tmp.columns)):
        fig.add_trace(go.Scatter(x=df_flow_tmp.index,
                                 y=df_flow_tmp[df_flow_tmp.columns[i]],
                                 name=('%s' %(df_flow_tmp.columns[i])),
                                 xaxis='x',
                                 yaxis='y',
                                 visible=True,
                                 legendgroup='Temperature',
                                 legendgrouptitle_text='Temperature'
                                )
                     )
    
    #Watlow
    for i in range(len(df_watlow.columns)):
        fig.add_trace(go.Scatter(x=df_watlow.index,
                                 y=df_watlow[df_watlow.columns[i]],
                                 name=('%s' %(df_watlow.columns[i])),
                                 xaxis='x',
                                 yaxis='y',
                                 visible=True,
                                 legendgroup='Temperature'
                                )
                     )
    
    #Picolog
    for i in range(len(df_pico.columns)):
        fig.add_trace(go.Scatter(x=df_pico.index,
                                 y=df_pico[df_pico.columns[i]],
                                 name=('%s' %(df_pico.columns[i])),
                                 xaxis='x',
                                 yaxis='y',
                                 visible='legendonly',
                                 legendgroup='Temperature'
                                )
                     )
     
    # fig.show()
##    fig.write_html(TGI_path + '/temperature.html', 
##                   auto_open=True,
##                   config={'modeBarButtonsToAdd':['drawline',
##                                                  'drawopenpath',
##                                                  'drawclosedpath',
##                                                  'drawcircle',
##                                                  'drawrect',
##                                                  'eraseshape'
##                                                 ]
##                          }
##                  )
    
    # return 1
    return fig

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Débits

def plot_flow(df_flow):
    '''
    Fonction qui permet d\'afficher les résultats des mesures en fonction de la date.
    * Entrée : dataframe -> tableau pandas contenant les données de mesures et la date traitée ;
    * Sortie : affiche directement un graphe avec les mesures en ordonnée et la date en abscisse.
    '''
    
    yd = [[0.86, 1],
          [0.66, 0.85],
          [0.5, 0.65],
          [0.33, 0.49],
          [0.16, 0.32],
          [0, 0.15]
         ]
    w = [0, 0.05, 0.3, 0.7, 0.95, 1]
    
    fig = go.Figure()
    
    fig.update_layout(title_x=0.5, 
                      title_text='Débits',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Flow'),
                      showlegend=True,
                      legend_title_text='Sensors'
                     )
    
    for i in range(len(df_flow.columns)):
        fig.add_trace(go.Scatter(x=df_flow.index,
                                 y=df_flow[df_flow.columns[i]],
                                 name=df_flow.columns[i]
                                )
                     )
    
    # fig.show()
##    fig.write_html(TGI_path + '/flow.html', 
##                   auto_open=True,
##                   config={'modeBarButtonsToAdd':['drawline',
##                                                  'drawopenpath',
##                                                  'drawclosedpath',
##                                                  'drawcircle',
##                                                  'drawrect',
##                                                  'eraseshape'
##                                                 ]
##                          }
##                  )
    
    # return 1
    return fig

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie UV + stabilité RMS + Puissance UV + (autres statistiques - moyenne + minimum + maximum)

def plot_UV(df_UV, df_UV_RMS, df_UV_hide, df_P):
    '''
    Fonction qui permet d\'afficher les résultats des mesures en fonction de la date.
    * Entrée : dataframe -> tableau pandas contenant les données de mesures et la date traitée ;
    * Sortie : affiche directement un graphe avec les mesures en ordonnée et la date en abscisse.
    '''
    
    yd = [[0.86, 1],
          [0.66, 0.85],
          [0.5, 0.65],
          [0.33, 0.49],
          [0.16, 0.32],
          [0, 0.15]
         ]
    w = [0, 0.05, 0.3, 0.7, 0.95, 1]
    
    color_UV=['#19D3F3']
    color_UV_RMS=['#636EFA']
    color_UV_hide=['#8C564B', '#222A2A', '#3366CC']
    color_P=['#AB63FA']
    
    fig = go.Figure()
    
    fig.update_layout(title_x=0.5,
                      title_text='UV', 
                      showlegend=True,
                      legend=dict(groupclick='toggleitem'),
                      legend_title_text='Legend',
                      xaxis=dict(domain=[w[1],w[-2]],
                                title='Date'),
                      yaxis=dict(title='Energy (mJ)',
                                 titlefont=dict(color=color_UV[0]),
                                 tickfont=dict(color=color_UV[0]),
                                 side='left'
                                ),
                      yaxis2=dict(title='RMS (%)',
                                  titlefont=dict(color=color_UV_RMS[0]),
                                  tickfont=dict(color=color_UV_RMS[0]),
                                  anchor='free',
                                  overlaying='y',
                                  side='left',
                                  position=w[0]
                                 ),
                      yaxis3=dict(title='Power (W)',
                                  titlefont=dict(color=color_P[0]),
                                  tickfont=dict(color=color_P[0]), 
                                  anchor='x',
                                  overlaying='y',
                                  side='right'
                                 )
                     )
    
    for i in range(len(df_UV.columns)):
        fig.add_trace(go.Scatter(x=df_UV.index,
                                 y=df_UV[df_UV.columns[i]],
                                 name=df_UV.columns[i],
                                 line=dict(color=color_UV[i]),
                                 legendgroup='Energy',
                                 legendgrouptitle_text='Energy',
                                 yaxis='y1'
                                )
                     )

    fig.add_trace(go.Scatter(x=df_UV_RMS.index,
                             y=df_UV_RMS[df_UV_RMS.columns[0]],
                             name=df_UV_RMS.columns[0],
                             line=dict(color=color_UV_RMS[i]),
                             legendgroup='Energy',
                             yaxis='y2'
                            )
                 )
    
    for i in range(len(df_UV_hide.columns)):
        fig.add_trace(go.Scatter(x=df_UV_hide.index,
                                 y=df_UV_hide[df_UV_hide.columns[i]],
                                 name=df_UV_hide.columns[i],
                                 line=dict(color=color_UV_hide[i]),
                                 visible='legendonly',
                                 legendgroup='Energy',
                                 yaxis='y1'
                                )
                     )
    
    for i in range(len(df_P.columns)):
        fig.add_trace(go.Scatter(x=df_P.index,
                                 y=df_P[df_P.columns[i]],
                                 name=df_P.columns[i],
                                 line=dict(color=color_P[i]),
                                 legendgroup='Power',
                                 legendgrouptitle_text='Power',
                                 yaxis='y3'
                                )
                     )
    
    # fig.show()
##    fig.write_html(TGI_path + '/UV.html', 
##                   auto_open=True,
##                   config={'modeBarButtonsToAdd':['drawline',
##                                                  'drawopenpath',
##                                                  'drawclosedpath',
##                                                  'drawcircle',
##                                                  'drawrect',
##                                                  'eraseshape'
##                                                 ]
##                          }
##                  )
    
    # return 1
    return fig

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Energie IR + stabilité RMS + Puissance depolar + (autres statistiques - moyenne + minimum + maximum)

def plot_IR(df_IR, df_IR_RMS, df_IR_hide, df_Pd):
    '''
    Fonction qui permet d\'afficher les résultats des mesures en fonction de la date.
    * Entrée : dataframe -> tableau pandas contenant les données de mesures et la date traitée ;
    * Sortie : affiche directement un graphe avec les mesures en ordonnée et la date en abscisse.
    '''
    
    yd = [[0.86, 1],
          [0.66, 0.85],
          [0.5, 0.65],
          [0.33, 0.49],
          [0.16, 0.32],
          [0, 0.15]
         ]
    w = [0, 0.05, 0.3, 0.7, 0.95, 1]
    
    color_IR=['#EF553B']
    color_RMS=['#FFA15A']
    color_IR_hide=['#8C564B', '#222A2A', '#3366CC']
    color_Pd=['#636EFA']
    
    fig = go.Figure()
    
    fig.update_layout(title_x=0.5,
                      title_text='IR', 
                      showlegend=True,
                      legend=dict(groupclick='toggleitem'),
                      legend_title_text='Legend',
                      xaxis=dict(domain=[w[1],w[-2]],
                                 title='Date'
                                ),
                      yaxis=dict(title='Energy (mJ)',
                                 titlefont=dict(color=color_IR[0]),
                                 tickfont=dict(color=color_IR[0]),
                                 side='left'
                                ),
                      yaxis2=dict(title='RMS (%)',
                                  titlefont=dict(color=color_RMS[0]),
                                  tickfont=dict(color=color_RMS[0]),
                                  anchor='free',
                                  overlaying='y',
                                  side='left',
                                  position=w[0]
                                 ),
                      yaxis3=dict(title='Power (W)',
                                  titlefont=dict(color=color_Pd[0]),
                                  tickfont=dict(color=color_Pd[0]), 
                                  anchor='x',
                                  overlaying='y',
                                  side='right'
                                 )
                     )
    
    for i in range(len(df_IR.columns)):
        fig.add_trace(go.Scatter(x=df_IR.index,
                                 y=df_IR[df_IR.columns[i]],
                                 name=df_IR.columns[i],
                                 line=dict(color=color_IR[i]),
                                 legendgroup='Energy',
                                 legendgrouptitle_text='Energy',
                                 yaxis='y1'
                                )
                     )

    fig.add_trace(go.Scatter(x=df_IR_RMS.index,
                             y=df_IR_RMS[df_IR_RMS.columns[0]],
                             name=df_IR_RMS.columns[0],
                             line=dict(color=color_RMS[0]),
                             legendgroup='Energy',
                             yaxis='y2'
                            )
                 )
    
    for i in range(len(df_IR_hide.columns)):
        fig.add_trace(go.Scatter(x=df_IR_hide.index,
                                 y=df_IR_hide[df_IR_hide.columns[i]],
                                 name=df_IR_hide.columns[i],
                                 line=dict(color=color_IR_hide[i]),
                                 visible='legendonly',
                                 legendgroup='Energy',
                                 yaxis='y1'
                                )
                     )
    
    for i in range(len(df_Pd.columns)):
        fig.add_trace(go.Scatter(x=df_Pd.index,
                                 y=df_Pd[df_Pd.columns[i]],
                                 name=df_Pd.columns[i],
                                 line=dict(color=color_Pd[i]),
                                 legendgroup='Power',
                                 legendgrouptitle_text='Power',
                                 yaxis='y3'
                                )
                     )
    
    # fig.show()
##    fig.write_html(TGI_path + '/IR.html', 
##                   auto_open=True,
##                   config={'modeBarButtonsToAdd':['drawline',
##                                                  'drawopenpath',
##                                                  'drawclosedpath',
##                                                  'drawcircle',
##                                                  'drawrect',
##                                                  'eraseshape'
##                                                 ]
##                          }
##                  )
    
    # return 1
    return fig

###--------------------------------------------------------------------------------------------------------------------------------------------###
#Caméra - Near Field/Far Field

def plot_field(df_field, field):
    '''
    Fonction qui permet d\'afficher les résultats des mesures en fonction de la date.
    * Entrée : dataframe -> tableau pandas contenant les données de mesures et la date traitée ;
    * Sortie : affiche directement un graphe avec les mesures en ordonnée et la date en abscisse.
    '''
    
    if (field == 'Near'):
        ff_nf = 'NF'
        width = 'mm'
    else:
        ff_nf = 'FF'
        width = 'µm'
        
    yd = [[0.86, 1],
          [0.66, 0.85],
          [0.5, 0.65],
          [0.33, 0.49],
          [0.16, 0.32],
          [0, 0.15]
         ]
    w = [0, 0.05, 0.3, 0.7, 0.95, 1]
    
    color_Position=['#19D3F3', '#636EFA']
    color_Width=['#FFA15A', '#EF553B']
    
    fig = go.Figure()
    
    fig.update_layout(title_x=0.5,
                      title_text=('Camera - %s Field' %field), 
                      showlegend=True,
                      legend=dict(groupclick='toggleitem'),
                      legend_title_text='Legend',
                      xaxis=dict(domain=[w[1],w[-2]],
                                 title='Date'
                                ),
                      yaxis=dict(title='Position (µm)',
                                 side='left'
                                ),
                      yaxis2=dict(title='Width (%s)' %width,
                                  anchor='x',
                                  overlaying='y',
                                  side='right'
                                 )
                     )
    
    #Position x
    fig.add_trace(go.Scatter(x=df_field.index, 
                             y=df_field['Position x %s' %ff_nf], 
                             name='Position x',
                             xaxis='x',
                             yaxis='y1',
                             line=dict(color=color_Position[0]),
                             visible=True,
                             legendgroup='Position',
                             legendgrouptitle_text='Position',
                            )
                 )
    
    #Position y
    fig.add_trace(go.Scatter(x=df_field.index, 
                             y=df_field['Position y %s' %ff_nf], 
                             name='Position y',
                             xaxis='x',
                             yaxis='y1',
                             line=dict(color=color_Position[1]),
                             visible=True,
                             legendgroup='Position',
                            )
                 )
    
    #Width x
    fig.add_trace(go.Scatter(x=df_field.index, 
                             y=df_field['1/e^2 X width %s' %ff_nf], 
                             name='1/e^2 x',
                             xaxis='x',
                             yaxis='y2',
                             line=dict(color=color_Width[0]),
                             visible=True,
                             legendgroup='Width',
                             legendgrouptitle_text='Width'
                            )
                 )
    
    #Width y
    fig.add_trace(go.Scatter(x=df_field.index, 
                             y=df_field['1/e^2 Y width %s' %ff_nf], 
                             name='1/e^2 y',
                             xaxis='x',
                             yaxis='y2',
                             line=dict(color=color_Width[1]),
                             visible=True,
                             legendgroup='Width'
                            )
                 )
    
    # fig.show()
##    fig.write_html(TGI_path + '/' + field + '_field.html', 
##                   auto_open=True,
##                   config={'modeBarButtonsToAdd':['drawline',
##                                                  'drawopenpath',
##                                                  'drawclosedpath',
##                                                  'drawcircle',
##                                                  'drawrect',
##                                                  'eraseshape'
##                                                 ]
##                          }
##                  )

    # return 1
    return fig
###

###
def plot_xshared(dfs):
    df_flow_tmp, df_watlow, df_pico, df_flow, df_UV, df_UV_RMS, df_UV_hide, df_P, df_IR, df_IR_RMS, df_IR_hide, df_Pd, df_nearfield, df_farfield = dfs
    
    yd = [[0.86, 1],
          [0.66, 0.85],
          [0.5, 0.65],
          [0.33, 0.49],
          [0.16, 0.32],
          [0, 0.15]
         ]
    w = [0, 0.05, 0.3, 0.7, 0.95, 1]
    
    color_UV=['#19D3F3']
    color_UV_RMS=['#636EFA']
    color_UV_hide=['#8C564B', '#222A2A', '#3366CC']
    color_P=['#AB63FA']
    
    color_IR=['#EF553B']
    color_IR_RMS=['#FFA15A']
    color_IR_hide=['#8C564B', '#222A2A', '#3366CC']
    color_Pd=['#636EFA']
    
    color_Position=['#19D3F3', '#636EFA']
    color_Width=['#FFA15A', '#EF553B']
    
    fig = go.Figure()
    
    fig.update_layout(showlegend=True,
                      title_text=('Endurance THEIA@500Hz from %s to %s' %(df_UV.index[1].strftime('%d-%m-%Y %H:%M:%S'), df_UV.index[-1].strftime('%d-%m-%Y %H:%M:%S'))),
                      title_x=0.5,
                      legend=dict(groupclick='toggleitem'),
                      legend_title_text='Legend',
                      xaxis1=dict(anchor='y1',
                                  domain=[w[1],w[-2]],
                                  matches='x12',
                                  showticklabels=False
                                 ),
                      yaxis1=dict(title='Energy UV (mJ)',
                                  titlefont=dict(color=color_UV[0]),
                                  tickfont=dict(color=color_UV[0]),
                                  domain=yd[0],
                                  range=[1,5],
                                  showgrid=False
                                 ), #UV
                      yaxis2=dict(title='RMS UV (%)',
                                  titlefont=dict(color=color_UV_RMS[0]),
                                  tickfont=dict(color=color_UV_RMS[0]),
                                  anchor='free',
                                  overlaying='y1',
                                  matches=None,
                                  side='left',
                                  # range=[0,0.5],
                                  position=w[0],
                                  domain=yd[0],
                                  showgrid=False
                                 ), #UV
                      yaxis3=dict(title='Power UV (W)',
                                  titlefont=dict(color=color_P[0]),
                                  tickfont=dict(color=color_P[0]),
                                  anchor='x1',
                                  overlaying='y1',
                                  matches=None,
                                  side='right',
                                  range=[200,300],
                                  domain=yd[0],
                                  showgrid=False
                                 ), #UV
                      xaxis4=dict(anchor='y4',
                                  matches='x12',
                                  showticklabels=False,
                                  domain=[w[1],w[-2]]
                                 ),
                      yaxis4=dict(title='Energy IR (mJ)',
                                  titlefont=dict(color=color_IR[0]),
                                  tickfont=dict(color=color_IR[0]),
                                  domain=yd[1],
                                  showgrid=False
                                 ), #IR
                      yaxis5=dict(title='RMS IR (%)',
                                  titlefont=dict(color=color_IR_RMS[0]),
                                  tickfont=dict(color=color_IR_RMS[0]),
                                  anchor='free',
                                  overlaying='y4',
                                  matches=None,
                                  side='left',
                                  # range=[0,0.2],
                                  position=w[0],
                                  domain=yd[1],
                                  showgrid=False
                                 ), #IR
                      yaxis6=dict(title='Power IR (W)',
                                  titlefont=dict(color=color_Pd[0]),
                                  tickfont=dict(color=color_Pd[0]),
                                  anchor='x6',
                                  overlaying='y4',
                                  matches=None,
                                  side='right',
                                  range=[30,50],
                                  domain=yd[1],
                                  showgrid=False
                                 ), #IR
                      xaxis7=dict(anchor='y7',
                                  matches='x12',
                                  showticklabels=False,
                                  domain=[w[1],w[-2]]
                                 ),
                      yaxis7=dict(title='Temperature (°C)',
                                  anchor='x7',
                                  overlaying='y7',
                                  matches=None,
                                  side='left',
                                  range=[10,35],
                                  domain=yd[2],
                                  showgrid=False
                                 ), #temperature
                      xaxis8=dict(anchor='y8',
                                  matches='x12',
                                  showticklabels=False,
                                  domain=[w[1],w[-2]]
                                 ),
                      yaxis8=dict(title='Position FF (µm)',
                                  titlefont=dict(color=color_Position[0]),
                                  tickfont=dict(color=color_Position[0]),
                                  domain=yd[3],
                                  range=[-200,200],
                                  showgrid=False
                                 ), #far field
                      yaxis9=dict(title='Width FF (µm)',
                                  titlefont=dict(color=color_Width[0]),
                                  tickfont=dict(color=color_Width[0]),
                                  anchor='x9',
                                  overlaying='y8',
                                  matches=None,
                                  side='right',
                                  range=[400,800],
                                  domain=yd[3],
                                  showgrid=False
                                 ), #far field
                      xaxis10=dict(anchor='y10',
                                   matches='x12',
                                   showticklabels=False,
                                   domain=[w[1],w[-2]]
                                  ),
                      yaxis10=dict(title='Position NF (µm)',
                                   titlefont=dict(color=color_Position[0]),
                                   tickfont=dict(color=color_Position[0]),
                                   domain=yd[4],
                                   range=[-200,200],
                                   showgrid=False
                                  ), #near field
                      yaxis11=dict(title='Width NF (mm)',
                                   titlefont=dict(color=color_Width[0]),
                                   tickfont=dict(color=color_Width[0]),
                                   anchor='x11',
                                   overlaying='y10',
                                   matches=None,
                                   side='right',
                                   range=[8,11],
                                   domain=yd[4],
                                   showgrid=False
                                  ), #near field
                      xaxis12=dict(anchor='y12',
                                   showticklabels=True,
                                   domain=[w[1],w[-2]],
                                   tickangle=45
                                  ), #common x shared axis
                      yaxis12=dict(title='Flow (L/min)',
                                   anchor='x12',
                                   overlaying='y12',
                                   matches=None,
                                   side='left',
                                   range=[0,10],
                                   domain=yd[5],
                                   showgrid=False
                                  ) #flow
                     )
    
    ### UV ###
    #Energy
    for i in range(len(df_UV.columns)):
        fig.add_trace(go.Scatter(x=df_UV.index,
                                 y=df_UV[df_UV.columns[i]],
                                 name=('%s' %(df_UV.columns[i])),
                                 xaxis='x1',
                                 yaxis='y1',
                                 line=dict(color=color_UV[i]),
                                 visible=True,
                                 legendgroup='UV',
                                 legendgrouptitle_text='UV'
                                )
                     )
    #Mean, Max, Min
    for i in range(len(df_UV_hide.columns)):
        fig.add_trace(go.Scatter(x=df_UV_hide.index,
                                 y=df_UV_hide[df_UV_hide.columns[i]],
                                 name=('%s' %(df_UV_hide.columns[i])),
                                 xaxis='x1',
                                 yaxis='y1',
                                 line=dict(color=color_UV_hide[i]),
                                 visible='legendonly',
                                 legendgroup='UV'
                                )
                     )

    #RMS
    fig.add_trace(go.Scatter(x=df_UV_RMS.index,
                             y=df_UV_RMS[df_UV_RMS.columns[0]],
                             name='UV RMS',
                             xaxis='x1',
                             yaxis='y2',
                             line=dict(color=color_UV_RMS[0]),
                             visible=True,
                             legendgroup='UV'
                            )
                 )

    #Power
    for i in range(len(df_P.columns)):
        fig.add_trace(go.Scatter(x=df_P.index,
                                 y=df_P[df_P.columns[i]],
                                 name=('%s' %(df_P.columns[i])),
                                 xaxis='x1',
                                 yaxis='y3',
                                 line=dict(color=color_P[i]),
                                 visible=True,
                                 legendgroup='UV'
                                )
                     )

    ### IR ###
    #Energy
    for i in range(len(df_IR.columns)):
        fig.add_trace(go.Scatter(x=df_IR.index,
                                 y=df_IR[df_IR.columns[i]],
                                 name=('%s' %(df_IR.columns[i])),
                                 xaxis='x4',
                                 yaxis='y4',
                                 line=dict(color=color_IR[i]),
                                 visible=True,
                                 legendgroup='IR',
                                 legendgrouptitle_text='IR'
                                )
                     )

    #Mean, Max, Min
    for i in range(len(df_IR_hide.columns)):
        fig.add_trace(go.Scatter(x=df_IR_hide.index,
                                 y=df_IR_hide[df_IR_hide.columns[i]],
                                 name=('%s' %(df_IR_hide.columns[i])),
                                 xaxis='x4',
                                 yaxis='y4',
                                 line=dict(color=color_IR_hide[i]),
                                 visible='legendonly',
                                 legendgroup='IR'
                                )
                     )

    #RMS
    fig.add_trace(go.Scatter(x=df_IR_RMS.index,
                             y=df_IR_RMS[df_IR_RMS.columns[0]],
                             name='IR RMS',
                             xaxis='x4',
                             yaxis='y5',
                             line=dict(color=color_IR_RMS[0]),
                             visible=True,
                             legendgroup='IR'
                            )
                 )
    
    #Depolar power
    for i in range(len(df_Pd.columns)):
        fig.add_trace(go.Scatter(x=df_Pd.index,
                                 y=df_Pd[df_Pd.columns[i]],
                                 name=('%s' %(df_Pd.columns[i])),
                                 xaxis='x4',
                                 yaxis='y6',
                                 line=dict(color=color_Pd[i]),
                                 visible=True,
                                 legendgroup='IR'
                                )
                     )
        
    ### TEMPERATURE ###
    #Flowmeter
    for i in range(len(df_flow_tmp.columns)):
        fig.add_trace(go.Scatter(x=df_flow_tmp.index,
                                 y=df_flow_tmp[df_flow_tmp.columns[i]],
                                 name=('%s' %(df_flow_tmp.columns[i])),
                                 xaxis='x7',
                                 yaxis='y7',
                                 visible=True,
                                 legendgroup='Temperature',
                                 legendgrouptitle_text='Temperature'
                                )
                     )
    
    #Watlow
    for i in range(len(df_watlow.columns)):
        fig.add_trace(go.Scatter(x=df_watlow.index,
                                 y=df_watlow[df_watlow.columns[i]],
                                 name=('%s' %(df_watlow.columns[i])),
                                 xaxis='x7',
                                 yaxis='y7',
                                 visible=True,
                                 legendgroup='Temperature'
                                )
                     )
    
    #Picolog
    for i in range(len(df_pico.columns)):
        fig.add_trace(go.Scatter(x=df_pico.index,
                                 y=df_pico[df_pico.columns[i]],
                                 name=('%s' %(df_pico.columns[i])),
                                 xaxis='x7',
                                 yaxis='y7',
                                 visible='legendonly',
                                 legendgroup='Temperature'
                                )
                     )

    ### FAR FIELD ###
    #Position x
    fig.add_trace(go.Scatter(x=df_farfield.index, 
                             y=df_farfield['Position x FF'], 
                             name='Position x - Far Field',
                             xaxis='x8',
                             yaxis='y8',
                             line=dict(color=color_Position[0]),
                             visible=True,
                             legendgroup='Far Field',
                             legendgrouptitle_text='Far Field',
                            )
                 )
    
    #Position y
    fig.add_trace(go.Scatter(x=df_farfield.index, 
                             y=df_farfield['Position y FF'], 
                             name='Position y - Far Field',
                             xaxis='x8',
                             yaxis='y8',
                             line=dict(color=color_Position[1]),
                             visible=True,
                             legendgroup='Far Field'
                            )
                 )
    
    #Width x
    fig.add_trace(go.Scatter(x=df_farfield.index, 
                             y=df_farfield['1/e^2 X width FF'], 
                             name='1/e^2 x - Far Field',
                             xaxis='x8',
                             yaxis='y9',
                             line=dict(color=color_Width[0]),
                             visible=True,
                             legendgroup='Far Field'
                            )
                 )
    
    #Width y
    fig.add_trace(go.Scatter(x=df_farfield.index, 
                             y=df_farfield['1/e^2 Y width FF'], 
                             name='1/e^2 y - Far Field',
                             xaxis='x8',
                             yaxis='y9',
                             line=dict(color=color_Width[1]),
                             visible=True,
                             legendgroup='Far Field'
                            )
                 ) 
    
    ### NEAR FIELD ###
    #Position x
    fig.add_trace(go.Scatter(x=df_nearfield.index, 
                             y=df_nearfield['Position x NF'], 
                             name='Position x - Near Field',
                             xaxis='x10',
                             yaxis='y10',
                             line=dict(color=color_Position[0]),
                             visible=True,
                             legendgroup='Near Field',
                             legendgrouptitle_text='Near Field',
                            )
                 )
    
    #Position y
    fig.add_trace(go.Scatter(x=df_nearfield.index, 
                             y=df_nearfield['Position y NF'], 
                             name='Position y - Near Field',
                             xaxis='x10',
                             yaxis='y10',
                             line=dict(color=color_Position[1]),
                             visible=True,
                             legendgroup='Near Field'
                            )
                 )
    
    #Width x
    fig.add_trace(go.Scatter(x=df_nearfield.index, 
                             y=df_nearfield['1/e^2 X width NF'], 
                             name='1/e^2 x - Near Field',
                             xaxis='x10',
                             yaxis='y11',
                             line=dict(color=color_Width[0]),
                             visible=True,
                             legendgroup='Near Field'
                            )
                 )
    
    #Width y
    fig.add_trace(go.Scatter(x=df_nearfield.index, 
                             y=df_nearfield['1/e^2 Y width NF'], 
                             name='1/e^2 y - Near Field',
                             xaxis='x10',
                             yaxis='y11',
                             line=dict(color=color_Width[1]),
                             visible=True,
                             legendgroup='Near Field'
                            )
                 )
    
    ### FLOW ###
    for i in range(len(df_flow.columns)):
        fig.add_trace(go.Scatter(x=df_flow.index,
                                 y=df_flow[df_flow.columns[i]],
                                 name=('%s' %(df_flow.columns[i])),
                                 xaxis='x12',
                                 yaxis='y12',
                                 visible=True,
                                 legendgroup='Flow',
                                 legendgrouptitle_text='Flow'
                                )
                     )
        
    # fig.show()
##    fig.write_html(path_result, 
##                   auto_open=True,
##                   config={'modeBarButtonsToAdd':['drawline',
##                                                  'drawopenpath',
##                                                  'drawclosedpath',
##                                                  'drawcircle',
##                                                  'drawrect',
##                                                  'eraseshape'
##                                                 ]
##                          }
##                  )
    
    # return 1
    return fig
###

###
data_Flowmeter_tmp = extract_data_flowmeter_Date(path_Flowmeter)
data_Flowmeter_tmp.drop(columns = ['Bench flow', 'Oscillator flow', 'Amplifier flow'], inplace = True)
data_Flowmeter_tmp.rename(columns = {'Bench temperature' : 'Bench',
                                     'Oscillator temperature' : 'Oscillator',
                                     'Amplifier temperature' : 'Amplifier'
                                    },
                          inplace=True
                         )
data_Watlow = extract_data_watlow_Date(path_Watlow)
data_Picolog = extact_data_picolog_Date(path_Picolog)

# plot_temperature(data_Flowmeter_tmp, data_Watlow, data_Picolog[::sampling_rate])

data_Flowmeter = extract_data_flowmeter_Date(path_Flowmeter)
data_Flowmeter.drop(columns = ['Bench flowmeter', 'Oscillator flowmeter', 'Amplifier flowmeter'], inplace = True)
data_Flowmeter.rename(columns = {'Bench flow' : 'Bench',
                                 'Oscillator flow' : 'Oscillator',
                                 'Amplifier flow' : 'Amplifier'
                                 },
                       inplace=True
                      )

# plot_flow(data_Flowmeter)

data_UV = extract_data_UV_Date(path_Ulink)
data_UV_stat = extract_data_UV_stat_Date(path_Ulink)
data_UV_RMS = pd.DataFrame(data_UV_stat['RMS UV'])
data_UV_hide = data_UV_stat.drop(columns = ['Sigma UV', 'RMS UV'], inplace = False)

data_P = extract_data_P_Date(path_P)

# plot_UV(data_UV, data_UV_RMS, data_UV_hide, data_P)

data_IR = extract_data_IR_Date(path_Ulink)
data_IR_stat = extract_data_IR_stat_Date(path_Ulink)
data_IR_RMS = pd.DataFrame(data_IR_stat['RMS IR'])
data_IR_hide = data_IR_stat.drop(columns = ['Sigma IR', 'RMS IR'], inplace = False)

data_Puissance_depolar = extract_data_Puissance_depolar_Date(path_Ulink)

# plot_IR(data_IR, data_IR_RMS, data_IR_hide, data_Puissance_depolar)

data_NearField = extract_data_cameraNF_Date(path_NearField)
# plot_field(data_NearField, field='Near')

data_FarField = extract_data_cameraFF_Date(path_FarField)
# plot_field(data_FarField, field='Far')

dataframes = [data_Flowmeter_tmp[::sampling_rate], 
              data_Watlow[::sampling_rate], 
              data_Picolog[::2*sampling_rate], 
              data_Flowmeter[::sampling_rate], 
              data_UV[::sampling_rate], 
              data_UV_RMS[::(int(sampling_rate/12)+1)], 
              data_UV_hide[::(int(sampling_rate/12)+1)], 
              data_P[::sampling_rate], data_IR[::sampling_rate], 
              data_IR_RMS[::(int(sampling_rate/12)+1)], 
              data_IR_hide[::(int(sampling_rate/12)+1)], 
              data_Puissance_depolar[::sampling_rate], 
              data_NearField[::sampling_rate], 
              data_FarField[::sampling_rate]
             ]
# plot_xshared(dataframes)
###

###
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([html.H1('Endurance THEIA@500Hz from %s to %s' %(data_UV.index[1].strftime('%d-%m-%Y %H:%M:%S'), data_UV.index[-1].strftime('%d-%m-%Y %H:%M:%S'))),
                       dcc.Tabs(id="tabs-graph",
                                value='tab-1-graph',
                                children=[dcc.Tab(label='UV',
                                                  value='tab-1-graph'
                                                  ),
                                          dcc.Tab(label='IR',
                                                  value='tab-2-graph'
                                                  ),
                                          dcc.Tab(label='Temperature',
                                                  value='tab-3-graph'
                                                  ),
                                          dcc.Tab(label='Far Field',
                                                  value='tab-4-graph'
                                                  ),
                                          dcc.Tab(label='Near Field',
                                                  value='tab-5-graph'
                                                  ),
                                          dcc.Tab(label='Flow',
                                                  value='tab-6-graph'
                                                  ),
                                          dcc.Tab(label='ALL',
                                                  value='tab-7-graph'
                                                  )
                                          ]
                                ),
                       html.Div(id='tabs-content-graph')
                       ]
                      )

@app.callback(Output('tabs-content-graph', 'children'),
              Input('tabs-graph', 'value')
              )

def render_content(tab):
	if tab == 'tab-1-graph':
		return html.Div([html.H3('UV'),
				 dcc.Graph(id='graph-1-tabs-dcc',
					   figure = plot_UV(data_UV, data_UV_RMS, data_UV_hide, data_P)
					   )
				 ]
				)
	
	elif tab == 'tab-2-graph':
		return html.Div([html.H3('IR'),
				 dcc.Graph(id='graph-2-tabs-dcc',
					   figure = plot_IR(data_IR, data_IR_RMS, data_IR_hide, data_Puissance_depolar)
					   )
				 ]
				)
	
	elif tab == 'tab-3-graph':
		return html.Div([html.H3('Temperature'),
				 dcc.Graph(id='graph-3-tabs-dcc',
					   figure = plot_temperature(data_Flowmeter_tmp, data_Watlow, data_Picolog[::sampling_rate])
					   )
				 ]
				)
	
	elif tab == 'tab-4-graph':
		return html.Div([html.H3('Far Field'),
				 dcc.Graph(id='graph-4-tabs-dcc',
					   figure = plot_field(data_FarField, field='Far')
					   )
				 ]
				)
	
	elif tab == 'tab-5-graph':
		return html.Div([html.H3('Near Field'),
				 dcc.Graph(id='graph-5-tabs-dcc',
					   figure = plot_field(data_FarField, field='Near')
					   )
				 ]
				)
	
	elif tab == 'tab-6-graph':
		return html.Div([html.H3('Flow'),
				 dcc.Graph(id='graph-6-tabs-dcc',
					   figure = plot_flow(data_Flowmeter)
					   )
				 ]
				)
	
	elif tab == 'tab-7-graph':
		return html.Div([html.H3('Flow'),
				 dcc.Graph(id='graph-7-tabs-dcc',
					   figure = plot_xshared(dataframes)
					   )
				 ]
				)

if __name__ == '__main__':
    app.run_server(debug=True)
###
