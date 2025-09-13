from PIL import Image, ImageDraw, ImageFont

# Create a blank image (white background)
width, height = 500, 700
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Medal center coordinates
center_x, center_y = width // 2, height // 2 + 100
medal_radius = 120
medal_top = center_y - medal_radius

# --- Draw strap first (behind medal) ---
draw.polygon([(center_x - 80, medal_top),     # left attach point
              (center_x - 150, medal_top - 200),
              (center_x - 100, medal_top - 200),
              (center_x - 40, medal_top)], fill="PURPLE")

draw.polygon([(center_x + 80, medal_top),     # right attach point
              (center_x + 150, medal_top - 200),
              (center_x + 100, medal_top - 200),
              (center_x + 40, medal_top)], fill="PURPLE")

# --- Medal drawn on top (overlays strap edges) ---
draw.ellipse((center_x - medal_radius, center_y - medal_radius,
              center_x + medal_radius, center_y + medal_radius),
             outline="black", width=5, fill="gold")

draw.ellipse((center_x - 70, center_y - 70,
              center_x + 70, center_y + 70),
             outline="black", width=3, fill="lightyellow")

# --- Decorations ---
draw.ellipse((center_x - 50, center_y + 60, center_x - 30, center_y + 80),
             fill="white", outline="black")
draw.ellipse((center_x - 10, center_y + 80, center_x + 10, center_y + 100),
             fill="white", outline="black")
draw.ellipse((center_x + 30, center_y + 60, center_x + 50, center_y + 80),
             fill="white", outline="black")

# --- Text in the center ---
try:
    font_center = ImageFont.truetype("arial.ttf", 28)
    font_bottom = ImageFont.truetype("arial.ttf", 24)
except:
    font_center = ImageFont.load_default()
    font_bottom = ImageFont.load_default()

text = "Player\nof the\nMatch"
bbox = draw.multiline_textbbox((0, 0), text, font=font_center, spacing=5)
text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]

draw.multiline_text((center_x - text_w//2, center_y - text_h//2),
                    text, fill="black", font=font_center,
                    align="center", spacing=5)

# --- Name at the bottom ---
player_name = "RAÑISES"
bbox_name = draw.textbbox((0, 0), player_name, font=font_bottom)
name_w, name_h = bbox_name[2] - bbox_name[0], bbox_name[3] - bbox_name[1]

draw.text((center_x - name_w//2, height - 60),
          player_name, fill="black", font=font_bottom)

# --- Show and save ---
image.show()
image.save("CSELEC3_RañisesLearwinCyron_Activity1.png")

