import gradio as gr
import json
import re


# pip install -r requirements.txt
#
# javascript = """
# (function(){
#     console.log(123);
#     async function saveResult(result) {
#         // 这里可以添加保存结果的逻辑，例如保存到localStorage
#         console.log(args);
#         const oldret = localStorage.getItem('taskResult');
#         console.log('oldRet:', oldret);
#         console.log('result:', result);
#         localStorage.setItem('taskResult', result);
#     }
#     window.saveResult = saveResult;
# })
# """
#
# def on_button_click():
#     return "1234"
#
# with gr.Blocks(js=javascript) as demo:
#     output = gr.Textbox(label="Task Result")
#     btn = gr.Button("Run Task and Save Result")
#     a = "123"
#     btn.click(on_button_click, inputs=None, outputs=output, postprocess=False).then(
#         lambda result: gr.update(value=result+' hi'),
#         inputs=output,
#         outputs=output,
#         postprocess=False
#     ).then(
#         lambda result: None,
#         inputs=output,
#         outputs=None,
#         js=f"saveResult"
#     )

def load_config():
    global drop_down_config
    with open('drop_down_config.json', 'r') as file:
        drop_down_config = json.load(file)


def parse_drop_down_desc(name, desc):
    ret = get_x_list_item(name, desc)
    return ret["tag"] if ret is not None else ""


def parse_check_box_desc(name, select_list):
    ret = ""
    for list_item in select_list:
        obj = get_x_list_item(name, list_item)
        if obj is not None:
            ret += obj["tag"] + ","
    return ret


def replace_comma_space(string):
    pattern = r',+(\s*,+)*'
    string = re.sub(pattern, ',', string)
    pattern = r'\s+,'
    string = re.sub(pattern, ',', string)
    pattern = r'^,'
    return re.sub(pattern, '', string)


def generater_tags(common_text_list, out_mode, people_desc, movement_desc, scene_desc,
                   expression_desc, other_desc_list_select, r_desc_list_select,
                   master_desc, clothes_desc, view_desc):
    ret_list = []
    # 基础描述
    common_desc_text = parse_check_box_desc("commons", common_text_list)
    # 输出模式
    mode_desc_text = parse_drop_down_desc("modes", out_mode)
    # 人物描述
    people_desc_text = parse_drop_down_desc("masters", people_desc)
    # 动作描述
    pose_desc_text = parse_drop_down_desc("poses", movement_desc)
    # 场景环境描述
    scene_desc_text = parse_drop_down_desc("scenes", scene_desc)
    # 表情情绪
    expression_desc_text = parse_drop_down_desc("expressions", expression_desc)
    # 其他描述
    other_desc_text = parse_check_box_desc("others", other_desc_list_select)
    # R级描述
    R_DESC_text = parse_check_box_desc("R_DESC", r_desc_list_select)
    # 自定义主体描述
    master_desc_text = master_desc
    # 服饰描述
    clothes_desc_text = parse_drop_down_desc("clothes", clothes_desc)
    # 观察者角度
    view_desc_text = parse_drop_down_desc("views", view_desc)

    print("common_desc_text:", common_desc_text)
    print("mode_desc_text:", mode_desc_text)
    print("people_desc_text:", people_desc_text)
    print("pose_desc_text:", pose_desc_text)
    print("scene_desc_text:", scene_desc_text)
    print("expression_desc_text:", expression_desc_text)
    print("other_desc_text:", other_desc_text)
    print("R_DESC_text:", R_DESC_text)
    print("master_desc_text:", master_desc_text)
    print("clothes_desc_text:", clothes_desc_text)
    print("view_desc_text:", view_desc_text)

    # 排序 基础描述+自定义主体描述+人物描述+服饰描述+动作描述+R级描述+场景环境描述+表情情绪+其他描述+输出模式+观察者角度
    ret_list.append(common_desc_text)
    ret_list.append(master_desc_text)
    ret_list.append(people_desc_text)
    ret_list.append(clothes_desc_text)
    ret_list.append(pose_desc_text)
    ret_list.append(R_DESC_text)
    ret_list.append(scene_desc_text)
    ret_list.append(expression_desc_text)
    ret_list.append(other_desc_text)
    ret_list.append(mode_desc_text)
    ret_list.append(view_desc_text)

    ret = ','.join(ret_list)
    ret = replace_comma_space(ret)

    print(ret)
    return ret


