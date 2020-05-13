import cli
import datetime

def get_version():
    version = cli.__version__
    parts = version.split('.')
    parts[-1] = datetime.datetime.now().strftime('%Y%m%d%H%M')
    return '.'.join(parts)

