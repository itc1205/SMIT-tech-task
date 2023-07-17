tortoise_cfg = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "db",
                "port": "5432",
                "user": "insurance",
                "password": "abc123",
                "database": "test",
            },
        }
    },
    "apps": {
        "models": {
            "models": ["src.model"],
            "default_connection": "default",
        }
    },
}
