# Sử dụng thuật toán local search giải quyết bài toàn Traveling Salesman Problem

Nhóm gồm có:  
1. Lê Trung Hiếu - 20021354  
2. Nguyễn Thị Thúy Quỳnh - 20021426  

Thiết lập bài toán với số lượng điểm cho trước sau đó có thể khởi tạo các điểm ngẫu nhiên hoặc nhập trước các tọa độ cho từng điểm.

~~~ python
# Tạo ra một số điểm ngẫu nhiên trong mặt phẳng
def create_random_points(num_points):
    points = []
    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        points.append((x, y))
    return points
~~~

Các bước thực hiện thuật toán local search để giải quyết TSP bao gồm:
1. Khởi tạo một giải pháp ban đầu: Chọn ngẫu nhiên hoặc sử dụng một thuật toán tìm kiếm cục bộ khác để tạo ra một đường đi ban đầu.

~~~ python
# Tạo ra một đường đi ban đầu ngẫu nhiên
def create_random_path(num_points):
    path = list(range(num_points))
    random.shuffle(path)
    return path
~~~

2. Tìm kiếm lân cận: Tìm kiếm tất cả các đường đi khác có thể được tạo ra bằng cách thay đổi một điểm trong đường đi hiện tại bằng một điểm khác.
3. Chọn đường đi tốt nhất: So sánh độ dài của các đường đi lân cận với đường đi hiện tại, và chọn đường đi có độ dài tốt nhất.
4. Lặp lại quá trình từ bước 2 cho đến khi không còn cách nào để cải thiện được đường đi.

~~~ python
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
~~~

Kết quả thực nghiệm với 50 điểm:
- Khởi tạo một giải pháp ban đầu (Initial Solution) có độ dài xấp xỉ 26.28
- Sau khi thực hiện thuật toán Local Search được quãng đường có độ dài gần như tối ưu xấp xỉ 8.3

![image](https://user-images.githubusercontent.com/78080006/221397094-f64487a5-e243-4c8b-8eac-1e176b8f58a2.png)
