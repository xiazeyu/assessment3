from app import create_app

if __name__ == '__main__':
    napp = create_app()
    napp.run(debug=False, host='0.0.0.0')
    # napp.run(debug=True, host='0.0.0.0')
