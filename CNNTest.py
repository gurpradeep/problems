import tensorflow as tf


class MNISTModel(object):
    def __init__(self,input_dim,output_size):
        self.input_dim= input_dim
        self.output_size = output_size


    def model_layers(self, inputs, is_training):
        reshaped_inputs = tf.reshape(inputs, [-1, self.input_dim, self.input_dim, 1])
        
        conv1 = tf.keras.layers.Conv2D(
        filters=32,kernel_size=[5, 5],padding='same',activation='relu', 
        name='conv1')(reshaped_inputs)
        
        pool1 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool1')(conv1)


        conv2 = tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(pool1)
        # Pooling Layer #2
        pool2 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool2')(conv2)

        hwc = pool2.shape.as_list()[1:]
        flattened_size = hwc[0] * hwc[1] * hwc[2]
        pool2_flat = tf.reshape(pool2, [-1, flattened_size])
        dense = tf.keras.layers.Dense(
            1024, activation='relu', name='dense')(pool2_flat)

        dropout = tf.keras.layers.Dropout(rate=0.4)(dense, training=is_training)

        logits = tf.keras.layers.Dense(self.output_size, name='logits')(dropout)
        return logits


    def run_model_setup(self, inputs, labels, is_training):
        logits = self.model_layers(inputs, is_training)

        # convert logits to probabilities with softmax activation
        self.probs = tf.nn.softmax(logits, name='probs')
        # round probabilities
        self.predictions = tf.math.argmax(
            self.probs, axis=-1, name='predictions')
        class_labels = tf.math.argmax(labels, axis=-1)
        # find which predictions were correct
        is_correct = tf.math.equal(
            self.predictions, class_labels)
        is_correct_float = tf.cast(
            is_correct,
            tf.float32)
    
        # compute ratio of correct to incorrect predictions
        self.accuracy = tf.math.reduce_mean(
            is_correct_float)
        # train model
        if self.is_training:
            labels_float = tf.cast(
                labels, tf.float32)
            # compute the loss using cross_entropy
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
                labels=labels_float,
                logits=logits)
            self.loss = tf.math.reduce_mean(
                cross_entropy)
            # use adam to train model
            adam = tf.compat.v1.train.AdamOptimizer()
            self.train_op = adam.minimize(
                self.loss, global_step=self.global_step)