import tensorflow as tf
import numpy as np
"""# 创建int32类型的0维张量，即标量
rank_0_tensor = tf.constant(4)
print(rank_0_tensor)
# 创建float32类型的1维张量
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(rank_1_tensor)
# 创建float16类型的⼆维张量
rank_2_tensor = tf.constant([[1, 2],
 [3, 4],
 [5, 6]], dtype=tf.float16)
print(rank_2_tensor)"""
# 创建float32类型的张量
rank_3_tensor = tf.constant([
 [[0, 1, 2, 3, 4],
 [5, 6, 7, 8, 9]],
 [[10, 11, 12, 13, 14],
 [15, 16, 17, 18, 19]],
 [[20, 21, 22, 23, 24],
 [25, 26, 27, 28, 29]],], dtype=tf.float32)
print(rank_3_tensor)