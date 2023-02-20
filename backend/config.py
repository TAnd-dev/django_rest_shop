from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    port: str
    password: str
    user: str
    database: str


@dataclass
class SetConfig:
    secret_key: str


@dataclass
class Config:
    db: DbConfig
    set: SetConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        db=DbConfig(
            host=env.str('DB_HOST'),
            port=env.str('PORT'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        set=SetConfig(
            secret_key=env.str('SECRET_KEY'),
        )
    )
