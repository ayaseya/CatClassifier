from PIL import Image
import os
import glob
import numpy as np
from sklearn import model_selection


if __name__ == '__main__':
    classes = ["cat", "dog"]
    num_classes = len(classes)
    image_size = 50

    # 画像の読み込み
    X = []  # 画像データ
    Y = []  # ラベルデータ

    # 画像を読み込み、配列に変換しリストに格納する
    for index, animal_class in enumerate(classes):
        photos_dir = "./img/" + animal_class
        files = glob.glob(photos_dir + "/*.jpg")
        for i, file in enumerate(files):
            if i >= 200:
                break
            image = Image.open(file)  # type: Image.Image
            image = image.convert("RGB")  # RGBの三色に変換する
            image = image.resize((image_size, image_size))
            data = np.asarray(image)  # 画像を数字の配列に変換する
            X.append(data)
            Y.append(index)

# TensorFlowが扱いやすいデータ型に揃える
X = np.array(X)
Y = np.array(Y)

# データを交差検証用に分割する(3:1)
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (x_train, x_test, y_train, y_test)
np.save("./animal.npy", xy)
