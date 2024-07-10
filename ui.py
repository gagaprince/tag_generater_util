import gradio as gr

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


def get_hua_feng_list():
    return [
        "无",
        "Pan Tianshou ----【古风画风1-成熟】",
        "Zhu Qizhan ----【古风画风2-艳丽】",
        "Qi Baishi ----【古风画风3-简约】",
        "Zhang Daqian ----【古风画风4-可爱】",
        "Henri Matisse ----【都市画风1-时尚】",
        "Georgia O'Keeffe ----【都市画风2-欧美】",
        "Craig Thompson ----【都市画风3-细腻】",
        "Henri Matisse ----【都市画风4-流行】",
        "Junji Ito - 代表作品为《die》等----【日式恐怖画风】",
        "Park Tae-joon - 代表作品为《muming》等----【小鲜肉都市】",
        "Park Ji-min - 代表作品为《kiming》等----【都市恋爱】",
        "Kim Hyeong-seop - 代表作品为《CC LOVE》等----【韩风都市恋爱】",
        "Kyoji Asano - 代表作品为《TK war》等----【细腻日漫】",
        "Carlos Dattoli - 代表作品为《Iron Man》等----【都市少男风格】",
        "Kuvshinov Ilya  - 代表作品为《CClove》等----【都市少女风格】",
        "Gary Larson, Gerard Houckgeest - 代表作品为《R》等----【美式漫画】",
        "Ruan Jia - 代表作品为《龙》等----【国风插画】",
        "Paolo Roversi, Cecily Brown - 代表作品为《T》等----【偏质感】",
        " Andreas Rocha  - 代表作品为《fun-class》等----【细节色彩】",
        "Ryohka - 代表作品为《小林家的龙女仆》等",
        "Rebecca Guay - 代表作品为《魔戒》等 ---【西方魔幻】",
        "Craig Mullins - 代表作品为《Halo 4》等---【末日科幻】",
        "Osamu Kobayashi - 代表作品为《Beck》等",
        "Ryoichi Ikegami - 代表作品为《浪客剑心》等",
        "Tite Kubo - 代表作品为《死神》等",
        "Hajime Isayama - 代表作品为《进击的巨人》等",
        "Makoto Shinkai - 代表作品为《你的名字。》等",
        "Naoko Takeuchi - 代表作品为《美少女战士》等",
        "Koyori - 代表作品为《只有我能进入的隐藏迷宫》等",
        "Mamoru Hosoda (细田守) - 代表作品为《时之歌》、《未来的未来》等",
        "Akira Toriyama - 代表作品为《龙珠》等",
        "Rumiko Takahashi - 代表作品为《犬夜叉》、《美少女战士》等",
        "Hideaki Anno - 代表作品为《新世纪福音战士》等", "Hayao Miyazaki - 代表作品为《龙猫》、《千与千寻》等---【经典动画】",
        "Hiromasa Yonebayashi - 代表作品为《借物少女艾莉緹》",
        "Kazuo Oga - 代表作品为《魔女宅急便》等", "Naoko Yamada - 代表作品为《声之形》、《春物》等",
        "Takahiro Kimura - 代表作品为《Code Geass 反叛的鲁路修》等",
        "Masashi Kishimoto - 代表作品为《火影忍者》等",
        "Walt Disney - 代表作品为《白雪公主与七个小矮人》等",
        "John Lasseter - 代表作品为《海底总动员》等---【皮克斯经典】",
        "Tim Burton - 代表作品为《魔发奇缘》等",
        "Glen Keane - 代表作品为《美女与野兽》等---【经典迪士尼】",
        "Genndy Tartakovsky - 代表作品为《星球大战：克隆人战争》等",
        "Chuck Jones - 代表作品为《汤姆猫和杰瑞鼠》等",
        "Isao Takahata - 代表作品为《火垂るの墓》"
    ]


def get_out_mode_list():
    return ["无", "黑白漫画模式", "彩色动画模式", "电影模式", "插画模式", "素描模式", "水彩模式", "游戏立绘模式",
            "像素模式", "图标模式"]


def generater_tags(quality_text, hua_feng, out_mode, people_desc, movement_desc, scene_desc,
                                    expression_desc, master_desc):
    print(quality_text, hua_feng, out_mode, people_desc, movement_desc, scene_desc,
                                    expression_desc, master_desc)
    return '123'


def get_people_list():
    return []


def get_movement_list():
    return []


def get_scene_list():
    return []


def get_expression_list():
    return []


def ui():
    hua_feng_list = get_hua_feng_list()
    out_mode_list = get_out_mode_list()
    people_list = get_people_list()
    movement_list = get_movement_list()
    scene_list = get_scene_list()
    expression_list = get_expression_list()

    with gr.Column():
        gr.Markdown("# 这是一个预设组合提示词生成器")
        gr.Markdown("## 质量+画风+风格+主体组合")
    with gr.Column():
        quality_text = gr.Textbox(label="输入质量描述,建议不必修改",
                                  value="(best quality,4k,8k,highres,masterpiece:1.2),ultra-detailed,(realistic,photorealistic,photo-realistic:1.37)",
                                  lines=2, elem_id="quality_text")

    with gr.Column():
        with gr.Row():
            hua_feng = gr.Dropdown(hua_feng_list, label="选择作者画风（预设）", value=0, type="value", elem_id="hua_feng",
                                   allow_custom_value=True)
            out_mode = gr.Dropdown(out_mode_list, label="选择输出风格", value=0, type="value", elem_id="out_mode",
                                   allow_custom_value=True)

    with gr.Column():
        with gr.Row():
            # 人物选择 服饰五官等人物描述 枚举一些常用的即可
            people_desc = gr.Dropdown(people_list, label="选择人物角色", value=0, type="value", elem_id="people_desc",
                                      allow_custom_value=True)
            # 动作姿态选择 手势+姿态+互动
            movement_desc = gr.Dropdown(movement_list, label="选择人物动作", value=0, type="value",
                                        elem_id="movement_desc", allow_custom_value=True)
            # 场景环境选择 所处环境描述 + 灯光 + 远近 + 物品
            scene_desc = gr.Dropdown(scene_list, label="选择场景", value=0, type="value", elem_id="movement_desc",
                                     allow_custom_value=True)
            # 表情+情感
            expression_desc = gr.Dropdown(expression_list, label="选择表情情感", value=0, type="value",
                                          elem_id="movement_desc", allow_custom_value=True)

        master_desc = gr.Textbox(label="输入主体其他自定义描述，比如 其他角色 或者 其他互动", lines=2)

    with gr.Column():
        generater_btn = gr.Button("生成", variant="primary")
        output_text = gr.Textbox(label="生成的提示词", lines=5)

        generater_btn.click(generater_tags,
                            inputs=[quality_text, hua_feng, out_mode, people_desc, movement_desc, scene_desc,
                                    expression_desc, master_desc], outputs=output_text)

    return [quality_text, hua_feng, out_mode, master_desc, generater_btn, output_text]


if __name__ == '__main__':
    with gr.Blocks() as demo:
        ui()
    demo.launch()
    print("main")
