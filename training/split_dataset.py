import splitfolders

# Replace 'plantVillage' with your folder name if different
input_folder = "plantVillage"
output_folder = "dataset"

# Split into 70% train, 10% val, 20% test
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(.7, .1, .2), group_prefix=None)
print("Dataset split completed!")
