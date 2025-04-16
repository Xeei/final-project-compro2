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
    def text_to_screen(screen, text, x, y, size=50, color=(255, 255, 255),
                    font_type='font/Playfair_Display/PlayfairDisplay-VariableFont_wght.ttf',
                    align="topleft",
                    draw_border=False,
                    border_color=(255, 255, 255),
                    border_thickness=2,
                    padding=10,
                    border_radius=10):
        try:
            text = str(text)
            font = pg.font.Font(font_type, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()

            if align == "center":
                text_rect.center = (x, y)
            else:
                setattr(text_rect, align, (x, y))

            if draw_border:
                border_rect = pg.Rect(
                    text_rect.left - padding,
                    text_rect.top - padding,
                    text_rect.width + padding * 2,
                    text_rect.height + padding * 2
                )
                pg.draw.rect(screen, border_color, border_rect, border_thickness, border_radius)

            screen.blit(text_surface, text_rect)

        except Exception as e:
            raise e
