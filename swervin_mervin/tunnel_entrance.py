import pygame
import settings as s

class TunnelEntrance:
    """Represents a Tunnel Entrance polygon."""

    def __init__(self):
        self.quantifier = 3

    def render(self, window, coords, clip):
        s_width    = s.DIMENSIONS[0]
        s_height   = int(s.TUNNEL_HEIGHT * coords["s"] * s.ROAD_WIDTH * self.quantifier)
        x          = 0
        y          = s.DIMENSIONS[1] - coords["y"] - s_height
        top_clip   = s.DIMENSIONS[1] - clip[1] - y

        if top_clip > 0:
            e_width  = coords["w"]
            e_height = int(s_height * 0.7)
            surf     = pygame.Surface([s_width, s_height], pygame.SRCALPHA, 32)
            surf     = surf.convert_alpha()
            points   = [(s_width, s_height),
                        ((s_width / 2) + (e_width / 2), s_height),
                        ((s_width / 2) + (e_width / 2), s_height - e_height),
                        ((s_width / 2) - (e_width / 2), s_height - e_height),
                        ((s_width / 2) - (e_width / 2), s_height),
                        (0, s_height),
                        (0, 0),
                        (s_width, 0)] 

            pygame.draw.polygon(surf, s.COLOURS["black"], points)
            window.blit(surf, (x, y), (0, 0, s_width, top_clip))