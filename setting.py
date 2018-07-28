from commandr import command
from commandr import Run
import configparser


@command('create')
def create_config_file():
    """
    Flickr用のAPIキーの情報を保存する設定ファイルを作成する
    下記コマンドでコマンドライン上から直接実行できる
    $ python setting.py create
    """
    config = configparser.ConfigParser()
    config['Flickr'] = {
        'key': 'xxxx',      # APIキー
        'secret': 'xxxx'    # SECRETキー
    }

    # iniファイルに保存する
    with open('config.ini', 'w') as ini_file:
        config.write(ini_file)


def get_api_key():
    """
    Flickr用のAPIキーを取得する
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Flickr']['key']


def get_secret_key():
    """
    Flickr用のSECRETキーを取得する
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Flickr']['secret']


if __name__ == '__main__':
    # コマンドラインから関数を実行するために必要なcommandrライブラリ用の処理
    Run()
