from typing import Final
import sqlite3

import os

''' 環境変数定義 '''
class Base:

  ''' 初期化 '''
  def __init__(self, debug:int):
    # 秘密情報を取得
    self.__secrets:Final(list) = self.init_database(debug)

    # シークレットキー
    self.__SECRET_KEY:Final(str) = self.__secrets[1]

    # DBのパスワード
    self.__POSTGRES_PASSWORD:Final(str) = self.__secrets[2]

    # 許可するホスト
    self._allowed_host: Final(list) = ['*']

  ''' 秘密情報レコード取得 '''
  def init_database(self,debug:int) -> list:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dbname = current_dir + '/secrets.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM secrets WHERE debug = {0}'.format(debug))

    result: list = cur.fetchone()
    return result

  
  ''' シークレットキー'''
  def get_secretkey(self) -> str:
    return self.__SECRET_KEY

  ''' 許可するホスト '''
  def get_allowed_host(self) -> list:
    return self._allowed_host
  
  ''' データベース '''
  def get_database_password(self) -> dict:
    return self.__POSTGRES_PASSWORD