def get_x_list(x):
    x = drop_down_config[x]
    return list(map(lambda item: item["name"], x))


def get_x_list_item(x, select_name):
    x_list = drop_down_config[x]
    if select_name == 0:
        return x_list[0]
    select_list = list(filter(lambda item: item["name"] == select_name, x_list))
    return select_list[0] if select_list else None



def ui():
    common_list = get_x_list("commons")
    out_mode_list = get_x_list("modes")
    people_list = get_x_list("masters")
    movement_list = get_x_list("poses")
    scene_list = get_x_list("scenes")
    expression_list = get_x_list("expressions")
    other_desc_list = get_x_list("others")
    r_desc_list = get_x_list("R_DESC")
    clothes_list = get_x_list("clothes")
    view_list = get_x_list("views")

    with gr.Column():
        gr.Markdown("# 这是一个预设组合提示词生成器")

    with gr.Column():
        with gr.Row():
            common_text_list = gr.CheckboxGroup(choices=common_list, label="基础参数决策", elem_id="common_text_list")
            out_mode = gr.Dropdown(out_mode_list, label="选择输出风格", value=0, type="value", elem_id="out_mode",
                                   allow_custom_value=True)

    with gr.Column():
        with gr.Row():
            # 人物选择 服饰五官等人物描述 枚举一些常用的即可
            people_desc = gr.Dropdown(people_list, label="选择人物角色", value=0, type="value", elem_id="people_desc",
                                      allow_custom_value=True)
            # 服饰选择

            clothes_desc = gr.Dropdown(clothes_list, label="选择服饰", value=0, type="value", elem_id="clothes_desc",
                                      allow_custom_value=True)

            # 动作姿态选择 手势+姿态+互动
            movement_desc = gr.Dropdown(movement_list, label="选择人物动作", value=0, type="value",
                                        elem_id="movement_desc", allow_custom_value=True)
    with gr.Column():
        with gr.Row():
            # 场景环境选择 所处环境描述 + 灯光 + 远近 + 物品
            scene_desc = gr.Dropdown(scene_list, label="选择场景", value=0, type="value", elem_id="movement_desc",
                                     allow_custom_value=True)
            # 表情+情感
            expression_desc = gr.Dropdown(expression_list, label="选择表情情感", value=0, type="value",
                                          elem_id="movement_desc", allow_custom_value=True)

            # 视角
            view_desc = gr.Dropdown(view_list, label="选择角度", value=0, type="value",
                                          elem_id="view_desc", allow_custom_value=True)

    with gr.Column():
        with gr.Row():
            other_desc_list_select = gr.CheckboxGroup(choices=other_desc_list, label="其他常用参数",
                                                      elem_id="other_desc_list_select")
            r_desc_list_select = gr.CheckboxGroup(choices=r_desc_list, label="R级参数",
                                                  elem_id="r_desc_list")
        master_desc = gr.Textbox(label="输入主体其他自定义描述，比如 其他角色 或者 其他互动", lines=2)

    with gr.Column():
        generater_btn = gr.Button("生成", variant="primary")
        output_text = gr.Textbox(label="生成的提示词", lines=5)

        generater_btn.click(generater_tags,
                            inputs=[common_text_list, out_mode, people_desc, movement_desc, scene_desc,
                                    expression_desc, other_desc_list_select, r_desc_list_select,
                                    master_desc, clothes_desc, view_desc],
                            outputs=output_text)

    return [common_text_list, out_mode, master_desc, generater_btn, output_text]


if __name__ == '__main__':
    load_config()
    with gr.Blocks() as demo:
        ui()
    demo.launch()
    print("main")
