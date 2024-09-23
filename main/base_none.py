from agents.base.profile import AgentWorkflow
from agents.base.run import BaseRun

if __name__ == "__main__":
    agent = AgentWorkflow()
    run = BaseRun()
    answer = run.run(agent=agent, question="16 + 23 * 44 + 99 / 9 = ?")
    print(answer)
