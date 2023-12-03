'''
通过gpt-3.5-turbo生成的代码
使用Flask框架创建一个Web API来提供接口给其他程序调用执行
'''

from flask import Flask, request, jsonify
import your_translation_module

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    
    api_key = data.get('api_key')
    model_type = data.get('model_type')
    openai_model = data.get('openai_model')
    model_url = data.get('model_url')
    file_format = data.get('file_format')
    book = data.get('book')
    
    # 调用你的翻译函数来执行翻译操作
    my_translation_module.translate(api_key, model_type, openai_model, model_url, file_format, book)
    
    return jsonify({'status': 'success'})
    
if __name__ == '__main__':
    app.run()