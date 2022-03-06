from app import app

if __name__ == '__main__':
    app.static_folder = 'static'
    app.run()