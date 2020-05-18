## python3をインストール  
Macの場合，下記のコマンドを実行する．  
```php
brew install python
```  
"brew: command not found" となった場合は，下記のサイトからコマンドをコピペしてHomebrew をインストールする必要あり．  
https://brew.sh/index_ja  
  
* すでにpython2系が入っている場合，下記のコマンドでpython3にアップデートできる．
```php
brew update
```

~/.bash_profile に次を記述．    
```php
export PATH=/usr/local/bin:$PATH
alias python="python3"
alias pip="pip3"
```
  
* pathについて困った場合は下記を参照．
https://qiita.com/soarflat/items/d5015bec37f8a8254380  

## pyenvのインストール(必要あれば)
```php
brew install pyenv
```
~/.bash_profileに次を記述
```php
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"<-これがないとpythonコマンドが別のディレクトリを参照しようとする
```
ローカルのレポジトリごとにpythonのバージョンを変更したい場合に以下のコマンドを流す
```php
cd [ローカルレポジトリ]
pyenv local [pythonのバージョン]
```
* pyenvで管理しているpythonのバージョンを確認する場合は以下を流す
```php
pyenv versions
```

terminal にて次のコマンドを実行．
```php
source ~/.bash_profile  
```
* pyenvについては
https://qiita.com/koooooo/items/b21d87ffe2b56d0c589b
  
## Djangoのインストール  
下記のコマンドでDjangoおよびDjango REST frameworkをインストール．  
```php
pip install django
pip install djangorestframework
```
  
## runsernerの起動  
```php
python manage.py runserver 192.168.2.105:8000
```
  
## appの作成  
```php
cd {$directory}
mkdir appname
cd ..
python manage.py appname {$directory}/appname
```
app作成時，projectディレクトリの下にappディレクトリができる．  
ディレクトリ構成は次のようになる．
```
/project_directory/config/settings.py (各種設定が記述されている．作成したappを登録するのもこのファイル)  
                         /urls.py (urlのルーティングを設定する大元のファイル．)  
/project_directory/appname/views.py (MVCで言うControlerを記述するファイル)                          
                          /models.py (MVCでいうModelを記述するファイル)  
                          /apps.py (app nameを記述するファイル)    
                          /urls.py (app以下のurlの設定をするファイル)  
                          /tests.py (appのtestをするファイル)
```
## Shellの起動・停止  
```php
python manage.py shell (起動)
exit() (停止)
```
  
## Migrationについて  
* modelの変更をした場合に実行するコマンド  
```php
python manage.py makemigrations appname
```
* DBに変更を登録するコマンド  
```php
python manage.py migrate
```

## クエリセットについて  
* Objectの作成  
User.objects.create(field1="", field2="", ...)  
* 単一のObjectの取得  
user = User.objects.get(field1="", field2="", ...)  
* 複数のObjectの取得  
users = User.objects.filter(field1="", field2="", ...)  
* AND条件で取得 
products = Product.objects.filter(name1="hogehoge", name2="fumufumu")
* IN条件で取得 
products = Product.objects.filter(name1__in=["hogehoge", fumufumu"])
* OR条件で取得  
from django.db.models import Q  
products = Product.objects.filter(Q(name1="hogehoge") | Q(name2="fumufumu"))



## 仕様
- htmlにhamlを採用
1. vscodeで表示する場合「Better Haml」エクステンションをインストール
1. vscode開く > code > preferences > extensions > 「Better Haml」で検索

