# добавляем файлы в архив
import pytest
import os
import zipfile
from path_config import source_dir, target_archive


@pytest.fixture(scope="session")
def add_files_to_zip():
    with zipfile.ZipFile(target_archive, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = file_path.replace(source_dir, '')
                zf.write(file_path, arcname=relative_path)

    yield

    os.remove(target_archive)
