
def act_eval(action, tool_env):
    try:
        action_result = eval(action, tool_env)
    except Exception as e:
        action_result = str(e)
    return action_result