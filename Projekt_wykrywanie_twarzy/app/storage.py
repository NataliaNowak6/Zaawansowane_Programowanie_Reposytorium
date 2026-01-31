tasks = {}

def save_status(task_id, status):
    tasks[task_id] = {"status": status}

def save_result(task_id, count, image):
    tasks[task_id].update({
        "status": "done",
        "people_count": count,
        "result_image": image
    })

def get_status(task_id):
    return tasks.get(task_id, {"status": "not_found"})