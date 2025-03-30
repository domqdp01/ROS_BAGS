import rosbag

input_bag = 'random_pav_duro_same_without_2.0_ms_rec.bag'
output_bag = 'random_pav_duro_same_with_1.bag'

# Mappa dei topic da rinominare
topic_map = {
    '/throttle_2': '/throttle_1',
    '/steering_2': '/steering_1',
    '/steering_angle_2': '/steering_angle_1'
}

with rosbag.Bag(output_bag, 'w') as outbag:
    for topic, msg, t in rosbag.Bag(input_bag).read_messages():
        # Rinomina il topic se è nella mappa
        new_topic = topic_map.get(topic, topic)
        outbag.write(new_topic, msg, t)
