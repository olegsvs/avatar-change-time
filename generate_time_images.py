import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 130
#130
TEXT_Y_POSITION = 1
TEXT_X_POSITION = 1
MOSCOW_UTC = 3 #for servers heroku

def convert_time_to_string(dt):
    dt += timedelta(hours=MOSCOW_UTC)
    return f"{dt.hour}:{dt.minute:02}"

def change_img():
#    W, H = (200, 200)
    W, H = (512,512)
    start_time = datetime.utcnow()
    text = convert_time_to_string(start_time)
    row = Image.new('RGBA', (512, 512), "black")
    parsed = ImageDraw.Draw(row)
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    _, _, w, h = parsed.textbbox((0, 0), text, font=font)
    parsed.text(((W-w)/2,  int(row.size[1]*0.35)), text, font=font, fill=(255,255,0))
#    parsed.text((int(row.size[0]*0.2), int(row.size[1]*0.35)), f'{text}', 
#                 align="center", font=font, fill=(255,255,0))
    row.save(f'time.png', "PNG")

if __name__ == '__main__':
    change_img()
