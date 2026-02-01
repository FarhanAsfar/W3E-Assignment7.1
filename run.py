from task_manager import create_app
from task_manager.extensions import db

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
