from CarbonFootprint_site.main import create_app

if __name__ == '__main__':

    curr_app = create_app(enable_profiler=True)
    curr_app.run()
