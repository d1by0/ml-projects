import os
import face_recognition
import joblib
from sklearn import svm

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "./model/dataset")
MODEL_PATH = os.path.join(BASE_DIR, "./model/saved_model.pkl")

print("[INFO] Starting training...")

encodings = []
names = []

# Go through each person in dataset
for person in os.listdir(DATA_DIR):
    person_dir = os.path.join(DATA_DIR, person)
    if not os.path.isdir(person_dir):
        continue

    print(f"[INFO] Processing {person}...")
    for image_name in os.listdir(person_dir):
        image_path = os.path.join(person_dir, image_name)

        try:
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            for encoding in face_encodings:
                encodings.append(encoding)
                names.append(person)
        except Exception as e:
            print(f"[WARNING] Skipping {image_path} due to error: {e}")

# Train an SVM classifier
print("[INFO] Training classifier...")
clf = svm.SVC(probability=True)
clf.fit(encodings, names)

# Save model
joblib.dump(clf, MODEL_PATH)
print(f"[INFO] Model saved to {MODEL_PATH}")
