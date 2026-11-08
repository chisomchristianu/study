from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parents[1]
vault = root / 'StudyVault'
if not (vault / '00-Dashboard' / 'Study Map.md').is_file():
    raise SystemExit('StudyVault study map is missing')
output = root / 'Materials-Science-StudyVault.zip'
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for path in sorted(vault.rglob('*')):
        if path.is_file():
            archive.write(path, path.relative_to(root))
with ZipFile(output) as archive:
    if archive.testzip() is not None:
        raise SystemExit('ZIP integrity check failed')
print(f'Created {output.name}')
