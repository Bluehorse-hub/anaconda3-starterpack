# Tensorflowを入れている
import tensorflow as tf

# GPUを認識するかの簡易テスト
if tf.test.is_gpu_available():
    print("上に出てくる出力は気にしないで大丈夫")
    print("GPUが認識されています！")

else:
    print("GPUが認識されていません...")