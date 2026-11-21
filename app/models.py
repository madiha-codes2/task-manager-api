from app.database import get_connection

def create_tables():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()

# Insering tasks
def insert_task(title, description, completed):

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tasks (title, description, completed)
        VALUES (?, ?, ?)
        """,
        (title, description, completed)
    )

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return task_id

# Retrieve all tasks
def get_all_tasks():

    connection = get_connection()

    cursor = connection.execute(
        "SELECT * FROM tasks"
    )

    tasks = cursor.fetchall()

    connection.close()

    return [dict(task) for task in tasks]

# Retrieve a task by ID
def get_task_by_id(task_id):

    connection = get_connection()

    cursor = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    connection.close()

    if task is None:
        return None

    return dict(task)

# Update task in database
def update_task(task_id, title, description, completed):

    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, completed = ?
        WHERE id = ?
        """,
        (title, description, int(completed), task_id)
    )

    connection.commit()

    rows_updated = cursor.rowcount

    connection.close()

    return rows_updated

# Delete a task from database
def delete_task(task_id):

    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    rows_deleted = cursor.rowcount

    connection.close()

    return rows_deleted