from StevenEx import app
from StevenEx.routes import live_price_editor


if __name__ == '__main__':
    live_price_editor()
    
    # db.create_all()
    app.run('127.0.0.1', 8080, debug=True)
# TODO: libraries in all files are updated in requirements.txt
