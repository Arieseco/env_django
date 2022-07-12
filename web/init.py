''' 
  .envファイルを作成する。
  起動方法 ./init.py 
'''
from django.core.management.utils import get_random_secret_key
import os

# シークレットキーの生成
secret_key = get_random_secret_key()
text = 'SECRET_KEY=\'{0}\''.format(secret_key)

# .envファイル出力場所
project_name = 'secrets'
path = './{0}/secret.env'.format(project_name)
f = open(path, 'w')
f.write(text)
f.close
