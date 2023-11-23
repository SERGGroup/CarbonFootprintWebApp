from .python_code.support.constants import EXCEL_DIR, PROFILE_DIR, MAIN_DIR
from flask import Flask, render_template, request, send_file
from .python_code.form_definition_class import MainFormClass
import flask_monitoringdashboard as dashboard
import os

def create_app(enable_profiler=False, enable_dashboard=False):

    app = Flask(__name__)

    if enable_dashboard:

        dashboard.config.init_from(file=os.path.join(MAIN_DIR, "config.cfg"))
        dashboard.bind(app)

    @app.route('/', methods=['POST', 'GET'])
    def home():

        main_class = MainFormClass()
        curr_form = main_class.form_class(request.form)

        if request.method == 'POST' and curr_form.validate():

            main_class.evaluate_results(curr_form)
            return render_template('results.html', main_class=main_class)

        return render_template('support/form_layout.html', form=curr_form, main_class=main_class)

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

        file_path = os.path.join(EXCEL_DIR, 'references_download.xlsx')
        return send_file(file_path, as_attachment=True)

    if enable_profiler:

        from werkzeug.middleware.profiler import ProfilerMiddleware

        app.debug = True
        app.config["PROFILER"] = True
        app.config["PROFILE"] = True
        app.wsgi_app = ProfilerMiddleware(

            app.wsgi_app,
            restrictions=[30],
            profile_dir=PROFILE_DIR,
            filename_format="{method}-{path}-{time:.0f}-{elapsed:.0f}ms.prof",

        )

    return app
