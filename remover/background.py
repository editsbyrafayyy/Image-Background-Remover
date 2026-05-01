from PIL import Image
from rembg import remove, new_session

def remove_bg(path: str) -> Image.Image:
    session = new_session("u2netp")
    
    with Image.open(path) as img:
        result = remove(
            img, 
            session=session,
            alpha_matting=True,
            alpha_matting_foreground_threshold=200,
            alpha_matting_background_threshold=20,
            alpha_matting_erode_size=10
        )
    
    if isinstance(result, Image.Image):
        return result.convert("RGBA")

    raise TypeError(f"Expected PIL Image from rembg, but got {type(result)}")