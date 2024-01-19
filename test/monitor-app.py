from CarbonFootprint_site.main import create_app
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

if __name__ == '__main__':

    port = 5000
    use_localhost = True
    curr_app = create_app(enable_dashboard=True, store_replies=True)

    if use_localhost:
        curr_app.run(port=port, debug=False)

    else:
        curr_app.run(host=IPAddr, port=port, debug=False)
