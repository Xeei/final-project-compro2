import pygame as pg
class GameUtils:
    @staticmethod
    def load_card_image(image_path, target_height=150):
        image = pg.image.load(image_path).convert_alpha()  # use alpha for transparency
        width, height = image.get_size()
        aspect_ratio = width / height
        target_width = int(target_height * aspect_ratio)
        return pg.transform.smoothscale(image, (target_width, target_height))