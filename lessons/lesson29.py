# lessons/lesson29.py
import utils

utils.show_base_name(__file__, True)
def main():
    """
    This lesson guides you through creating a simple web application using FastAPI.
    Since a web server needs to run continuously, this lesson provides instructions
    instead of running the app directly.
    """
    print("--- Lesson 29: Simple Web App with FastAPI ---")

    # 1. What is FastAPI?
    # FastAPI is a modern, high-performance web framework for building APIs with Python.
    # Key features:
    # - Fast: Very high performance, on par with NodeJS and Go.
    # - Fast to code: Increases development speed significantly.
    # - Fewer bugs: Reduces human-induced errors.
    # - Automatic docs: Interactive API documentation (Swagger UI and ReDoc).

    print("\n--- 1. Understanding FastAPI ---")
    print("This lesson will show you how to create a simple web app that responds to HTTP requests.")
    print("---" * 20)

    # 2. Setup and Installation
    # To use FastAPI, you need to install it and a web server like Uvicorn.

    print("\n--- 2. Setup and Installation ---")
    print("Open your terminal and make sure your project's virtual environment is activated.")
    print("Then run the following command to install the necessary packages:")
    print("  pip install fastapi \"uvicorn[standard]\"")
    print("\nNote: If you have issues, you can install them separately:")
    print("  pip install fastapi")
    print("  pip install uvicorn")
    print("---" * 20)

    # 3. Create the Web App File
    # You need to create a new Python file for your web application.

    print("\n--- 3. Create the Web App File ---")
    print("In the root of your 'pythonEx' project, create a new file named 'web_app.py'.")
    print("Copy the following code into 'web_app.py':")

    web_app_code = """
# web_app.py
from fastapi import FastAPI

# 1. Create a FastAPI instance
app = FastAPI()

# In-memory "database"
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 2. Define a path operation decorator (a "route")
@app.get("/")
async def read_root():
    # This function will be executed for GET requests to the root URL (e.g., http://127.0.0.1:8000)
    return {"message": "Hello, World! Welcome to your first FastAPI app."}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    # Route with query parameters: http://127.0.0.1:8000/items/?skip=0&limit=2
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    # Route with a path parameter `item_id` and an optional query parameter `q`.
    # Example: http://127.0.0.1:8000/items/5?q=somequery
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
"""
    # Use indentation to make the code block stand out
    indented_code = "\n".join([f"  {line}" for line in web_app_code.strip().split("\n")])
    print(indented_code)
    print("---" * 20)

    # 4. Run the Web Server
    # Now, you can run your web application using Uvicorn.

    print("\n--- 4. Run the Web Server ---")
    print("In your terminal (from the 'pythonEx' root directory), run the following command:")
    print("  uvicorn web_app:app --reload")
    print("\nExplanation:")
    print("  - 'web_app': The file 'web_app.py'.")
    print("  - 'app': The FastAPI instance created inside 'web_app.py' (`app = FastAPI()`).")
    print("  - '--reload': Makes the server restart after code changes.")
    print("\nYou should see output like: 'Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)'")
    print("---" * 20)

    # 5. Interact with Your App
    # Once the server is running, you can interact with your new web app.

    print("\n--- 5. Interact with Your App ---")
    print("Open your web browser and go to the following URLs:")
    print("  - http://127.0.0.1:8000")
    print("  - http://127.0.0.1:8000/items/")
    print("  - http://127.0.0.1:8000/items/5?q=somequery")
    print("\nFastAPI also automatically generates interactive API documentation.")
    print("Visit one of these URLs to see it:")
    print("  - http://127.0.0.1:8000/docs  (Swagger UI)")
    print("  - http://127.0.0.1:8000/redoc (ReDoc)")
    print("---" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)