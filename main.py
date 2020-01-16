from fastapi import FastAPI
from todo import router as todo_router

app = FastAPI(
        title="Test FastAPI",
        description="Performance validation"
)


@app.get("/")
def main():
    """
    Root view, returns {"hello": "world"}
    """
    return {"hello": "world"}

app.include_router(todo_router, prefix='/todo', tags=["todo"])
