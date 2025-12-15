import pathlib
BASE_DIR = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
STUDENTS_FILE = DATA_DIR / "students.json"
 # backup file used for export
BACKUP_FILE = DATA_DIR / "students_backup.json"