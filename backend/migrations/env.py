from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context

from app.models.base import Base
from app import models  # this ensures all models are imported
# import all models here
from app.db import engine

# Alembic Config object
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# <-- FIX: set target_metadata properly
target_metadata = Base.metadata

# Offline migrations
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# Online migrations
def run_migrations_online() -> None:
    connectable = engine  # use your engine from app.db

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
