from .function import calcola_tot, crea_grafici, controlla_ingressi,dividi_df, calcola_output, write_results
from .constants import MAIN_DIR,  IMAGES_DIR, get_coefficients
from flask import Flask, render_template, request, send_file
import pandas as pd
import os


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():

        if os.path.isfile('output.csv'):
            os.remove('output.csv')

        return render_template('index.html')

    @app.route('/home')
    def home1():
        return render_template('index.html')

    @app.route('/results', methods=['POST', 'GET'])
    def result():

        if request.method == 'POST':

            # rende un dizionario con delle liste contenente tutte le variabili create nell'html
            html_data = request.form
            coefficients = get_coefficients(request.form)
            n_correct_inputs = controlla_ingressi(html_data)

            if n_correct_inputs == 1:

                # controlla che sia stato possibile trasformare tutti i dati in float,
                # altrimenti i dati in ingresso erano sbagliati

                return """
                    
                    The input data are not correct. 
                    Remember that you can not insert string and float number must use dot
                    
                """

            prodotto = calcola_output(n_correct_inputs, coefficients)

            # creo data Frame dei valori co2 per ogni categoria
            df_totale = pd.DataFrame(prodotto, index=[0])
            lista_df = dividi_df(df_totale)

            # lista dei totali della co2 per macroarea
            output = calcola_tot(lista_df)

            # questa funzione crea il file excel/crea il file partendo dal template già caricato in cartella
            write_results(prodotto)

            # questa funzione genera i grafici da mostrare con i risultati
            crea_grafici(lista_df)

            # salvo su un file csv i dati output
            output_df = pd.DataFrame([output], columns=['dieta', 'trasporti', 'casa', 'abbigliamento', 'totale'])

            # salvo il database
            output_df.to_csv('output.csv')

            return render_template('results.html', output=output)

        elif os.path.isfile('output.csv'):

            output = list()
            output_df = pd.read_csv('output.csv', index_col=0)

            output.append(output_df.at[0, 'dieta'])
            output.append(output_df.at[0, 'trasporti'])
            output.append(output_df.at[0, 'casa'])
            output.append(output_df.at[0, 'abbigliamento'])
            output.append(output_df.at[0, 'totale'])

            return render_template('results.html', output=output)

        else:

            return 'First insert your data and calculate your carbon footprint!'

    @app.route('/download')
    def download():

        # Percorso del file Excel da scaricare
        file_path = os.path.join(MAIN_DIR, 'results_download.xlsx')

        # Invia il file Excel al client come allegato
        return send_file(file_path, as_attachment=True)

    return app


if __name__ == '__main__':

    curr_app = create_app()
    curr_app.run(debug=True)

    

