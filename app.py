from App import create_app

app = create_app()
print(f"App root: {app.root_path}")
if __name__ == '__main__':
    app.run(host='0.0.0.0')


