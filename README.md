pandoc-filters-ja-util
====

* pandoc utilities for writing JP text (aozora format ruby, JP style line break/paragraph,  etc)
* panfluteで書かれた日本語markdownに関するフォーマットを変更するフィルタの詰め合わせです。以下のフィルタを含みます。
  * `panflute-aozora-ruby`
    * 青空文庫記法の`|漢字《ルビ》`を`<ruby>漢字<rt>ルビ</rt></ruby>`に変換するフィルタ（※[haskel版](https://github.com/minoki/pandoc-aozora-ruby)は既に存在するので車輪の再発明です）
  * `panflute-linebreak-paragraph`
    * pandocのオプション `-t markdown+hard_line_breaks` で改行を`<br />`に変更できますが、これを段落切り替え`</p><p>`に変換するフィルタ
  * `panflute-horizontal-dash`, `panflute-vertical-dash`
    * ダッシュ（―）を表示フォントによる途切れをなくすために罫線（─ or │）に変更するフィルタ

## Prerequisite
* Python 3.x系
* panflute module

## Usage
1. フィルタを適当にpathの通っているところに置く
2. 使いたいフィルタを次のように
```pandoc --filter panflute-linebreak-paragraph.py```


## Licence
[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author
[ayhy](https://github.com/ayhy)