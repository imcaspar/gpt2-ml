import argparse

from google.colab import auth
from googleapiclient.discovery import build
from apiclient.http import MediaIoBaseDownload
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Contextual generation (aka given some metadata we will generate articles')
parser.add_argument(
    '-file_id',
    dest='file_id',
    type=str,
    help='Path to a JSONL containing metadata',
)
parser.add_argument(
    '-file_path',
    dest='file_path',
    type=str,
    help='Out jsonl, which will contain the completed jsons',
)

args = parser.parse_args()

auth.authenticate_user()
drive_service = build('drive', 'v3')

# file_id, file_ext = ('1n_5-tgPpQ1gqbyLPbP1PwiFi2eo7SWw_', '.data-00000-of-00001')
# filename = '%s/model.ckpt-%d%s' % (model_dir, 100000, file_ext)
req = drive_service.files().get_media(fileId=args.file_id)
with open(args.file_path, 'wb') as f:
    downloader = MediaIoBaseDownload(f, req, chunksize=100*1024*1024)
    done = False
    pbar = tqdm(total=100, desc='%s' % args.file_path)
    progress = 0
    while done is False:
        status, done = downloader.next_chunk()
        new_progress = int(status.progress() * 100)
        pbar.update(new_progress - progress)
        progress = new_progress
    pbar.close()
