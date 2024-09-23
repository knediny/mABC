from agents.base.profile import AgentWorkflow
from agents.base.run import ReActTotRun
# import agents.tools.base_tools
from agents.tools import base_tools

if __name__ == "__main__":
    agent = AgentWorkflow()
    run = ReActTotRun()

    agents = [agent]
    eval_run = run
    # answer = run.run(agent=agent, question="16 + 23 * 44 + 99 / 9 = ?", agent_tool_env=vars(agents.tools.base_tools ), )
    answer = run.run(agent=agent, question="16 + 23 * 44 + 99 / 9 = ?", agent_tool_env=vars(base_tools), eval_run=eval_run, agents=agents)
    print(answer)
