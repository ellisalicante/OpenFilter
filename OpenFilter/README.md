# OpenFilter: the framework

## Requirements:
(1) an Android Emulator;
(2) a computing machine;
(3) a virtual webcam. 

A pipeline of the sketch is provided in the figure below.

![OpenFilter pipeline.](assets/pipeline.png)

The Android emulator runs on the machine, where the social media application targeted in the research is installed. In the emulator, the researcher may access any available AR filter of the social media platform. Most of these filters can only be applied on live images from the camera. To overcome this limitation, the virtual webcam projects the existing image dataset on the camera enabling the application of the AR filters on it. The process is automatized by means of an auto-clicker system: each image is first projected on the camera; next, the filter is applied to the image and finally the filtered image is saved on disk. OpenFilter processes an image every 4 seconds on a Intel(R) Core(TM) i7-8565U machine with NVIDIA GeForce MX150, i.e. around 900 images per hour and 22,000 per day. 

## 1. Instructions for use
#### 1.1 Installation
In our implementation, we run OpenFilter using BlueStacks 5.7 (www.bluestacks.com). On the virtual phone, researchers can download any targeted social media application for research (in our implementation, we refer to Instagram). Once the application is downloaded, the researcher should log in or create a new account.

(put image of instagram login page on the android emulator)

The researcher should also download ManyCam 7.10 (www.manycam.com). The aim of this virtual camera is to by-pass the issue related to the application of AR-based filters only on live image. 

The process of the application of these filters is automatized through an auto-clicker script, available in our file **put name of the file**.

#### 1.2 Set-up
(necessary settings, expecially regarding the camera, the display, and all these things! It would be good to have a comprehensive yet synthetic list.)

Being based on an auto-clicker system, the positioning of the objects on the display is key for the functioning of the OpenFilter. In the Figure below, we provide a screenshot of the ideal set-up on a 1920 x 1080 monitor.

(put image here of how it should look like)

Note that the Android emulator must be positioned at the left-hand side of the screen, aligned with the borders of the screen (left, top, bottom). The interface of the virtual camera, instead, has to be positioned on the right-hand side, leaving space for the command line at the bottom. It is extremely relevant that the width of the virtual camera window leaves the targeted file positioning (highlighted in red in the image) free, so that the autoclicker can use that space to temporarily save the images.

We strongly encourage our readers to deactivate notifications while running OpenFilter. Sudden pop-ups could damage the final results. 

(explain why. do we take screenshots finally? YES!)

#### 1.3 Error handling
The current version of OpenFilter occasionally might create some errors while running. In the preparation of our datasets, we encountered two types of errors: (1) ManyCam does not load an image successfully and displays a noise screen; and (2) ManyScren gets stuck and processes the same image multiple times. Under the name **put file name**, we share the code to automatically detect these errors and encourage our readers to perform error checks and corrections when creating new datasets using OpenFilter.

(put some more details regarding how to use these files)

## 2. License and attribution
CC BY-NC 4.0
The framework and the datasets are part of a scientific paper currently under review for **NAME OF THE CONFERENCE**, under the title **TITLE OF THE PAPER**.

