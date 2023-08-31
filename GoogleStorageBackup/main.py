from google.cloud import storage
import os

client = storage.Client.from_service_account_json('key.json')
bucket = client.get_bucket("backup-system-upload")


def backup():
    dir_from = "files"
    dir_to = ""

    bucket.blob(dir_to)

    for file in os.listdir(dir_from):
        local_path = os.path.join(dir_from, file)
        bucket_path = os.path.join(dir_to, os.path.relpath(local_path, dir_from))

        blob = bucket.blob(bucket_path)
        blob.upload_from_filename(local_path)

        print(f"Backed up {local_path} successfully!")


if __name__ == '__main__':
    backup()
