import cli
import datetime

def get_version():
    version = cli.__version__
    parts = version.split('.')
    parts[-1] = datetime.datetime.now().strftime('%y%j%H%M')
    return '.'.join(parts)

