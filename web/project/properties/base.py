from typing import Final
import environ
from pathlib import Path

''' 環境変数定義 '''
class Base:

  ''' 初期化 '''
  def __init__(self):

    self.BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # 環境変数ファイルの読み込み
    self.root = environ.Path(self.BASE_DIR / 'secrets')
    self.env_secret = environ.Env()
    self.env_secret.read_env(self.root('secret.env'))

    # シークレットキー
    self.SECRET_KEY = self.env_secret('SECRET_KEY')

    # 開発環境、本番環境の判定
    self.is_development: bool = True

    # シークレットキー
    #self._secretkey: Final[str] = self._env_secretkey('SECRET_KEY')

    # デバッグ
    self._debug: bool = self.is_development

    # 許可するホスト
    self._allowed_host: list = ['*']

    # インストールしたアプリケーション
    self._installed_apps: list = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
    ]

    # データベース
    self._databases: dict = {
      'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'django_db',
        'PORT': '5432',
      }
    }
  
  ''' シークレットキー'''
  def get_secretkey(self) -> str:
    return self.SECRET_KEY

  ''' デバッグモード判定 '''
  def get_isdebug(self) -> bool:
    return self._debug

  ''' 許可するホスト '''
  def get_allowed_host(self) -> list:
    return self._allowed_host
  
  def set_installed_apps(self,apps):
    self._installed_apps.append(apps)

  ''' インストールしたアプリケーション '''
  def get_installed_apps(self) -> list:
    return self._installed_apps
  
  ''' データベース '''
  def get_databases(self) -> dict:
    return self._databases
