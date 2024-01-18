from CarbonFootprint_site.carbon import create_app
import socket


if __name__ == '__main__':

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    curr_app = create_app(enable_dashboard=False)
    curr_app.run(host=IPAddr, port=5000, debug=False)


