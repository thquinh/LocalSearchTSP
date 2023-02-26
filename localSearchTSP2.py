import random
import math
import matplotlib.pyplot as plt

# Tạo ra một số điểm ngẫu nhiên trong mặt phẳng
def create_random_points(num_points):
    points = []
    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        points.append((x, y))
    return points

# Tính khoảng cách Euclid giữa hai điểm
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Tính tổng độ dài của một đường đi
def path_length(points, path):
    length = 0
    for i in range(len(path)):
        j = (i + 1) % len(path)
        length += distance(points[path[i]], points[path[j]])
    return length

# Tạo ra một đường đi ban đầu ngẫu nhiên
def create_random_path(num_points):
    path = list(range(num_points))
    random.shuffle(path)
    return path

# Hàm thực hiện thuật toán local search
def local_search(points, path):
    best_path = path
    best_length = path_length(points, path)
    improved = True
    while improved:
        improved = False
        for i in range(len(path)):
            for j in range(i + 1, len(path)):
                new_path = path[:]
                new_path[i], new_path[j] = new_path[j], new_path[i]
                new_length = path_length(points, new_path)
                if new_length < best_length:
                    best_path = new_path
                    best_length = new_length
                    improved = True
        path = best_path
    return best_path, best_length

# Vẽ đường đi trên mặt phẳng
def plot_path(points, path):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x, y, 'bo')
    for i in range(len(path)):
        j = (i + 1) % len(path)
        plt.plot([points[path[i]][0], points[path[j]][0]], [points[path[i]][1], points[path[j]][1]], 'g-')
    plt.axis('equal')

# Số lượng điểm
num_points = 50

# Tạo ra các điểm ngẫu nhiên
points = create_random_points(num_points)

# Tạo ra một đường đi ban đầu ngẫu nhiên
path = create_random_path(num_points)
print("Initial path length:", path_length(points, path))
plt.title("Initial solution") 
plot_path(points, path)

# Thực hiện thuật toán local search để cải thiện đường đi ban đầu
best_path, best_length = local_search(points, path)

# In kết quả và vẽ đường đi trên mặt phẳng
print("Shortest path length found:", best_length)
plt.figure()
plt.title("Final solution")
plot_path(points, best_path)
plt.show()