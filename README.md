# recursion_filemanipulator
データストリームを使うコードやファイルの操作を行うコード集です。

## 概要
3つのpythonファイルがあります。question.pyとfile_manipulator.pyとfile_converter.pyです。

question.pyは数字あてゲーム用のコードです。
バックエンド開発環境の構築に慣れるために作成し、シンプルなCLI（コマンドラインインターフェース）スクリプトを作りました。Ubuntuをデュアルブートで使用し、Visual Studio Code、Python、そしてGitを利用して開発しました。PythonスクリプトをCLIを通じて実行すると、正しい回答が提供されるか、ゲームが終了するまで、標準入力から読み込み、標準出力に書き出します。

file_manipulator.pyはファイル操作のためのコードです。

file_converter.pyはmdファイルをhtmlに変換します。
## 作成の経緯
データストリームを使う練習とファイルの操作の練習で作成しました。
## 使用技術
Python
## 使用方法
### question.py
question.py は数字あてゲーム用のコードです。
ユーザーは最大値と最小値を入力し、ゲームが始まります。プログラムが用意した数字を10回以内に当てるとゲームクリアです。

### file_manipulator.py
file_manipulator.pyはファイル操作のためのコードです。
ユーザーは以下の4つのコマンドをターミナルに入力することでそれぞれの動作を実行することが出来ます。

・python3 file_manipulator.py reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。

・python3 file_manipulator.py copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。

・python3 file_manipulator.py duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。

・python3 file_manipulator.py replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

### file_converter.py
file_converter.pyはｍｄファイルをhtmlに変換します。コマンドは以下を使用して下さい
python3 file-converter.py markdown inputfile outputfile
