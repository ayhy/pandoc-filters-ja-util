pandoc-filters-ja-util
====

* pandoc lua filter for writing japanese novels (ruby tag, connected dashes), requires `pandoc 2.17` or above.
* these filter works with  html / epub output format.

### convert_ruby.lua
usage: `pandoc -L convert_ruby.lua`
* input:`｜本文《ふりがな》` -> output:`<ruby>本文<rt>ふりがな</rt></ruby>`
* ルビ開始記号`｜` or `|`、ふりがな開始記号`《`、ルビ終了記号`》`はカスタマイズできます。luaフィルタを開いて冒頭の変数を変更してください。
* luaの制約上、漢字・カタカナ・ひらがなの連続に開始記号なしでルビが振れる青空文庫の仕様には対応していません。

### elongate_dash.lua

usage: `pandoc -L elongate_dash.lua -C dash_horizontal.css` （when `writing-mode: horizontal-tb;`）

usage: `pandoc -L elongate_dash.lua -C dash_vertical.css` （when `writing-mode: vertical-lr;`）

* input:`――` -> output:`<span class="dash"><span class="dashline">―</span>　</rt></ruby>`
* ダッシュ（―）を表示フォントによる途切れをなくすために200%に伸ばして表示します。

## Licence
[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author
[ayhy](https://github.com/ayhy)