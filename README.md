# KMUTT Machine Learning Tensorflow Image Classifier Tutorial
Image Classification workshop for Machine Learning CS532 Lecture on September 21 at KMUTT.
Use this [CodeLab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/?utm_campaign=chrome_series_machinelearning_063016&utm_source=gdev&utm_medium=yt-desc#0) by Google as a guide. Also this [tutorial](https://www.tensorflow.org/versions/r0.9/how_tos/image_retraining/index.html) is quite helpful.

![maxresdefault](https://user-images.githubusercontent.com/28506207/30697140-242e8178-9f08-11e7-93a6-f93b47c28e22.jpg)

## Requirements

* [docker](https://www.docker.com/products/docker-toolbox)

Download docker image file [tensorflow/tensorflow](https://hub.docker.com/r/tensorflow/tensorflow/).
* docker pull tensorflow/tensorflow

#### Build the Docker image locally
docker run -it -p 6006:6006 -v "$(PWD)"/tensorflow_starwars:/notebooks/sharedfolder tensorflow/tensorflow bash

## Alternative (Windows)
You'll need Python 2.7 or Python 3.6 to run this code. You'll also need to install tensorflow library with pip.

#### Training a model
Using bash command train.sh or python command below \

```shell
$ TRAIN_DIR=/tmp/train_logs \
$ python -m scripts.retrain \\ \
  --bottleneck_dir=tf_files/bottlenecks \\ \
  --how_many_training_steps=500 \\ \
  --model_dir=tf_files/models/ \\ \
  --output_graph=tf_files/retrained_graph.pb \\ \
  --output_labels=tf_files/retrained_labels.txt \\ \
  --image_dir=tf_files/star_wars
```

#### Testing a model
```shell
$python -m scripts.starwars_class \\ \
--graph=tf_files/retrained_graph.pb  \\ \
--image=tf_files/star_wars/vader/pic_013.jpg
```
#### TensorBoard

To visualize the losses and other metrics during training, you can use
[TensorBoard](https://github.com/tensorflow/tensorboard)
by running the command below.

```shell
tensorboard --logdir=${TRAIN_DIR}
```

