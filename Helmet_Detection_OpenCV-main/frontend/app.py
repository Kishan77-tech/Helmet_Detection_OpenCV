import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Helmet Detection System",
    page_icon="🪖",
    layout="centered"
)

st.title("🪖 Helmet Detection System")
st.write("Upload an image to detect Helmet / No Helmet.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Show original image
    st.subheader("Original Image")

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🔍 Detect Helmet", type="primary"):

        with st.spinner("Detecting helmet..."):

            try:

                # Reset file position
                uploaded_file.seek(0)

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        uploaded_file.type
                    )
                }

                # Send image to backend
                response = requests.post(
                    f"{BACKEND_URL}/detect",
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    if "error" in result:
                        st.error(result["error"])

                    else:

                        st.success(
                            "Detection completed successfully!"
                        )

                        # Display counts
                        col1, col2 = st.columns(2)

                        with col1:
                            st.metric(
                                "Helmet",
                                result["helmet_count"]
                            )

                        with col2:
                            st.metric(
                                "No Helmet",
                                result["no_helmet_count"]
                            )

                        # Get processed image
                        result_filename = result["result_file"]

                        image_response = requests.get(
                            f"{BACKEND_URL}/result/{result_filename}"
                        )

                        if image_response.status_code == 200:

                            result_image = Image.open(
                                BytesIO(image_response.content)
                            )

                            st.subheader(
                                "Detection Result"
                            )

                            st.image(
                                result_image,
                                caption="Helmet Detection Result",
                                use_container_width=True
                            )

                        else:
                            st.error(
                                "Could not load detection result."
                            )

                else:
                    st.error(
                        f"Backend error: {response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Backend is not running. "
                    "Please start the FastAPI backend first."
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )
