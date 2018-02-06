import os
from hurry.filesize import size
from hurry.filesize import alternative
def get_size(start_path = 'C:\eclipse'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

print size(get_size(), system=alternative)
