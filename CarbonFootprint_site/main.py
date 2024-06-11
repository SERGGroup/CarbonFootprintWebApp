from .python_code.support.constants import EXCEL_DIR, PROFILE_DIR, MONITORING_DIR
from flask import Flask, render_template, request, send_file
from .python_code.form_definition_class import MainFormClass
from .python_code.db_handler import DatabaseHandler
import secrets
import os


def create_app(enable_profiler=False, enable_dashboard=False, store_replies=False):

    app = Flask(__name__)

    if enable_dashboard:

        import flask_monitoringdashboard as dashboard
        dashboard.config.init_from(file=os.path.join(MONITORING_DIR, "config.cfg"))

    if store_replies:

        db_handler = DatabaseHandler(app)

    app.config["SECRET_KEY"] = secrets.token_urlsafe(16)

    @app.route('/', methods=['POST', 'GET'])
    def home():

        main_class = MainFormClass(is_italian=True)
        curr_form = main_class.form_class(request.form)

        if request.method == 'POST' and curr_form.validate():

            main_class.append_data(curr_form)
            main_class.evaluate_co2_cost()

            if store_replies:

                db_handler.append_to_db(main_class)

            return render_template('Ita/results.html', main_class=main_class)

        return render_template('Ita/Supporto/form_layout.html', form=curr_form, main_class=main_class)

    @app.route('/eng', methods=['POST', 'GET'])
    def home_eng():

        main_class = MainFormClass(is_italian=False)
        curr_form = main_class.form_class(request.form)

        if request.method == 'POST' and curr_form.validate():

            main_class.append_data(curr_form)
            main_class.evaluate_co2_cost()

            if store_replies:
                db_handler.append_to_db(main_class)

            return render_template('Eng/results.html', main_class=main_class)

        return render_template('Eng/Support/form_layout.html', form=curr_form, main_class=main_class)

    @app.route('/explanation')
    def explanation():
        return render_template('Ita/how-it-works.html')

    @app.route('/explanation_eng')
    def explanation_eng():
        return render_template('Eng/how-it-works.html')

    @app.route('/download')
    def download():

        # Percorso del file Excel da scaricare
        file_path = ('results_download_ita.xlsx')

        # Invia il file Excel al client come allegato
        return send_file(file_path, as_attachment=True)

    @app.route('/download_eng')
    def download_eng():

        # Percorso del file Excel da scaricare
        file_path = ('results_download_eng.xlsx')

        # Invia il file Excel al client come allegato
        return send_file(file_path, as_attachment=True)

    @app.route('/references')
    def download_ref():
        file_path = os.path.join(EXCEL_DIR, 'References_ita.xlsx')
        return send_file(file_path, as_attachment=True)

    @app.route('/references_eng')
    def download_ref_eng():
        file_path = os.path.join(EXCEL_DIR, 'references_eng.xlsx')
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

    if enable_dashboard:

        dashboard.config.enable_logging = True
        dashboard.bind(app)

    return app
