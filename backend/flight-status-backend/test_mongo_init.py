from app import create_app

app = create_app()

with app.app_context():
    from app import mongo
    print("MongoDB Initialized:", mongo is not None)
