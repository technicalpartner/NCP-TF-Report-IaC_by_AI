import os
import glob

# ファイル結合後にPandocでPDFを出力
import subprocess

def combine_markdown_files():
    # カレントディレクトリの.mdファイルを取得（サブディレクトリは除外）
    md_files = glob.glob('../report/*.md')
    
    # ファイル名でソート
    md_files.sort()
    
    # 出力ファイルを開く
    with open('../report_all/report.md', 'w', encoding='utf-8') as outfile:
        for i, md_file in enumerate(md_files):
            # ファイルを読み込む
            with open(md_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                
                # ファイルの内容を書き込む
                outfile.write(content)
                
                # 最後のファイル以外は改ページを挿入
                if i < len(md_files) - 1:
                    outfile.write('\n\n<div style="page-break-after: always;"></div>\n\n')

if __name__ == '__main__':
    combine_markdown_files()

