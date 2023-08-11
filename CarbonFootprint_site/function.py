from .constants import MAIN_DIR,  IMAGES_DIR
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import functools
import openpyxl
import os


DEFAULT_OTHER_LIMIT = 0.04


def crea_grafici(lista_df):

    # Questa parte fino al cancelletto serve per riscrivere
    # il df in modo che il programma riesca a fare il grafico

    # Calcola i totali di ogni macroarea
    lista_tot = calcola_tot(lista_df)[0:4]

    # Percentuale sotto la quale la categoria
    # viene contrassegnata come 'altro'
    perc = 0.04

    # Create the category graph
    plot_names = ["dieta", "trasporti", "casa", "abbigliamento"]

    for i in range(len(plot_names)):

        __plot_data_frame_category(lista_df[i], plot_names[i], perc=perc)

    # Create the overall graph
    __plot_data_frame_overall(lista_tot, 'totale')

    #costruzione del grafico a barre che confronta la cf personale con le medie mondiali
    __plot_data_frame_comparison(lista_tot, 'comparativa')

def __check_plot_creation(function_in):

    @functools.wraps(function_in)
    def decorated_func(df_in, df_name, perc=DEFAULT_OTHER_LIMIT):

        try:

            function_in(df_in, df_name, perc=perc)

        except:

            graph_path = __get_graph_path(df_name)

            if os.path.isfile(graph_path):
                os.remove(graph_path)

    return decorated_func

@__check_plot_creation
def __plot_data_frame_category(df_in, df_name, perc=DEFAULT_OTHER_LIMIT):

    # get the column indices
    keys = list(df_in.columns)

    values_list = list()
    index_list = list()
    other = 0

    for i in keys:

        # If the category does not reach the 'perc' level of impact (default is 4%)
        # it is automatically moved in the 'other' category

        if df_in.at[0, i] / np.array(df_in).sum() < perc:

            other += df_in.at[0, i]

        else:

            # If its impact is > than 'perc', the program insert the data in the lists
            values_list.append(df_in.at[0, i])
            index_list.append(i)

    if other > 0:

        values_list.append(other)
        index_list.append('others')

    # Plot and Save graph
    df_graph = pd.DataFrame({df_name: values_list}, index=index_list)
    graph = df_graph.plot(kind='pie', y=df_name, label='', legend='', figsize=(5, 5,))
    graph.figure.savefig(__get_graph_path(df_name))

@__check_plot_creation
def __plot_data_frame_overall(lista_tot, df_name, perc):

    df_graf_tot = pd.DataFrame({

        df_name: lista_tot

    },

        index=[

            'Diet',
            'Transport',
            'Home',
            'Clothes'

        ]

    )

    graf_tot = df_graf_tot.plot(kind='pie', y=df_name, label='', legend='', figsize=(5, 5,))
    graf_tot.figure.savefig(__get_graph_path(df_name))

@__check_plot_creation
def __plot_data_frame_comparison(lista_tot, df_name, perc):

    impact_capita = {

        'Europe': 7.11 * 1000, 'Asia': 4.62 * 1000, 'Italy': 5.55 * 1000, 'Bangladesh': 0.55 * 1000,
        'France': 4.74 * 1000, 'Germany': 8.09 * 1000, 'Spain': 4.92 * 1000, 'United States': 14.86 * 1000,
        'World': 4.69 * 1000, 'You': sum(lista_tot) * 365

    }

    grafico_comp = pd.DataFrame(impact_capita, index=[0])
    grafico_comparativa = grafico_comp.plot(kind='bar', figsize=(6, 6,))
    plt.ylabel('kgCO2 per capita/year')

    grafico_comparativa.figure.savefig(__get_graph_path(df_name))

def __get_graph_path(df_name):

    return os.path.join(IMAGES_DIR, 'grafico_{}.png'.format(df_name))

