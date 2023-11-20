from flask import Flask, render_template, request, send_file
from python_code.form_class import RegistrationForm
from python_code.function import calcola_tot, crea_grafici, controlla_ingressi,dividi_df, calcola_output, write_results
import pandas as pd
import os
app = Flask(__name__)


@app.route('/')
def home():

    form = RegistrationForm(request.form)
    return render_template('form_layout.html', form=form)

    # return render_template('form_layout.html')

@app.route('/results',methods=['POST', 'GET'])
def result():

    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

          # dati_html = request.form #rende un dizionario con delle liste contenente tutte le variabili create nell'html
          # coefficienti={
          #     #alimentazione
          #     'beef_herd':68.25/7/1000,#kgCO2/kg
          #     'lumb_mutton':24/7/1000,#kgCO2/kg
          #     'cheese':21/7/1000,#kgCO2/kg
          #     'beef_dairy':44.75/7/1000,#kgCO2/kg
          #     'chocolate':19/7/1000,#kgCO2/kg
          #     'coffee':0.05953/7,#kgCO2/cup
          #     'prawns_farmed':12/7/1000,#kgCO2/kg
          #     'pig_meat':7.9/7/1000,#kgCO2/kg
          #     'wheat_rye':1.4/7/1000,#kgCO2/kg
          #     'tomatoes':1.4/7/1000,#kgCO2/kg
          #     'maize':1/7/1000,#kgCO2/kg
          #     'peas':0.9/7/1000,#kgCO2/kg
          #     'soy_milk':0.9/7/1000,#kgCO2/kg
          #     'poultry_meat':10.4/7/1000,#kgCO2/kg
          #     'olive_oil':6/7/1000,#kgCO2/kg
          #     'fish_farmed':5/7/1000,#kgCO2/kg
          #     'pasta':1.12/7/1000, #kgCO2/kg
          #     'bread':0.731/7/1000, #kgCO2/kg
          #     'eggs':4.5/20/7,#kgCO2/kg /20 perchè un uovo è circa 50g
          #     'rice':4/7/1000,#kgCO2/kg
          #     'fish_wildcatch':3/7/1000,#kgCO2/kg
          #     'milk':3/7/1000,#kgCO2/kg
          #     'cane_sugar':3/7/1000,#kgCO2/kg
          #     'groundnuts':2.5/7/1000,#kgCO2/kg
          #     'bananas':0.7/7/5,#kgCO2/kg
          #     'root_vegetables':0.4/7/1000,#kgCO2/kg
          #     'apples':0.4/7/4,#kgCO2/kg- una mela pesa 250g
          #     'citrus_fruit':0.3/7/4,#kgCO2/kg
          #     'nuts':0.3/7/1000,#kgCO2/kg
          #     #trasporti
          #     'domestic_flight':0.255/365,
          #     'mediumcar_petrol':0.269/7/float(request.form['passengers_petrol']),
          #     'mediumcar_diesel':0.229/7/float(request.form['passengers_diesel']),
          #     'short_flight':0.156/365,
          #     'long_flight':0.150/365,
          #     'bus':0.093/7,
          #     'motorcycle':0.0968/7/float(request.form['passengers_moto']),
          #     'electric_vehicle':0.12/7/float(request.form['passengers_electric']),
          #     'national_rail':0.041/7,
          #     'ferry':0.019/7,
          #     'eurostar':0.006/7,
          #     #casa
          #     'refrigerator':0.14/float(request.form['number_family']), #kgco2/day
          #     'food_cooking':0.05048/float(request.form['number_family']), #kgco2/meal
          #     'oven':0.7091/7/float(request.form['number_family']), #kgco2/meal
          #     'washing_machine':0.6283/7/float(request.form['number_family']), #kgco2/cycle
          #     'shower':0.6057/7,#kgco2/shower
          #     'laptop':100/365,
          #     'smartphone':120/365,
          #     'heating':0.19*float(request.form['efficiency_class'])/float(request.form['number_family'])/365, #from user it returns directly the number of co2
          #     'cooling':0.2605*float(request.form['cooling_power'])*float(request.form['hot_days'])/float(request.form['number_family'])/365,
          #     #abbigliamento
          #     'cotton_shirt':20*0.150/365, #kgco2/unit
          #     'cotton_sweatjacket':20*0.55/365, #kgco2/unit
          #     'acrylic_jacket':35.7*0.55/365, #kgco2/unit
          #     'woolen_sweater':13.12/365, #kgco2/unit
          #     'polyester_shirt':27.2*0.15/365, #kgco2/unit
          #     'jeans':33.4/365 , #kgco2/unit
          #     }
          # ingressi_corretti=controlla_ingressi(dati_html)
          # if ingressi_corretti==1: #controlla che sia stato possibile trasformare tutti i dati in float, altrimenti i dati in ingresso erano sbagliati
          #     return 'The input data are not correct. Remember that you can not insert string and float number must use dot'
          # prodotto=calcola_output(ingressi_corretti, coefficienti)
          # df_totale=pd.DataFrame(prodotto,index=[0])#creo data Frame dei valori co2 per ogni categoria
          # lista_df=dividi_df(df_totale)
          # output=calcola_tot(lista_df) #lista dei totali della co2 per macroarea
          # write_results(prodotto) #questa funzione crea il file excel/crea il file partendo dal template già caricato in cartella
          # try:
          #     crea_grafici(lista_df) #funzione che crea grafici e li salva sulla cartella static
          # except:#se non riesce a fare la funzione crea_grafici() cancella i grafici se esistono già
          #    if os.path.isfile('./static/images/grafico_abbigliamento.png'):
          #        os.remove('./static/images/grafico_abbigliamento.png')
          #    if os.path.isfile('./static/images/grafico_trasporti.png'):
          #        os.remove('./static/images/grafico_trasporti.png')
          #    if os.path.isfile('./static/images/grafico_dieta.png'):
          #        os.remove('./static/images/grafico_dieta.png')
          #    if os.path.isfile('./static/images/grafico_casa.png'):
          #        os.remove('./static/images/grafico_casa.png')
          #    if os.path.isfile('./static/images/grafico_totale.png'):
          #        os.remove('./static/images/grafico_totale.png')
          #    if os.path.isfile('./static/images/grafico_comparativa.png'):
          #       os.remove('./static/images/grafico_comparativa.png')
          #

        output = [30, 150, 100, 20, 300]
        return render_template('results.html', output=output)

    else:

        return render_template('form_layout.html', form=form)
        return 'First insert your data and calculate your carbon footprint!'
        
@app.route('/download')
def download():
    
    # Percorso del file Excel da scaricare
    file_path = 'results_download.xlsx'

    # Invia il file Excel al client come allegato
    return send_file(file_path, as_attachment=True)

@app.route('/explanation')
def explanation():
    return render_template('how-it-works.html')

@app.route('/references')
def download_ref():
    
    # Percorso del file Excel da scaricare
    file_path = 'references_download.xlsx'

    # Invia il file Excel al client come allegato
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':

    app.run(debug=True)
