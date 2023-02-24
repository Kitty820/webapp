import streamlit as st
from PIL import Image
import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import math

# Set page title and favicon
st.set_page_config(page_title="Data analytics II group work", page_icon=":bar_chart:")

# Set page background color and font
st.markdown(
    """
    <style>
    body {
        color: #36454F;
        background-color: #E0FFFF;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Add background image
image = Image.open("/Users/mengqingyong/webapp/Everything-logos.jpeg")
st.image(image, use_column_width=True)

data = np.genfromtxt("./product.csv", delimiter=',', skip_header=1)
cluster_points = np.genfromtxt("./cluster_data.csv", delimiter=',')

if 'model_images' not in st.session_state:
    st.session_state.model_images = [random.choice(cluster_points[i][~np.isnan(cluster_points[i])]) for i in range(9)]

print(st.session_state.model_images)

images = data.reshape((-1, 28, 28))


def display_images(images):
    for image in images:
        st.image(image, use_column_width=True)

st.set_page_config(page_title="Data analytics II group work", page_icon=":bar_chart:")

st.markdown(
    """
    <style>
    body {
        color: #36454F;
        background-color: #E0FFFF;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Data analytics II group work")
st.header("Jack MENGGG's masterpiece")
st.subheader("Get recommendation for similar pictures using k-means algorithm")


for i in range(9):
    fig=plt.figure()
    plt.imshow(images[int(st.session_state.model_images[i] - 1)], cmap='gray')
    plt.show()
    plt.axis("off")
    st.pyplot(fig)
    st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")

    if st.button(f"Get Recommendation for example {i+1}"):

        filtered_points = []
        for x in cluster_points[i]:
            if not np.isnan(x):
                filtered_points.append(x-1)
        print(filtered_points)
        recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
        position = 0
        for m in recommendations:
            recommendations[position] = int(m)
            position = position + 1
            fig = plt.figure()
            plt.imshow(images[int(m)], cmap='gray')
            plt.show()
            st.pyplot(fig)
            plt.axis("off")
    if st.button(f"Hide recommendation for example {i+1}"):
        pass
