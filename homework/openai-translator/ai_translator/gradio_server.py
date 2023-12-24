import sys
import os
import gradio as gr

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from translator import PDFTranslator, TranslationConfig


def translation(input_file, source_language, target_language, output_file_format, translate_style):
    LOG.debug(f"[翻译任务]\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}\n输出格式: {output_file_format}\n翻译风格: {translate_style}")

    output_file_path = Translator.translate_pdf(
        input_file.name, source_language=source_language, target_language=target_language, output_file_format=output_file_format, translate_style=translate_style)

    return output_file_path

def launch_gradio():
    language_option=["Chinese", "English", "French", "Korean", "Japanese"]
    output_file_option=["pdf", "markdown"]
    translate_style_option=["novels", "news", "writer"]

    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v2.0(PDF 电子书翻译工具)",
        inputs=[
            gr.File(label="上传PDF文件"),
            # gr.Textbox(label="源语言（默认：英文）", placeholder="English", value="English"),
            # gr.Textbox(label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese")
            gr.Dropdown(choices=language_option, label="源语言（默认：英文）", value="English"),
            gr.Dropdown(choices=language_option, label="目标语言（默认：中文）", value="Chinese"),
            gr.Dropdown(choices=output_file_option, label="文件保存格式（默认：markdown）", value="markdown"),
            gr.Dropdown(choices=translate_style_option, label="翻译风格（默认：小说）", value="novels")
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never"
    )

    iface.launch(share=True, server_name="0.0.0.0")

def initialize_translator():
    # 解析命令行
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 初始化配置单例
    config = TranslationConfig()
    config.initialize(args)    
    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    global Translator
    Translator = PDFTranslator(config.model_name)


if __name__ == "__main__":
    # 初始化 translator
    initialize_translator()
    # 启动 Gradio 服务
    launch_gradio()
