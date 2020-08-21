import tensorflow as tf
from encoder_adain import Encoder
from decoder_adain import Decoder
from adaptive_instance_norm import AdaIN

MODEL_SAVE_PATHS = "./models/style_weight_2e0.ckpt"

class StyleTransferNet(object):

    def __init__(self, encoder_weights_path):
        self.encoder = Encoder(encoder_weights_path)
        self.decoder = Decoder()

    def transform(self, content, style):
        # switch RGB to BGR
        content = tf.reverse(content, axis=[-1])
        style   = tf.reverse(style,   axis=[-1])

        # preprocess image
        content = self.encoder.preprocess(content)
        style   = self.encoder.preprocess(style)

        # encode image
        enc_c, enc_c_layers = self.encoder.encode(content)
        enc_s, enc_s_layers = self.encoder.encode(style)

        self.encoded_content_layers = enc_c_layers
        self.encoded_style_layers   = enc_s_layers

        # pass the encoded images to AdaIN
        target_features = AdaIN(enc_c, enc_s)
        self.target_features = target_features

        # decode target features back to image
        generated_img = self.decoder.decode(target_features)

        # deprocess image
        generated_img = self.encoder.deprocess(generated_img)

        # switch BGR back to RGB
        generated_img = tf.reverse(generated_img, axis=[-1])

        # clip to 0..255
        generated_img = tf.clip_by_value(generated_img, 0.0, 255.0)

        return generated_img



def stylize_single_adain(content_img, style_img, encoder_path):

    with tf.Graph().as_default(), tf.Session() as sess1:
        # build the dataflow graph
        content = tf.placeholder(
            tf.float32, shape=(1, None, None, 3), name='content')
        style   = tf.placeholder(
            tf.float32, shape=(1, None, None, 3), name='style')

        stn = StyleTransferNet(encoder_path)

        sess1.run(tf.global_variables_initializer())

        saver = tf.train.Saver()
        saver.restore(sess1, MODEL_SAVE_PATHS)

        output_image = stn.transform(content, style)

        result = sess1.run(output_image,
                    feed_dict={content: content_img, style: style_img})

        sess1.close()


    return result[0]