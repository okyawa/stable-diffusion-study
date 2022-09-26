# StableDiffusionパイプラインの準備

from diffusers import StableDiffusionPipeline

device = 'cpu' # サンプルコードでは'cuda'になっているが、GPUが使えない場合は`cpu`を指定

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True)

pipe = pipe.to(device)

# テキストから画像生成

prompt = "cute cat paly with ball"

image = pipe(prompt)["sample"][0]

image.save("cat3.png")