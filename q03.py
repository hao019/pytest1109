from pkg.modu import print_json, process_data, read_json, write_json


def main():
    # 讀取菜單
    menu = read_json('menu.json')

    # 顯示原始菜單
    print_json(menu)

    # 新增主菜項目
    new_item = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
    menu['categories'][1]['items'].append(new_item)

    # 讓使用者輸入折數
    discount = float(input("請輸入折數(0.0 ~ 1.0): "))

    # 根據折數修改價格
    process_data(menu, discount)

    # 顯示修改後的菜單
    print_json(menu)

    # 寫入 output.json
    write_json(menu, 'output.json')


if __name__ == "__main__":
    main()
