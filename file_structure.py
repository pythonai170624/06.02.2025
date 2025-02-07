import os

def format_size(size_in_bytes):
    """Convert bytes to human-readable format (KB, MB, GB)."""
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"
    elif size_in_bytes < 1024 ** 2:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024 ** 3:
        return f"{size_in_bytes / (1024 ** 2):.2f} MB"
    else:
        return f"{size_in_bytes / (1024 ** 3):.2f} GB"

def list_files_recc(folder_path, indent=0):
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isdir(full_path):
            # FOLDER
            print(indent * ' ' + '[' + item + ']')  # "d:\test\1" -- no
            if not item.startswith('.') and not item.startswith('__'):
                list_files_recc(full_path, indent + 4)
        else:
            # FILE
            size = format_size(os.path.getsize(full_path))
            print(indent * ' ', item, ' ', size)  # "d:\test\1" -- no

list_files_recc(r"d:\docker")

