# frongend

DockerによるReact開発環境の立ち上げ。

## 立ち上げ方法

Dockerfileの10行目<br>

`command: sh -c "cd testapp && npm start"`

のtestappを[作成するプロジェクト名]に変更する。

以下コマンドを打ち、db_data, [作成するプロジェクト名]ディレクトリができていることを確認する。

```bash
docker-compose build
docker-compose run --rm react sh -c "npm install -g create-react-app && create-react-app [作成するプロジェクト名]"
```

typescriptを使用する場合は2つ目のコマンドを以下に変更する。

`docker-compose run --rm react sh -c "npm install -g create-react-app && create-react-app [作成するプロジェクト名] --template typescript"`

docker-composeをバックグラウンドで立ち上げる。(上記はプロジェクト立ち上げの最初だけ行う。立ち上げ後はここより下のコマンドを実行するだけでおけ。)

`docker-compose up -d`

コマンド実行後localhost:3000をブラウザで確認。反映されるまで数十秒かかる場合あり。

## 使用方法

- 自身のPCにこのレポジトリをcloneしてfrontend,backendともにREADMEに従ってコンテナを立ち上げる。
- backendのtemplateの中にlocal_settings.pyファイルを作成する。
- ターミナルで`docker-compose run web sh -c "cd template && python get_random_secret_key.py > local_settings.py"`
- chromeにmodheader拡張機能をインストールする。
- django側でcreatesuperuserでuserを作成する。
- postmanでユーザーネームとパスワードを以下のURLにPOSTリクエストで送る。<br>
`http://127.0.0.1:8000/auth/`
- `frontend/template/src/components/DrfApiFetch.jsx`の10行目`'Authorization': "Token ここにトークンを入力"`

のToken ここにトークンを入力の箇所にレスポンスのtokenを入力する。

- backendとfrontendでdocker-composeを起動させる。
- modheaderを開き、Nameに`Authorization`、Valueに`Token 取得したトークン`を入力する。
- `http://127.0.0.1:8000/api/tasks`に適当な値をdjangoの管理画面から登録。
- `http://127.0.0.1:3000`にreactのロゴとtasksに登録した値が表示される。

## 注意点

reactのコンテナでnpmコマンドを実行する場合(djangoの場合も同じ)

```bash
docker-compose run react sh -c "cd template && npm install axios"
```

のようにする。`cd template &&`がないとnode_modulesがないディレクトリでnmpコマンドを実行してしまう。

