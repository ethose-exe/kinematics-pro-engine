# PRISM ENGINE v1.1 - Physics optimized
import pygame
import math
import random

# --- VIBRANT THEME CONFIG ---
WIDTH, HEIGHT = 1280, 720
CLR_BG = (15, 23, 42)        # Rich Deep Navy
CLR_ACCENT = (56, 189, 248)  # Sky Blue
CLR_PURPLE = (168, 85, 247)  # Electric Purple
CLR_PINK = (236, 72, 153)    # Hot Pink
G = 9.81

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ANUV.PRISM // KINEMATICS_V4")
clock = pygame.time.Clock()
font_hud = pygame.font.SysFont("Consolas", 16, bold=True)

class Particle:
    def __init__(self, pos, color):
        self.pos = list(pos)
        self.vel = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.life = 255
        self.color = color

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.life -= 8

def draw_vibrant_bg():
    # Subtle Radial Gradient effect (Visual Polish)
    for i in range(3):
        pygame.draw.circle(screen, (20, 30, 60), (WIDTH//2, HEIGHT//2), 600 - (i*100))

def main():
    u, angle = 85, 45
    time = 0
    points = [] 
    particles = []
    running, active = True, True

    while running:
        screen.fill(CLR_BG)
        draw_vibrant_bg()
        
        # Draw Technical Grid (Thinner & Blue-ish)
        for x in range(0, WIDTH, 60):
            pygame.draw.line(screen, (30, 41, 59), (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, 60):
            pygame.draw.line(screen, (30, 41, 59), (0, y), (WIDTH, y), 1)

        rad = math.radians(angle)
        t_f = (2 * u * math.sin(rad)) / G
        max_h = (u**2 * (math.sin(rad)**2)) / (2 * G)
        range_v = (u**2 * math.sin(2 * rad)) / G

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: u += 5
                if event.key == pygame.K_DOWN: u = max(5, u - 5)
                if event.key == pygame.K_RIGHT: angle = min(85, angle + 2)
                if event.key == pygame.K_LEFT: angle = max(5, angle - 2)
                if event.key == pygame.K_SPACE:
                    time, points, particles, active = 0, [], [], True

        # --- PHYSICS & PARTICLE GENERATION ---
        vx = u * math.cos(rad)
        vy_i = u * math.sin(rad)
        
        if active:
            px = (vx * time * 4.2) + 100
            py = (HEIGHT - 120) - (vy_i * time - 0.5 * G * time**2) * 4.2
            
            if py > HEIGHT - 120:
                py = HEIGHT - 120
                active = False
            else:
                points.append((px, py))
                # Add particles for that "spark" effect
                particles.append(Particle((px, py), CLR_ACCENT if time < t_f/2 else CLR_PINK))
                time += 0.04

        # --- RENDER TRAIL (Neon Gradient) ---
        if len(points) > 1:
            for i in range(1, len(points)):
                # Color flows from Blue to Pink
                perc = i / (len(points) if not active else 100)
                color = [int(CLR_ACCENT[j] + (CLR_PINK[j] - CLR_ACCENT[j]) * perc) for j in range(3)]
                
                # Dynamic trail width (gets thinner at the end)
                width = 4 if active and i == len(points)-1 else 2
                pygame.draw.line(screen, color, points[i-1], points[i], width)
                # Glow layers
                s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                pygame.draw.line(s, (*color, 50), points[i-1], points[i], 10)
                screen.blit(s, (0,0))

        # --- UPDATE & DRAW PARTICLES ---
        for p in particles[:]:
            p.update()
            if p.life <= 0:
                particles.remove(p)
            else:
                s = pygame.Surface((4,4), pygame.SRCALPHA)
                pygame.draw.circle(s, (*p.color, p.life), (2,2), 2)
                screen.blit(s, p.pos)

        # --- LUXURY HUD ---
        panel = pygame.Surface((280, 180), pygame.SRCALPHA)
        pygame.draw.rect(panel, (255, 255, 255, 20), [0, 0, 280, 180], border_radius=15)
        
        stats = [
            ("INIT_V", f"{u} m/s", CLR_ACCENT),
            ("ANGLE ", f"{angle}°", CLR_ACCENT),
            ("RANGE ", f"{range_v:.1f} m", CLR_PURPLE),
            ("HEIGHT", f"{max_h:.1f} m", CLR_PINK),
            ("STATUS", "TRACKING" if active else "LOCKED", (255, 255, 255))
        ]
        
        for i, (k, v, c) in enumerate(stats):
            t1 = font_hud.render(k, True, (148, 163, 184))
            t2 = font_hud.render(v, True, c)
            panel.blit(t1, (20, 30 + (i*25)))
            panel.blit(t2, (100, 30 + (i*25)))
        screen.blit(panel, (40, 40))

        # Neon Ground Line
        pygame.draw.line(screen, CLR_ACCENT, (0, HEIGHT-120), (WIDTH, HEIGHT-120), 3)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
