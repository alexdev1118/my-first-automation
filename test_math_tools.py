from math_tools import calculate_discount

print("开始测试电商打折功能...")

# 测试案例：原价 100 元的东西，打 8 折（折扣率 0.2）
# 期望的结果应该是 80
final_price = calculate_discount(100, 0.2)

if final_price == 80:
    print("✅ 测试通过！折扣计算正确！")
else:
    # 如果算出来的不是 80，打印出具体的错误信息
    print(f"❌ 测试失败！期望得到 80，但实际算出来的是 {final_price}")
    # exit(1) 是告诉系统：程序异常崩溃了！这样 GitHub Actions 就会亮红灯。
    exit(1)
