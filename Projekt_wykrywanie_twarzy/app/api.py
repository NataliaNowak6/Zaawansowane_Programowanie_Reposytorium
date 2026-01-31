from fastapi import APIRouter, UploadFile
from app.rabbitmq import publish_task
from app.storage import save_status
import uuid

from Zaawansowane_Programowanie_Reposytorium.Projekt_wykrywanie_twarzy import get_status

router = APIRouter()

@router.post("/analyze/upload")
def upload_image(file: UploadFile):
    task_id = str(uuid.uuid4())
    path = f"uploads/{task_id}.jpg"

    with open(path, "wb") as f:
        f.write(file.file.read())

    save_status(task_id, "pending")

    publish_task({
        "task_id": task_id,
        "source": path,
        "type": "local"
    })

    return {"task_id": task_id}

@router.get("/tasks/{task_id}")
def get_task(task_id: str):
    return get_status(task_id)