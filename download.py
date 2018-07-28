from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import setting
import os
import time
import sys


if __name__ == '__main__':
    # APIキーの情報
    api_key = setting.get_api_key()
    api_secret = setting.get_secret_key()

    # FlickrAPIにリクエストする際の待機時間(秒)
    wait_time = 1

    # コマンドラインの引数から動物名を取得する
    keyword = sys.argv[1]

    # 保存先のフォルダが存在しない場合は新規作成する
    save_dir = './img/' + keyword
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    # Flickrのラッパークラスを生成する
    flickr = FlickrAPI(api_key, api_secret, format='parsed-json')

    # キーワードをFlickrで検索する
    # flickr.photos.search()はwrapperであるFlickrAPI内に定義されている訳ではないので
    # Pycharmの入力補完で候補に表示されることはない
    # そのためAPIの関数名は下記URLのドキュメントを参照する必要がある
    # https://www.flickr.com/services/api/
    result = flickr.photos.search(
        text=keyword,
        per_page=400,
        media='photos',
        sort='relevance',
        safe_search=1,
        extras='url_q, license'
    )

    # 検索結果から検索条件に一致した全ての写真情報を取り出す
    photos = result['photos']

    # 写真のURLを取り出し、ダウンロードして保存する
    for i, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        file_path = save_dir + '/' + photo['id'] + '.jpg'

        # 同じ写真ファイルが存在する場合はダウンロードと保存の処理をスキップする
        if os.path.exists(file_path):
            continue

        # 写真を保存先にダウンロードする
        urlretrieve(url_q, file_path)
        time.sleep(wait_time)
