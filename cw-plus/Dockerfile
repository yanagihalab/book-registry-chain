# Rustの公式イメージ（最新の安定版）を使用
FROM rust:latest

# 作業ディレクトリの設定
WORKDIR /usr/src/myapp

# ソースコードをコンテナにコピー
COPY . .

# 依存関係をダウンロードしてキャッシュを活用
RUN cargo build --release

# 実行コマンドを指定
CMD ["./target/release/myapp"]