def controlla_ingressi(ingressi):

    #nota bene che i dizionari hanno gli stessi indici
    #funzione che riscrive gli ingressi in un nuovo dizionario e controlla che i dati inseriti siano corretti
    #se i dati inseriti non sono corretti rende 1
    #se gli input sono corretti rende il dizionario 'input_corretti'
    #devono essere 

    chiavi=list(ingressi.keys()) #lista delle chiavi del dizionario
    input_corretti={}

    for i in chiavi:

        if ingressi[i]=='':

            quantita=0.0

        else:

            try:

                quantita=float(ingressi[i])

            except ValueError: #se la funzione float non è applicabile

                return 1

        input_corretti[i]=quantita #cosi converto gli elementi vuoti in zeri e tutti in float

    return input_corretti

def calcola_output(ingressi, coefficienti): 
    chiavi=list(coefficienti.keys())    
    prodotto={}    
    for i in chiavi:
        prodotto[i]=ingressi[i]*coefficienti[i]
    return prodotto 

def dividi_df(df_totale):
    #questa funzione prende come ingresso il df_totale, quindi il df con tutti gli elementi in un unico elemento e li divide in sottogruppi
    
    chiavi=list(df_totale.columns) #crea una lista con i nomi delle colonne
    diz_dieta={}
    diz_trasporti={}
    diz_casa={}
    diz_abbigliamento={}
    trasporti=False
    casa=False
    abbigliamento=False
    
    for i in chiavi : #cosi i assume tutti i valori delle chiavi
        if i=='domestic_flight':
            trasporti=True
        elif i=='refrigerator':
            casa=True
        elif i=='cotton_shirt':
            abbigliamento=True
        
        if (not trasporti and not casa and not abbigliamento):
            diz_dieta[i]=[df_totale.at[0,i]]
        elif (trasporti and not casa and not abbigliamento):
            diz_trasporti[i]=[df_totale.at[0,i]]
        if (trasporti and casa and not abbigliamento):
            diz_casa[i]=[df_totale.at[0,i]]
        if (trasporti and casa and abbigliamento):
            diz_abbigliamento[i]=[df_totale.at[0,i]]
              
    df_dieta=pd.DataFrame(diz_dieta)#qui creo il dataframe usando il dizionario e lo assegno
    df_trasporti=pd.DataFrame(diz_trasporti)
    df_casa=pd.DataFrame(diz_casa)
    df_abbigliamento=pd.DataFrame(diz_abbigliamento)
    
    return [df_dieta,df_trasporti,df_casa,df_abbigliamento]#rende una lista dei dataframe divisi

def calcola_tot(lista_df):
     #funzione che prende i dataframe divisi di ogni macroarea in una lista,
     #e per ogni  macroarea restituisce la co2 totale

     df_dieta=lista_df[0]
     df_trasporti=lista_df[1]
     df_casa=lista_df[2]
     df_abbigliamento=lista_df[3]
     
     chiavi_dieta=list(df_dieta.columns) #estraggo i nomi delle colonne e creo lista
     tot_dieta=0
     for i in chiavi_dieta:
         tot_dieta+=df_dieta.at[0,i]
     
     chiavi_trasporti=list(df_trasporti.columns)
     tot_trasporti=0
     for i in chiavi_trasporti:
         tot_trasporti+=df_trasporti.at[0,i]
     
     chiavi_casa=list(df_casa.columns)
     tot_casa=0
     for i in chiavi_casa:
         tot_casa+=df_casa.at[0,i]
    
     chiavi_abbigliamento=list(df_abbigliamento.columns)
     tot_abbigliamento=0
     for i in chiavi_abbigliamento:
         tot_abbigliamento+=df_abbigliamento.at[0,i]
     tot_dieta=round(tot_dieta,2)
     tot_trasporti=round(tot_trasporti,2)
     tot_casa=round(tot_casa,2)
     tot_abbigliamento=round(tot_abbigliamento,2)
     tot=round(tot_dieta+tot_trasporti+tot_casa+tot_abbigliamento,2)
     
     return [tot_dieta,tot_trasporti,tot_casa,tot_abbigliamento,tot]

def write_results(prodotti):

    count = 1
    file = openpyxl.load_workbook('template_results.xlsx')
    sheet = file['Sheet3']
    chiavi = list(prodotti.keys())

    for i in chiavi:

        tcount = str(count)
        sheet['A'+tcount] = i
        sheet['B'+tcount] = prodotti[i]
        count = count + 1

    file.save('results_download.xlsx')