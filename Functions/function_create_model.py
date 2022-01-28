 def create_model(model_url,num_classes=10):
  """
  Takes TF hub URL and creates keras sequentional model 

  Args:
    model_url(str): A tf hub feature extaction url
    num_classes(int): number of output neurons in the output layer
      Should be equal to number of target classes

  Returns:
    An uncompiled Keras Sequential model with model_url as feature extractor 
    layer and Dense output layer with num_classes output neurons
  """
  #Download the pretrained model save it as keras layer 
  feature_extractor_layer =  hub.KerasLayer(model_url,
                                             trainable=False,
                                             name="feature_extraction_layer",
                                             input_shape=IMAGE_SHAPE+(3,)) # freeze the already learned patterns
  #Create our own model
  model = tf.keras.Sequential([
    feature_extractor_layer,
    layers.Dense(num_classes, activation="softmax", name="output_layer")                             
  ])

  return model
