from sqlmodel import create_engine, SQLModel


def get_engine():
    url = 'sqlite:///database.db'
    url = 'postgresql+psycopg2://postgres:tasks_senha123V@db.lfhqvmxbrworgpptumfe.supabase.co:5432/postgres'
    return create_engine(url, echo=True)


def create_tables():
    SQLModel.metadata.create_all(get_engine())
