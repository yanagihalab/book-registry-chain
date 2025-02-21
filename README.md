# **Book (Novel) Registry-Chain DApp**

## **はじめに**  
**本ソースコードは、プロトタイプバージョンです。**  
**Book (Novel) Registry-Chain DApp** は、書籍（小説など）の情報をブロックチェーン上に
記録し、透明性と永続性を確保するための分散型アプリケーション（DApp）です。
本プロジェクトでは、**書籍の著作権や出版情報の管理、所有権の証明** などを
スマートコントラクトを活用して実現します。  
さらに、原稿の履歴やテキスト情報（手形）をブロックチェーンに記録することで、盗用や盗作を
防ぎ、著作者の権利を主張可能性を提供します。 

### **主な目的**  
- 書籍情報をブロックチェーン上に**永続的に記録**し、不正な改ざんを防ぐ  
- 著作権や出版情報を透明にし、**クリエイターや出版社の権利を保護**  
- NFT技術を活用し、**デジタル所有権の証明**を可能にする  
- ユーザーが書籍情報を**簡単に検索・検証できる**プラットフォームを提供  

### **主な機能**  
- 書籍情報の登録  
- 書籍情報の検索  
- 書籍情報の検証  
- NFT発行  
- 著作権管理  

### 今後追加予定機能
- XXXXXXXXX
- XXXXXXX 
- XXXXXXXX
- XXXXXXXX
- XXXXXX 

### リポジトリのファイル構造

```
📦 book-registry-dapp
├── 📂 frontend           # フロントエンド関連 (React, JavaScript)
├── 📂 templates
│     ├── login_test.html
│     ├── msg_test.html
│     ├── registration_test.html
│     ├── send.html
│     ├── send_test.html
│     ├── top_test.html
│     ├── user_test.html
│     └── view_test.html
│
│────── 📂 src
│       ├── 📂 components  # UI コンポーネント
│       ├── 📂 pages       # 各ページ
│       └── index.js       # エントリーポイント
│
├── 📂 backend            # バックエンド関連 (Flask)
│   ├── 📂 api            # API エンドポイント
│   ├── app.py           # メインアプリケーション
│   ├── requirements.txt  # Python 依存関係
│   └── README.md
│
├── 📂 contracts         # スマートコントラクト (CosmWasm)
│   ├── 📂 src           # スマートコントラクトのソースコード
│   ├── Cargo.toml       # Rust パッケージ設定
│   ├── schema.rs        # スマートコントラクトのスキーマ
│   └── README.md
├── .gitignore
├── README.md
└── LICENSE
```

### **技術スタック**  
| コンポーネント | 技術 |
|---------------|------|
| **フロントエンド** | React, JavaScript |
| **バックエンド** | Flask |
| **スマートコントラクト** | CosmWasm (Cosmos SDK) |
| **ブロックチェーン** | Cosmos Hub またはその他の Cosmos SDK 互換チェーン |

共有ソースコードのブロックチェーンは, [neutron](https://www.neutron.org/) を使用
---

## **システム構成**  
- **フロントエンド**: Webアプリケーションを通じて、ユーザーが書籍情報の登録や検索を行う  
- **バックエンド**: Flask を使用した API でデータを処理
- **DB**: ユーザー管理用のデータベース
- **スマートコントラクト**: CosmWasm を使用し、ブロックチェーン上でデータの管理・検証を実施  
- **ブロックチェーン**: Cosmos SDK 互換のネットワークで原稿データを記録  
---

## **コントラクトアドレス**  
| Deploy ネットワーク | コントラクトアドレス | Blockchain Explorer |
|----------------|--------------------------------|--------------------------------|
| **テストネット** | neutron14zpjn72zg7535nqgtv78l7uhl08qp664h0mlu5x422vqxxtrhgsqudtcz8 | [リンク](https://www.mintscan.io/neutron-testnet/wasm/contract/neutron14zpjn72zg7535nqgtv78l7uhl08qp664h0mlu5x422vqxxtrhgsqudtcz8/) |
| **メインネット** | neutron1fndrppflxqwsgnwrr3299n369t3d49fgwznq9cdvt6hk62nc2jgsh6sdhz | [リンク](https://www.mintscan.io/neutron/wasm/contract/neutron1fndrppflxqwsgnwrr3299n369t3d49fgwznq9cdvt6hk62nc2jgsh6sdhz/) |


## システム構成図


## **貢献**  
このプロジェクトへの貢献は大歓迎です。Pull Request を送信してください。  

---

## **参考資料**  
本ソースコードを実行するには、Cosmos SDK のブロックチェーン（BC）を操作するために `ABCI-CLI` が必要です。  
**ABCI-CLI（Application Blockchain Interface CLI）** は、CometBFT（旧Tendermint）に
関連するコマンドラインツールであり、ABCI メッセージの送信を通じてデバッグや開発を支援します。  
また、操作するブロックチェーンを選定し、適切に `ABCI-CLI` を準備する必要があります。  
本ソースコードでは、neutronの`neutrond`（ABCI-CLI） を利用しています。  
- [neutron](https://www.neutron.org/)  
- [neutrond リポジトリ](https://github.com/neutron-org/neutron)  
- [neutrond のインストールとチュートリアル](https://lab.stir.network/neutron-token-mint/)  
---

## **免責事項**  
この DApp は実験的なものであり、完全な保証はありません。  
このひな型をベースに、あなたのプロジェクトに合わせてカスタマイズしてください。  