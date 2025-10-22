import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def draw_info(frame, info,
              font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              font_size=28):

    img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font_path, font_size)

    for text, pos in info.get("texts", []):
        x, y = pos
        bbox = draw.textbbox((x, y), text, font=font)
        draw.rectangle(bbox, fill=(0, 0, 0))
        draw.text((x, y), text, font=font, fill=(255, 255, 255))

    frame = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    for (x1, y1), (x2, y2) in info.get("lines", []):
        cv2.line(frame, (x1, y1), (x2, y2), (200, 200, 200), 3) 

    img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)

    for (cx, cy), angle in info.get("angles", []):
        angle_text = f"{int(angle)} deg"
        bbox = draw.textbbox((cx, cy), angle_text, font=font)
        draw.rectangle(bbox, fill=(0, 0, 0))
        draw.text((cx, cy), angle_text, font=font, fill=(255, 255, 255))

    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)