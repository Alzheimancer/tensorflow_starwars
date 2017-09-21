import tensorflow as tf
import sys
import argparse

# change this as you see fit
#image_path = sys.argv[1]
file_name = '' 
parser = argparse.ArgumentParser()
parser.add_argument("--image", help="image to be processed")
parser.add_argument("--graph", help="graph/model to be executed")
args = parser.parse_args()

if args.graph:
    model_file = args.graph
if args.image:
    file_name = args.image
 
# Read in the image_data
image_data = tf.gfile.FastGFile(file_name, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line in tf.gfile.GFile("tf_files/retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))