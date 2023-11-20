#here are defined all functions usefull into carbon.py
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

def crea_grafici(lista_df):
    #questa parte fino al cancelletto serve per riscrivere il df in modo che il programma riesca a fare il grafico
    lista_tot=calcola_tot(lista_df)[0:4] #calcola i totali di ogni macroarea
    perc=0.04 #percentuale altro
    df_dieta=lista_df[0]
    chiavi_dieta=list(df_dieta.columns) #prendo i nomi delle colonne
    valori_dieta=[]
    indici=[]
    altro=0
    for i in chiavi_dieta:
        if df_dieta.at[0,i]/lista_tot[0]<perc: #ciclo che controlla che il contributo sia superiore al 7% del totale, sennò viene assegnato alla categoria altro
            altro+=df_dieta.at[0,i]
        else:
         valori_dieta.append(df_dieta.at[0,i]) #prende ogni elemento nel df riga 0 colonna i(nome colonna)
         indici.append(i)
    valori_dieta.append(altro)
    df_dieta_grafico=pd.DataFrame({'dieta':valori_dieta},index=indici+['others'])
    #
    graf_dieta=df_dieta_grafico.plot(kind='pie',y='dieta',label='',legend='',figsize=(5,5,))
    graf_dieta.figure.savefig('./static/images/grafico_dieta.png') #funzione per salvare il grafico nella cartella
    
    df_trasporti=lista_df[1]
    chiavi_trasporti=list(df_trasporti.columns) #prendo i nomi delle colonne
    valori=[]
    indici=[]
    altro=0
    for i in chiavi_trasporti:
        if df_trasporti.at[0,i]/lista_tot[1]<perc: #ciclo che controlla che il contributo sia superiore al 7% del totale, sennò viene assegnato alla categoria altro
            altro+=df_trasporti.at[0,i]
        else:
            valori.append(df_trasporti.at[0,i]) #prende ogni elemento nel df riga 0 colonna i(nome colonna)
            indici.append(i)
    valori.append(altro)
    indici.append('others')
    df_trasporti_grafico=pd.DataFrame({'trasporti':valori},index=indici)
    graf_trasporti=df_trasporti_grafico.plot(kind='pie',y='trasporti',label='',legend='', figsize=(5,5,))
    graf_trasporti.figure.savefig('./static/images/grafico_trasporti.png')
    
    df_casa=lista_df[2]
    chiavi_casa=list(df_casa.columns) #prendo i nomi delle colonne
    valori=[]
    indici=[]
    altro=0
    for i in chiavi_casa:
        if df_casa.at[0,i]/lista_tot[2]<perc: #ciclo che controlla che il contributo sia superiore al 7% del totale, sennò viene assegnato alla categoria altro
            altro+=df_casa.at[0,i]
        else:
            valori.append(df_casa.at[0,i]) #prende ogni elemento nel df riga 0 colonna i(nome colonna)
            indici.append(i)
    valori.append(altro)
    indici.append('others')
    df_casa_grafico=pd.DataFrame({'casa':valori},index=indici)
    graf_casa=df_casa_grafico.plot(kind='pie',y='casa',label='',legend='',figsize=(5,5,))
    graf_casa.figure.savefig('./static/images/grafico_casa.png')
    
    df_abbigliamento=lista_df[3]
    chiavi_abbigliamento=list(df_abbigliamento.columns) #prendo i nomi delle colonne
    valori=[]
    indici=[]
    altro=0
    for i in chiavi_abbigliamento:
        if df_abbigliamento.at[0,i]/lista_tot[3]<perc: #ciclo che controlla che il contributo sia superiore al 7% del totale, sennò viene assegnato alla categoria altro
            altro+=df_abbigliamento.at[0,i]
        else:
            valori.append(df_abbigliamento.at[0,i]) #prende ogni elemento nel df riga 0 colonna i(nome colonna)
            indici.append(i)
    valori.append(altro)
    indici.append('others')
    df_abbigliamento_grafico=pd.DataFrame({'abbigliamento':valori},index=indici)
    graf_abbigliamento=df_abbigliamento_grafico.plot(kind='pie',y='abbigliamento',label='',legend='',figsize=(5,5,))
    graf_abbigliamento.figure.savefig('./static/images/grafico_abbigliamento.png')
    
    df_graf_tot=pd.DataFrame({'riepilogo':lista_tot},index=['Diet','Transport','Home','Clothes']) #prende la lista sopra e crea df
    graf_tot=df_graf_tot.plot(kind='pie',y='riepilogo',label='',legend='',figsize=(5,5,))
    graf_tot.figure.savefig('./static/images/grafico_totale.png')
    
    #costruzione del grafico a barre che confronta la cf personale con le medie mondiali
    impact_capita={'Europe':7.11*1000,
                   'Asia':4.62*1000,
                   'Italy':5.55*1000,
                   'Bangladesh': 0.55*1000,
                   'France': 4.74*1000,
                   'Germany': 8.09*1000,
                   'Spain': 4.92*1000,
                   'United States':14.86*1000,
                   'World':4.69*1000,
                   }
    impact_capita['You']=sum(lista_tot)*365
    grafico_comp=pd.DataFrame(impact_capita, index=[0])
    grafico_comparativa=grafico_comp.plot(kind='bar',figsize=(6,6,))
    plt.ylabel('kgCO2 per capita/year')
    grafico_comparativa.figure.savefig('./static/images/grafico_comparativa.png')
    
    
    return

def controlla_ingressi(ingressi): #nota bene che i dizionari hanno gli stessi indici
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
	count=1
	file=openpyxl.load_workbook('template_results.xlsx')
	sheet=file['Sheet3']
	chiavi=list(prodotti.keys())
	for i in chiavi:
		tcount=str(count)
		sheet['A'+tcount]=i
		sheet['B'+tcount]=prodotti[i]
		count=count+1
	file.save('results_download.xlsx')
	return