import os
import dotenv

env_defaults = dotenv.dotenv_values()

PORT = int(os.getenv('PORT', env_defaults['PORT']))
FILES_DIR = os.getenv('FILES_DIR', env_defaults['FILES_DIR'])