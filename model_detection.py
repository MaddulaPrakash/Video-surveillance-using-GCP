!pip install google-cloud-storage

from google.colab import auth

auth.authenticate_user()

from google.cloud import storage

bucket_name = 'my-mksp-bucket'
client = storage.Client()

bucket = client.get_bucket(bucket_name)

blob = bucket.blob('vid10.mp4')
blob.upload_from_filename('/content/vid10.mp4')

!pip install -r /content/yolov5/requirements.txt

!git clone https://github.com/ultralytics/yolov5


cd yolov5


%run /content/yolov5/detect.py --source /content/vid2.mp4

from google.cloud import storage
import shutil

def upload_to_gcs(local_file, gcs_path):
    bucket_name = gcs_path.split('/')[2]
    blob_name = '/'.join(gcs_path.split('/')[3:])
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_file)

def upload_image_to_gcs(local_folder, bucket_name, destination_blob_name):
    # Create a zip file of the labeled frames
    shutil.make_archive(local_folder, 'zip', local_folder)

    # Upload the zip file to GCS
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(f'{local_folder}.zip')


upload_to_gcs('/content/yolov5/runs/detect/exp4/vid2.mp4', 'gs://my-mksp-bucket/results/vid_from_gcs_2.mp4')
upload_image_to_gcs('/content/labeled_frames', 'my-mksp-bucket', 'images2.zip')



!docker build -t your-yolo-image .

# Install Docker in Colab
!curl -fsSL https://get.docker.com -o get-docker.sh
!sh get-docker.sh


# Build Docker image using nvidia-docker
!docker build -t your-yolo-image .

# Install Docker in Colab
!curl -fsSL https://get.docker.com -o get-docker.sh
!sh get-docker.sh

# Build Docker image
!docker build -t your-yolo-image .

# Run Docker container
!docker run -it your-yolo-image

sudo systemctl status docker

!python /content/yolov5/export.py --include pb

!gsutil cp -r /content/yolov5/export.py gs://my-mksp-bucket/export.py

# Upload SavedModel to Google Cloud Storage
!gsutil cp -r /content/yolov5/yolov5s_saved_model gs://my-mksp-bucket/od-model-y

!gcloud app deploy /content/yolov5/models/yolov5s.yaml --project  fluent-aileron-402402