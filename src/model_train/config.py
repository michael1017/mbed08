DATA_NAME = "accel_ms2_xyz"
LABEL_NAME = "gesture"

# label name (you should keep "negative" in the end of the list)
labels = ["ring", "rtl", "ltr", "utd", "negative"]

# data split configuration
# note that train_ratio + valid_ratio + test_ratio = 1
train_ratio = 0.75
valid_ratio = 0.25
data_split_random_seed = 32

# model configuration
model = "CNN"
seq_length = 64 # the input size of the model
epochs = 25
steps_per_epoch =1000
batch_size = 512
