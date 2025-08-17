import os
import joblib
import streamlit as st
import cv2
import numpy as np
import face_recognition

# ----------------------------
# Load Model
# ----------------------------
MODEL_PATH = "./model/saved_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(f"❌ Model file not found: {MODEL_PATH}\nPlease run `train_model.py` first.")
    st.stop()

model = joblib.load(MODEL_PATH)

# Build reverse dictionary directly from model.classes_
inv_class_dict = {i: name for i, name in enumerate(model.classes_)}

# ----------------------------
# Streamlit App UI
# ----------------------------
st.set_page_config(page_title="Who's That?", page_icon="🧑‍💻", layout="centered")

st.title("🧑‍💻 Who's That? - Face Recognition App")
st.write("Upload an image and let the AI recognize the person.")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.image(rgb_img, channels="RGB", caption="📸 Uploaded Image")

    # Face detection using face_recognition
    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

    if len(face_encodings) == 0:
        st.warning("⚠️ No face detected.")
    else:
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            preds = model.predict_proba([face_encoding])[0]
            best_idx = int(np.argmax(preds))
            best_class = inv_class_dict[best_idx]
            best_conf = preds[best_idx] * 100

            # Draw bounding box
            cv2.rectangle(rgb_img, (left, top), (right, bottom), (0, 200, 0), 2)
            cv2.putText(rgb_img, f"{best_class} ({best_conf:.1f}%)", (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)

            # Show predictions
            st.subheader("🔮 Top Predictions")
            for i, p in enumerate(preds):
                cls_name = inv_class_dict[i]
                st.text(f"{cls_name} - {p*100:.2f}%")
                st.progress(int(p*100))

            # Final verdict
            st.subheader("🧑 Final Verdict:")
            if best_conf < 60:
                st.error(f"❓ Unknown (Best confidence: {best_conf:.2f}%)")
            else:
                st.success(f"✅ {best_class} ({best_conf:.2f}%)")

        # Show final annotated image
        st.image(rgb_img, channels="RGB", caption="📌 Recognition Result")
