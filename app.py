from app import app


def main():
    app.static_folder = 'static'
    app.run()


if __name__ == '__main__':
    main()