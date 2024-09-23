import inspect
import re

def extract_functions(file_content):
    # 这个正则表达式尝试匹配函数定义和它们的文档字符串
    pattern = re.compile(
        r"def\s+(\w+)\s*\(([^)]*)\)\s*->\s*([^:]+):\s*('''(.*?)'''|\"\"\"(.*?)\"\"\")",
        re.DOTALL  # DOTALL让 . 匹配包括换行符在内的所有字符
    )
    matches = pattern.findall(file_content)
    functions = []
    for match in matches:
        function_name = match[0]
        parameters = match[1]
        return_type = match[2].strip()
        doc = match[4] or match[5]  # 根据捕获组选择正确的文档字符串
        doc = doc.strip()  # 移除文档字符串前后的空白字符
        functions.append((function_name, parameters, return_type, doc))
    return functions

def get_function_info(func_info):
    function_name, parameters_str, return_type, doc = func_info  # 解包元组
    # 处理参数字符串，转换为期望的格式
    # 假设parameters_str是以逗号分隔的参数列表
    parameters = parameters_str.split(',') if parameters_str else []
    formatted_parameters = []
    for param in parameters:
        param_name, _, param_type = param.partition(':')
        param_name = param_name.strip()
        param_type = param_type.strip() or 'Any'  # 如果没有指定类型，则使用'Any'
        formatted_parameters.append(f"{param_name}: {param_type}")
    # 生成并返回函数定义字符串
    template = '''
    def {function_name}({parameters}) -> {return_type}:
    """
    {doc}
    """
    '''
    return template.format(
        function_name=function_name,
        parameters=', '.join(formatted_parameters),
        return_type=return_type or 'None',  # 如果没有指定返回类型，则使用'None'
        doc=doc
        # doc='Documentation not available'  # 假设我们没有从源文件获取文档字符串
    ), function_name

# def extract_functions(file_content):
#     # 使用正则表达式匹配函数定义
#     pattern = re.compile(r"def\s+(\w+)\s*\(([^)]*)\)\s*->\s*([^:]+):")
#     matches = pattern.findall(file_content)
#     functions = []
#     for match in matches:
#         function_name = match[0]
#         functions.append(globals()[function_name])
#     return functions

# def get_function_info(func):
#     # 获取函数信息的函数
#     signature = inspect.signature(func)
#     parameters = signature.parameters
#     template = '''
#     def {function_name}({parameters}):
#     """
#     {doc}
#     """
#     '''
#     function_name = func.__name__
#     doc = func.__doc__
#     parameters = []
#     for param_name in signature.parameters:
#         param = signature.parameters[param_name]

#         param_type = param.annotation
#         start_index = str(param_type).find("'") + 1
#         end_index = str(param_type).rfind("'")
#         param_type = str(param_type)[start_index:end_index]

#         if param.default is inspect._empty:
#             param_default = "None"
#         else:
#             param_default = param.default
#         parameters.append(f"{param_name} : {param_type} = {param_default}")
#     parameters = ", ".join(parameters)
#     return template.format(function_name=function_name, doc=doc, parameters=parameters)

def get_agent_tool_list_prompt(file_path):
    """
    根据 tool.py 自动生成 tool_list_prompt
    """
    with open(file_path, "r") as file:
        file_content = file.read()
    tool_list = extract_functions(file_content)
    tool_and_tool_name_pair_list = [get_function_info(func) for func in tool_list]
    tools = [i[0] for i in tool_and_tool_name_pair_list]
    tool_names = [i[1] for i in tool_and_tool_name_pair_list]
    return "".join(tools), ", ".join(tool_names)

