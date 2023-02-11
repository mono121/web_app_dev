# frontend

Dockerによるreactの立ち上げ

## 立ち上げ方法

/backend/README.mdの内容に従いbackendを立ち上げる。

/frontendで下記コマンドを打つ。

```bash
docker-compose build
```

docker-composeをバックグラウンドで立ち上げる。

`docker-compose up -d`

ブラウザでlocalhost:3000を入力しreactのページが表示されたらOK。

backendで

`docker exec -it <webのコンテナID> python manage.py createsuperuser`

を実行し作成したusernameとpasswordをフォームに入力しログインボタンを押し、Show Tasksボタンを押すと作成したtaskが表示される。

## 開発終了時

立ち上げたコンテナ・ボリューム・イメージを削除する。

`docker-compose down`

コンテナの停止だけしたい場合は

`docker-compose stop`

再起動は

`docker-compose start`
