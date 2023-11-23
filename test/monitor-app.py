from CarbonFootprint_site.carbon import create_app


if __name__ == '__main__':

    curr_app = create_app(enable_dashboard=True)
    curr_app.run(debug=True)
