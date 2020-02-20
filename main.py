from fastapi import FastAPI
from todo import router as todo_router
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, log_level ="info")