tortoise_cfg = {
    'connections': {
        # Dict format for connection
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'insurance',
                'password': 'abc123',
                'database': 'test',
            }
        },
    },
    'apps': {
        'models': {
            'models': ['src.model'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        }
    }
}