from sklearn.linear_model import LinearRegression

# ===========================================
# FILE NÀY: Huấn luyện mô hình (Backend)
# ===========================================

# 1. Dữ liệu huấn luyện
X = [[50, 1], [60, 2], [70, 2], [80, 3], [100, 3]]
y = [1500, 2000, 2300, 3000, 3800]

# 2. Huấn luyện mô hình
model = LinearRegression()
model.fit(X, y)
