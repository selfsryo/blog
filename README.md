# blog
DjangoとVue.js製のブログのサンプルです。


## 概要
・Djangoのアドミンページから記事を投稿できます。

<br>


## 確認バージョン
| docker | docker-compose |
:---:|:---:
| 19.03.13 | 1.27.4 |

<br>


## 環境構築
・リポジトリをクローン
```
git clone https://github.com/selfsryo/blog
```

・バックグラウンドでコンテナ立ち上げ&ビルド
```
docker-compose up -d --build
```

・マイグレート
```
docker-compose run --rm web python3 manage.py migrate
```

・管理者作成
```
docker-compose run --rm web python3 manage.py createsuperuser
```

・以下URLからアドミンページに遷移。記事を登録します。
```
http://127.0.0.1:8000/admin/
```

・（上記でコンテナを起動した状態で）Vueのコンテナに入る
```
docker exec -it vue /bin/bash
```

・移動
```
cd vue_blog/
```

・パッケージインストール
```
npm install
```

・開発サーバー起動
```
npm run serve
```

・以下URLでページ表示
```
http://127.0.0.1:8080/
```

<br>

### 特記事項
・ブログはMarkdownを採用しており、見出しの作成を前提としているため、本文の一番最初に`[TOC]`という文字を記述する必要があります。
