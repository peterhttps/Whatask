from rich.console import Console
from rich.table import Table
from datetime import datetime
from .database import get_db_cursor

console = Console()

def task_exists(task_id):
    """ Check if a task exists in the database. """
    with get_db_cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE id = %s", (task_id,))
        return cursor.fetchone()[0] > 0

def add_task(title, description):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO tasks (title, description, is_completed, created_at) VALUES (%s, %s, %s, %s) RETURNING id",
            (title, description, False, datetime.now())
        )
        task_id = cursor.fetchone()[0]
        console.print(f"[green]Task added with ID: {task_id}[/green]")

def delete_task(task_id):
    if not task_exists(task_id):
        console.print(f"[red]Task {task_id} does not exist![/red]")
        return
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        console.print(f"[green]Task {task_id} deleted.[/green]")

def list_tasks(show_completed=False):
    with get_db_cursor() as cursor:
        query = "SELECT id, title, description, is_completed, created_at, completed_at FROM tasks"
        query += " WHERE is_completed = TRUE" if show_completed else " WHERE is_completed = FALSE"
        cursor.execute(query)
        tasks = cursor.fetchall()
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Title", min_width=20)
        table.add_column("Description", min_width=20)
        table.add_column("Created At", min_width=20)
        table.add_column("Completed At", min_width=20)
        table.add_column("Status", min_width=12)

        for task in tasks:
            status = '✅ Completed' if task[3] else '🕒 Active'
            completed_at = task[5].strftime('%Y-%m-%d %H:%M:%S') if task[5] else 'Pending'
            created_at = task[4].strftime('%Y-%m-%d %H:%M:%S')
            table.add_row(str(task[0]), task[1], task[2], created_at, completed_at, status)

        console.print("[bold magenta]Whatask - Task Management[/bold magenta]", "✨", justify="center")
        console.print(table)

def complete_task(task_id):
    if not task_exists(task_id):
        console.print(f"[red]Task {task_id} does not exist![/red]")
        return
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "UPDATE tasks SET is_completed = TRUE, completed_at = %s WHERE id = %s",
            (datetime.now(), task_id)
        )
        console.print(f"[green]Task {task_id} marked as completed.[/green]")

def update_task(task_id, new_title, new_description):
    if not task_exists(task_id):
        console.print(f"[red]Task {task_id} does not exist![/red]")
        return
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "UPDATE tasks SET title = %s, description = %s WHERE id = %s",
            (new_title, new_description, task_id)
        )
        console.print(f"[green]Task {task_id} updated.[/green]")
