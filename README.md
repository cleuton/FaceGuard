# FaceGuard - Face recognition + Machine Learning + IoT Demo

Most of the source code in this demo is a derivative from [**David Sandberg's** work](https://github.com/davidsandberg). The original license is included as file [**ORIGINAL_LICENSE.md**](./ORIGINAL_LICENSE.md).

The source code added by this work is composed of files: 
- [**photoserver.py**](./facenetmaster/src/photoserver.py): Photo server app, which receives a Photo and uses the Classifier to get a match;
- [**Foto.py**](./facenetmaster/src/Foto.py): Auxiliary class for the Photo server;
- [**photoclient.py**](./FaceNet/photoclient.py): Raspberry client, which captures a photo and sends it to the server.

All of the added source code is licensed using Apache 2.0 (included in the project).

## Description 

This is an implementation of FaceNet using IoT for face recognition. Using a Raspberry PI 3, with a Raspberry camera, a person "shoots" a photo, which will be sent to a remote server for processing. The remote server aligns and loads it into a Classifier to get a match. If it matches more than 60%, then a positive result is sent back to Raspberry PI.

## Setup

First, you'll need to create a Python virtual environment for you, using *Anaconda*! [**Install Anaconda**](https://www.anaconda.com) and run the following command: 

```
conda env create -f ds-env.yml
```

The file [**ds-env.yml**](./ds-env.yml) is in the main repository folder. Any time you want to run this tutorial, activate the environment: "source activate facenet" (for Linux and MacOS) or "activate facenet" (for MS Windows).

You'll need to train a Classifier using [*LFW public dataset*](https://github.com/davidsandberg/facenet/wiki/Validate-on-LFW). 

You can then train again using [*your own photos*](https://github.com/davidsandberg/facenet/wiki/Train-a-classifier-on-own-images). After that, you can run the [*photoserver*](./facenetmaster/src/photoserver.py) and install and run the [*photoclient*](./FaceNet/photoclient.py) on your **Raspberry PI 3**.

## Raspberry PI circuit

I will publish a guide to assemble the Raspberry PI circuit here.



