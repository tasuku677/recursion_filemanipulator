# recursion_filemanipulator
recursion filemanipulatorプロジェクト用

2つのpythonファイルがあります。question.pyとfile_manipulator.pyです。
quetion.py は数字あてゲーム用のコードです。
ユーザーは最大値と最小値を入力し、ゲームが始まります。プログラムが用意した数字を10回以内に当てるとゲームクリアです。

file_manipulator.pyはファイル操作のためのコードです。
ユーザーは以下の4つのコマンドをターミナルに入力することでそれぞれの動作を実行することが出来ます。
・python3 file_manipulator.py reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
・python3 file_manipulator.py copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
・python3 file_manipulator.py duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
・python3 file_manipulator.py replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
