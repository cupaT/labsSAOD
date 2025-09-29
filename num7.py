import matplotlib.pyplot as plt
import numpy as np


def displace(p1, p2, roughness):
    mid = (p1 + p2) / 2
    mid[1] += np.random.uniform(-roughness, roughness)
    return mid


def draw_mountain(ax, p1, p2, p3, roughness, min_side):
    # Если треугольник достаточно маленький рисуем его
    if np.linalg.norm(p1 - p2) < min_side and np.linalg.norm(p2 - p3) < min_side and np.linalg.norm(p3 - p1) < min_side:
        ax.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color='grey', edgecolor='k')
        return
    # Находим середины сторон с шумом
    m12 = displace(p1, p2, roughness)
    m23 = displace(p2, p3, roughness)
    m31 = displace(p3, p1, roughness)
    # Рекурсивно рисуем 4 треугольника
    draw_mountain(ax, p1, m12, m31, roughness / 2, min_side)
    draw_mountain(ax, m12, p2, m23, roughness / 2, min_side)
    draw_mountain(ax, m31, m23, p3, roughness / 2, min_side)
    draw_mountain(ax, m12, m23, m31, roughness / 2, min_side)


if __name__ == "__main__":
    # Начальный большой треугольник
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, 0.8])
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_mountain(ax, p1, p2, p3, roughness=0.25, min_side=0.02)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()
