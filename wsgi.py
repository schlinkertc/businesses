"""Application entry point"""

# "wsgi.py is always our app entry point in this app pattern. This is standard practice"

from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)