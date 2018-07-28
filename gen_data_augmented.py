from PIL import Image
import os
import glob
import numpy as np
from sklearn import model_selection


if __name__ == '__main__':
    classes = ["cat", "dog"]
    num_classes = len(classes)
    image_size = 50
    num_test_data = 100

    # 画像の読み込み
    X_train = []  # 学習用の画像データ
    X_test = []   # テスト用の画像データ
    Y_train = []  # 学習用のラベルデータ
    Y_test = []   # テスト用の画像データ

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

            if i < num_test_data:
                # テスト用の画像データを追加
                X_test.append(data)
                Y_test.append(index)
            else:
                # 学習用の画像データを追加
                for angle in range(-20, 20, 5):
                    # 回転
                    img_r = image.rotate(angle)
                    data = np.asarray(img_r)
                    X_train.append(data)
                    Y_train.append(index)

                    # 反転
                    img_trans = img_r.transpose(Image.FLIP_LEFT_RIGHT)
                    data = np.asarray(img_trans)
                    X_train.append(data)
                    Y_train.append(index)

            # X.append(data)
            # Y.append(index)

# TensorFlowが扱いやすいデータ型に揃える
# X = np.array(X)
# Y = np.array(Y)
x_train = np.array(X_train)
x_test = np.array(X_test)
y_train = np.array(Y_train)
y_test = np.array(Y_test)


# データを交差検証用に分割する(3:1)
#x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (x_train, x_test, y_train, y_test)
np.save("./animal_aug.npy", xy)
