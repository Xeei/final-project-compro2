import pygame as pg
class GameUtils:
    @staticmethod
    def load_card_image(image_path, target_height=150):
        image = pg.image.load(image_path).convert_alpha()  # use alpha for transparency
        width, height = image.get_size()
        aspect_ratio = width / height
        target_width = int(target_height * aspect_ratio)
        return pg.transform.smoothscale(image, (target_width, target_height))
    
    @staticmethod
    def load_image(image_path, target_height, target_width):
        image = pg.image.load(image_path).convert_alpha()
        return pg.transform.smoothscale(image, (target_width, target_height))
    
    @staticmethod
    def text_to_screen(screen, text, x, y, size=50, color=(200, 0, 0),
                    font_type='font/Playfair_Display/PlayfairDisplay-VariableFont_wght.ttf',
                    align="topleft"):
        try:
            text = str(text)
            font = pg.font.Font(font_type, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()

            if align == "center":
                text_rect.center = (x, y)
            else:
                setattr(text_rect, align, (x, y))

            screen.blit(text_surface, text_rect)

        except Exception as e:
            raise e