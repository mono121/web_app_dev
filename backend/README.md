# backend

DockerによるDjangoとPostgreSQLの立ち上げと接続

## 立ち上げ方法

以下コマンドを打ち、db_data, [作成するプロジェクト名]ディレクトリができていることを確認する。

```bash
docker-compose build
docker-compose run web django-admin.py startproject [作成するプロジェクト名] .
```

[作成するプロジェクト名]内にあるsettings.pyのDATABASEを以下に置き換える。

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

docker-composeをバックグラウンドで立ち上げる。(上記はプロジェクト立ち上げの最初だけ行う。立ち上げ後はここより下のコマンドを実行するだけでおけ。)

`docker-compose up -d`

ブラウザでlocalhost:8000を入力しdjangoのページが表示されたらOK。

## DBへ反映

`docker exec <webのコンテナID> python manage.py makemigrations`

`docker exec <webのコンテナID> python manage.py migrate`

`docker exec -it <webのコンテナID> python manage.py createsuperuser`
※superuserを作成していない場合

## 開発終了時

立ち上げたコンテナ・ボリューム・イメージを削除する。

`docker-compose down`

コンテナの停止だけしたい場合は

`docker-compose stop`

再起動は

`docker-compose start`
