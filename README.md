# Stable Diffusion のMacローカル環境検証

![Python Version Badge](https://img.shields.io/badge/Python-3.8.5-blue.svg)

## Hugging Face での設定

- [Hugging Face](https://huggingface.co/) のサイトに登録してアカウントを作成
- [Stable Diffusionのページ](https://huggingface.co/CompVis/stable-diffusion-v1-4) にアクセスし、 `I have read the License ang agree with its terms` のライセンス同意にチェックを入れてから、 `Access repository` をクリック
- [Hugging FaceのAccess Token](https://huggingface.co/settings/tokens) 画面からトークンを発行

## セットアップ

```sh
pip install -r requirements.txt
```

### Hugging Faceのトークン指定

- ローカルPCで以下のコマンドを実行し、Hugging FaceのTokenを入力

```sh
huggingface-cli login
```

- 下記のエラーが表示されたら、指示通り `git config --global credential.helper store` を実行し、再度ログインを実行
> Authenticated through git-credential store but this isn't the helper defined on your machine.
You might have to re-authenticate when pushing to the Hugging Face Hub. Run the following command in your terminal in case you want to set this credential helper as the default
> 
> git config --global credential.helper store

- 無事ログインが成功すると、 `~/.huggingface/token` にトークン情報が保存された旨の完了メッセージが表示される

## 実行

- ローカル環境のMacがGPUを使って実行できない環境のため、CPUで実行するため、完了までにかなり時間がかかる

```py
python demo.py
```
