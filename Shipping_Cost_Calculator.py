# 配送料計算プログラム
# パッケージの重さと配送料率を入力する
weight = float(input("Enter the package weight in kilograms: "))  # パッケージの重さをキログラム単位で入力
rate = float(input("Enter the shipping rate per kilogram: "))  # 配送料率を1キログラムあたりの単価で入力

# 配送料を計算する
shipping_cost = weight * rate  # 重さと配送料率を掛け合わせて配送料を計算

# 計算結果を表示する
print(f"Shipping Cost: {shipping_cost} USD")  # 配送料を米ドルで表示
