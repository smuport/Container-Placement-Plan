import pandas as pd
import json

# 读取 Excel 文件
excel_file = 'excel2.xlsx'

block_df = pd.read_excel(excel_file, sheet_name='blockAreas')
plans_df = pd.read_excel(excel_file, sheet_name='plans')
instructions_df = pd.read_excel(excel_file, sheet_name='instructions')
qc1_df = pd.read_excel(excel_file, sheet_name='qc1')
qc2_df = pd.read_excel(excel_file, sheet_name='qc2')
qc3_df = pd.read_excel(excel_file, sheet_name='qc3')
# type_df = pd.read_excel(excel_file, sheet_name='instructions')


# 将 NaN 替换为 None
# def replace_nan_with_none(df):
#     return df.where(pd.notnull(df), None)


# block_df = replace_nan_with_none(block_df)
# plans_df = replace_nan_with_none(plans_df)
# instructions_df = replace_nan_with_none(instructions_df)
# qc1_df = replace_nan_with_none(qc1_df)
# qc2_df = replace_nan_with_none(qc2_df)
# qc3_df = replace_nan_with_none(qc3_df)
# type_df = replace_nan_with_none(type_df)

# 构建 workQueues
work_queues = [
    {
        "qc": "qc1",
        "containers": qc1_df.to_dict(orient='records')
    },
    {
        "qc": "qc2",
        "containers": qc2_df.to_dict(orient='records')
    },
    {
        "qc": "qc3",
        "containers": qc3_df.to_dict(orient='records')
    }
]

# 构建 blockAreas
block_areas = []
for _, row in block_df.iterrows():
    block_area = {
        "block": row["block"],
        "area": row["area"],
        "plans": [],
        "yc": {
            "name": row["yc_name"],
            "location": row["yc_location"]
        },
        "instructions":
            [
            ]
    }

    # 添加 plans 数据
    for _, plan_row in plans_df[(plans_df["block"] == row["block"]) & (plans_df["area"] == row["area"])].iterrows():
        block_area["plans"].append({
            "group": plan_row["group"],
            "bay": plan_row["bay"],
            "capacity": plan_row["capacity"]
        })

    # 添加 instructions 数据
    for _, instr_row in instructions_df[
        (instructions_df["block"] == row["block"]) & (instructions_df["area"] == row["area"])].iterrows():
        instruction = {
            "type": instr_row["type"],
            "status": instr_row["status"],
            "from": instr_row["from"],
            "to": instr_row["to"],
            "containerID": instr_row["containerID"]
        }
        block_area["instructions"].append(instruction)

    block_areas.append(block_area)

# 构建最终的 JSON 数据
data = {
    "workQueues": work_queues,
    "blockAreas": block_areas
}

# 将数据保存为 JSON 文件
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

