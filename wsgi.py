import sys
sys.path.insert(0, 'C:\\inetpub\\wwwroot\\carbon_app\\CarbonFootprintWebApp')
from CarbonFootprint_site.main import create_app

curr_app = create_app(enable_dashboard=True)


