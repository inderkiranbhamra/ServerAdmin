from app import app, create_table

if __name__ == '__main__':
    # Create the table when the app starts
    create_table()
    app.run(debug=True)