# Skeleton-based-Hand-Gesture-Recognition

# Introduction:
This repo is a Skeleton-based Hand Gesture Recognition written in Python for the [SHREC 2021](https://univr-vips.github.io/Shrec21/) dataset. The accuracy of the model is 84 percent. You may download the dataset from this [link](https://univr-vips.github.io/Shrec21/).

# Preprocess Train and Test Data:
First, we fetch important data from each .txt file and save all of the important data to CSV files. You may find more useful information about the important data in each file in the [process_train_data](https://github.com/seyyedjavadrazavi/Skeleton-based-Hand-Gesture-Recognition/blob/6495196c4c83c16f6e2fc5fcd6471342e842c838/training_set/process_train_data.ipynb) and [process_test_data](https://github.com/seyyedjavadrazavi/Skeleton-based-Hand-Gesture-Recognition/blob/6495196c4c83c16f6e2fc5fcd6471342e842c838/test_set/process_test_data.ipynb). It is not very different between running tests or training data at first. You should locate the "sequences" and "annotations_revised" in the training_set and test_set folders, change the path of files in Python codes, and then run the related Python code.

# Train and Test:
After the preprocessing phase, you run the [SVM.ipynb](https://github.com/seyyedjavadrazavi/Skeleton-based-Hand-Gesture-Recognition/blob/6495196c4c83c16f6e2fc5fcd6471342e842c838/SVM.ipynb) file. We employed the SVM machine learning model. 



