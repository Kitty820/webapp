import streamlit as st
from PIL import Image
import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from numpy import genfromtxt
import math

st.set_option('deprecation.showPyplotGlobalUse', False)


data = genfromtxt("/Users/mengqingyong/Desktop/product_images.csv", delimiter=',', skip_header=1)
cluster_points = genfromtxt("/Users/mengqingyong/Desktop/cluster_data 3.csv", delimiter=',')

if 'model_images' not in st.session_state:
    st.session_state.model_images = [random.choice(cluster_points[i][~np.isnan(cluster_points[i])]) for i in range(9)]

# st.session_state.model_images = []
# for i in range(9):
#     idx = np.isnan(cluster_points[i])
#     st.session_state.model_images.append(random.choice(cluster_points[i][~np.isnan(cluster_points[i])]))
    #images = data.reshape((-1, 28, 28))
    #plt.imshow(images[int(random.choice(cluster_points[i][~idx]))], cmap='gray')
    #plt.show()
    #print(cluster_points,data)
print(st.session_state.model_images)

images = data.reshape((-1, 28, 28))
#ig = [26,33,171,205, 219, 255, 272, 326, 339, 380, 412, 446, 480]
#for i in ig:
#    plt.imshow(images[i-1], cmap='gray')
#    plt.show()
# Load dataset from CSV file
#random_values = [random.choice(data_tolist) for _ in range(len(data_tolist))]
#print(random_values)
# Reshape pixel values into images


#images = data.reshape((-1, 28, 28))
# Display the first 10 images
#for i in range(3):
  #  plt.imshow(images[i], cmap='gray')
  #   plt.show()



def display_images(images):
    for image in images:
        st.image(image, use_column_width=True)
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

# Add header and subheader
st.title("Data analytics II group work")
st.header("Jack MENGGG's masterpiece")
st.subheader("Get recommendation for similar pictures using k-means algorithm")

# Add image and text
#image = Image.open("/Users/mengqingyong/Desktop/IMG_6302.png")



# Convert the image to bytes for displaying it on a new page
#with io.BytesIO() as output:
   # image.save(output, format="PNG")
    #contents = output.getvalue()

#example picture 1

for i in range(9):
    plt.imshow(images[int(st.session_state.model_images[i] - 1)], cmap='gray')
    plt.show()
    st.pyplot()
    st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")

    if st.button(f"Get Recommendation for example {i+1}"):
        #while len(recommendations) < 9:

        #idx = np.isnan(cluster_points[i])
        #recommendations = random.sample(cluster_points[0][~idx], 9)

            #recommendations.append(random.choice(cluster_points[0][~idx]))
        #for x in cluster_points[0]:
            #if not np.isnan(x):

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
            plt.imshow(images[int(m)], cmap='gray')
            plt.show()
            st.pyplot()
    #display_images(random.sample(images_cluster1, 2))
    if st.button(f"Hide recommendation for example {i+1}"):
        st.remove()
#st.empty()
#
# #example picture 2
# plt.imshow(images[int(st.session_state.model_images[1]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 2"):
#     filtered_points = []
#     for x in cluster_points[1]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 2"):
#     pass
#
#
# #example picture 3
# plt.imshow(images[int(model_images[2]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 3"):
#     filtered_points = []
#     for x in cluster_points[2]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 3"):
#     pass
#
#
# #example picture 4
# plt.imshow(images[int(model_images[3]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 4"):
#     filtered_points = []
#     for x in cluster_points[3]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 4"):
#     pass
#
#
# #example picture 5
# plt.imshow(images[int(model_images[4]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 5"):
#     filtered_points = []
#     for x in cluster_points[4]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 5"):
#     pass
#
#
# #example picture 6
# plt.imshow(images[int(model_images[5]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 6"):
#     filtered_points = []
#     for x in cluster_points[5]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 6"):
#     pass
#
#
# #example picture 7
# plt.imshow(images[int(model_images[6]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 7"):
#     filtered_points = []
#     for x in cluster_points[6]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 7"):
#     pass
#
#
# #example picture 8
# plt.imshow(images[int(model_images[7]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 8"):
#     filtered_points = []
#     for x in cluster_points[7]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 8"):
#     pass
#
#
# #example picture 9
# plt.imshow(images[int(model_images[8]-1)], cmap='gray')
# plt.show()
# st.pyplot()
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 9"):
#     filtered_points = []
#     for x in cluster_points[8]:
#         if not np.isnan(x):
#             filtered_points.append(x - 1)
#     print(filtered_points)
#     recommendations = random.sample(filtered_points, min(9, len(filtered_points)))
#     position = 0
#     for i in recommendations:
#         recommendations[position] = int(i)
#         position = position + 1
#         plt.imshow(images[int(i)], cmap='gray')
#         plt.show()
#         st.pyplot()
# #display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 9"):
#     pass
#
#
#
# '''
# plt.imshow(images[int(model_images[0])])
# plt.show()
#
# st.image(plt.imshow(images[int(model_images[0])], cmap='gray'), use_column_width=True)
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 1"):
#     display_images(random.sample(images_cluster1, 2))
# if st.button("Hide recommendation for example 1"):
#     st.empty()
#
# st.image(image10, use_column_width=True)
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 2"):
#     display_images(random.sample(images_cluster2, 2))
# if st.button("Hide recommendation for example 2"):
#     st.empty()
#
# st.image(image19, use_column_width=True)
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 3"):
#     display_images(random.sample(images_cluster3, 2))
# if st.button("Hide recommendation for example 3"):
#     st.empty()
#
# st.image(image28, use_column_width=True)
# st.write("Click the button to get recommendations for similar pictures. Click again to get other similar pictures")
# if st.button("Get Recommendation for example 4"):
#     display_images(random.sample(images_cluster4, 2))
# if st.button("Hide recommendation for example 4"):'''
