DATA_NAME = "accel_ms2_xyz"
LABEL_NAME = "gesture"

# label name (you should keep "negative" in the end of the list)
labels = ["line, ""ring", "slope", "negative"]

# data split configuration
# note that train_ratio + valid_ratio + test_ratio = 1
train_ratio = 0.8
valid_ratio = 0.2
data_split_random_seed = 31

# model configuration
model = "CNN"
seq_length = 32 # the input size of the model
epochs = 30
steps_per_epoch =1000
batch_size = 512
