'''
通过gpt-3.5-turbo生成的代码
参考main.py生成trnaslation_module文件
在web_api中调用它
'''

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

def translate(api_key, model_type, openai_model, model_url, file_format, book):
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 利用传入的参数进行适当的设置
    if api_key:
        args.openai_api_key = api_key
        
    if model_type == "OpenAIModel":
        args.openai_model = openai_model
    elif model_type == "GLMModel":
        args.model_url = model_url
        
    if file_format:
        args.file_format = file_format
        
    if book:
        args.book = book
    
    config_loader = ConfigLoader(args.config)
    config = config_loader.load_config()

    model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    model = OpenAIModel(model=model_name, api_key=api_key)

    pdf_file_path = args.book if args.book else config['common']['book']
    file_format = args.file_format if args.file_format else config['common']['file_format']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, file_format)