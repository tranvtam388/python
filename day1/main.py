import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Hàm để cập nhật ảnh động
def update(frame):
    ax.cla()  # Xóa trục trước khi vẽ khung hình mới
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # Vẽ Ngân hà xoay (Ví dụ: Hình tròn xoay)
    angle = frame * 5  # Góc xoay của Ngân hà
    x = 5 * frame * 0.1  # Di chuyển Ngân hà theo trục X
    y = 0  # Di chuyển Ngân hà theo trục Y

    ax.plot(x, y, 'o', markersize=10)
    ax.plot(0, 0, 'yo', markersize=100)  # Vẽ mặt trời ở tâm Ngân hà

# Tạo đối tượng figure và trục
fig, ax = plt.subplots()

# Tạo đối tượng animation
animation = FuncAnimation(fig, update, frames=range(100), interval=100)

plt.show()
# Hiển thị ảnh động
plt.show()
