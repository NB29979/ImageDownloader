# ImageDownloader
ターゲットとなるサイトの諸パラメータをsite_props.jsonに記述する．python3で動作．ターゲットのサイトに合わせ適宜コードは変更する必要がある．

## パラメータ
| パラメータ | 内訳 |
----|----
| SITE_NAME | サイトの区別のための適当な名前 |
| rss | サイトのRSSのURL |
| prev_link | 前回アクセス時のリンク |
| tag_attributes | URLの共通部分 |
| split_char | セパレータ |

## 依存モジュール
- selenium
- requests
- BeautifulSoup
- feedparser
