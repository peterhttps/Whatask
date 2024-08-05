import click
from app.commands import add_task, delete_task, list_tasks, complete_task, update_task, help_command
from app.database import initialize_db

@click.group()
def cli():
    """Whatask - A simple task management system."""
    initialize_db() 
    pass

@cli.command()
def help():
    """Show this help message and exit."""
    help_command()

@cli.command()
@click.argument('title')
@click.option('--description', default='', help='Description of the task')
def add(title, description):
    """Add a new task."""
    add_task(title, description)

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task."""
    delete_task(task_id)

@cli.command()
@click.option('--completed', is_flag=True, help='Show only completed tasks')
def list(completed):
    """List all tasks. Optionally, show only completed tasks."""
    list_tasks(show_completed=completed)

@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark a task as completed."""
    complete_task(task_id)

@cli.command()
@click.argument('task_id', type=int)
@click.option('--title', prompt='Enter new title', help='New title for the task')
@click.option('--description', prompt='Enter new description', help='New description for the task')
def update(task_id, title, description):
    """Update an existing task."""
    update_task(task_id, title, description)

if __name__ == '__main__':
    cli()
