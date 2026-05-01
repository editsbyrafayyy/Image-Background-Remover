from PIL import Image
from super_image import EdsrModel, ImageLoader
import torchvision.transforms as T

def upscale(img: Image.Image, scale: int = 4) -> Image.Image:
    model = EdsrModel.from_pretrained("eugenesiow/edsr-base", scale=scale)
    model.eval()

    rgb = img.convert("RGB")
    inputs = ImageLoader.load_image(rgb)
    preds = model(inputs)

    upscaled = T.ToPILImage()(preds.squeeze(0).cpu().clamp(0, 1))

    alpha = img.split()[3].resize(upscaled.size, Image.LANCZOS)
    upscaled = upscaled.convert("RGBA")
    upscaled.putalpha(alpha)
    return upscaled