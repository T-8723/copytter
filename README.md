# Twitter モドキ作成

学習のための試作プロジェクトのため、ツッコミどころ、詰めが甘いところなど多々あるかと思いますが寛容な目で見て頂ければ幸いです。

- [Twitter モドキ作成](#twitter-モドキ作成)
  - [目的](#目的)
  - [課題](#課題)
  - [要件](#要件)
  - [構成](#構成)
  - [現状](#現状)
    - [2021/11/27](#20211127)
  - [設計・備忘録](#設計備忘録)
    - [環境](#環境)
      - [Googke AppEngne の使い方マジでわからん](#googke-appengne-の使い方マジでわからん)
      - [デプロイまでのざっくりした流れ](#デプロイまでのざっくりした流れ)
      - [心臓に悪い](#心臓に悪い)
    - [Django](#django)
      - [はじめての Django](#はじめての-django)
      - [モデル設定](#モデル設定)
      - [ドキュメント生成](#ドキュメント生成)
      - [備忘録・詰まったとこ](#備忘録詰まったとこ)
        - [django-allauth](#django-allauth)
        - [django-cors-headers](#django-cors-headers)
        - [django-environ](#django-environ)
        - [djangorestframework、djangorestframework-jwt](#djangorestframeworkdjangorestframework-jwt)
    - [Vue](#vue)
      - [初めての Vue.js](#初めての-vuejs)
      - [お作法](#お作法)
      - [TypeDoc との連携](#typedoc-との連携)
      - [デザイン](#デザイン)
      - [openapi-generator-cli すごい](#openapi-generator-cli-すごい)
  - [(一応)プロジェクトの使い方](#一応プロジェクトの使い方)
  - [開発・デプロイまでの流れ](#開発デプロイまでの流れ)

## 目的

1. 流行りのクラウド環境下での開発の知見を得る

2. Node.js 以外の環境での開発を行う

3. ~~最近すっかり住みづらくなった Twiter を倒して陰キャーネットの覇権コミュニケーションツールを作る~~

## 課題

1. Node.js 以外の言語の習得

2. 後々の言語学習で使用できるよう代替しやすいような綺麗な構造の REST API 準拠のシステムを作る

3. Google Cloud Platform (GoogleAppEngine など)の使い方を把握する


## 要件

1. アプリケーションの基本構成は以下の通り

   - クラウドプラットフォーム： [Google Cloud Platform](https://cloud.google.com/gcp/)
   - サービス： [AppEngine](https://cloud.google.com/appengine/)
   - フロントサイド： [Vue.js 3(TypeScript)](https://v3.ja.vuejs.org)
   - バックエンド: [django(Python)](https://docs.djangoproject.com/ja/3.2/)
   - DB-MySQL： [Goolge Cloud SQL](https://cloud.google.com/sql/)

2. Twiter のミニブログサービスとしての最低限の要素を実装する。

   - タイムライン
     - 最大文字数 300 文字を上限とした記事投稿機能
     - メディア（画像・できれば動画）投稿機能
     - フォローしている投稿者の記事閲覧機能
     - 投稿検索機能
   - ユーザーアカウント管理機能
     - フォロー、フォロワー一覧閲覧機能
     - ユーザー検索機能
   - ~~Google・Twiter と連携したソーシャルログインの実装~~ 今回はとりあえず保留

3. 課題 1 後の代替を意識してドキュメント自動生成ツールを使用して設計ドキュメントをなるべく簡単に出力できるようにする。

   - フロントサイド： TypeDoc
   - バックエンド： OpenAPI

## 構成

- app : アプリケーション本体
  - api : Django API サーバー
    - config : サーバー基本設定
    - copytter : サーバー本体
  - client : Vue クライアントアプリケーション
    - public : index.html などの静的ファイル
    - app : アプリケーション本体
      - App : ベースコンポーネント
      - common : プロジェクト内共通部品
      - views : 画面
        - components : 各画面コンポーネント
          - Auth : ログイン画面
          - Home : ホーム画面
          - Profile : ユーザープロフィール初期登録画面
          - Relation : フォロー・フォロワー管理画面
          - Search : 投稿・ユーザー検索画面
        - router : Vue 側ルーティング定義
- docs : 関連ドキュメント


## 現状

### 2021/11/27

アプリケーションの基本構成（Google Cloud Platform へのデプロイ、Cloud Platform でのサービス有効化、フロント・バックエンドの環境構築、バックエンドのＤＢ連携）は一通り完了して、実際に[Google上のページ](https://copytter.an.r.appspot.com/Home)でアクセス可能な状態です。  
本来であれば、ログイン → 閲覧 → 投稿 のあたりまで作成して公開すべきかと思いましたが、とりあえずログインと閲覧の動作確認ができる程度の完成度です…  
今後も少しずつ手を入れていくつもりです。


## 設計・備忘録

### 環境

#### Googke AppEngne の使い方マジでわからん

Google のドキュメントは量も多いしワードも難解…自分のオツムに呆れます。  
[公式ガイド](https://cloud.google.com/python/django?hl=ja)通りにやったつもりが何故かエラーが頻発しました。  
幸いにも Django + GAE 環境での開発はそこそこ先駆者がいるようで、参考にさせて頂きなんとかデプロイできました。

ありがたき先人方

- [https://qiita.com/waka424/items/67b52631991660799bde](https://qiita.com/waka424/items/67b52631991660799bde)
- [https://qiita.com/MaxBaconPower/items/89b18c608dc7dd2b946b](https://qiita.com/MaxBaconPower/items/89b18c608dc7dd2b946b)

#### デプロイまでのざっくりした流れ

基本的に[公式](https://cloud.google.com/python/django/appengine?hl=ja#header)に沿って実行。

1. プロジェクトの作成
   - ![スクショ 1](./docs/img/gcp_01.png '画面上部をクリック')
   - ![スクショ 2](./docs/img/gcp_02.png 'プロジェクトを作成')
   - ![スクショ 3](./docs/img/gcp_03.png '命名、作成')
2. プロジェクトで使用するサービスの有効化
   - ![スクショ 4](./docs/img/gcp_04.png '左側メニューから使用するサービスをクリック')
   - 有効化するサービスは、App Engne、Cloud SQL、Secret Manager など
3. SDK のダウンロード、インストール
   - [ダウンロード](https://cloud.google.com/sdk/docs/install?hl=ja)
4. django プロジェクトの作成
5. app.yaml の記述
6. デプロイコマンドの実行

#### 心臓に悪い

この時点で請求金額は 300 円…クラウドは心臓に悪い…  
※ 個人的に YoutubeDataAPI でデータ収集してたりしていて前から使用していたので課金対象でしたが、本来は試用クレジットがあります。

Cloud SQL は最安価の構成で組みましたが、**放置でも請求が発生するようなので**、１２月中だけ動かしてみていったん止めます。

### Django

#### はじめての Django

あまり DB を意識せず実装ができるフレームワークのようで、恥ずかしながら SQL 周りには疎い自分には助かりました。
アプリケーションの構成としては、

- \[プロジェクト]
  - settings.py : サーバー設定モジュール
  - ulrs.py : 大元の URL 定義。管理用の URL などをここで定義して、アプリケーション側の urls を読み込む
- \[アプリケーション]
  - model.py : データ定義全般を記述する部分
  - serializers.py : DB への橋渡し役？ 調査中
  - urls.py : API の URL 定義
  - views.py : API 実処理

といった感じでしょうか。  
サーバー側は基本的なところから勉強不足なので、ちょくちょく調べて行こうと思います。  
とりあえずインストールした拡張ライブラリは以下の通り。

- django
- django-filter : URL パラメータから QuerySet を動的にフィルタリングできるようにしてくれる
- django-allauth : ユーザー認証実装のため
- django-cors-headers : 開発環境で localhost:8080(vue)から localhost:8000(django)へリクエストを許可するため
- django-environ : 環境内の機密情報を外部化するため
- djangorestframework : Django を REST API 発行に最適化するライブラリ
- djangorestframework-jwt : JSON WEB-token 認証用ライブラリ
- mysqlclient : mysql 連携
- Pillow : 画像アップロードに必要
- flake8 : フォーマッター
- gunicorn : 何者…？

#### モデル設定

基本的に作りながら調べて設計に起こす、みたいな流れで作っているため、設計書的なものを作る練習もいずれしないとな…と思う今日この頃…  
とりあえず最低限このくらいはいるかなーと思って定義して、これが足りないあれが足りない…と継ぎ足しした結果、最終的に落ち着いたのは下記の通りです。

- Profile モデル : ユーザーに紐づいて作成されるユーザープロフィールの情報。ユーザーは Django の機能使って自動生成しているのでカスタマイズするには色々ノウハウがあるようなのですが、今回は User の生成と同時に連携したデータを生成するような流れにしました。デフォルトの User に登録される情報はパスワードやメールアドレスなど機密性の高い情報なので弄らず、Twiter で言うところのフォロワー数やアイコン画像のような公開情報を別管理とすることで、一覧検索なども実装しやすいと思われたのも理由の一つです。
- Follow モデル : フォロー関係の関係性情報。「この人はこの人をフォローしている」というデータを蓄積していき、更新時に Profile のカウントだけ操作する形にしました。
- Entry モデル : 投稿本文定義。リツイート機能のために relation_id を設定。ここに Entry の id が指定されかつ本文が殻ならリツイート、本文ありなら引用リツイートといった形を実現します。
- Media モデル : ツイートに付属するメディア情報定義。メディアのタイプとアップロード先の URL を設定します。

#### ドキュメント生成

REST API ドキュメントを生成するにあたってよく見るものとして OpenAPI などよく聞くので使用してみます。  
OpenAPI は API スキーマ（どのような URL にどのようなリクエストを送ればどのようなレスポンスが返ってくるかという API の定義を記述したもの）の仕様のことを指すようです。  
OpenAPI 仕様で出力されたスキーマ定義をもとにドキュメント生成を行うのが API ドキュメンテーション機能と呼ばれ、今回使用する Django REST Framework では drf-spectacular というライブラリでドキュメンテーション機能が使用可能になります。

[参考](https://akiyoko.hatenablog.jp/entry/2020/12/08/120230)

インストールして、下記設定を追加

```setting.py
INSTALLED_APPS = [
    ...（略）...

    'drf_spectacular',  # 追加

    ...
]

...

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # 追加
}
```

スキーマ定義ファイル生成  
`python manage.py spectacular --file schema.yml`

API ドキュメント画面を自動生成

```urls.py
rom django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView  # 追加

urlpatterns = [
    ...（略）...
]

if settings.DEBUG:
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),                                      # 追加
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # 追加
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),              # 追加
    ]
```

これで <http://127.0.0.1:8000/api/schema/swagger-ui/>にアクセスすれば Swagger UI 形式の API ドキュメント画面、<http://127.0.0.1:8000/api/schema/redoc/>にアクセスすれば ReDoc 形式の API ドキュメント画面を表示することができます。

#### 備忘録・詰まったとこ

##### django-allauth

Django はデフォルトでユーザー管理の機能がありますが、それを拡張してユーザー側からログイン・ログアウトなどの操作を行うような機能を提供するライブラリです。（使用しないかも？）

こいつをインストールした途端に/admin でアクセスできるはずの管理画面にアクセスできなくなりました。  
結論、どうやら管理画面の URL に変更がかかるようで、追加される setting 項目に SITE_ID を設定してやらないと変更後の管理画面へアクセスできなくなる模様。

##### django-cors-headers

今回は開発環境として vue 側も django 側もホットリロードが可能なローカルサーバーの立ち上げが可能なので、vue から呼び出しができるようにしておきます。  
そのまま飛ばすと CORS Origin ではじかれるため、このライブラリで追加される setting 項目の CORS_ORIGIN_WHITELIST に <http://localhost:8080> を追加しておきます。  
ただこのまま GAE にデプロイするわけにはいかないので、`os.getenv('GAE_APPLICATION', None)`で分岐をかけました。

##### django-environ

setting 内には SECRET_KEY や DATABASES-PASSWORD などソースに乗せるべきでない情報が載っているため、.env ファイルに外部化して、.env ファイルは Git 等の監視対象から外すのが一般的な用法のようです。  
GCP もこの方式で機密情報を管理できるようになっていて、GCP の Secret Manager では django_settings という名前で Secret を作成すると、デプロイされたパッケージから.env ファイルとして自動で読み込んでくれます。

.env ファイルでハマったとことして、DB 接続時のパスワードに$や#などの記号を使う場合、Pythonでは$をコマンド呼び出しの予約語（？）として認識するようで、ローカルサーバー立ち上げのタイミングでパスワードとして設定した値がコマンドとして実行されエラーが発生します。  
当然エスケープ文字 \ を入力するわけですが、ここで問題発生。  
Cloud SQL のローカルテスト用に実行する cloud_sql_proxy.exe から接続が閉じられたというエラーが出て、またもやローカルサーバーが起動不可になりました。  
どうやら cloud_sql_proxy.exe 側（Python 側？）では\を文字として認識しているようで、お手上げ状態となりました。  
パスワードに記号が使えないというのは最近の風潮としては疑問が残る部分ではありますが、とりあえずユーザーに見える場所ではないので保留としてます。

##### djangorestframework、djangorestframework-jwt

Django を REST API サーバーとして設定するのに最適な機能を提供するライブラリのようです。  
今回は未ログインユーザーは閲覧のみ、ログイン済みユーザーは投稿機能も実装するといった機能を持たせたいので、認証情報の発行のために JWT でトークンを発行できる拡張の djangorestframework-jwt もインストールしました。  
allauth の方ではソーシャルログインなども対応してますが、こちらはどう実装したらいいのか今のところ見当もつかず…  
認証系の話もまだまだ不勉強なので色々調べてみたいとは思います。

発行するトークンの設定は settings.py に JWT_AUTH を定義して色々設定できるようです。色々調整すべきかと思いますが、とりあえずテキトーに…

### Vue

#### 初めての Vue.js

フロントサイドフレームワークは Angular をメインでやってきましたが、業務で使う機会があり採用。  
三大フレームワークくらいは抑えておこうと思ってたので丁度よかったです。そのうち React で置き換えてみたいと思います。  
テンプレート、スクリプト、スタイルシートが一つのファイルでシンプルに収まるので、中小規模でパパっと作りたいみたいなケースでは有用なのかなと思います。  
ただ Angular と比較して余計な機能が省略されている分、徐々に規模が大きくなるようなプロジェクトとなると後々パッケージ入れたりみたいな作業が面倒くさいのかな…？と思いました。  
TypeScript との相性も Angular の方がいいイメージで、型をきっちり嵌めていくためには自分で定義してやらないといけない部分が多い気がします。
インストールした追加パッケージは下記の通り。

- vue
- vue-axios : Vue 向けに最適化された axios ライブラリ
- vue-class-component : class-style コンポーネント作成のためのライブラリ
- vue-router : Router 機能ライブラリ
- vuex : 状態管理ライブラリ
- axios : API 通信用ライブラリ
- core-js
- element-plus : UI コンポーネントライブラリ
- @element-plus/icons : element-plus の icon ライブラリ
- @openapitools/openapi-generator-cli : OpenAPI スキーマ定義からコードを自動生成するライブラリ

#### お作法

vue の書き方として大まかに 2 種類あるようです。

- Object-Stlye
- Class-Stlye

data() や porps をオブジェクト形式で列挙していく書き方を前者、クラスとしてプロパティや関数を定義するものを後者と呼ぶようです。  
[公式リファレンス](https://v3.ja.vuejs.org/guide/introduction.html)では Object-Stlye に沿った説明がなされています。  
が、使用されてきた長さとしては [Class-Stlye](https://class-component.vuejs.org) の方が長く、ドキュメントも多いとのこと。
どちらに準拠するかは現段階では読みやすさやドキュメントの多さといった違いしかないようなので、今回は Angular に近しい後者の Class-Stlye で記載しています。

```HelloWorld.ts - Object-Stlye
export default {
  components: { RepositoriesFilters, RepositoriesSortBy, RepositoriesList },
  props: {
    user: {
      type: String,
      required: true
    }
  },
  setup(props) {
    console.log(props)
    return {}
  }
}
```

```HelloWorld.ts - Class-Stlye
import { Options, Vue } from "vue-class-component";

@Options({
  props: {
    msg: String,
  },
})
export default class HelloWorld extends Vue {
  msg!: string;
}
```

#### TypeDoc との連携

TypeDoc ではどうやっても.vue の中身を ts ファイルとして読み込むことはできないので、.ts ファイルとして独立させることで読み込ませました。  
今回は保守性の観点を優先してコマンド一つで TypeDoc のドキュメントを出力できるようにするため、通常の単一コンポーネントの書き方から TypeScript 部分のみファイルを切り出して配置します。  
最初に触ったフロントサイドフレームワークが Angular だったため、このスタイルはだいぶしっくりきました。ただ、Vue 本来のシンプルさは失われたのであまり好まれない構成ではありそうです。

- CLI 生成後の構成

```構成

view
 - HelloWorld.vue

```

```HelloWorld.vue
<template>...</template>

<script lang="ts">
    export defalut defineComponent({
        Props: {
            msg: {
                type: String,
                require: true,
                default: "HelloWorld."
            }
        }
    })
</script>

<style>...（略）...</style>
```

- 今回構成

```構成

view
 - HelloWorld.vue
 - HelloWorld.ts
```

```HelloWorld.vue
<template>...（略）...</template>

<script src="./HelloWorld.ts" lang="ts"></script>

<style>...（略）...</style>
```

```HelloWorld.ts
export const props: Props<strig> = {
    msg: {
        type: String,
        require: true,
        default: "HelloWorld."
    }
};

export const component = defineComponent({
    props: props,
});

export defalut component;
```

TypeScript のファイルが Vue から分離できたので、TypeDoc 側で.ts ファイルとしてこれらのファイルが認識されます。  
あとは関数や変数に JavaDoc（TypeDoc）に準拠したコメント（@param や@returns の型情報は書かなくても自動で記載）を記載すれば、整ったドキュメントを生成してくれます。

この辺は正直 Vue に最適化されたドキュメント生成ツールなど他にもありそうですが、html など開発者以外に展開しやすい形で出力するツールが見当たらなかったため TypeDoc を採用しているといった感じです。

#### デザイン

CSS を０から書く気力はなかったので、ＵＩコンポーネントとして [Vuetify](https://vuetifyjs.com/ja/) を使用します。  
…と思いきやどうやら今回使用の Vue 3 にはまだ対応していない（開発版のみ？）のようでうまくインストールできず…  
代わりに[element-plus](https://element-plus.org/en-US/) を使用します。

#### openapi-generator-cli すごい

Django 側で生成した OpenAPI スキーマ定義から TypeScript 向けの API 型定義が出力できるとのことで導入してみました。  
ざっくり呼んだ時点では interface 定義ファイルを出力できる CLI アプリケーションなのかな？と思いきや、なんと API 送信のための関数まで自動生成してくれるという優れもの。

インストール  
`npm install @openapitools/openapi-generator-cli -D`

```package.json
  "scripts": {
    ...（略）...
    "openapi:gen": "openapi-generator-cli generate -g typescript-axios -i ../api/schema.yml -o ./src/common/services/openapi"
  },
```

これで、../api/schema.yml のスキーマ定義 YAML ファイルから生成したコードを/src/common/services/openapi 配下に生成してくれます。  
めちゃくちゃ便利。若干手動修正も必要な感じの記載もありますが、とりあえず今まこの状態で使えそうなので OK。

[参考](https://kimuson.dev/blog/django/drf_serializer_auto_type/)

```Home.ts
...（略）...
import { ApiApi, AuthApi } from "@/common/services/openapi";

@Options({
  components: { Entry },
})
export default class Home extends Vue {
  url = process.env.NODE_ENV === "production" ? "." : "http://localhost:8000";
  API = new ApiApi(undefined, this.url);
...（略）...

  mounted(): void {
    this.requestEntriesList();
  }

  requestEntriesList(): void {
    this.API.apiEntriesList().then((item) => {
      console.log(item);
    });
  }

...（略）...
}

```

![結果](./docs/img/openapi_vue_1.png 'コンソール')

これでもうバックエンドとの通信部分はほぼ書くことがなくなりました。

…と思いきや問題発生。  
自動生成された認証トークン取得 API を要求する authCreate 関数でレスポンス型が実態と一致しない現象が発生しました。  
レスポンス型にリクエスト型が割振られていて token の値が読めないという致命的な不整合が生じていました。  
確認しているのはこの関数だけなので、Django 側のライブラリ間での相性かバグのようですが、とりあえず TypeScript 側で強引に型を貼り直しました。  
as は型の安全性を損なうのでなるべく使用したくないのですが致し方なし…

```Auth.ts

this.API_auth.authCreate({
  username: this.form.username,
  password: this.form.pass,
})
  .then((response) => {

    /** なぜか openapi-generator-cli で生成したレスポンス型のここだけ実態と違う */
    const responseData = response.data as unknown as { token: string };

    ...（略）...
  })
  .catch(() => {
    ...（略）...
  });

```

## (一応)プロジェクトの使い方

Python3、NodeJS をインストール済みとして想定

1. GCP の環境を設定する-[参考](https://cloud.google.com/python/django/appengine?hl=ja)
2. 上記、cloud_sql_proxy.exe を app/api/配下に配置する
3. API 側、Clinnt 側で別ウィンドウで VSCode を立ち上げ
4. API : DB ローカル接続設定 `../../../cloud_sql_proxy -instances=[project nmae]:[Cluod SQL instance]:5432`
5. API : Django ローカルサーバー立ち上げ `python manage.py runserver`
6. Client : npm パッケージ依存関係インストール `npm install`
7. Client : Vue ローカルサーバー立ち上げ `npm run serve`

## 開発・デプロイまでの流れ

1. モデル（models.py）でデータモデルを定義・修正
2. マイグレーション`python manage.py makemigrations` `python manage.py migrate` を実行
3. スキーマ定義 YAML の出力 `python manage.py spectacular --file schema.yml`
4. スキーマ定義からクライアント側からの API 呼び出しコードを生成 `npm run openapi:gen`
5. 画面を作成
6. クライアントアプリケーションのビルド `npm run build`
7. GCP にデプロイ `gcloud app deploy --project=copytter`
