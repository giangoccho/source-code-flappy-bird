import pygame
import sys
import random


print("sử dụng nút space để nhảy")
# Khởi tạo Pygame
pygame.init()

# Các biến cấu hình
WIDTH, HEIGHT = 600, 400
FPS = 30
GROUND_HEIGHT = 50
BIRD_SIZE = 30
PIPE_WIDTH = 50
PIPE_HEIGHT = 200
PIPE_GAP = 100
GRAVITY = 2
JUMP_VELOCITY = -20

# Màu sắc
WHITE = (255, 255, 255)
GREEN = (0,128,0)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)
# Tạo cửa sổ game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load hình ảnh
bird_img = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
bird_img.fill(WHITE)

pipe_img = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_img.fill(GREEN)

ground_img = pygame.Surface((WIDTH, GROUND_HEIGHT))
ground_img.fill(GREEN)

# Khởi tạo các đối tượng
bird = pygame.Rect(WIDTH // 4, HEIGHT // 2, BIRD_SIZE, BIRD_SIZE)
pipes = []
clock = pygame.time.Clock()

# Hàm vẽ đối tượng
def draw_objects():
    screen.fill(BLACK)

    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

    pygame.draw.rect(screen, WHITE, bird)
    pygame.draw.rect(screen, BROWN, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

    pygame.display.flip()


# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.y += JUMP_VELOCITY

    # Cập nhật vị trí của chim
    bird.y += GRAVITY

    # Tạo ống mới khi ống cuối cùng chỉ còn 1/2 màn hình
    if len(pipes) == 0 or pipes[-1].right < WIDTH / 2:
        pipe_height = random.randint(PIPE_GAP, HEIGHT - GROUND_HEIGHT - PIPE_GAP)
        top_pipe = pygame.Rect(WIDTH, 0, PIPE_WIDTH, pipe_height)
        bottom_pipe = pygame.Rect(WIDTH, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT - GROUND_HEIGHT - pipe_height - PIPE_GAP)
        pipes.append(top_pipe)
        pipes.append(bottom_pipe)

    # Di chuyển ống và xoá ống nếu chúng ra khỏi màn hình
    pipes = [pipe.move(-5, 0) for pipe in pipes if pipe.right > 0]

    # Kiểm tra va chạm với ống
    for pipe in pipes:
        if bird.colliderect(pipe):
            pygame.quit()
            sys.exit()

    # Kiểm tra va chạm với mặt đất hoặc trần nhà
    if bird.top <= 0 or bird.bottom >= HEIGHT - GROUND_HEIGHT:
        pygame.quit()
        sys.exit()

    # Vẽ các đối tượng
    draw_objects()

    # Đặt FPS và cập nhật cửa sổ
    clock.tick(FPS)
