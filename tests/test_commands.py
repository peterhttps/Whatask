import pytest
from unittest.mock import MagicMock, ANY, call
from psycopg2 import connect 
from app.commands import add_task, delete_task, update_task

@pytest.fixture
def mock_connection(mocker):
    mock_conn = MagicMock()
    
    mock_cursor = MagicMock()
    mock_cursor.execute = MagicMock()
    mock_cursor.fetchone = MagicMock(return_value=[1])
    mock_cursor.fetchall = MagicMock(return_value=[])
    
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.__enter__.return_value = mock_conn
    mock_conn.__exit__ = MagicMock()

    mocker.patch("app.database.get_db_connection", return_value=mock_conn)
    
    return mock_conn

def test_add_task(mock_connection):
    add_task("Test Task", "Test Description")
    mock_connection.cursor().execute.assert_called_with(
        "INSERT INTO tasks (title, description, is_completed, created_at) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Test Task", "Test Description", False, ANY)
    )

def test_delete_task(mock_connection):
    delete_task(1)
    mock_connection.cursor().execute.assert_called_with("DELETE FROM tasks WHERE id = %s", (1,))

def test_update_task_not_exists(mock_connection):
    mock_connection.cursor().fetchone.return_value = [0]
    update_task(1, "New Title", "New Description")
    
    calls = [call("SELECT COUNT(*) FROM tasks WHERE id = %s", (1,))]
    mock_connection.cursor().execute.assert_has_calls(calls)
    mock_connection.cursor().execute.assert_called_once()
